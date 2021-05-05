# PCBMaking

Recently, I tried making a mini-CNC to mill PCBs. This project ended up failing, mostly due to it not being stiff enough. I likely cheaped out too much on the materials, and probably the spindle too. It worked a bit though, and I tried milling a few PCBs with mixed results. Honestly, mostly negative, but at least I gained some experience with the open-source KiCad software for designing PCBs, which was quite a bit of fun.

<table>
    <tr>
        <td>Project</td>
        <td>Description</td>
    </tr>
    <tr>
        <td>2n2222 audio amp</td>
        <td>This project was meant to be a simple test of my PCB milling capabilities. I actually managed to get a somewhat successful PCB from this one, but it didn't work that well. Probably because I hadn't learned transistor-based circuit analysis and I honestly didn't know what I was doing. It was neat to see it come together though.</td>
    </tr>
    <tr>
        <td>ATmega8U2 breakout</td>
        <td>Had my milling proven more successful and able to mill smaller traces, I was sort of planning on getting some ATmega 8U2 ICs and putting them on breakout boards to use in projects. Oh well, I'll do that when I build an actually-working mill.</td>
    </tr>
    <tr>
        <td>CNC-Trace-Stress-Test</td>
        <td>This was a simple stress test of basic traces of varying thicknesses. I managed to mostly get the 0.4mm trace, but I more reliably managed the 0.5 and larger. Though, this was with a wide clearance, and I couldn't put them as close as I wanted.</td>
    </tr>
    <tr>
        <td>RGB-ShiftRegister</td>
        <td>More of a test of my PCB-making skills, I designed this simple board to try to multiplex some RGB LEDs with a shift register and a microcontroller. This never made it to production as the traces were too close and small for my crappy PCB-mill.</td>
    </tr>
    <tr>
        <td>ShiftRegisterLEDs</td>
        <td>Same concept as the last one, but simplified to have a better chance of working. No transistors and no RGB, just simple LEDs to test it out. It still never made production.</td>
    </tr>
    <tr>
        <td>TylerMoon</td>
        <td>If the PCB milling had worked out, I had planned on making a custom PCB and using a microcontroller to light up a 3D printed moon in lunar phases for my brother. This was never finished in PCB layout because I got discouraged when my mill didn't work out well enough and didn't bother finishing it (and because it wasn't going to lay out that nicely with what I had planned anyways)</td>
    </tr>
</table>