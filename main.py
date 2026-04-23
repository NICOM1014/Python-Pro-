diccionario_gamer = {
    "AFK": "Away From Keyboard. Significa que el jugador no esta frente a su teclado o esta inactivo.",
    "LURK": "Moverse por el mapa de forma silenciosa para sorprender a los enemigos por la espalda.",
    "CALL": "Dar informacion importante a tus compañeros sobre la posicion o estrategia del enemigo.",
    "GAMESENSE": "La habilidad de entender que esta pasando en la partida basandose en la experiencia.",
    "AIM": "La punteria o precision que tiene un jugador al disparar.",
    "ACE": "Cuando un solo jugador elimina a todos los miembros del equipo rival.",
    "AGGRO": "Jugar de forma agresiva o provocar que los enemigos se centren en ti.",
    "BANEO": "Restriccion o expulsion de un jugador por romper las reglas.",
    "BAIT": "Engañar al enemigo para que caiga en una trampa o gaste sus recursos.",
    "BUILD": "La configuracion de objetos, habilidades o equipo de un personaje.",
    "CAMPEAR": "Quedarse en un solo lugar esperando a que pase un enemigo para eliminarlo.",
    "DROP": "Soltar un objeto o arma para que un compañero la recoja.",
    "NERF": "Cuando los desarrolladores reducen el poder de un arma o personaje porque estaba muy fuerte."
}

print("--- ¡Bienvenido al Diccionario Gamer Técnico! ---")
print("Aprende los terminos que usan los jugadores profesionales.")
print("Escribe tus consultas en MAYUSCULAS (Ejemplo: AFK, AIM, ACE).")
print("Las palabras existentes son: AFK, LURK, CALL, GAMESENSE, AIM, ACE, AGGRO, BANEO, BAIT, BUILD, CAMPEAR, DROP, NERF.")
print("--------------------------------------------------")

for i in range(5):
    print("Consulta numero:", i + 1, "de 5")
    word = input("Escribe el termino gamer que quieres buscar: ")

    if word in diccionario_gamer:
        print("Significado:", diccionario_gamer[word])
    else:
        print("Ese termino no esta en nuestra base de datos, ¡quizas es un nuevo mod!")
    
    print("--------------------------------------------------")

print("Has agotado tus consultas de la partida. ¡GG WP!")
