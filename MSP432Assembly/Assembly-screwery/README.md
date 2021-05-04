# Introductory assembly projects

Just simple things like toggling LEDs, and moving memory around. There is nothing complicated here, but I have to start somewhere, and this is the place.

<table>
    <tr>
        <td>Project</td>
        <td>Description</td>
    </tr>
    <tr>
        <td>AssemblyOne.asm</td>
        <td>This was my first experiment with assembler, and it's dead-simple job is to activate the red LED on the MSP432 launchpad</td>
    </tr>
    <tr>
        <td>AssemblyWhiteBlink.asm</td>
        <td>Number two, it's job is to blink the Red, Green, and Blue LEDs all together to blink white. of course, it's too fast to see any blinking and essentially becomes PWM at 50%, but it's a start.</td>
    </tr>
    <tr>
        <td>AssemblyRGBCycle.asm</td>
        <td>Now we're getting somewhere. I still haven't figured out the timers in assembly yet, so it just uses a countdown counter to time the cycling of the RGB, but it performs it's job just fine and cycles through all the possible RGB colors.</td>
    </tr>
</table>