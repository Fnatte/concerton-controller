from mpd import MPDClient
import 	RPi.GPIO as GPIO

ip_addr = "127.0.0.1"
port = 6600;

client = MPDClient()
client.timeout = 10
client.idletimeout = None

print("Connecting.. ")
client.connect(ip_addr, port)
print("Connected to " + ip_addr + ":" + str(port))

def gpio_callback(channel):
	print("Edge detected on channel %s."%channel)
	if(channel == 16):
		client.play()
	elif(channel == 15):
		client.pause()
	elif(channel == 13):
		client.next()
	elif(channel == 18):
		client.previous()

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.IN) # Switch 1
GPIO.setup(15, GPIO.IN) # Switch 2
GPIO.setup(13, GPIO.IN) # Switch 3
GPIO.setup(18, GPIO.IN) # Switch 4
GPIO.setup(22, GPIO.IN) # Switch 5
GPIO.setup(11, GPIO.IN) # Switch 6

GPIO.add_event_detect(16, GPIO.RISING, callback=gpio_callback, bouncetime=100)
GPIO.add_event_detect(15, GPIO.RISING, callback=gpio_callback, bouncetime=100)
GPIO.add_event_detect(13, GPIO.RISING, callback=gpio_callback, bouncetime=100)
GPIO.add_event_detect(18, GPIO.RISING, callback=gpio_callback, bouncetime=100)
GPIO.add_event_detect(22, GPIO.RISING, callback=gpio_callback, bouncetime=100)
GPIO.add_event_detect(11, GPIO.RISING, callback=gpio_callback, bouncetime=100)

# GPIO.add_event_callback(16, gpio_callback)
# GPIO.add_event_callback(15, gpio_callback)
# GPIO.add_event_callback(13, gpio_callback)
# GPIO.add_event_callback(18, gpio_callback)
# GPIO.add_event_callback(22, gpio_callback)
# GPIO.add_event_callback(11, gpio_callback)

raw_input("Press enter to stop.")

GPIO.cleanup()
client.close()
client.disconnect()
