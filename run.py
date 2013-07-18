from mpd import MPDClient

ip_addr = "127.0.0.1"
port = 6600;

client = MPDClient()
client.timeout = 10
client.idletimeout = None

print("Connecting.. ")
client.connect(ip_addr, port)
print("Connected to " + ip_addr + ":" + str(port))

print(client.next())

client.close()
client.disconnect()
