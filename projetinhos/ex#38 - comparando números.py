n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O \033[32mPRIMEIRO\033[m número é \033[34mMAIOR\033[m!')
elif n2 > n1:
    print('O \033[32mSEGUNDO\033[m número é \033[34mMAIOR\033[m!')
else:
    print('\033[32mOs DOIS\033[m números são \033[34mIGUAIS\033[m!')
