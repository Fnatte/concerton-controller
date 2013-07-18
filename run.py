from mpd import MPDClient
import 	RPIO

ip_addr = "127.0.0.1"
port = 6600;

client = MPDClient()
client.timeout = 10
client.idletimeout = None

print("Connecting.. ")
client.connect(ip_addr, port)
print("Connected to " + ip_addr + ":" + str(port))

def gpio_callback(channel, val):

	if(val == 0):
		return

	print("Edge detected on channel %s."%channel)
	if(channel == 16):
		client.play()
	elif(channel == 15):
		client.pause()
	elif(channel == 13):
		client.next()
	elif(channel == 18):
		client.previous()

RPIO.setmode(RPIO.BOARD)

RPIO.setup(16, RPIO.IN) # Switch 1
RPIO.setup(15, RPIO.IN) # Switch 2
RPIO.setup(13, RPIO.IN) # Switch 3
RPIO.setup(18, RPIO.IN) # Switch 4
RPIO.setup(22, RPIO.IN) # Switch 5
RPIO.setup(11, RPIO.IN) # Switch 6

RPIO.add_interrupt_callback(16, gpio_callback, edge='rising', debounce_timeout_ms=200)
RPIO.add_interrupt_callback(15, gpio_callback, edge='rising', debounce_timeout_ms=200)
RPIO.add_interrupt_callback(13, gpio_callback, edge='rising', debounce_timeout_ms=200)
RPIO.add_interrupt_callback(18, gpio_callback, edge='rising', debounce_timeout_ms=200)
RPIO.add_interrupt_callback(22, gpio_callback, edge='rising', debounce_timeout_ms=200)
RPIO.add_interrupt_callback(11, gpio_callback, edge='rising', debounce_timeout_ms=200)

# GPIO.add_event_callback(16, gpio_callback)
# GPIO.add_event_callback(15, gpio_callback)
# GPIO.add_event_callback(13, gpio_callback)
# GPIO.add_event_callback(18, gpio_callback)
# GPIO.add_event_callback(22, gpio_callback)
# GPIO.add_event_callback(11, gpio_callback)

RPIO.wait_for_interrupts()

RPIO.cleanup()
client.close()
client.disconnect()
