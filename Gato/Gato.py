def pintar_gato(gato):
	print("JUEGO DEL GATO")
	print("╔═══╦═══╦═══╗")
	print("║",gato[0],"║",gato[1],"║",gato[2],"║")
	print("╠═══╬═══╬═══╣")
	print("║",gato[3],"║",gato[4],"║",gato[5],"║")
	print("╠═══╬═══╬═══╣")
	print("║",gato[6],"║",gato[7],"║",gato[8],"║")
	print("╚═══╩═══╩═══╝")

def turno_X(X):
	reset = True
	while reset:
		match X:
			case 1:
				if gato[0] != "O" and gato[0] != "X":
					gato[0] = "X"
					reset = False
				else:
					print("Lugar Ocupado")
					try:
						X = int(input("Donde pondras 1-9 :"))
					except ValueError:
						print("Valor invalido!")
			case 2:
				if gato[1] != "O" and gato[1] != "X":
					gato[1] = "X"
					reset = False
				else:
					print("Lugar Ocupado")
					try:
						X = int(input("Donde pondras 1-9 :"))
					except ValueError:
						print("Valor invalido!")
			case 3:
				if gato[2] != "O" and gato[2] != "X":
					gato[2] = "X"
					reset = False
				else:
					print("Lugar Ocupado")
					try:
						X = int(input("Donde pondras 1-9 :"))
					except ValueError:
						print("Valor invalido!")
			case 4:
				if gato[3] != "O" and gato[3] != "X":
					gato[3] = "X"
					reset = False
				else:
					print("Lugar Ocupado")
					try:
						X = int(input("Donde pondras 1-9 :"))
					except ValueError:
						print("Valor invalido!")
			case 5:
				if gato[4] != "O" and gato[4] != "X":
					gato[4] = "X"
					reset = False
				else:
					print("Lugar Ocupado")
					try:
						X = int(input("Donde pondras 1-9 :"))
					except ValueError:
						print("Valor invalido!")
			case 6:
				if gato[5] != "O" and gato[5] != "X":
					gato[5] = "X"
					reset = False
				else:
					print("Lugar Ocupado")
					try:
						X = int(input("Donde pondras 1-9 :"))
					except ValueError:
						print("Valor invalido!")
			case 7:
				if gato[6] != "O" and gato[6] != "X":
					gato[6] = "X"
					reset = False
				else:
					print("Lugar Ocupado")
					try:
						X = int(input("Donde pondras 1-9 :"))
					except ValueError:
						print("Valor invalido!")
			case 8:
				if gato[7] != "O" and gato[7] != "X":
					gato[7] = "X"
					reset = False
				else:
					print("Lugar Ocupado")
					try:
						X = int(input("Donde pondras 1-9 :"))
					except ValueError:
						print("Valor invalido!")
			case 9:
				if gato[8] != "O" and gato[8] != "X":
					gato[8] = "X"
					reset = False
				else:
					print("Lugar Ocupado")
					try:
						X = int(input("Donde pondras 1-9 :"))
					except ValueError:
						print("Valor invalido!")
			case _:
				print("Error...Rango invalido!")
				try:
					X = int(input("Donde pondras 1-9 :"))
				except ValueError:
					print("Valor invalido!")

def revisar_ganador(gato):
	if gato[0] == gato[1] == gato[2]:
		return gato[0]
	elif gato[3] == gato[4] == gato[5]:
		return gato[3]
	elif gato[6] == gato[7] == gato[8]:
		return gato[6]
	elif gato[0] == gato[3] == gato[6]:
		return gato[0]
	elif gato[1] == gato[4] == gato[7]:
		return gato[1]
	elif gato[2] == gato[5] == gato[8]:
		return gato[2]
	elif gato[0] == gato[4] == gato[8]:
		return gato[0]
	elif gato[2] == gato[4] == gato[6]:
		return gato[2]
	else:
		return None

#_____________________PROCESO PRINCIPAL_____________________
gato = ["1","2","3","4","5","6","7","8","9"]

turno = 0
ganador = None

while turno < 9 and ganador is None:
	if turno % 2 == 0:
		pintar_gato(gato)
		print("Tu turno X: ")
		try:
			X = int(input("Donde pondras 1-9 :"))
			if X > 0 and X < 10:
				turno_X(X)
				ganador = revisar_ganador(gato)
				turno = turno + 1
			else:
				print("Error...Rango invalido!")
		except ValueError:
			print("Valor invalido!")
	else:
		pintar_gato(gato)
		print("Tu turno O: ")
		try:
			O = int(input("Donde pondras 1-9 :"))
			if O > 0 and O < 10:
				match O:
					case 1:
						if gato[0] != "O" and gato[0] != "X":
							gato[0] = "O"
							ganador = revisar_ganador(gato)
							turno = turno + 1
						else:
							print("Lugar Ocupado")
					case 2:
						if gato[1] != "O" and gato[1] != "X":
							gato[1] = "O"
							ganador = revisar_ganador(gato)
							turno = turno + 1
						else:
							print("Lugar Ocupado")
					case 3:
						if gato[2] != "O" and gato[2] != "X":
							gato[2] = "O"
							ganador = revisar_ganador(gato)
							turno = turno + 1
						else:
							print("Lugar Ocupado")
					case 4:
						if gato[3] != "O" and gato[3] != "X":
							gato[3] = "O"
							ganador = revisar_ganador(gato)
							turno = turno + 1
						else:
							print("Lugar Ocupado")
					case 5:
						if gato[4] != "O" and gato[4] != "X":
							gato[4] = "O"
							ganador = revisar_ganador(gato)
							turno = turno + 1
						else:
							print("Lugar Ocupado")
					case 6:
						if gato[5] != "O" and gato[5] != "X":
							gato[5] = "O"
							ganador = revisar_ganador(gato)
							turno = turno + 1
						else:
							print("Lugar Ocupado")
					case 7:
						if gato[6] != "O" and gato[6] != "X":
							gato[6] = "O"
							ganador = revisar_ganador(gato)
							turno = turno + 1
						else:
							print("Lugar Ocupado")
					case 8:
						if gato[7] != "O" and gato[7] != "X":
							gato[7] = "O"
							ganador = revisar_ganador(gato)
							turno = turno + 1
						else:
							print("Lugar Ocupado")
					case 9:
						if gato[8] != "O" and gato[8] != "X":
							gato[8] = "O"
							ganador = revisar_ganador(gato)
							turno = turno + 1
						else:
							print("Lugar Ocupado")
			else:
				print("Error...Rango invalido!")
		except ValueError:
			print("Valor invalido!")

print("\n"*50)
pintar_gato(gato)

if ganador is not None:
	print("Gano el jugador:", ganador)
else:
	print("Empate!")
