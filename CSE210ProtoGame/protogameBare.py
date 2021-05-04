import sys
sys.path.append('pygame_engines')
import config

import math
import time
import random

import pgRenderer as Renderer
import SoundEngine
import RayCasterBare as RayCaster
import VectorOps
import ListOps
import mapTools
import entities
import GUI

width = 640
height = 480
hudHeight = 75

FOV = (config.FOV * math.pi) / 180
cameraDist = 0.1 / math.tan(FOV / 2)

class Game:
    def __init__(self):
        self.loopTime, self.fpsTime, self.fps, self.deltaTime, self.playStartTime, self.playEndTime = 0, 0, 0, 0, 0, 0
        self.timer()
        self.screen = Renderer.pgRenderer(width, height, cameraDist=cameraDist, FogofWar=config.FogofWar, hudHeight=hudHeight)
        
        self._running = True
        self.gameWon = False
        self.keysPressed, self.keysHeld = [], []
        self.rayCaster = RayCaster.Screen(mapTools.map, width = width, height = height - hudHeight, supersampling = config.supersampling, cameraDist = cameraDist, Renderer=self.screen)
        
        self.player = entities.Player(position = [2.5,5.5], direction=(1,0))

        self.spritesOnScreen = []
        self.mobAI = entities.MobAI(mapTools.map) #initialize the AI pather with the map data
        self.enemies = [
            entities.Goblin(position = [2.8,1.4]),      #organized by rooms
            entities.ArmoredGoblin(position = [2,2]),
            entities.Goblin(position = [2.9,1.6]), 

            entities.Goblin(position = [2,8.4]),    #Top Right Room

            entities.Goblin(position = [7.5,9.5]), #Top Right end
            
            entities.Goblin(position = [8.5,1.5]),  #Mid Left quarter
            entities.FastGoblin(position = [7.7,2.3]),
            entities.Goblin(position = [9,3.1]),

            entities.ArmoredGoblin(position = [12.5,5.5]), #exit room

            entities.Goblin(position = [11.5,9.5]), #Mid Right dead end
            entities.FastGoblin(position = [13,9]),

            entities.Goblin(position = [12,2]), # Mid left passage
            entities.Goblin(position = [14.5,1.6]),

            entities.ArmoredGoblin(position = [16,7]), # Big Bottom middle room
            entities.FastGoblin(position = [19,7.2]),
            entities.Goblin(position = [20,6.4]),

            entities.ArmoredGoblin(position = [20.5,3.2]), # Bottom left room
            entities.FastGoblin(position = [21.2,2.5]),

            entities.ArmoredGoblin(position = [18,9.5]), #bottom right dead end passage
        ]
        for i in self.enemies:
            i.entityList = self.enemies
        
        self.gui = GUI.Hud(self.screen, self.player)

        self.soundManager = SoundEngine.SoundManager()
        self.player.walking = False
        self.enemyAttacking = False
        self.music = SoundEngine.Music(song=SoundEngine.mainTheme)
        
    def on_event(self, event):
        if event[0] == 'QUIT':
            self._running = False
        elif event[1] == 'press' and not event[0] in self.keysHeld:
            self.keysPressed.append(event[0])
            self.keysHeld.append(event[0])
        elif event[1] == 'release' and event[0] in self.keysHeld:
            self.keysHeld.remove(event[0])
    
    def loop(self):
        def playerMovement():
            if 'left' in self.keysHeld or 'a' in self.keysHeld:
                self.player.direction = VectorOps.rotate(self.player.direction, -3.14 * self.deltaTime)
            elif 'right' in self.keysHeld or 'd' in self.keysHeld:
                self.player.direction = VectorOps.rotate(self.player.direction, 3.14 * self.deltaTime)
            if 'up' in self.keysHeld or 'w' in self.keysHeld:
                self.player.move(VectorOps.rotate((0,self.player.maxSpeed * self.deltaTime),VectorOps.angle(self.player.direction)))
                self.player.walking = 'forward'
            elif 'down' in self.keysHeld or 's' in self.keysHeld:
                self.player.move(VectorOps.rotate((0,-self.player.maxSpeed * self.deltaTime * 0.5),VectorOps.angle(self.player.direction)))
                self.player.walking = 'backward'
            else:
                self.player.walking = False
        def generateSpriteList():
            sprites = []
            for i in self.enemies:
                spriteDist = VectorOps.distance(i.position, self.player.position)
                sprites.append([i, spriteDist])
            sprites = ListOps.sortbyindex(sprites, 1)

            for i in reversed(sprites):
                sides = VectorOps.perpendicular(VectorOps.sub(self.player.position, i[0].position), i[0].position, i[0].radius)
                spriteAngle = [VectorOps.angleWrap(VectorOps.angle(n) - VectorOps.angle(self.player.direction)) for n in VectorOps.sub(sides, self.player.position)]
                i.append(spriteAngle)
                if not ((-FOV/2 < VectorOps.angleWrap(spriteAngle[0]) < FOV/2 or -FOV/2 < VectorOps.angleWrap(spriteAngle[1]) < FOV/2) and (-1.56 < VectorOps.angleWrap(spriteAngle[0]) < 1.56 and -1.56 < VectorOps.angleWrap(spriteAngle[1]) < 1.56)):
                    sprites.remove(i)
                    continue
                if not (self.rayCaster.TestLoS(self.player.position, sides[0]) or self.rayCaster.TestLoS(self.player.position, sides[1])) or not (-FOV/2 < VectorOps.angleWrap(spriteAngle[0]) < FOV/2 or -FOV/2 < VectorOps.angleWrap(spriteAngle[1]) < FOV/2):
                    sprites.remove(i)
                    continue
            return sprites
        def checkwin():
            if mapTools.map[int(self.player.position[0])][int(self.player.position[1])] == 1:
                print("you win!")
                self.gameWon = True
                self._running = False
        def useHpPotion():
            if self.player.inventory["Health Potion"] > 0:
                if self.player.currentHealth < self.player.health:
                    self.player.inventory["Health Potion"] -= 1
                    self.player.currentHealth += 30
                    if self.player.currentHealth > self.player.health:
                        self.player.currentHealth = self.player.health
                    self.screen.addConsoleMessage("used health potion! +30 health!")
                else:
                    self.screen.addConsoleMessage("you already have max health!")
            else:
                self.screen.addConsoleMessage("you have no more health potions!")
        
        playerMovement()
        checkwin()
        self.spritesOnScreen = generateSpriteList()
        if 'h' in self.keysPressed:
            useHpPotion()
        if 'space' in self.keysPressed and self.loopTime - self.player.attackTime > self.player.attackCoolDown:
            self.player.attackTime = self.loopTime
            self.screen.startAttack()
            if len(self.spritesOnScreen) != 0:
                damage = self.player.attack(self.spritesOnScreen[0][0], self.spritesOnScreen[0][1])
                if(damage == 0):
                    self.screen.addConsoleMessage("The target is too far!")
                else:
                    self.screen.addConsoleMessage("you dealt {damage} damage!".format(damage = damage))
                    self.player.attackHit = True
            else:
                self.player.attackHit = False
                self.screen.addConsoleMessage("you missed!")
            self.player.attacking = True
        else:
            self.player.attacking = False
            self.player.attackHit = False

        for enemy in self.enemies: #enemy pathing
            if self.rayCaster.TestLoS(self.player.position, enemy.position):
                if -0.4 < enemy.position[0] - self.player.position[0] < 0.4 and -0.4 < enemy.position[1] - self.player.position[1] < 0.4:
                    continue
                enemy.destination = (self.player.position[0],self.player.position[1])
                try: #throws an error when the enemy is in the same tile as the target
                    path = self.mobAI.findPath( (enemy.position[0],enemy.position[1]), enemy.destination)
                    sConst = enemy.maxSpeed * self.deltaTime
                    enemy.move(VectorOps.multiply(VectorOps.normalize([(path[1][0] - enemy.position[0]), (path[1][1] - enemy.position[1])]),sConst), normalizeResult=False, smoothCollision = True)
                except:
                    pass
        
        self.enemyAttacking = False
        for enemy in self.enemies: #enemy attacking
            if self.rayCaster.TestLoS(self.player.position, enemy.position):
                if self.loopTime - enemy.attackCoolDown > enemy.attackTime:
                    damage = enemy.attack(self.player,((enemy.position[0] - self.player.position[0])**(2)+(enemy.position[1] - self.player.position[1])**(2))**(1/2))
                    if(damage == -1):
                        self._running = False
                    elif(damage > 0):
                        self.enemyAttacking = True
                        #it might be better to have the sword or GUI flash red and have a health bar
                        self.screen.addConsoleMessage("you recieved {damage} damage!".format(damage = damage))
                        self.screen.addConsoleMessage("you are at {health} health!".format(health = self.player.currentHealth))

    def on_render(self):
        self.screen.drawBG()

        if config.FullScreenSweep:
            rays = self.rayCaster.RaySweep(self.player.position,self.player.direction, simplify=True)
        else:
            rays = self.rayCaster.RaySearch(self.player.position,self.player.direction, simplify=True)

        polygons = self.rayCaster.RenderSweep(rays, sort=True)
        
        for enemy in self.enemies: #reset enemy color overlays
            if enemy.colorAniTime - self.loopTime < 0:
                enemy.colorMultiplier = [1,1,1]
        sprites = self.spritesOnScreen[:]
        
        if config.texturedWalls == True:
            self.screen.renderTextured(polygons, sprites)
        else:
            self.screen.render(polygons, sprites)


        if config.debugLevel >= 1:
            self.screen.debugFPS(self.fps)
            if config.debugLevel >= 2:
                self.screen.debugCompass(int(VectorOps.angle(VectorOps.rotate(self.player.direction, math.pi/2)) * 180 / math.pi))
        
        self.screen.drawWeapon()

        if self._running == False and self.gameWon:
            self.screen.displayGameWin()
            self.screen.addConsoleMessage("you've won! press Esc to quit")
        elif self._running == False and self.gameWon == False:
            self.screen.displayDeath()
            self.screen.addConsoleMessage("you've Died! press Esc to quit")

        self.gui.drawHud(playerInfo = self.player)

    def manageSounds(self):
        if self.player.walking:
            self.soundManager.walkSound(walking=True, walkDelay=(0.6 if self.player.walking == 'forward' else 1))
        else:
            self.soundManager.walkSound(walking=False)

        if self.player.attacking:
            self.soundManager.swingSound(True)
        else:
            self.soundManager.swingSound(False)

        if self.player.attackHit:
            self.soundManager.attackHitSound(True)
        else:
            self.soundManager.attackHitSound(False)

        if self.enemyAttacking:
            self.soundManager.enemyAttackHitSound(True)
        else:
            self.soundManager.enemyAttackHitSound(False)

        self.soundManager.playSounds()

    def timer(self):
        self.deltaTime = time.perf_counter() - self.loopTime
        self.loopTime = time.perf_counter()
        self.fpsTime += self.loopTime
        if self.fpsTime > 250:
            self.fps = int(1/self.deltaTime)
            #print("FPS:", self.fps)
            self.fpsTime = 0

    def on_execute(self):
        def fadeIn(duration, image, coords = [0,0], hold = 0):
            self.timer()
            self.timer()
            self.screen.fadeIn(0, duration=duration, hold=hold, image=image, coords=coords) #initialize fade variables
            while self.screen.fadeIn(self.deltaTime): #perform fade
                self.timer()
        def fadeOut(duration, hold = 0, fadeMusic=False):
            self.timer()
            self.timer()
            self.screen.fadeOut(0, duration=duration, hold=hold) #initialize fade variables
            while self.screen.fadeOut(self.deltaTime): #perform fade
                self.timer()
                if fadeMusic:
                    self.music.fadeOut(self.deltaTime, 3)
        
        #MAIN GAME SEQUENCE
        self.music.play() #start title music
        fadeIn(4, self.screen.titleScreenImage) #fade into title screen
        fadeIn(3, self.screen.titleScreenSubTitleImage, coords=(261,5))
        fadeIn(2, self.screen.titleScreenTitleImage, coords=(164,36))
        fadeIn(1, self.screen.titleScreenAuthorsImage, coords=(156,93), hold=1.5)
        self.screen.titleScreenBegin()

        while(not 'return' in self.keysHeld and not 'space' in self.keysHeld): #Wait for keypress on title screen
            self.keysPressed = []
            for event in self.screen.events():
                self.on_event(event)
        
        fadeOut(3, hold = 1, fadeMusic = True)  #fade to black
        self.music.pause() #stop music at the end of the fade

        self.on_render() #Render first frame
        fadeIn(1.5, self.screen.screen.convert_alpha()) #fade into game
        
        self.playStartTime = time.perf_counter()
        self.screen.events() #clear event queue
        while( self._running ): #Main Game Loop
            self.timer()
            self.keysPressed = []
            for event in self.screen.events():
                self.on_event(event)
            self.loop()
            self.on_render()
            self.screen.update() #update screen with rendered frame
            self.manageSounds()
        self.playEndTime = time.perf_counter()

        self.player.score += ( 100 - (self.playEndTime - self.playStartTime) / 2 if (self.playEndTime - self.playStartTime) / 2 < 100 else 0) + self.player.currentHealth
        print(self.player.score)
        self._running = True
        while( self._running ):
            for event in self.screen.events():
                self.on_event(event)

def mainLaunch(renderer = ''):
    controller = Game()
    controller.on_execute()

if __name__ == "__main__":
    mainLaunch()