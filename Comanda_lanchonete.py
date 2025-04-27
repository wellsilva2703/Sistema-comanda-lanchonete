print('=== Bem vindo a Biroska do Carlão ===')

Lanches = {
    'Bauru = R$12,99',
    'X-burguer = R$15,99',
    'X-tudo = R$21,99',
}

Porções = {
    'Batata frita P = R$9,99',
    'Batata c/ bacon = R$16,99',
    'Frango a passarinho = R$22,99',
}

Bebidas = {
    'Refri lata = R$6,99',
    'Refris 2L = R$11,99',
    'Suco natural = R$13,99',
    'Agua = R$4,99',
}

print(f'"Lanches ->"{Lanches}\n"Porções ->"{Porções}\n"Bebidas ->"{Bebidas}')
print('-'* 65)

print('=== Comanda Cliente ===')

Primeiro_Pedido = input('Qual o Primeiro pedido?\n')
Segundo_Pedido = input('Qual o Segundo pedido?\n')
Terceiro_Pedido = input('Qual o Terceiro pedido?\n')
Valor_primeiro_pedido = float(input('Qual o valor do primeiro pedido:\n'))
Valor_segundo_pedido = float(input('Qual o valor do segundo pedido:\n'))
Valor_terceiro_pedido = float(input('Qual o valor do terceiro pedido:\n'))
Valor_artistico = float(input('Qual o valor do cover artistico?\n'))
print('-'* 65)

print('=== Total da comanda atual ===')

Resultado_Comanda = Valor_primeiro_pedido + Valor_segundo_pedido + Valor_terceiro_pedido
Valor_Total = Resultado_Comanda * Valor_artistico
print(f'O valor final é de R${Resultado_Comanda}, incluindo o cover artistico.')
print('-'* 65)

Forma_Pagamento = input('Qual a forma de pgto?\n')

if Forma_Pagamento == 'Pix': 
    print(f'Pagamento realizado com sucesso')
elif Forma_Pagamento == 'Credito':
    print(f'Pagamento realizado com sucesso')
elif Forma_Pagamento == 'Debito':
    print(f'Pagamento realizado com sucesso')
elif Forma_Pagamento == 'Dinheiro':
    print(f'Pagamento realizado com sucesso')
else:
    print('Não aceitamos Cheque!!')  
print('=== Volte sempre! ===')