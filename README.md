# Modulo1 Cálculo del IMC
## Programa de calculo de IMC

Para la realización de este programa primero tuvimos que prestar atención a hacer un analisis concienzudo del problema que estabamos trabajando, porque suena
fácil al principio hacer un cálculo tan sencillo como una division de una cantidad entre otra que esta al cuadrado. pero es ahí cuando te das cuenta que si bien la
operación no es complicada hay factores muy sencillos como la obtención de datos que si no se realizan de manera correcta puede arrojarnos datos erróneos y 
y malfuncionamiento del programa.

Por lo cual la primera parte fue una obtención correcta de los datos del usuario mediante validaciones de cada dato cuidando tanto el tipo de dato como las conversiones 
que pudieramos llegar a necesitar del mismo. Validar los datos fue un poco complicado pero no de implementar sino de pensar como con las herramientas que los profesores 
pusieron a disposición podiamos estructurar correctamente esto, puesto que cada dato es un caso diferente, por ejemplo conocer en cuantas formas pueden proporcionarnos 
una cifra como en el peso, que puede ser en forma de decimales o en enteros, y saber qué posibles casos de error tendríamos al obtenerlos y como manejar esos errores.

Una vez hecho este analisis, se implementó un ciclo de obtención de cada dato dentro del cual validabamos los posibles casos de error en cada uno y de ciertos datos
como el peso y la estatura una segunda validación de la conversión del tipo de dato y el rango en el cual podíamos permitir que se obtuviera un dato correcto, ya que por
ejemplo si obteniamos un valor correcto de  estatura en numero como el cero (el cual es un valor numerico correcto en su tipo) para la logica de la operación de calculo del IMC
nos iba a ocasionar un error que pararía el programa, ya que la división por cero no es permitida por irse al infinito

Y no solamente necesitabamos almacenar la información obtenida del usuario, sino definir ciertas variables de control que nos permitieran tener una estructura secuencial q 
que nos ayude a realizar todo el proceso de inicio a fin para no permitir el paso de datos incoherentes.

Una vez obtenidos todos los datos y habiendo corroborado que las operaciones matematicas en los intervalos definidos permitían operaciones sin error, pudimos mediante 
print y cadenas de formato mostrar en pantalla los datos obtenidos más los datos calculados y su correcta interpretación mediante condicionales if anidadas, lo cual
le muestra al usuario en qué rango de IMC está y qué es lo que representa ese valor.

Hasta el momento me ha parecido muy interesante la manera en que python hace el manejo de de todas las caracterisicas de programación, lo fluido que es programar con 
este lenguaje y lo que me parece genial e el manejo de todo el proceso de programación median Git y Github, ya que permite llevar una secuencia logica de cambios 
y versiones del trabajo que estamos realizando sin la complicación de perdernos entre varios archivos distintos. La manera en que los profesores enseñan los temas me 
me parece muy dinamica y la resolución de dudas ha sido un gran apoyo para llegar a este punto del curso.
