#Trivias de Geografia
#Silabuz
#Alex Barreto

import random 
#puntos
puntaje = 0
iniciar_trivia = True
intentos = 0

#color
RED = '\033[31m'
GREEN = '\033[32m'
MAGENTA = '\033[35m'
RESET = '\033[39m'


#  texto de bienvenida 
print(RED+"Bienvenido a mi trivia sobre Geografía"+RESET)
print("Pondremos a prueba tus conocimientos")
print("Tienes", puntaje, RED+"Puntos"+RESET)


#ingresar Nombre
nombre = input("Ingresa tu nombre: ")

# instrucciones sobre cómo jugar:
print(
    "\n Hola", nombre,
    "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"
)

#ciclo de intentos 
while iniciar_trivia == True:
  intentos += 1
  

  #muestra los intentos
  print(MAGENTA+"\nIntento número:"+RESET, intentos,"\n")

  # Pregunta 1
  print(MAGENTA+"1) ¿Cuál es el país que tiene forma de bota?"+RESET)
  print("a) España")
  print("b) Honduras")
  print("c) Italia")
  print("d) Alemania")
  
  # Almacenamos la respuesta 
  respuesta_1 = input("\nTu respuesta: ").lower()
  
  #Validacion Respuesta 1
  while respuesta_1 not in ("a", "b", "c", "d"):
      respuesta_1 = input(
          "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  
  if respuesta_1 == "a":
    print(RED+"Incorrecto!"+RESET, nombre, "Cerca, sigue intentando\n")
    puntaje -= 3
  elif respuesta_1 == "b":
    print(RED+"Incorrecto!"+RESET, nombre, "lejos, sigue intentando\n")
    puntaje -= 5
  elif respuesta_1 == "d":
    print(RED+"Incorrecto!"+RESET, nombre, "Cerca, sigue intentando\n")
    puntaje -= 3
  else:
    print(GREEN+"Muy bien"+RESET, nombre, "!\n")
    puntaje += 10

  #Muestra el Puntaje
  print (nombre, "Tienes", puntaje, "puntos !\n")
  
      
  
  # Pregunta 2
  print(MAGENTA+"2)  ¿Cuál es la única ciudad que está en dos continentes distintos?"+RESET)
  print("a) Moscú")
  print("b) Estambul")
  print("c) Berlín")
  print("d) Nueva Delhi")
  
  respuesta_2 = input("\nTu respuesta: ").lower()
  
  #Validacion Respuesta 2
  while respuesta_2 not in ("a", "b", "c", "d"):
      respuesta_2 = input(
          "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
    
  if respuesta_2 == "a":
    print(RED+"Incorrecto!"+RESET, nombre, "Cerca, sigue intentando\n")
    puntaje -= 3
  elif respuesta_2 == "c":
    print(RED+"Incorrecto!"+RESET, nombre, "lejos, sigue intentando\n")
    puntaje -= 5
  elif respuesta_2 == "d":
    print(RED+"Incorrecto!"+RESET, nombre, "lejos, sigue intentando\n")
    puntaje -= 5
  else:
    print(GREEN+"Muy bien"+RESET, nombre, "!\n")
    puntaje += 10

  #muestra el puntaje
  print (nombre, "Tienes", puntaje, "puntos !\n")
    
  
  # Pregunta 3
  print(MAGENTA+"3)  ¿En qué continente se encuentra Surinam?"+RESET)
  print("a) África")
  print("b) Oceanía")
  print("c) Asia")
  print("d) Sur América")
  
  respuesta_3 = input("\nTu respuesta: ").lower()
  
  #Validacion de Respuesta 3
  while respuesta_3 not in ("a", "b", "c", "d"):
      respuesta_3 = input(
          "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_3 == "a":
    print(RED+"Incorrecto!"+RESET, nombre, "lejos, sigue intentando\n")
    puntaje -= 5
  elif respuesta_3 == "c":
    print(RED+"Incorrecto!"+RESET, nombre, "lejos, sigue intentando\n")
    puntaje -= 5
  elif respuesta_3 == "b":
    print(RED+"Incorrecto!"+RESET, nombre, "lejos, sigue intentando\n")
    puntaje -= 5
  else:
    print(GREEN+"Muy bien"+RESET, nombre, "!\n")
    puntaje += 10

   #muestra el puntaje
  print (nombre, "Tienes", puntaje, "puntos !\n")


   # Pregunta 4
  print(MAGENTA+"4)  ¿Cuál es el país más poblado del mundo Cuál?"+RESET)
  print("a) India")
  print("b) Indonesia")
  print("c) China")
  print("d) Estados Unidos")
  
  respuesta_4 = input("\nTu respuesta: ").lower()
  
  #Validacion Respuesta 4
  while respuesta_4 not in ("a", "b", "c", "d"):
      respuesta_4 = input(
          "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
   
  if respuesta_4 == "a":
    print(RED+"Incorrecto!"+RESET, nombre, "Cerca, sigue intentando\n")
    puntaje -= 3
  elif respuesta_4 == "b":
    print(RED+"Incorrecto!"+RESET, nombre, "Cerca, sigue intentando\n")
    puntaje -= 3
  elif respuesta_4 == "d":
    print(RED+"Incorrecto!"+RESET, nombre, "lejos, sigue intentando\n")
    puntaje -= 5
  else:
    print(GREEN+"Muy bien"+RESET, nombre, "!\n")
    puntaje += 10

  #muestra el puntaje
  print (nombre, "Tienes", puntaje, "puntos !\n")



    # Pregunta 5
  print(MAGENTA+"5)  ¿ Cuál es la Capital de Nicaragua?"+RESET)
  print("a) Managua")
  print("b) San Jose")
  print("c) Asunción")
  print("d) Cali")
  
  respuesta_5 = input("\nTu respuesta: ").lower()
  
  #Validacion Respuesta 5
  while respuesta_5 not in ("a", "b", "c", "d"):
      respuesta_5 = input(
          "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
    
  if respuesta_5 == "c":
    print(RED+"Incorrecto!"+RESET, nombre, "Cerca, sigue intentando\n")
    puntaje -= 3
  elif respuesta_5 == "b":
    print(RED+"Incorrecto!"+RESET, nombre, "Cerca, sigue intentando\n")
    puntaje -= 3
  elif respuesta_5 == "d":
    print(RED+"Incorrecto!"+RESET, nombre, "lejos, sigue intentando\n")
    puntaje -= 5
  else:
    print(GREEN+"Muy bien"+RESET, nombre, "!\n")
    puntaje += 10
  
    print (MAGENTA+"Gracias"+RESET, nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos")

  #condicional si desea jugar de Nuevo
  print(MAGENTA+"\n¿Deseas intentar la trivia nuevamente?"+RESET)
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  
  if repetir_trivia != "si":  
     print("\n",nombre, GREEN+",Espero que lo hayas pasado bien, hasta pronto!"+RESET)
     iniciar_trivia = False  # evitamos que se repita.

  else:
     puntaje =random.randint(0, 10)
     print("\n",MAGENTA+"Te Regalaremos puntos al azar para aumentar tus posibilidades en el proximo intento "+RESET, puntaje," Puntos")
   

