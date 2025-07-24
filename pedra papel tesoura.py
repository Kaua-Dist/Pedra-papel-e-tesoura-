import random 

print('=' * 25,
      'Pedra , papel e tesoura',
      '=' * 25,
      '*uma copia do taunt de tf2*',sep='\n'
      )


def Jogaço():#def = variavel nova
    Opçoes = ['pedra' , 'papel' , 'tesoura']#opçoes gerais
    Player = input('Olá jogador! qual vai ser sua jogada?: ').lower()#o input em geral vai sempre ficar em minusculo
    V1     = random.choice(Opçoes)

    print(f'o V1 escolheu {V1}'  )
    print(f'já vc pegou {Player}')

    
    if Player not in Opçoes:
        print(f'A jogada não é valida!, tente uma da opçoes: {Opçoes}')
        return
    
    if Player == V1: 
        print('Empate')
    
    elif (
        (Player == 'pedra'   and V1 == 'tesoura') or
        (Player == 'papel'   and V1 == 'pedra'  ) or
        (Player == 'tesoura' and V1 == 'papel') 
    ):

        print('voce venceu!!')
    else:
        print('Perdeu >=) V1 wins')  


Jogaço()

