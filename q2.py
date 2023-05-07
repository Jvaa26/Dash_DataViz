print("Fast-food McPluto's - Mariana")
vP = float(input('Valor do pedido: R$ '))
ind = int(input('Quantidade de indicacoes'))

if vP > 0 and ind >= 0:
    if ind > 11:
        
        d = 0.14
    elif ind >= 5:
        d = 0.11
    elif ind > 1:
        d = 0.8
    elif ind == 1:
        d = 0.4
    else:
        d = 0
    vF = vP - (vP*d)
    print(f'Valor final: {vF:.2f}')
    vPag = float(input('Valor pago: '))
    while vPag < vF:
        vPag = float(input('Valor incompativel ,valor pago: '))
    t = vPag - vF
    print(f'Troco: {t}')
else:
    print('Erro nas entradas')