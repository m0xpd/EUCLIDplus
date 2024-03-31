# EUCLID+ in Software

This folder describes a software implementation of the principles behind EUCLID+

There is a basic coding of the EUCLID+ method in [MicroPython](https://micropython.org/) [here](https://github.com/m0xpd/EUCLIDplus/blob/main/Software%20Version/EuclidPlus.py), intended to run on the [Raspberry Pi PICO](https://www.raspberrypi.com/products/raspberry-pi-pico/). It could easily be ported to RPi platforms, such as [EuroPi](https://allensynthesis.co.uk/modules/europi.html). 

I have also sketched a partial KiCad project showing how the code could be supported by hardware which could easily be elaborated into a module. 

The code and hardware were validated at breadboard level on a simple system, shown below:

<p width=100%, align="center">
<img width=60%, src="https://github.com/m0xpd/EUCLIDplus/blob/main/Software%20Version/Platform/EUCLID%2B%20Pi%20Prototype.png">
</p>

The example system and its circuitry included only manual controls (for clock division, internal oscillator frequency, etc) with no provision for Voltage Control. These could readily be included using standard methods. 

The pin allocation for the RPi is shown below:

<p width=100%, align="center">
<img width=60%, src="https://github.com/m0xpd/EUCLIDplus/blob/main/Software%20Version/Platform/EUCLID%2B%20Pi%20Prototype.png">
</p>
