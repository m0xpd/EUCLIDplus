# EUCLID+ Operation

This section contains a description of the principles behind EUCLID+ and a detailed description of the implementation of these principles in the module hardware.

A [defining property](https://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf) of Euclidean Rhythms (*E*'s) is the fact that an *E* of length L having N onsets is the most even distribution of the N onsets over L beats. 
This led me to investigate the idea of setting a switching waveform of period L/x against the period, L, where x is continuously variable. When x is a simple positive integer 
(1, 2, 3, ...) this just gives a exact number of periods of the internal oscillator for every period, L, and will identify the perfect division of L into x sections.

If we could identify the FIRST of the clock pulses which occur in each of these sections, we shall have found the most even distribution of x pulses - 
a Euclidean Rhythm of Length=L and Density=x, *E*(x,L).

For example, the graphic below shows an idealised Clock signal and the internal oscilator signal, 'Osc', set to L = 8, x = 3

<p width=100%, align="center">
<img width=80%, src="https://github.com/m0xpd/EUCLIDplus/blob/main/Operation/Collateral/State%20Machine%20Operation%20Principle.png">
</p>

The first clock pulse within each period of the 'Osc' signal is identified in red - readers familiar with Euclidean Rhythms will recognise the result as a valid *E*(3,8).

This is what EUCLID+ does - it takes the incoming clock signal and turns it into a pulse train at the clock leading edge (using a one-shot/monostable around U1A) 
and generates a high duty cycle signal, 'Osc', from the internal VCO. The first clock pulse in every period of the VCO signal is identified by the signal FIRST, which is held on a 
S-R flip-flop (implemented on gates A and B of U2&3). When FIRST is true, the output is set when both the internal oscillator (Osc) and the clock are true (i.e. the system just ANDs 
the clock and internal oscillator together for the first pulse). HOWEVER, for subsequent clock pulses (when FIRST is false) no output is produced. 

This is achieved by the additional logic (U8, gates D and C) ahead of the S-R flip flop (formed from gates A and B of U2&3). The entire state machine is shown below:

<p width=100%, align="center">
<img width=80%, src="https://github.com/m0xpd/EUCLIDplus/blob/main/Operation/Collateral/EUCLID%2B%20State%20Machine.png">
</p>

This amounts to what I describe as 'conditional modulation', for want of a better phrase. Rather than simply forming the logical AND of the clock and the internal oscillator (equivalent to multipliying the signals), derivation of the FIRST signal and its use in the formation of the SET input to the second S-R fip flop imposes a conditionality upon the modulation, which gives the interesting rhythmic patterns we seek. 

When x is not an integer, there are not a fixed number of periods of the 'Osc' signal in the repeat period (L times the clock period). This will make the resulting output change every period, which can give a useful result (particularly if x is close to an integer or is close to a ratio of small integers, like x ~ 3/2,  x ~ 7/5 etc). 

EUCLID+ is capable of hard-syncing the internal Oscillator to the output of its internal clock divider, which is provided for this purpose. This will force a periodic output, even with non-integer x. The  non-integer values generate additional (non-Euclidean) patterns in synchronous mode, including some "dotted" effects.

In practice, it is not possible to set the oscilator to an exact integer value of x, because of drift in EUCLID+'s oscillator and - indeed - because there may be drift in the incoming clock. For this reason, the synchronous mode is used in all cases where a fixed, periodic output sequence is sought and the asychronous mode is used when a free, evolving pattern is required.

Variations arising from the inherent drift of EUCLID+'s simple VCO are seen as a positive feature of the system; those seeking more 'metronomic' and regular Euclidean Rhythm sources are encouraged to use one of the existing software-based solutions on the market. These variations give EUCLID+ a human / 'organic' feel, which I believe is associated to that which is sought by those who prefer 'analog' to 'digital' methods in synthesis (although, of course, EUCLID+ is mainly a switching/*digital* system).  Those wishing to explore the method of Euclidean Rhythm generation without messing with hardware can look at the Python version described here.

Having outlined the principle of operation, I'll now give a description of the main circuit blocks in the electronics.

# Circuit Description

EUCLID+ is realised using 4000 series logic and op-amps, on two Printed Circuit boards, the schematics of which are described separately below.

## Main Board

The Main Board schematic is linked below (click on the graphic to open the file, which you can then download, or work with the KiCad .sch file in your PCB program).

<p width=100%, align="center">
<img width=100%, src="https://github.com/m0xpd/EUCLIDplus/blob/main/Operation/Collateral/EUCLID%2B%20Main%20Board%20Schematic.svg">
</p>

Working around the schematic, reading left to right and down the page, we first meet:

## CLOCK PROCESSING
which accepts an externally applied clock signal from the Control Board. It is inverted by U1B, to produce the (positive-definite) signal _INPUT. It is also recitified to produce the (positive-definite) signal INPUT' and passed to an edge deterctor, to generate dPINPUT. The input signal also triggers a one-shot (U1A), the output of which is passed to another edge detector, which produces a signal dNINPUT, at the end of the one-shot's pulse.

The POWER, BOARD INTERFACE and POWER DISTRIBUTION blocks are trivial.

The **State Machine** has already been discusssed (above).

## INTERNAL OSCILLATOR
The VCO is a standard Shaner (a.k.a. "Synthmonger") 40106 oscillator, first published [here](https://electro-music.com/forum/topic-28799.html) back in 2008, which I have modified slightly to include the hard-sync (Q3, driven by enabling logic in U8 A&B). I ahve also d.c. coupled the oscilaltor to the subsequent comparator stages (U6 B&C) to avoid the long time constants associated with the low frequencies of operation, which would accompany a filtering approach. U6B generates the high duty cycle Osc signal, whilst U6C makes an approximately square signal for the MULT output. An edge detector generates a pulse on the rising edge of the Osc signal ('dOsc'), which is buffered by spare gates in the 40106 to ensure it is at adequate level to drive logic.

## CLOCK DIVIDER A to D CONVERTER
The clock divider requires a parallel digital input. This would have been easiest to generate with a PIC or similar device reading the voltage on a potentiometer, but I wanted to make this a 'hardware-only' project. Accordingly, a ladder-type ADC is used, based on op-amp comparators. Precedents for this type of design exist in two-bit form [here](https://sfcs.neocities.org/module/SFP37/) and - more importantly - in a four-bit version [here](https://modwiggler.com/forum/viewtopic.php?p=464251#p464251). The structure is easy to extrapolate to five bits, but performance becomes sensitive to (e.g.) resistor tolerances at this resolution - I wouldn't fancy pushing the method beyond 5 bits! Still, it is working well-enough for this application.

## CLOCK DIVIDER
My original prototype used a simple 4017 decade counter, which was inadequate to achieve the 12 and 16 count sequences which are of inteest among Euclidean Rhythms, forcing me to look to a different approach. 4017s are actually difficult to cascade in this type of application, so I used instead a 4024 7-stage counter, U11. I am using five of its stages to achieve the 5-bit count I require and detecting when I reach the end of the count using 4030 XOR gates, U9 & U10. the outputs of the XOR gates are ORed together by a 5 input OR gate formed by D14, D15, D16, D19 & D23 and Q5 and adjactent resistors. This OR gate resets the 4024 to 0 and sets the output flip-flops U5 A&B by clocking them when the count reaches the number set on the A to D converter. Note that this has to be the desired output period (L) + 1; in other words to get an output with period 8, you set "9" (0, 1, 0, 0, 1) on the divider display LEDs.

Additionally, the system can be reset (e.g. to align the clock to an external reference beat on the clock, such as a "bar line") by the RESET signal.

## Control Board

The Control Board schematic is linked below (click on the graphic to open the file, which you can then download, or work with the KiCad .sch file in your PCB program).

<p width=100%, align="center">
<img width=100%, src="https://github.com/m0xpd/EUCLIDplus/blob/main/Operation/Collateral/EUCLID%2B%20Control%20Board%20Schematic.svg">
</p>

The Control Board hosts all User Interface controls, and all Inputs and Outputs. It also contains some signal conditioning circuitry to support the IO functions.

Working L to R and top to bottom on the schematic:

## SYNC / FREE Control

Switching between synchronous and asynchronous mode is achieved by pressing the pushbutton SW1, which causes toggling action of the flip-flop formed by op-amp stage U1A.

An external input exceeding approximately 1.5V applied to the Sync Input U$3 will drive the output of comparator stage U1B high.

The outputs of U1A and U1B are ORed togther by D1, D2 & R11. If either output is high, the synchronous mode is enabled (ESYNC = 1) and D3 is illuminated.

## DIVIDE Control
The clock divider is set by a control voltage 'ADC_IN' which is the sum of a local voltage set on VR2 and the voltage input to the Divide input, U$1, applied to the attenuverted formed by U1C. C2 is critical to ensure sufficient noise rejection.

## CLOCK INPUT
A signal applied to the Clock input U$2 exceeding approx 1.5V will cause the output of comparator stage U2D ('CLOCK_IN') to go high.

## VCO Control
The internal oscillator frequency is set by the control voltage 'VCO_IN' formed of the sum of a local voltage set on VR4 and the voltage input to the Freq input, U$5, applied to the attenuverted formed by U2A. 

## DIVIDE LENGTH DISPLAY
The resistor network RN1 (in common with RN1 on the main board) is an 8-commoned package, of which only five resistors are used. I find these earier to source than other configurations. 
You should chose the resistance to give appropriate brightness with your LEDs - remember that the resistors and the LEDs are dropping 24V in this case. 10k worked for me, but your LEDs may not be the same as mine.

## OUTPUTS
The output stages are all similar, common collector types. Again, choose the current limiting resistors R41, R42, R43, R51 & R52 to suit your diodes (this time dropping 11.5V).

The COMP output stage is slightly different than the rest, as it incorporates a diode AND gate (D14, D15) to combine the _Q signal with the system clock.

