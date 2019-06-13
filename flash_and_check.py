#!/usr/bin/env python3

import esptool
import serial
import urllib.request
import time
from os import path
from urllib.request import urlretrieve

test_prog = """print('hello feminist python meetup!')\r\n"""

# please check on the website if it's *really* the latest version
if not path.isfile('esp8266-latest.bin'):
    urlretrieve(
        'https://micropython.org/resources/firmware/esp8266-20190529-v1.11.bin',
        'esp8266-latest.bin'
    )

erase_command = ['--port', '/dev/ttyUSB0', 'erase_flash']
flash_command = ['--port', '/dev/ttyUSB0', '--baud', '460800',
                 'write_flash', '--flash_size=detect', '0', 'esp8266-latest.bin']

print('Erasing flash with %s' % ' '.join(erase_command))
esptool.main(erase_command)

print('Flashing with %s' % ' '.join(erase_command))
esptool.main(flash_command)

print('waiting for board to reboot')
time.sleep(2)

# test if the flashing was successfull
with serial.Serial('/dev/ttyUSB0', 115200, timeout=1) as ser:
    ser.readline()
    ser.readline()
    print(ser.readline().decode().rstrip())

    ser.write(test_prog.encode())

    ser.readline()
    ser.readline()

    # this line is the echo we get back
    line = ser.readline().decode() # this should be our output
    if line != 'hello feminist python meetup!\r\n':
        print('failed to test this board')
        exit(1)
    else:
        print('board flashed and tested')
