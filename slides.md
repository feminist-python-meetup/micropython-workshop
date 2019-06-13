# Feminist MicroPython

<media-tag src="https://pads.c3w.at/blob/07/074d9cdf0847855207eddbe684fbfa636e759549ca933d9f" data-crypto-key="cryptpad:EQV+492ieW88Lgjj7xOmrV8eJDtLGsxy9KWyrPAYoVs="></media-tag>

---

# Overview

- What is MicroPython?
- What is a Microcontroller?
- Internet of Things and the ESP8266
- Connecting to it
- Making it blink
- Coding with your browser
- Short Electronics introduction by Zoé
- What can I do with it?
- (Optional) Automate all the things!

---

# What is MicroPython


Straight from the horses mouth:
>  MicroPython is a lean and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimised to run on microcontrollers and in constrained environments. 

---

# What is a Microcontroller?

> A microcontroller (MCU for microcontroller unit, or UC for μ-controller) is a small computer on a single integrated circuit.


* They're everywhere
* And cheap
* And some are even fun to program


---

# Internet of Things and the ESP8266

* The ESP8266 is everywhere
* Smart lightbulbs
* Smart heating
* Smart surveillance in your own home
* But also: Automation

---

# Connecting to it

Linux/*BSD:

`python -m serial.tools.miniterm /dev/ttyUSB0 115200`

&nbsp;

On Mac `/dev/ttyUSB0` is usually called `/dev/cu.usbserial`, if this doesn't work it should show up under another name in `/dev/cu.*`

---

# Making it blink

Let's get to it!

```python
# We want to toggle a pin
from machine import Pin
# second pin, set as output
led = Pin(2, Pin.OUT)
# toggle the led off and on
led.on()
led.off()
```
---

# Making it blink (2)
```python
import time

for i in range(10):
    led.off()
    time.sleep(0.5)
    led.on()
    time.sleep(0.5)
```
---

# Coding with your browser

In case that you want to use a browser to code

```python
import network
import webrepl
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('CodeFactory1',
             'Everyb0dyCanC0de!!')
webrepl.start()
```

---

# Coding with your browser (2)

Connect to your WiFi at boot time

&nbsp;

Install ampy:

`pip3 install --user adafruit-ampy`

&nbsp;

Push it to the board:

`ampy --port /dev/ttyUSB0 put connect_to_wifi.py /main.py`

&nbsp;

Replace the port with `/dev/cu.usbserial` on Mac again

---

# Short Electronics introduction

The holy trinity of Voltage (U), Resistance (R) and Current (I)

<media-tag src="https://pads.c3w.at/blob/ae/aef327714f940419bf52b545573763064a9e06933b244840" data-crypto-key="cryptpad:aVRuNS0iVH/s+k9YIMCEOW2hc6u1RsJ5F2JDK3fFdlc="></media-tag>

---

# Short Electronics introduction (2)

&nbsp;

&nbsp;


### - Voltage is always *between*

### - Current flows

### - Resistance is ~~futile~~ makes everything harder

---

# What can I do with it?

- Air quality monitoring

- Party light for your fridge

- Door opener for the front door (because your landlord only gave you one key)

- Turn on your coffee-maker at 7am
 - if that's your thing

- Build complex systems to make your life ~~harder~~ easier
 - or just to learn new things

---

# Automate all the things!

Flashing a lot of boards is very repetitive:

&nbsp;

- (Once) Fetch latest firmware
- Erase the flash memory
- Program firmware to flash
- Open connection to board
  - load an example program
  - get output of program
    - if it matches, we're done
    
&nbsp;
    
Code is in `flash_and_check.py`

---
# Have fun with MicroPython!

[Quick reference](http://docs.micropython.org/en/latest/pyboard/quickref.html)

[Documentation](https://docs.micropython.org/en/latest/index.html)

<media-tag src="https://pads.c3w.at/blob/07/074d9cdf0847855207eddbe684fbfa636e759549ca933d9f" data-crypto-key="cryptpad:EQV+492ieW88Lgjj7xOmrV8eJDtLGsxy9KWyrPAYoVs="></media-tag>
