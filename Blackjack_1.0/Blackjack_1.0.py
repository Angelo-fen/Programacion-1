#Archivo: Blackjack_1.0.py
#Descripción: Juego de Blackjack donde el jugador compite contra el dealer(la maquina), se puede pedir cartas, plantarse y reiniciar la partida.
#Nombre: Angel Gustavo Camargo Bermudez y Luis Suares Garcia.
#Fecha: 2026-11-11
#---------------- PROCESO PRINCIPAL -----------------
import pygame
import random
import sys
# Iniciar pygame
pygame.init()
#---------------- CONFIGURACION DE VENTANA -----------------
pantalla = pygame.display.set_mode((750, 550))
pygame.display.set_caption("Blackjack")
#---------------- COLORES -----------------
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (34, 139, 34)
ROJO = (200, 0, 0)
AZUL = (0, 100, 200)
DORADO = (218, 165, 32)
#---------------- FUENTES -----------------
fuente = pygame.font.SysFont("DejaVu Sans", 26, bold=True)
fuente_carta = pygame.font.SysFont("DejaVu Sans", 20, bold=True)
fuente_simbolo = pygame.font.SysFont("DejaVu Sans", 38)
#---------------- BOTONES -----------------
btn_agarrar = pygame.Rect(80, 460, 170, 50)
btn_plantarse = pygame.Rect(290, 460, 170, 50)
btn_reiniciar = pygame.Rect(500, 460, 170, 50)
#---------------- FUNCION CREAR BARAJA -----------------
def crear_baraja():
    # Crear los palos
    palos = ['♠', '♣', '♥', '♦']
    # Crear los valores
    valores = ['A', '2', '3', '4', '5', '6', '7',
               '8', '9', '10', 'J', 'Q', 'K']
    # Lista para guardar las cartas
    baraja = []
    i = 0
    # Recorrer los palos
    while i < len(palos):
        j = 0
        # Recorrer los valores
        while j < len(valores):
            carta = (palos[i], valores[j])
            baraja.append(carta)
            j = j + 1
        i = i + 1
    # Mezclar las cartas
    random.shuffle(baraja)
    return baraja
#---------------- FUNCION CALCULAR PUNTOS -----------------
def calcular_puntos(mano):
    puntos = 0
    ases = 0
    indice = 0
    # Recorrer las cartas
    while indice < len(mano):
        palo = mano[indice][0]
        valor = mano[indice][1]
        # Comprobar si es un As
        if valor == 'A':
            puntos = puntos + 11
            ases = ases + 1
        # Comprobar si es una figura
        elif valor == 'J' or valor == 'Q' or valor == 'K' or valor == '10':
            puntos = puntos + 10
        else:
            puntos = puntos + int(valor)
        indice = indice + 1
    # Comprobar si nos pasamos de 21
    while puntos > 21 and ases > 0:
        puntos = puntos - 10
        ases = ases - 1
    return puntos
#---------------- FUNCION REINICIAR JUEGO -----------------
def reiniciar_juego():
    global baraja
    global mano_jugador
    global mano_dealer
    global fin_juego
    # Crear una nueva baraja
    baraja = crear_baraja()
    # Crear las manos vacias
    mano_jugador = []
    mano_dealer = []
    # Indicar que el juego sigue activo
    fin_juego = False
    contador = 0
    # Repartir dos cartas a cada uno
    while contador < 2:
        # Carta del jugador
        carta_jugador = baraja.pop()
        mano_jugador.append(carta_jugador)
        # Carta del dealer
        carta_dealer = baraja.pop()
        mano_dealer.append(carta_dealer)
        contador = contador + 1
#---------------- FUNCION DIBUJAR UNA CARTA -----------------
def dibujar_carta(pos_x, pos_y, palo, valor):
    # Elegir el color de la carta
    if palo == '♥' or palo == '♦':
        color_palo = ROJO
    else:
        color_palo = NEGRO
    # Crear el rectangulo de la carta
    rect_carta = pygame.Rect(pos_x, pos_y, 75, 105)
    # Dibujar el fondo blanco
    pygame.draw.rect(pantalla, BLANCO, rect_carta, border_radius=8)
    # Dibujar el borde negro
    pygame.draw.rect(pantalla, NEGRO, rect_carta, 2, border_radius=8)
    # Crear el texto de la esquina
    texto = str(valor) + str(palo)
    texto_esquina = fuente_carta.render(texto, True, color_palo)
    pantalla.blit(texto_esquina, (pos_x + 6, pos_y + 5))
    # Crear el simbolo grande del centro
    simbolo = fuente_simbolo.render(palo, True, color_palo)
    # Obtener el rectangulo del simbolo
    rect_simbolo = simbolo.get_rect()
    # Colocar el simbolo en el centro
    rect_simbolo.center = (pos_x + 37, pos_y + 55)
    # Mostrar el simbolo
    pantalla.blit(simbolo, rect_simbolo)
