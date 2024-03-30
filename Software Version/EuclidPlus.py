# EuclidPlus.py
# 
# v0.1
# for the RPi PICO
#
# P Darlington m0xpd
# See https://github.com/m0xpd/EUCLIDplus

from machine import ADC, Pin
from machine import Timer

import time
import math
import array as arr
interrupt_flag=0
sync_interrupt_flag = 0
debounce_time=0
clk_in = Pin(5, Pin.IN, Pin.PULL_UP)	# Clock input
clk_in2 = Pin(6, Pin.IN, Pin.PULL_UP)	# Repeat of the clock to set up a second HW Interrupt!
syncpin = Pin(7, Pin.IN, Pin.PULL_UP)	# Sync Toggle Pushbutton
led = Pin(12, Pin.OUT)					
led2 = Pin(13, Pin.OUT)					
out_clock = Pin(14, Pin.OUT)			
comp = Pin(10, Pin.OUT)					# comp is the COMPLEMENT of the pattern output
div = Pin(11, Pin.OUT)					# div is the DIVIDE output
pattern = Pin(15, Pin.OUT)				# pettern is the main output
syncLED = Pin(16, Pin.OUT)				# sync/free status
FIRSTPin = Pin(17, Pin.OUT)
pot = ADC(26)							# Read Clock Divide Value
pot2 = ADC(27)							# Read Internal Oscillator Frequency
# Declare and inmitialise global variables...
count=0
last_beat=0
beat=0
BPM=10
beta=0.25
Old_Tavg=0
clock_multiply=4
tperiod = 130
tperiod2 = 10
old_tperiod = 10
out_count = 1
Euclid=1
max_count = 4
sync=1
osc = 0
FIRST=0
Q = 0
INPUT = 0
oldINPUT = 0		# Previous values of INPUT in a delay line
old1INPUT = 0
old2INPUT = 0
old3INPUT = 0
        

# A few function definitions....

def synccallback(syncpin):
    # Handle the togging pushbutton to set sync/free operation
    global sync_interrupt_flag, debounce_time
    if (time.ticks_ms()-debounce_time) > 250:
        sync_interrupt_flag= 1
        debounce_time=time.ticks_ms()

def Q_Off(Source):
    # Turn output Off (part of the main State Machine)
    global Q
    Q = 0
    pattern.value(Q)


def callback(clk_in):
    # Handle Leading edge of clock actions...
    global interrupt_flag, debounce_time, beat, last_beat, BPM, beta, Old_Tavg, FIRST, osc, Q
    interrupt_flag= 1
    #Manage STATE MACHINE....
    if((FIRST==1)and(osc==1)):
        Q = 1
        pattern.value(Q)        
    led.value(1)
    led_Timer = Timer(period=5, mode=Timer.ONE_SHOT, callback=LED_Off)
      
      
    if(Q == 0):
        comp.value(1)

def callback2(clk_in2):
    # Handle actions on falling edge of clock
    global Q
    Q = 0
    pattern.value(Q)
    comp.value(0)
    div.value(0)

   
def LED_Off(Source):
    # Set led = 0
    global FIRST, Q    
    FIRST = 0
    FIRSTPin.value(FIRST) 
    led.value(0)


def LED2_Off(Source):
    # set led2 = 0
    led2.value(0)


def Out_Off_Handler(Source):
    # Operate Internal Oscillator (Low Phase) 
    global osc
    osc = 0    
    out_clock.value(osc)
    out_off.init(period=1, mode=Timer.ONE_SHOT, callback=Out_On_Handler)
    


def Out_On_Handler(Source):
    # Operate Internal Oscillator (High Phase)
    global tperiod, FIRST, osc
    osc = 1    
    out_clock.value(osc)
    FIRST = 1
    FIRSTPin.value(FIRST)
    out_on.init(period=tperiod, mode=Timer.ONE_SHOT, callback=Out_Off_Handler)
    
# End of function definitions
#================================================================================
# Now some Timers and Interrupt Requests...


out_on=Timer(period=tperiod, mode=Timer.ONE_SHOT, callback=Out_Off_Handler)
out_off=Timer(period=1, mode=Timer.ONE_SHOT, callback=Out_On_Handler)
syncpin.irq(trigger=Pin.IRQ_RISING, handler=synccallback)
clk_in.irq(trigger=Pin.IRQ_FALLING, handler=callback)
clk_in2.irq(trigger=Pin.IRQ_RISING, handler=callback2)


# This is the main 'Loop'....


while True:
    if interrupt_flag is 1:
          raw = pot.read_u16()                                             # get the clock divide value
          max_count=math.floor(raw * 31 / 65535 ) + 1												
          raw_tperiod = pot2.read_u16()
          tperiod=math.floor(raw_tperiod * 1000 / 65535 ) + 1				# and the internal oscillator frequency     
          led2.value(0)                                                                 
          count = count+1
          if (count>=max_count):
              count = 0
              div.value(1)
              led2.value(1)
              led2_Timer = Timer(period=1, mode=Timer.ONE_SHOT, callback=LED2_Off)
              if (sync==1):
                  out_on.deinit()
                  out_on.init(period=tperiod, mode=Timer.ONE_SHOT, callback=Out_Off_Handler)
                  out_off.deinit()
                  out_off=Timer(period=1, mode=Timer.ONE_SHOT, callback=Out_On_Handler)
                  osc = 0
                  out_clock.value(osc)
          interrupt_flag=0                                                 # reset the interrupt flag

    else:
        old3INPUT = old2INPUT
        old2INPUT = old1INPUT
        old1INPUT = oldINPUT
        oldINPUT = INPUT
        INPUT=clk_in.value()
        if((INPUT==1)and(oldINPUT==1)and(old1INPUT==1)and(old2INPUT==1)and(old3INPUT==1)):
            Q1 = 0
    if(sync_interrupt_flag==1):
        sync_interrupt_flag = 0
        if(sync==1):
            sync=0
            syncLED.value(sync)
        else:
            sync=1
            syncLED.value(sync)
        
