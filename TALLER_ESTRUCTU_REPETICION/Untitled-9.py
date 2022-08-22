
alc= 0
gas= 0
die= 0
t= 0
while t!=4:
    t=int(input())
    if t==1:
        alc=alc+1
    if t==2:
        gas=gas+1
    if t==3:
        die=die+1
print("MUITO OBRIGADO")
print("Alcool: " + str(alc))
print("Gasolina: " + str(gas))
print("Diesel: " + str(die))