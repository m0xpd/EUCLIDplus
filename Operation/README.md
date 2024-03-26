# EUCLID+ Operation

This section contains a description of the principles behind EUCLID+ and a detailed description of the implementation of these principles in the module hardware.

A defining property of Euclidean Rhythms (ERs) is the fact that an ER of length L having N onsets is the most even distribution of the N onsets over L beats (1). 
This led me to investigate the idea of setting a switching waveform of period L/x against the period, L, where x is continuously variable. When x is a simple positive integer 
(1, 2, 3, ...) this just gives a number of periods of the internal oscillator for every period, L, and will identify the division of L into x sections.

If we could identify the FIRST of the clock pulses which occur in each of these sections, we shall have found the most even distribution of x pulses - 
a Euclidean Rhythm of Length=L and Density=x.

This is what EUCLID+ does - it takes the incomeing clock signal and turns it into a pulse train at the clock leading edge (using a one-shot/monostable around U1A) 
and generates a high duty cycle signal, 'Osc', from the internal VCO. The first clock pulse in every period of the VCO signal is identified by the signal FIRST, which is held on a 
S-R flip-flop (implemented on gates A and B of U2&3). When FIRST is true, the output is set when both the internal oscillator (Osc) and the clock are true (i.e. the system just ANDs 
the clock and internal oscillator together for the first pulse). HOWEVER, for subsequent clock pulses (when FIRST is false) no output is produced. 

This is achieved by the additional logic (U8, gates D and C) ahead of the S-R flip flop (formed from gates A and B of U2&3). The entire state machine is shown below:

<p width=100%, align="center">
<img width=40%, src="https://github.com/m0xpd/EUCLIDplus/blob/main/Operation/Collateral/EUCLID%2B%20State%20Machine.png">
</p>


This amounts to what I have described as 'conditional modulation' (for want of a better phrase) - rather than simply forming the logical AND of the clock and the internal oscillator 
(equivalent to multipliying the signals), derivation of the FIRST signal and its use in the formation of the SET input to the second S-R fip flop imposes a conditionality to the modulation, 
which gives the interesting rhythmic patterns we seek. 


References

(1) 
