import ipaddress

#byt ut mot en adress jag vill räkna på, nu tog jag min egna och lade till /26
text = "192.168.1.128/26"

#modluelt ipadress gör beräkningen
net = ipaddress.ip_network(text, strict=False)

# Alla adresser du kan ge en enhet
usable = list(net.hosts())

print (f"nat:               {net.network_address}")
print (f"Natmask:           {net.netmask}")
print (f"Broadcast :        {net.broadcast_address}")
print (f"Forsta adress:     {usable[0]}")
print (f"Sista adress:      {usable[-1]}")
print (f"Antal enheter:     {len(usable)}")