import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("ressf01","Mot2Passe")
print(wlan.isconnected())