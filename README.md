# EUCLID+
EUCLID+ is a novel Clock Divider, Oscillator and Rhythm Sequencer for electronic music applications. 

EUCLID+ builds gate pattern, including [Euclidean Rhythms.](https://en.wikipedia.org/wiki/Euclidean_rhythm) Unlike most instances of Euclidean Rhythms, which are generated by algorithms, EUCLID+ is realised entirely in hardware and builds its patterns using a conditional modulation of an external clock signal and the signal from an oscillator internal to EUCLID+.

EUCLID+ divides the applied clock signal by any integer clock division (up to 31 countes) making EUCLID+ a useful voltage-controlled hardware clock divider.

The VCO inside EUCLID+ can run asynchronously to the applied clock, giving the resulting rhythm outputs a useful varying quality.

Alternatively, EUCLID+ can hard-sync its VCO to the clock divider output. In this condition, the rhythm pattern is fixed, having the same period as the clock divider. The output rhythm in this synchronous mode includes the familiar Euclidean Rhythms (of length 2:31).

Full design details for EUCLID+ including schematics, PCB layouts and a Front Panel design, are presented in the hardware folder.  

EUCLID+ is published under [CC BY-SA 4.0 License](https://github.com/m0xpd/EUCLIDplus/blob/main/LICENSE.txt).