#---------------- FUNCION DIBUJAR BOTONES -----------------
def dibujar_botones():
    # Dibujar los botones
    pygame.draw.rect(pantalla, VERDE, btn_agarrar, border_radius=10)
    pygame.draw.rect(pantalla, ROJO, btn_plantarse, border_radius=10)
    pygame.draw.rect(pantalla, NEGRO, btn_reiniciar, border_radius=10)
    # Crear los textos
    texto_agarrar = fuente.render("Agarrar", True, BLANCO)
    texto_plantarse = fuente.render("Plantarse", True, BLANCO)
    texto_reiniciar = fuente.render("Reiniciar", True, BLANCO)
    # Obtener los rectangulos de los textos
    rect_agarrar = texto_agarrar.get_rect()
    rect_plantarse = texto_plantarse.get_rect()
    rect_reiniciar = texto_reiniciar.get_rect()
    # Colocar los textos en el centro de los botones
    rect_agarrar.center = btn_agarrar.center
    rect_plantarse.center = btn_plantarse.center
    rect_reiniciar.center = btn_reiniciar.center
    # Mostrar los textos
    pantalla.blit(texto_agarrar, rect_agarrar)
    pantalla.blit(texto_plantarse, rect_plantarse)
    pantalla.blit(texto_reiniciar, rect_reiniciar)
#---------------- FUNCION DIBUJAR CARTAS JUGADOR -----------------
def dibujar_cartas_jugador():
    pos_x = 50
    pos_y = 305
    indice = 0
    # Recorrer las cartas del jugador
    while indice < len(mano_jugador):
        palo = mano_jugador[indice][0]
        valor = mano_jugador[indice][1]
        # Dibujar la carta
        dibujar_carta(pos_x, pos_y, palo, valor)
        # Cambiar la posicion
        pos_x = pos_x + 90
        indice = indice + 1
#---------------- FUNCION DIBUJAR CARTAS DEALER -----------------
def dibujar_cartas_dealer():
    pos_x = 50
    pos_y = 75
    indice = 0
    # Recorrer las cartas del dealer
    while indice < len(mano_dealer):
        palo = mano_dealer[indice][0]
        valor = mano_dealer[indice][1]
        # Comprobar si el juego termino
        if fin_juego == True:
            # Mostrar la carta
            dibujar_carta(pos_x, pos_y, palo, valor)
        else:
            # Crear una carta oculta
            rect_oculta = pygame.Rect(pos_x, pos_y, 75, 105)
            # Dibujar el fondo negro
            pygame.draw.rect(pantalla, NEGRO, rect_oculta, border_radius=8)
            # Dibujar el borde dorado
            pygame.draw.rect(pantalla, DORADO, rect_oculta, 3, border_radius=8)
            # Crear el signo de interrogacion
            signo = fuente.render("?", True, DORADO)
            rect_signo = signo.get_rect()
            rect_signo.center = rect_oculta.center
            # Mostrar el signo
            pantalla.blit(signo, rect_signo)
        # Cambiar la posicion
        pos_x = pos_x + 90
        indice = indice + 1
#---------------- FUNCION MOSTRAR PUNTUACION -----------------
def mostrar_puntuacion():
    # Calcular puntos del jugador
    puntos_jugador = calcular_puntos(mano_jugador)
    # Convertir los puntos a texto
    texto_jugador = "Tu: " + str(puntos_jugador)
    imagen_jugador = fuente.render(texto_jugador, True, BLANCO)
    # Mostrar los puntos
    pantalla.blit(imagen_jugador, (50, 265))
    # Comprobar si el juego termino
    if fin_juego == True:
        # Calcular puntos del dealer
        puntos_dealer = calcular_puntos(mano_dealer)
        texto_dealer = "Dealer: " + str(puntos_dealer)
        imagen_dealer = fuente.render(texto_dealer, True, BLANCO)
        pantalla.blit(imagen_dealer, (50, 35))
    else:
        # Ocultar los puntos del dealer
        texto_dealer = fuente.render("Dealer: ??", True, BLANCO)
        pantalla.blit(texto_dealer, (50, 35))
