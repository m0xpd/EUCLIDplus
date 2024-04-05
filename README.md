# EUCLID+
EUCLID+ is a novel Clock Divider, Clock Multiplier and Rhythm Sequencer for electronic music applications. 

<p width=100%, align="center">
<img width=40%, src="https://github.com/m0xpd/EUCLIDplus/blob/main/Hardware/Images/Euclid%20Front.jpg">
</p>

EUCLID+ builds gate patterns, including [Euclidean Rhythms.](https://en.wikipedia.org/wiki/Euclidean_rhythm) Unlike most instances of Euclidean Rhythms, which are generated by algorithms, EUCLID+ is realised entirely in hardware and builds its patterns using what I shall call [conditional modulation](https://github.com/m0xpd/EUCLIDplus/tree/main/Operation#readme) of an external clock signal by the signal from an oscillator internal to EUCLID+.

Strictly speaking, EUCLID+ *usually* produces a *rotation* of a Euclidean Rhythm (which is an instance of the same '[rhythm necklace](https://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf)' as the Euclidean Rhythm). EUCLID+ *occasionally* produces a Euclidean Rhythm.

If you're looking for a module where you just dial in parameters and out pops a Euclidean Rhythm, this isn't for you. However, if you're interested in working with a creative platform on which you can explore possibilities in rhythm generation, and are open to the surprises which you meet along the way, EUCLID+ might be of interest. 

Here's a 'scope trace of EUCLID+ producing the [tresillo](https://en.wikipedia.org/wiki/Tresillo_(rhythm)) (or habanera) rhythm, which is Euclidean Rhythm "*E*(3,8)" (= [10010010] or, as more frequently represented in the notation used in musicology, [x..x..x.]).

<p width=100%, align="center">
<img width=40%, src="https://github.com/m0xpd/EUCLIDplus/blob/main/Hardware/Images/E38.png">
</p>

There are more examples of EUCLID+ performance [here](https://github.com/m0xpd/EUCLIDplus/blob/main/Operation/README.md#performance-examples).

EUCLID+ divides an applied clock signal by any integer divisor up to 30, making EUCLID+ useful as a voltage-controlled hardware clock divider. The start of the clock divide cycle can be reset manually, using the RESET pushbutton, or under CV control via the Reset input.

EUCLID+ includes an integral VCO, operating in the LFO range, which can serve as a voltage controlled clock multiplier. Signals from the clock divider and clock multiplier are available for external use on the DIVIDE and MULT outputs. 

EUCLID+ combines the clock input and the signal from the clock multiplier to provide gate patterns on the RHYTHM output. The complements of these patterns appear on the COMP output. The duty cycle of the RHYTHM and COMP outputs follows that of the input Clock waveform.

EUCLID+ can hard-sync its VCO to the clock divider output. In this condition, the output pattern is fixed, having the same period as the clock divider. The patterns in this synchronous mode include the familiar [Euclidean Rhythms](https://en.wikipedia.org/wiki/Euclidean_rhythm) (of length up to 30). Note that [the complement of a Euclidean Rhythm is itself Euclidean](https://www.researchgate.net/publication/228841028_Interlocking_and_Euclidean_rhythms); the COMP output produces musically useful triggers for primary voices in complementary and interlocking rhythmic structures as well as for producing "ghost notes".

Alternatively, the VCO inside EUCLID+ can run asynchronously to the applied clock, giving the resulting pattern outputs a useful varying quality, but one which retains much of the structure (/correlation/'feel') of the behaviour in synchronous mode. Careful tuning of the VCO in asynchronous mode can exploit this variation to impart slow, organic change into what can otherwise be a dry, sterile, mechanistic process.

Switching between synchronous and asynchronous operation can be achieved manually, using the SYNC pushbutton, or under CV control via the Sync input.

There is a fuller description of the principles behind EUCLID+ operation [here](https://github.com/m0xpd/EUCLIDplus/tree/main/Operation#readme) and a detailed description of circuit operation [here](https://github.com/m0xpd/EUCLIDplus/tree/main/Operation#circuit-description).

The Clock Divider's DIVIDE setting is reported on five LEDs at the top left of the front panel. There are two idosyncracies of this display worth explaining. 

First, the binary display is arranged with least significant bit on the left, which (of course) is opposite to ordinary practice. This reversal felt more 'natural' in use, given the display's placement immediately above the DIVIDE potentiometer, which generates an increasing value as it is rotated clockwise. 

Second, as explained in the [description of system operation](https://github.com/m0xpd/EUCLIDplus/tree/main/Operation#readme), the binary number on the display must be set to one greater than the desired clock divisor. In other words, to achieve a clock division of 8, you must set the number 9 (1,0,0,1) on the LEDs.  

Full design details for EUCLID+ including schematics, PCB layouts for the [Main Board](https://github.com/m0xpd/EUCLIDplus/tree/main/Hardware/Main%20Board#readme) and [Control Board](https://github.com/m0xpd/EUCLIDplus/tree/main/Hardware/Control%20Board#readme) and a [Front Panel](https://github.com/m0xpd/EUCLIDplus/tree/main/Hardware/Front%20Panel#readme) design, are presented in the hardware folder.  

For those who are discouraged by the complexity of the hardware approach - or those who would simply like to play with the rhythm generation method used in EUCLID+ in a context which avoids oscillator drift and other non-ideal behaviours associated with hardware - a software implementation of EUCLID+ is presented [here](https://github.com/m0xpd/EUCLIDplus/tree/main/Software%20Version#readme)

# Introductory Video

A [simple video](https://youtu.be/RWJx1ux7fJk) demonstrates some of the basic functionalty of EUCLID+

# License

EUCLID+ (including the descriptions of its operating principles, and the hardware and software embodiments described in this repository) is published under [CC BY-SA 4.0 License](https://github.com/m0xpd/EUCLIDplus/blob/main/LICENSE.txt).

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

The 12V current drain was fluctuating during measurement (with the module's switching behaviour during operation and during operation of the controls); the 30mA figure quoted above is an 'eyeball estimate' of average current - the peak drain observed was 35mA.
The -12V current drain was steady; 15mA is the average consumption.
