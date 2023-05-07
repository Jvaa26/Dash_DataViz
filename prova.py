def nota(m):
    p = 1
    s = 0
    for i in m:
        n = -1
        while n < 0 or n>10:
            n = float(input(f'Nota em {i}: '))
        n = n*p
        p = p+1
        s = n + s
    media = s/6
    return media

materias = ['BCC124','BCC730','BCC846']

print('DECOM - Projeto estagio')
nome = input('Nome: ')
nF = nota(materias)

if nF > 7:
    print('Pode participar com remuneracao')
elif nF >= 5.5:
    print('Pode participar sem remuneracao')
else:
    print('Nao pode participar')