#---------------- FUNCION COMPROBAR GANADOR -----------------
def comprobar_ganador():
    puntos_jugador = calcular_puntos(mano_jugador)
    puntos_dealer = calcular_puntos(mano_dealer)
    resultado = ""
    # Variables para saber el resultado
    victoria = False
    derrota = False
    # Comprobar si el jugador perdio
    if puntos_jugador > 21:
        resultado = "Te pasaste, pierdes XC!"
        derrota = True
    # Comprobar si el dealer perdio
    elif puntos_dealer > 21:
        resultado = "Ganas, el dealer se paso XD!"
        victoria = True
    # Comprobar si gano el jugador
    elif puntos_jugador > puntos_dealer:
        resultado = "Tu ganas OMG!!"
        victoria = True
    # Comprobar si gano el dealer
    elif puntos_jugador < puntos_dealer:
        resultado = "Gana el dealer :("
        derrota = True
    # Si tienen los mismos puntos
    else:
        resultado = "Empate :V"
    # Crear el rectangulo del resultado
    pos_x = 140
    pos_y = 200
    ancho = 470
    alto = 50
    rect_resultado = pygame.Rect(pos_x, pos_y, ancho, alto)
    # Crear la superficie transparente
    superficie = pygame.Surface((ancho, alto), pygame.SRCALPHA)
    # Elegir el color del resultado
    if victoria == True:
        superficie.fill((34, 139, 34, 210))
    elif derrota == True:
        superficie.fill((200, 0, 0, 210))
    else:
        superficie.fill((80, 80, 80, 210))
    # Mostrar el fondo del resultado
    pantalla.blit(superficie, (pos_x, pos_y))
    # Dibujar el borde blanco
    pygame.draw.rect(pantalla, BLANCO, rect_resultado, 2)
    # Crear el texto
    texto = fuente.render(resultado, True, BLANCO)
    rect_texto = texto.get_rect()
    # Centrar el texto
    rect_texto.center = rect_resultado.center
    # Mostrar el resultado
    pantalla.blit(texto, rect_texto)
#---------------- FUNCION TURNO DEL DEALER -----------------
def turno_dealer():
    global fin_juego
    # Calcular los puntos iniciales
    puntos = calcular_puntos(mano_dealer)
    # El dealer pide cartas mientras tenga menos de 17
    while puntos < 17:
        # Sacar una carta
        carta = baraja.pop()
        # Agregarla a su mano
        mano_dealer.append(carta)
        # Volver a calcular sus puntos
        puntos = calcular_puntos(mano_dealer)
    # Terminar el juego
    fin_juego = True
#---------------- FUNCION AGARRAR CARTA -----------------
def agarrar_carta():
    global fin_juego
    # Sacar una carta de la baraja
    carta = baraja.pop()
    # Agregar la carta al jugador
    mano_jugador.append(carta)
    # Calcular sus puntos
    puntos = calcular_puntos(mano_jugador)
    # Comprobar si llego a 21 o se paso
    if puntos >= 21:
        fin_juego = True
#---------------- FUNCION REVISAR EVENTOS -----------------
def revisar_eventos():
    global corriendo
    # Obtener todos los eventos
    eventos = pygame.event.get()
    indice = 0
    # Recorrer los eventos
    while indice < len(eventos):
        evento = eventos[indice]
        # Comprobar si se cerro la ventana
        if evento.type == pygame.QUIT:
            corriendo = False
        # Comprobar si se hizo clic con el mouse
        if evento.type == pygame.MOUSEBUTTONDOWN:
            # Comprobar si fue el boton izquierdo
            if evento.button == 1:
                # Obtener la posicion del mouse
                posicion = pygame.mouse.get_pos()
                # Comprobar el boton agarrar
                if btn_agarrar.collidepoint(posicion):
                    if fin_juego == False:
                        agarrar_carta()
                # Comprobar el boton plantarse
                elif btn_plantarse.collidepoint(posicion):
                    if fin_juego == False:
                        turno_dealer()
                # Comprobar el boton reiniciar
                elif btn_reiniciar.collidepoint(posicion):
                    reiniciar_juego()
        indice = indice + 1
#---------------- INICIAR JUEGO -----------------
reiniciar_juego()
corriendo = True
#---------------- BUCLE PRINCIPAL -----------------
while corriendo:
    # Pintar el fondo de azul
    pantalla.fill(AZUL)
    # Revisar los eventos
    revisar_eventos()
    # Dibujar las cartas del dealer
    dibujar_cartas_dealer()
    # Dibujar las cartas del jugador
    dibujar_cartas_jugador()
    # Mostrar las puntuaciones
    mostrar_puntuacion()
    # Comprobar si el juego termino
    if fin_juego == True:
        comprobar_ganador()
    # Dibujar los botones
    dibujar_botones()
    # Actualizar la pantalla
    pygame.display.flip()
#---------------- FIN -----------------
pygame.quit()
sys.exit()