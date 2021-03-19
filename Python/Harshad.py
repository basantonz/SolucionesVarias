#Se solicita al usuario un dato y este es guardado en formato String
numero=str(input("Ingresa el número que deseas comprobar que sea Harshad: "))
acum=0
#Usamos el tamaño del número como iterador y acumulamos cada valor por separado convertido en Int
for i in range(len(numero)):
	acum+=int(numero[i])
#Convertimos nuestra variable a entero
numero=int(numero)
#Verificamos que ya acumulado es Harshad mediante la división del número entre nuestro número acumulado
#Mostramos mensajes dependiendo del resultado
if int(numero)%acum==0:
	print(f"{numero}/{acum} = {int(int(numero)/acum)} ... es divisible, por tanto es un número Harshad.")
else:
	print(f"{numero}/{acum} = {int(numero)/acum} ... no es divisible, por tanto no es un número Harshad.")