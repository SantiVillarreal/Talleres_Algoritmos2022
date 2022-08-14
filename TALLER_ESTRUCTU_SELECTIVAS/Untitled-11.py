


temp = int(input("Digite la temperatura en grados farenheit: "))
deporte = ""

if temp > 85:
    deporte = "Natacion"
elif (temp > 70) and (temp <= 85):
    deporte = "Tenis"
elif (temp > 32) and (temp <= 70):
    deporte = "Golf"
elif (temp > 10) and (temp <=32):
    deporte = "Esquí"
else:
    deporte = "Marcha"

print(f"Si la temperatura es de {temp}°F, se puede practicar {deporte}")