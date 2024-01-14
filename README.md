##### Raspberry Pico Wireless.

Objectif :
Tester la fonctionnalité Wifi du Raspberry Pico.  

Pour en savoir plus : 
[https://how2electronics.com/getting-started-with-raspberry-pi-pico-w-using-micropython/](https://how2electronics.com/getting-started-with-raspberry-pi-pico-w-using-micropython/)  
[https://dev.webonomic.nl/scanning-network-with-the-raspberry-pi-pico-w](https://dev.webonomic.nl/scanning-network-with-the-raspberry-pi-pico-w)  


#### 1/ Présentation du Raspberry Pico W.

Documentation officiel : 
[https://docs.micropython.org/en/latest/library/network.WLAN.html#class-wlan-control-built-in-wifi-interfaces](https://docs.micropython.org/en/latest/library/network.WLAN.html#class-wlan-control-built-in-wifi-interfaces)  

Le Pico W a 2 interfaces réseaux sans-fils :  

- network.STA_IF : L'interface 'station' ou 'standard'  
Cette interface par défaut est utilisé pour connecter le Pico W à un autre point d'accès wifi.  

- network.AP_IF : l'interface 'point d'accès'/'access-point'  
Cette interface est utilisé pour mettre le Pico W en un point d'accès Wifi.  
Il est possible d'y connecter 4 appareils en même temps.  


#### 2/ Installer la dernière version du firmware qui est téléchargeable ici : 

[https://micropython.org/download/rp2-pico-w/](ttps://micropython.org/download/rp2-pico-w/)


#### 3/ Script pour scanner des points d'accès : scanap_v2.py

En résultat, on obtient :

numéro, ssid, bssid, canal, RSSI, sécurité, caché

Pour le champs 'sécurité' : 

```
0 : Ouvert
1 : WEP
2 : WPA-PSK
3 : WPA2-PSK
4 : WPA/WPA2-PS
```

Pour le champs caché : 
```
0 : Visible
1 : Caché
```


####4/ Script pour se connecter à réseau sans-fil : conres_v2.py

En résultat, on obtient : 
Adresse ip, masque de sous-réseau, gateway, serveur DNS


#### 5/ Script de création de serveur web en tant que 'station' : server_station_v1.py

Pour en savoir plus :
[https://www.petecodes.co.uk/creating-a-basic-raspberry-pi-pico-web-server-using-micropython/](https://www.petecodes.co.uk/creating-a-basic-raspberry-pi-pico-web-server-using-micropython/])

Ce script permet de contrôler l'allumage et l'extinction de la DEL verte du Raspberry Pico via une page web.

Voici une erreur possible : 

```
OSError: [Errno 98] EADDRINUSE
```

Solution : 

```
Enlever le Raspberry Pico, attendre quelques secondes et le rebrancher.
```


#### 6/ Script de création de serveur web en tant que 'point d'accès' : server_accesspoint_v1.py

Pour en savoir plus :
[https://microcontrollerslab.com/raspberry-pi-pico-w-soft-access-point-web-server-example/](https://microcontrollerslab.com/raspberry-pi-pico-w-soft-access-point-web-server-example/)



Lorsque le script est lancé, dans la fenêtre 'shell' est indiqué l'adresse ipv4 du point d'accès : 

```
Connection is successful
('192.168.4.1', '255.255.255.0', '192.168.4.1', '0.0.0.0')
```

Soit : 192.168.4.1


Avec un smartphone, se connecter au point d'accès : RPI_PICO_AP

Puis taper dans la barre d'adresse internet du navigateur : 
[http://192.168.4.1](http://192.168.4.1)

Une page web s'affiche avec titre : 
Bienvenue sur le point d'accès RaspPico


Dans la fenêtre 'Shell', s'affiche l'adresse ip du matériel connecté au point d'accès : 

```
Got a connection from ('192.168.4.16', 36222)
Content = b'GET / HTTP/1.1\r\nHost: 192.168.4.1\r\nUser-Agent: Mozilla/5.0 (Android 8.1.0; Mobile; rv:94.0) Gecko/94.0 Firefox/94.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: fr-FR\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'
```
