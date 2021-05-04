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
    <tr>
        <td>AssemblyFibonacci.asm</td>
        <td>Some work testing out some new stuff I learned about conditional branching, specifically the condition fields and their mnemonics, which will prove to be incredibly useful. I also accidentally reminded myself that the MSP 432 only has 64k of sram, which is less than I thought, but still substanstially more than is needed to store the fibonacci numbers that fit within 32 bits. Maybe I should use this as a chance to learn how to make big numbers like 64 bits using 2 words. Could be fun.</td>
    </tr>
</table>