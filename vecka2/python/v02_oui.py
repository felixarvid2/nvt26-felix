vendors = {
    "a4:c3:f0": "Intel",
    "3c:d9:2b": "Hewlett-Packard",
    "00:1a:a1": "Cisco Systems",
    "a8:2b:dd": "LCFC(Hefei) Electronics Technology co., ltd",
    "28:95:29": "Intel Corporate",
    "e0:55:3d": "Cisco Meraki",
}
#byt ut mot riktiga mac adresser sen
addresses = [
    "a4:c3:f0:11:3a:b7",
    "3c:d9:2b:2d:11:88",
    "a8:2b:dd:dc:67:7e",
    "28:95:29:4c:ff:ea",
    "e0:55:3d:e1:27:c0",
    
]
for address in addresses:
    prefix = address [0:8]
    if prefix in vendors:
        name = vendors[prefix]
    else:
        name = "okand tillverkare"
    print (f"{address} -> {name}")
