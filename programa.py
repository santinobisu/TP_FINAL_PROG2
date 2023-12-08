import sys
from funciones_aux.funciones import *

def main(nombre_persona):

    archivo_entrada = open("./Entradas/" + nombre_persona + ".txt","r")
    archivo_frases = open("./Frases/" + nombre_persona + ".txt", "r")
    archivo_salida = open("./Salidas/" + nombre_persona + ".txt","w")

    palabras_entrada = archivo_entrada.read() #Leo todas las palabras del archivo de entrada

    lista_palabras_entrada = palabras_entrada.split() #Y las ordeno en una lista de una en una

    lineas_frases = archivo_frases.readlines() #Lista con todas las frases
    
    for linea_frase in lineas_frases:

        linea_frase.replace('\n','') #Se elimina el salto de linea en cada una

        lista_palabras_frase = linea_frase.split() #Separo las palabras de la linea para encontrar la posicion de '_'

        posicion_palabra_frase = 0 #Posicion de '_'

        for indice in range(len(lista_palabras_frase)):

            if lista_palabras_frase[indice] == '_':
                posicion_palabra_frase = indice #Encuentro la posicion de la palabra a encontrar
            
        palabra_encontrada = encontrarPalabra(posicion_palabra_frase,lista_palabras_entrada,lista_palabras_frase,1,50) #Se ejecuta la funcion encontrarPalabra que retornara la palabra encontrada

        lista_palabras_frase[posicion_palabra_frase] = palabra_encontrada #Reemplazo por la palabra encontrada

        frase_formada = ' '.join(lista_palabras_frase) + '\n' #Junto las palabras de la frase para formar un string con salto de linea

        archivo_salida.write(frase_formada) #Finalmente se escribe en el archivo
        
    archivo_entrada.close()
    archivo_frases.close()
    archivo_salida.close() # Se cierran todos los archivos

main(sys.argv[1]) #Se ejecuta el programa con el argumento pasado