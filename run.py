from mpd import MPDClient
import 	RPIO

ip_addr = "127.0.0.1"
port = 6600;

client = MPDClient()
client.timeout = 10
client.idletimeout = None

keymap = {
	23: 'play',
	22: 'pause',
	27: 'next',
	24: 'prev',
	25: 'unmapped1',
	17: 'none' 
}

print("Connecting.. ")
client.connect(ip_addr, port)
print("Connected to " + ip_addr + ":" + str(port))

def gpio_callback(channel, val):

	if(val == 0):
		return

	action = keymap[channel]

	print 'Edge detected on channel {0}, mapped to action "{1}".'.format(channel, action)

	if(action == "play"):
		client.play()
	elif(action == "pause"):
		client.pause()
	elif(action == "next"):
		client.next()
	elif(action == "previous"):
		client.previous()

# RPIO.setmode(RPIO.BOARD)

for gpio_id in keymap:
	RPIO.setup(gpio_id, RPIO.IN)
	RPIO.add_interrupt_callback(gpio_id, gpio_callback, edge='rising', debounce_timeout_ms=200)

RPIO.wait_for_interrupts()

RPIO.cleanup()
client.close()
client.disconnect()
