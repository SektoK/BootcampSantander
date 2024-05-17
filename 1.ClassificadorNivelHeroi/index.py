heroi = input("Qual o nome do seu personagem?")
exp = int(input("Entre 1000 e 10000, qual o nível de experiência?"))

if exp <= 1000:
    xp = 'Ferro'
elif 1001 >= exp <= 2000 :
    xp = 'Bronze'
elif 2001 >= exp <= 5000 :
    xp = 'Prata'
elif 5001 >= exp <= 7000 :
    xp = 'Ouro'
elif 7001 >= exp <= 8000 :
    xp = 'Platina'
elif 8001 >= exp <= 9000 :
    xp = 'Ascendente'
elif 9001 >= exp <= 10000 :
    xp = 'Imortal'
elif exp > 10000 :
    xp = 'Radiante'
print('O seu herói chamado '+heroi+', foi classificado para a classe ' ,xp+ ', parabéns!' )

##Se XP for menor do que 1.000 = Ferro
##Se XP for entre 1.001 e 2.000 = Bronze
##Se XP for entre 2.001 e 5.000 = Prata
##Se XP for entre 5.001 e 7.000 = Ouro
##Se XP for entre 7.001 e 8.000 = Platina
##Se XP for entre 8.001 e 9.000 = Ascendente
##Se XP for entre 9.001 e 10.000 = Imortal
##Se XP for maior ou igual a 10.001 = Radiante

##- Variáveis
##- Operadores
##- Laços de repetição
##- Estruturas de decisões