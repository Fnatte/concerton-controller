# from mpd import MPDClient

# ip_addr = "127.0.0.1"
# port = 6600;

# client = MPDClient()
# client.timeout = 10
# client.idletimeout = None

# print("Connecting.. ")
# client.connect(ip_addr, port)
# print("Connected to " + ip_addr + ":" + str(port))

# print(client.next())

# client.close()
# client.disconnect()

try:
	import 	RPi.GPIO as GPIO
except RuntimeError:
	print("Failed to import RPi.GPIO. Did you run the script with root privileges?")

def gpio_callback(channel):
	print("Edge detected on channel %s."%channel)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.IN) # Switch 1
GPIO.setup(15, GPIO.IN) # Switch 2
GPIO.setup(13, GPIO.IN) # Switch 3
GPIO.setup(18, GPIO.IN) # Switch 4
GPIO.setup(22, GPIO.IN) # Switch 5
GPIO.setup(11, GPIO.IN) # Switch 6

GPIO.add_event_detect(16, GPIO.RISING)
GPIO.add_event_detect(15, GPIO.RISING)
GPIO.add_event_detect(13, GPIO.RISING)
GPIO.add_event_detect(18, GPIO.RISING)
GPIO.add_event_detect(22, GPIO.RISING)
GPIO.add_event_detect(11, GPIO.RISING)

GPIO.add_event_callback(16, gpio_callback)
GPIO.add_event_callback(15, gpio_callback)
GPIO.add_event_callback(13, gpio_callback)
GPIO.add_event_callback(18, gpio_callback)
GPIO.add_event_callback(22, gpio_callback)
GPIO.add_event_callback(11, gpio_callback)

GPIO.wait_for_interrupts()
GPIO.cleanup()
