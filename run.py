# -*- coding: utf-8 -

from mpd import MPDClient, MPDError
from select import select
from time import sleep
import 	RPIO

# Config
ip_addr = "127.0.0.1"
port = 6600;

# Setup MDP
client = MPDClient()
# client.timeout = 10
# client.idletimeout = None

keymap = {
	23: 'play',
	22: 'pause',
	27: 'next',
	24: 'prev',
	25: 'makeout',
	17: 'none' 
}



def connect():

	client.connect(ip_addr, port)
		


def disconnect():
	global client

	try:
		client.close()

	except (MPDError, IOError):
		pass

	try:
		client.disconnect()
	
	except (MPDError, IOError):
		client = MPDClient()


def trySendAction(action, retry=True):
	try:
		if(action == "play"):
			client.play()
		elif(action == "pause"):
			client.pause()
		elif(action == "next"):
			client.next()
		elif(action == "previous"):
			client.previous()
		elif(action == "makeout"):
			client.clear();
			client.add('spotify:user:niklass0n:playlist:5sWsYBtvkFAMTsNRnxDkmu');
			client.play();
	except (MPDError, IOError):
		if retry:
			disconnect()
			try:
				connect()
				return trySendAction(action, retry=False)
			except (MPDError, IOError):
				return False

		return False


def gpio_callback(channel, val):

	if(val == 0):
		return

	action = keymap[channel]

	print 'Edge detected on channel {0}, mapped to action "{1}".'.format(channel, action)

	tries = 0
	while tries < 3:
		if trySendAction(action):
			pass
		else:
			tries += 1
			

# Connect
print("Connecting.. ")
connect()
print("Connected to " + ip_addr + ":" + str(port))

# Setup gpio mapping
for gpio_id in keymap:
	RPIO.setup(gpio_id, RPIO.IN)
	RPIO.add_interrupt_callback(gpio_id, gpio_callback, edge='rising', debounce_timeout_ms=200)

# RPIO.wait_for_interrupts(threaded=True)
RPIO.wait_for_interrupts()

RPIO.cleanup()
disconnect()
