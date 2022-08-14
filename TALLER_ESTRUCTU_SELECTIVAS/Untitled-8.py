
P = int(input("Digite el valor de P: "))
Q = int(input("Digite el valor de Q: "))
t = (P**3)+(Q**4)-(2*P**2)
if(t < 680):
    print(str(P),"y"+str(Q),"No satisfacen la expresión")
elif(t > 680):
    print(str(P),"y"+str(Q),"Satisfacen la expresión")