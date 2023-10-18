nota = 9.0

if(nota>=7.0):
    situacao = 'aprovado'
elif(nota>=5.0):
    situacao = 'em recuperação'
else:
    situacao = 'reprovado'

print(f'O estudante está:{situacao} ')