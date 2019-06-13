import network
import webrepl

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('CodeFactory1', 'Everyb0dyCanC0de!!')

webrepl.start()