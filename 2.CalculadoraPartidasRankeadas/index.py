def calcularRank(vitorias, derrotas):
  saldo = vitorias - derrotas
  
  if saldo <= 10:
    rank = 'Ferro'
  elif 11 <= saldo <= 20:
    rank = 'Bronze'
  elif 21 <= saldo <= 50:
    rank = 'Prata'
  elif 51 <= saldo <= 80:
    rank = 'Ouro'
  elif 81 <= saldo <= 90:
    rank = 'Diamante'
  elif 91 <= saldo <= 100:
    rank = 'Lendário'
  elif saldo > 100:
    rank = 'Imortal'

  print("- O Herói tem saldo de" , saldo ," e está no nível de" , rank)

VITORIA = int(input('Digite o numéro de Vitórias:'))
DERROTA = int(input('Digite o numéro de Derrotas:'))

calcularRank(VITORIA,DERROTA)



