
# Entradas
from lib2to3.pgen2 import grammar


au = float(input("Digite los chelines autríacos\n"))
gr = float(input("Digite los dracmas griegos\n"))
ps = float(input("Digite las pesetas\n"))

# Caja negra
a = (au * 956871)/100
b = gr/22.64572381
c = ps/122499
d = (ps*100)/9289

# Salidas 
print(f"\n{au} Chelines austríacos en pesetas son {a}\n{gr} Dracmas griegos en Francos franceses son {b}\n{ps} Pesetas en Dolares son {c}\n{ps} Pesetas en Liras italianas son {b}\n")
