# EUCLID+ in Software

This folder describes a software implementation of the principles behind EUCLID+

There is a basic coding of the EUCLID+ method in Python [here](https://github.com/m0xpd/EUCLIDplus/blob/main/Software%20Version/EuclidPlus.py), intended to run on the [Raspberry Pi PICO](https://www.raspberrypi.com/products/raspberry-pi-pico/). It could easily be ported to other RPi-based platforms, such as [EuroPi](https://allensynthesis.co.uk/modules/europi.html). 

The code certainly isn't pretty - I hacked it from a Ratcheting clock multiplier application I had been playing with, so many of the variable names and the overall structure didn't start on a blank canvas, which would have been better practice. However, it does the job.

I have also sketched a partial KiCad project showing how the code could be supported by hardware which could easily be elaborated into a module. Most importantly, there's a [.sch file](https://github.com/m0xpd/EUCLIDplus/blob/main/Software%20Version/Platform/EuclidPlusPi.kicad_sch) and a (graphical) schematic...

<p width=100%, align="center">
<img width=60%, src="https://github.com/m0xpd/EUCLIDplus/blob/main/Software%20Version/Platform/EuclidPlusPi%20Schematic.svg">
</p>

The code and hardware were validated at breadboard level on a simple system, shown below:

<p width=100%, align="center">
<img width=60%, src="https://github.com/m0xpd/EUCLIDplus/blob/main/Software%20Version/Platform/EUCLID%2B%20Pi%20Prototype.png">
</p>

The example system and its circuitry include only manual controls (for clock division, internal oscillator frequency, etc) with no provision for Voltage Control. CV inputs could readily be included using standard methods, such as those used in the EUCLID+ module, appropriately adapted for the (0:3V3) operating range of the RPi.

The pin allocation for the RPi is shown below:

<p width=100%, align="center">
<img width=60%, src="https://github.com/m0xpd/EUCLIDplus/blob/main/Software%20Version/Platform/EUCLID%2B%20Pi%20Pin%20Allocation.png">
</p>

Notice that I originally named the main 'RHYTHM' output of EUCLID+ 'PATTERN'. Apologies for this (and any other) notational anomaly.
