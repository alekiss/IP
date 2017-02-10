#### Indicies de um string

### \n = pular linha

c = "gatos" [0]
n = "Ryan" [3]

print(c)
print(n)

#### Len, Lower, Upper, Str

parrot = "Azul Marinho"

print(len(parrot))
print(parrot.lower())
print(parrot)
print(parrot.upper())
print(parrot)

#####input

nome = input("Digite seu nome")
Idade = input("Tu tem quantos anos em?")
comida = input("Tu come?")

print("Ah então seu nome é %s , sua idade é %s e tu come %s." % (nome,Idade,comida))


### Exercicio

my_string = "Palmeiras"

print(len(my_string))

print(my_string.upper())

###Lembrar das aspas na variavel e de abrir e fechar o parentese quando for printar um upper ou lower

### Usando o DATETIME

from datetime import datetime
now = datetime.now()
print("A hora é... %s " % (now))

### Oraganizando a data e hora no nosso padrão

from datetime import datetime
now = datetime.now()

print("A hora é... %s\%s\%s " % (now.day ,now.month, now.year))

###Continuando com datetime

from datetime import datetime
now = datetime.now()
print("A hora é... %s:%s:%s " % (now.hour, now.minute, now.second))

### Teste Eduardo

