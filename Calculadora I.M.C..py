# Nombre: Francisco Javier Salas Palomo
# Matrícula UTEL: 010610548

# Tarea Calculadora I.M.C. Curso - Fundamentos de Python.

#Aquí se declaran las variables y su contenido y formato de texto o numérico, también se agrega un bloqueo para evitar que los campo queden vacíos

def validar_texto(cadena):
    if not cadena.replace(" ", "").isalpha():
        print("Error: Solo se acepta texto. Ingresa un valor válido.")
        return False
    return True

nombre = input("Ingresa tu nombre((s): ")
while not validar_texto(nombre):
    nombre = input("Ingresa tu nombre(s) (campo obligatorio): ")


apellido_pa = input("Ingresa tu apellido paterno: ")
while not apellido_pa or not validar_texto(apellido_pa):
    apellido_pa = input("Ingresa tu apellido paterno (campo obligatorio): ")

apellido_ma = input("Ingresa tu apellido materno: ")
while not apellido_ma or not validar_texto(apellido_ma):
    apellido_ma = input("Ingresa tu apellido materno (campo obligatorio): ")

edad = None
while edad is None:
    try:
        edad = int(input("Ingresa tu edad: "))
    except ValueError:
        print("Entrada inválida. Ingresa un valor numérico.")

peso = None
while peso is None:
    try:
        peso = float(input("Ingresa tu peso (kg): "))
    except ValueError:
        print("Entrada inválida. Ingresa un valor numérico.")

estatura = None
while estatura is None:
    try:
        estatura = float(input("Ingresa tu estatura (m): "))
    except ValueError:
        print("Entrada inválida. Ingresa un valor numérico.")

# Aquí se imprimen los resultados.

print(" Nombre: " + nombre + " " + apellido_pa + " "+ apellido_ma)
print(" Su edad:", edad, "años")
print(" Su peso:", peso, " kg")
print(" Su estatura: ", estatura, " m\n")
imc = round((peso/(estatura)**2),2)
print("Su I.M.C. es: ",imc)


# Aquí declaro los indicadores de las masas coporales si cumplen algun criterio manden el mensaje segun corresponda.
print("**************************")
if imc <= 18.5:
    print("\n Tienes bajo peso, te recomendamos acudir con el nutriólogo ")
    print("*****************************************************************\n")

if 18.5 < imc < 24.9:
    print("\n   Su peso es normal")
    print("*********************\n")

if 25 < imc < 29.9:
    print("\n   Tienes sobre peso")
    print("***********************\n")

if 30 < imc < 34.5 :
    print("\n   ¡ Tienes obesidad Grado 1, te sugerimos acudir con un nutriólogo para cuidar tu salud !")
    print("*******************************************************************************************\n")

if 35 < imc < 39.5 :
    print("\n   ¡ Tienes obesidad Grado 2, te sugerimos acudir con un nutriólogo para cuidar tu salud !")
    print("*******************************************************************************************\n")

if  39.5 < imc < 40 :
    print("\n   ¡ Tienes obesidad Grado 3, te sugerimos acudir con un nutriólogo para cuidar tu salud !")
    print("*******************************************************************************************\n")

print("""-------->╔══╗
         ╚╗╔╝
         ╔╝(¯`v¯)
         ╚══`.. MI SALUD Y ME CUIDO ! \n""")

print("=================== By Francisco Javier Salas Palomo ======================")
print("====================== Matrícula UTEL: 010610548 ==========================")
print("======== Tarea Calculadora I.M.C. Curso - Fundamentos de Python ===========\n\n")




# Fuente de consulta de medidas de IMC "http://www.nutrisanaeducacion.com/indice-de-masa-corporal/"


#Fin del programa.

#Gracias por lo que nos enseñaron.
