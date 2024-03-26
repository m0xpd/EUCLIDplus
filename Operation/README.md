# EUCLID+ Operation

This section contains a description of the principles behind EUCLID+ and a detailed description of the implementation of these principles in the module hardware.

A defining property of Euclidean Rhythms (ERs) is the fact that an ER of length L having N onsets is the most even distribution of the N onsets over L beats (1). 
This led me to investigate the idea of setting a switching waveform of period L/x against the period, L, where x is continuously variable. When x is a simple positive integer 
(1, 2, 3, ...) this just gives a number of periods of the internal oscillator for every period, L, and will identify the division of L into x sections.

If we could identify the FIRST of the clock pulses which occur in each of these sections, we shall have found the most even distribution of x pulses - 
a Euclidean Rhythm of Length=L and Density=x.

For example, the graphic below shows an idealised Clock signal and the internal oscilator signal, 'Osc', set to L = 8, x = 3

<p width=100%, align="center">
<img width=80%, src="https://github.com/m0xpd/EUCLIDplus/blob/main/Operation/Collateral/State%20Machine%20Operation%20Principle.png">
</p>

The first clock pulse within each period of the 'Osc' signal is identified in red - readers familiar with Euclidean Rhythms will recognise the result as a valid ER(8,3).

This is what EUCLID+ does - it takes the incoming clock signal and turns it into a pulse train at the clock leading edge (using a one-shot/monostable around U1A) 
and generates a high duty cycle signal, 'Osc', from the internal VCO. The first clock pulse in every period of the VCO signal is identified by the signal FIRST, which is held on a 
S-R flip-flop (implemented on gates A and B of U2&3). When FIRST is true, the output is set when both the internal oscillator (Osc) and the clock are true (i.e. the system just ANDs 
the clock and internal oscillator together for the first pulse). HOWEVER, for subsequent clock pulses (when FIRST is false) no output is produced. 

This is achieved by the additional logic (U8, gates D and C) ahead of the S-R flip flop (formed from gates A and B of U2&3). The entire state machine is shown below:

<p width=100%, align="center">
<img width=80%, src="https://github.com/m0xpd/EUCLIDplus/blob/main/Operation/Collateral/EUCLID%2B%20State%20Machine.png">
</p>

This amounts to what I describe as 'conditional modulation', for want of a better phrase. Rather than simply forming the logical AND of the clock and the internal oscillator (equivalent to multipliying the signals), derivation of the FIRST signal and its use in the formation of the SET input to the second S-R fip flop imposes a conditionality upon the modulation, which gives the interesting rhythmic patterns we seek. 

When x is not an integer, there are not a fixed number of periods of the 'Osc' signal in the repeat period (L times the clock period). This can make the resulting output change continually, which can give a useful result (particularly if x is close to an integer or is close to a ratio of small integers, like x~3/2, x~7/5 etc). 

However, EUCLID+ can also work with non-integer values of x by hard-syncing the internal Oscillator to the output of its internal clock divider, which is provided for this purpose. The non-integer values can generate additional (non-Euclidean) patterns in synchronous mode, including some "dotted" effects.

In practice, it is not possible to set the oscilator to an exact integer value of x, because of drift in the oscillator and - indeed - because there may be drift in the incoming clock. For this reason, the synchronous mode is used in all cases where a fixed, periodic output sequence is sought and the asychronous more is used when a free, evolving pattermn is required.

Variations arising from the inherent drift of EUCLID+'s simple VCO are seen as a positive feature of this system; those seeking more 'metronomic' and regular Euclidean Rhythm sources are encouraged to use one of the existing software-based solutions on the market. These variations give EUCLID+ a human / 'organic' feel, which I believe is associated to that which is sought by those who prefer 'analog' to 'digital' methods in synthesis (although, of course, EUCLID+ is mainly a swithchig/logic/*digital* system).  




References

(1) 
