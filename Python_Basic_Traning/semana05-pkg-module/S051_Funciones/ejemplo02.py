def mostrarPalabras(*frase):
	longitud = len(frase)	
	for palabra in frase:
		print(palabra)
	return(longitud)
	
#
def main():
	l = mostrarPalabras("hola", "cómo", "estás")
	print("Numero Palabras => " + str(l))
#
main()
