#Programa para el calculo de Indice de Masa Corporal




from ast import If


print("""                           ** BIENVENIDO A LA CALCULADORA DE IMC **
            Calcularemos su Índice de Masa Corporal en base a los datos que nos proporcione""")

#Hacemos la petición y validación de los datos de nombre, apellidos, edad, peso y estatura.

#DATOS DE TIPO CADENA: NOMBRE, APELLIDOS PATERNO Y APELIDO MATERNO.
#Datos que son de tipo cadena como nombre, apellido paterno y materno.
#Inicializamos una variable validaNombre que funciona como bandera para ejecutar el ciclo while para pedir y revisar 
#la cadena "nombre", para que entre al ciclo al menos una vez.
#La condición de while evalua si la cadena es vacía, son espacios en blanco o tiene sólo caracteres alfabeticos (a-z)

validaNombre = ""      
while validaNombre == "" or validaNombre.isspace() or not validaNombre.isalpha(): #Inicia ciclo
    nombre =  input("¿Cuál es tu nombre?: ")                                      #Pide cadena "nombre"
   
    validaNombre = nombre    #el valor de nombre se asigna a la bandera
    

    separarNombre = validaNombre.partition(" ") #Separamos el nombre buscando el primer espacio en blanco de la cadena

    #Una vez separada la cadena nombre, evaluamos dos casos posibles: 
    #1) Es un nombre compuesto por dos nombres. Usamos el método count para localizar un solo espacio en la cadena, y revisamos 
    #que las dos cadenas a los lados del espacio sean alfabeticas.
    #2) Es una cadena exclusivamente alfabetica.
    if validaNombre.count(" ")== 1 and separarNombre[0].isalpha() and separarNombre[2].isalpha() or nombre.isalpha():
        
        validaNombre = separarNombre[0]    #si se cumplen alguno de los casos la bandera Se llena con la cadena 
                                           #para salir del ciclo     
    else:
        print("Dato inválido.")            #Si no se cumple alguno de los dos casos anteriores, la bandera se le asigna      
        validaNombre = ""                  #una cadena vacía para forzar que se se entre de nuevo al ciclo cuando se   
                                           #evalué, pidiendode nuevo cadena de nombre valida. 
    


#Hacemos ciclos similares al anterior para evaluar la petición de apellido paterno y materno pero más sencillos.
validaApPaterno = ""   #iniciamos bandera para forzar entrar al ciclo
while validaApPaterno== "" or validaApPaterno.isspace() or not validaApPaterno.isalpha():
    apPaterno =  input("¿Cuál es tu apellido paterno?: ")   #Peticion de cadena apellido paterno
    validaApPaterno = apPaterno                             #asignamos cadena obtenida a la bandera
    #Validamos si es una cadena vacía, solo espacios o con caracteres no alfabeticos. Si alguno de los tres se cumple
    #informamos al usuario que es inválido su dato y ciclamos para pedirlo de nuevo.
    if validaApPaterno== "" or validaApPaterno.isspace() or not validaApPaterno.isalpha():
        print("Dato inválido.")


#La estructura se repite junto con las condicionales para pedir y validar el aepllido materno
validaApMaterno = ""
while validaApMaterno== "" or validaApMaterno.isspace() or not validaApMaterno.isalpha():
    apMaterno =  input("¿Cuál es tu apellido materno?: ")
    validaApMaterno= apMaterno 
    if validaApMaterno== "" or validaApMaterno.isspace() or not validaApMaterno.isalpha():
        print("Dato inválido.")


#dATOS DE TIPO NUMÉRICO: EDAD, PESO Y ESTATURA. 
#Datos de tipo numerico, ya sean enteros (int) o decimales (float), el primero para la edad y el segundo para
#el peso y la estatura.

#Iniciamos el ciclo while para pedir y validar la edad
validaEdad = ""   #inicio de bandera
#El ciclo evalua si es una cadena vacia, de espacios en blanco o contiene caracateres alfabeticos aparte de digitos

while validaEdad == "" or validaEdad.isspace() or not validaEdad.isdigit():
    
    edad = input("¿Cuál es tu edad en años?: ")    #Peticion de cadena edad
    validaEdad = edad                              #se asigna a la bandera 
    
    #Una condicional If evalua si cadena vacia, espacio blancos o alfabeticos entre los digitos
    if validaEdad == "" or validaEdad.isspace() or not validaEdad.isdigit():
    
        print("Dato inválido.")           #si cumple alguno de los tres casos, infroma al usuario de dato inválido   
        validaEdad =""                    #la bandera se manda a vacío para su evaluación en el while  
    else : 
        edadNumero =int(edad)                    #Si la cadena es válida, se formatea a tipo entero 
        if edadNumero > 99 or edadNumero <= 0:   #limitamos el intervalo de edades a manejar para obtener una edad 
            print("Edad fuera de rango.")        #razonable, entre 1 y 99 años. De no ser asi, informamos de dato 
            validaEdad = ""                      #invalido y limpiamos la bandera al tiempo que con ella entramos 
                                                 #de nuevo al ciclo while  
    

