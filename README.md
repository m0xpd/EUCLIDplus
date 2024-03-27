# EUCLID+
EUCLID+ is a novel Clock Divider, Clock Multiplier and Rhythm Sequencer for electronic music applications. 

<p width=100%, align="center">
<img width=40%, src="https://github.com/m0xpd/EUCLIDplus/blob/main/Hardware/Images/Euclid%20Front.jpg">
</p>

EUCLID+ builds gate patterns, including [Euclidean Rhythms.](https://en.wikipedia.org/wiki/Euclidean_rhythm) Unlike most instances of Euclidean Rhythms, which are generated by algorithms, EUCLID+ is realised entirely in hardware and builds its patterns using [conditional modulation](https://github.com/m0xpd/EUCLIDplus/tree/main/Operation#readme) of an external clock signal and the signal from an oscillator internal to EUCLID+.

If you're looking for a module where you just dial in parameters and out pops a Euclidean Rhythm, this isn't for you. However, if you're interested in working with a creative platform on which you can explore possibilities in rhythm generation - and be open to the surprises which pop out along the way - EUCLID+ might be for you.

EUCLID+ divides an applied clock signal by any integer divisor up to 30, making EUCLID+ useful as a voltage-controlled hardware clock divider. The start of the clock divide cycle can be reset manually, using the RESET pushbutton, or under CV control via the Reset input.

EUCLID+ includes an integral VCO, which can serve as a voltage controlled clock multiplier. Signals from the clock divider and clock multiplier are available for external use on the DIVIDE and MULT outputs. 

EUCLID+ combines the clock input and the signal from the clock multiplier to provide gate patterns on the RHYTHM output. The complements of these patterns appear on the COMP output. The duty cycle of the RHYTHM and COMP outputs follows that of the input Clock waveform.

EUCLID+ can hard-sync its VCO to the clock divider output. In this condition, the output pattern is fixed, having the same period as the clock divider. The patterns in this synchronous mode include the familiar [Euclidean Rhythms](https://en.wikipedia.org/wiki/Euclidean_rhythm) (of length up to 30). Note that the complement of a Euclidean Rhythm is itself Euclidean; the COMP output produces musically useful triggers for primary voices in complementary and interlocking rhythmic structures as well as for producing "ghost notes".

Alternatively, the VCO inside EUCLID+ can run asynchronously to the applied clock, giving the resulting pattern outputs a useful varying quality, but one which retains much of the structure (/correlation/'feel') of the behaviour in synchronous mode. Careful tuning of the VCO in asynchronous mode can exploit this variation to impart slow, organic change into what can otherwise be a dry, sterile, mechanistic process.

Switching between syncrhonous and asynchronous operation can be achieved manually, using the SYNC pushbutton, or under CV control via the Sync input.

There is a fuller description of the principles behind EUCLID+ operation [here](https://github.com/m0xpd/EUCLIDplus/tree/main/Operation#readme) and a detailed description of circuit operation [here](https://github.com/m0xpd/EUCLIDplus/tree/main/Operation#circuit-description).

Full design details for EUCLID+ including schematics, PCB layouts for the [Main Board](https://github.com/m0xpd/EUCLIDplus/tree/main/Hardware/Main%20Board#readme) and [Control Board](https://github.com/m0xpd/EUCLIDplus/tree/main/Hardware/Control%20Board#readme) and a [Front Panel](https://github.com/m0xpd/EUCLIDplus/tree/main/Hardware/Front%20Panel#readme) design, are presented in the hardware folder.  

EUCLID+ is published under [CC BY-SA 4.0 License](https://github.com/m0xpd/EUCLIDplus/blob/main/LICENSE.txt).

# Specifications

**Width:** 

EUCLID+ is **16HP wide**.

**Depth:**

EUCLID+ extends **43 mm** behind the front panel when a conventional Eurorack power header **with strain relief** is inserted 

If your power header doesn't have a strain relief (which is probably more typical, judging by the power cables delivered with commercial modules) EUCLID+ extends **37 mm** behind the front panel.

**Power Consumption:**

| Power Rail | Current |
|---|---|
| +12V | **30mA** | 
| -12V | **15mA** |
| 5V | **0** |

The 12V current drain was fluctuating during operation (with switching behaviour); the 30mA figure quoted above is an eyeball estimate of average current - the peak was 35mA.
The -12V current drain was steady; the 15mA is average drain.
