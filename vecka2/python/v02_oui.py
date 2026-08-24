vendors = {
    "a4:c3:f0": "Intel",
    "3c:d9:2b": "Hewlett-Packard",
    "00:1a:a1": "Cisco Systems",
    "a8:2b:dd": " LCFC(Hefei) Electronics Technology co., ltd"
}
#byt ut mot riktiga mac adresser sen
addresses = [
    "a4:c3:f0:11:3a:b7",
    "3c:d9:2b:2d:11:88",
    "a8:2b:dd:dc:67:7e",
    
]
for address in addresses:
    prefix = address [0:8]
    if prefix in vendors:
        name = vendors[prefix]
    else:
        name = "okand tillverkare"
    print (f"{address} -> {name}")