#Iniciamos ciclo while para obtener y validar el peso
validaPeso = ""     #iniciamos bandera
while validaPeso == "" or validaPeso.isspace():    #validamos si es cadena vacia o de espacios
    peso = input("¿Cuál es tu peso en kg?: ")      #Peticion de cadena peso 
    validaPeso = peso                              #asignamos la cadena peso a bandera
    
    

    separarPeso = validaPeso.partition(".")     #separamos la cadena obtenida usando como separador el punto

    #Validamos dos casos respecto a la cadena ya separada
    # 1) La cadena separada tiene un solo punto como separador (con método count), y cadenas de digitos a ambos lados.
    # Esto significaría que el peso lo estan escribiendo con punto decimal  
    # 2) La cadena son puros digitos, lo cual nos indica que el peso nos lo dan en valor entero.

    if validaPeso.count(".")== 1 and separarPeso[0].isdigit() and separarPeso[2].isdigit or peso.isdigit():
        pesoNumero = float(peso)                          #Convertimos la cadena a float. En este punto ya sabemos
                                                           #que es un numero, así que 
        if pesoNumero > 200.00 or pesoNumero <= 0.0:       #Verificamos que peso esté en un intervalo razonable 
            print("Peso fuera de rango.")                  # de valores. Si no. avisamos que esta fuera de rango 
            validaPeso = ""                                # y mandamos la bandera a cadena vacía para el ciclo while 
                                                           #pida de nuevo el valor para peso 
    else:
        print("No es un valor correcto de peso.")          #Cualquier valor que no haya entrado en la validación de los 
        validaPeso = ""                                    #dos casos de peso como int o float se maneja aqui, mandando 
                                                           #la bandera a cadena vacía para pedir un nuevo dato para evaluar  


#Ciclo while para la obtención y validación de la estatura
#Este ciclo es técnicamente la misma estructura del cilo while para la obtencion del valor de peso
validaEstatura = ""      #Iniciamos bandera
while validaEstatura == "" or validaEstatura.isspace():    #Validamos cadena vacía o blancos
    estatura = input("¿Cuál es tu estatura en metros?: ")   #Pedimos valor para estatura
    validaEstatura = estatura                               #Asignamos el valor de estatura a la bandera   
    
    

    separarEstatura = validaEstatura.partition(".")   #Particionamos mediante metodo count la cadena
    #Evaluamos los dos casos: cadena con un solo punto y dos cadenas de digitos a los lados (que la estatura venga como float)
    # o que la cadena sea integramente de digitos (que venga como entero) 
    if validaEstatura.count(".")== 1 and separarEstatura[0].isdigit() and separarEstatura[2].isdigit() or estatura.isdigit():
        estaturaNumero = float(estatura)                      #Convertimos a float
         
        if estaturaNumero > 2.00 or estaturaNumero <= 0.0:    #Evaluamos que el valor de estatura esté en un intervalo razonable
            print("Estatura fuera de rango.")                 #mayor a cero y menor a dos metros. Esto es muy importante
            validaEstatura = ""                               #ya que al ser el valor que va a dividir NO PUEDE SER CERO 
                                                              #Si no es válido, limpiamos la bandera e informamos de dato invalido al usuario 
    else:
        print("No es un valor correcto de estatura.")         #cualquier caso que no sea cadena de decimales o entero se 
        validaEstatura = ""                                   #maneja aquí, como cadena vacía, de espacios o letras.  
                                                         
  
#CALCULO DEL IMC

#En los dos ciclos de validación de peso y estatura ya verificamos que los datos sean correctos para hacer el cálculo
#del IMC
imc = pesoNumero / estaturaNumero ** 2

#Hacemos la impresión de los valores obtenidos del usuario y de los valores calculados por el programa
#mediante print y cadenas formateadas
print("\n ")
print("El cálculo de su Índice de Masa Corporal esta listo {} {} {} ".format(nombre, apPaterno, apMaterno))
print("Su edad es {} años.".format(edad))
print("Su peso es {} kilogramos.".format(peso))
print("Su estatura es {} metros.".format(estatura))
print("Su IMC es de {:.4f}".format(imc))
print("Usted tiene", end=" ")
#Introducimos una serie de condicionales if elif para dar la interpretación del valor numérico del IMC
if imc >= 0 and imc <= 15.99 :
        print ("delgadez severa.")
elif imc >= 16.00 and imc <= 16.99 :
        print ("delgadez moderada.")
elif imc >= 17.00 and imc <= 18.49:
        print ("delgadez leve.")
elif imc >= 18.50 and imc <= 24.99 :
        print ("peso normal.")
elif imc >= 25.00 and imc <= 29.99:
        print ("sobrepeso.")
elif imc >= 30.00 and imc <= 34.99:
        print ("obesidad leve.")
elif imc >= 35.00 and imc <= 39.99:
        print ("obesidad media.")
elif imc >= 40.00:
        print ("obesidad morbida.")
