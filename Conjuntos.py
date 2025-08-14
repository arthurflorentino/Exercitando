# Suponha que você foi contratado para desenvolver uma funcionalidade
# no sistema do RH de um novo banco digital. Esse banco teve acesso
# ao cadastro de clientes de outras três empresas concorrentes
# (Nubank, C6 e Inter) e gostaria de saber quais são os potenciais
# clientes. Para isso, pediu que você gerasse um relatório com 12
# items. Atenção, use apenas um print por item.

nubank = set(['ana', 'bia', 'clara', 'duda', 'fabio'])
c6     = set(['bia', 'elena', 'fabio', 'gabriel', 'helio'])
inter  = set(['duda', 'fabio', 'ilma', 'joão', 'katia', 'luiza'])

# 01) Quais são os clientes de cada uma, separadamente.
print(f'1) Nubank: {nubank - c6 - inter};\n C6: {c6 - nubank - inter};\n Inter: {inter - nubank - c6}.\n')

# 02) Quais são os clientes de todas as concorrentes.
print(f'2) Todos clientes: {nubank | c6 | inter}.\n')

# 03) Quais são os clientes da Nubank que também são clientes do C6.
print(f'3) Nubank e C6: {nubank & c6}\n')
    
# 04) Quais são os clientes da Nubank que também são clientes do Inter.
print(f'4) Nubank e Inter: {nubank & inter}\n')

# 05) Quais são os clientes do C6 que também são clientes do Inter.
print(f'5) C6 e Inter: {c6 & inter}\n')

# 06) Quais são os clientes apenas da Nubank.
print(f'6) Nubank: {nubank - c6 - inter}\n')

# 07) Quais são os clientes apenas do C6.
print(f'7) C6: {c6 - nubank - inter}\n')

# 08) Quais são os clientes apenas do Inter.
print(f'8) Inter: {inter - nubank - c6}\n')

# 09) Clientes da Nubank e C6, mas não das duas ao mesmo tempo.
print(f'9) Nubank e C6: {(nubank | c6) - (nubank & c6)}\n')

# 10) Clientes da Nubank e Inter, mas não das duas ao mesmo tempo.
print(f'10) Nubank e Inter: {(nubank | inter) - (nubank & inter)}\n')

# 11) Clientes do C6 e Inter, mas não dos dois ao mesmo tempo.
print(f'11) C6 e Inter: {(c6 | inter) - (c6 & inter)}\n')

# 12) Quais são os clientes das três simultaneamente.-
print(f'12) Simultaneamente das 3: {(nubank & c6 & inter)}\n')