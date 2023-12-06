
def crearDiccionario(posicion_palabra_frase,lista_palabras_entrada,lista_palabras_frase):

    diccionario_apariciones = {} #Creo un diccionario de la forma {"Palabra":Apariciones de la palabra}
            
    for indice in range(len(lista_palabras_entrada)): #Busco la palabra a encontrar
        
        #El algoritmo se basa en buscar igualdad de palabra precedente o siguiente de '_' dentro de las palabras de entrada
        #y agregar la palabra siguiente o precedente en entrada, correspondientemente al diccionario junto a su cantidad de
        #apariciones

        if posicion_palabra_frase == 0: #Caso '_' sea la primera palabra

            if lista_palabras_entrada[indice] == lista_palabras_frase[1]:

                if not lista_palabras_entrada[indice-1] in diccionario_apariciones:
                    diccionario_apariciones[lista_palabras_entrada[indice-1]] = 1 
                        
                else:
                    diccionario_apariciones[lista_palabras_entrada[indice-1]] += 1 

        elif posicion_palabra_frase == (len(lista_palabras_frase) - 1): #Caso '_' sea la ultima palabra

            if lista_palabras_entrada[indice] == lista_palabras_frase[-2]: 

                if not lista_palabras_entrada[indice+1] in diccionario_apariciones:
                    diccionario_apariciones[lista_palabras_entrada[indice+1]] = 1 
                        
                else:
                    diccionario_apariciones[lista_palabras_entrada[indice+1]] += 1 
        
        else: # Caso '_' no sea ni la primera ni la ultima palabra

            if lista_palabras_entrada[indice] == lista_palabras_frase[posicion_palabra_frase + 1]:

                if not lista_palabras_entrada[indice-1] in diccionario_apariciones:
                    diccionario_apariciones[lista_palabras_entrada[indice-1]] = 1 
                        
                else:
                    diccionario_apariciones[lista_palabras_entrada[indice-1]] += 1

            elif lista_palabras_entrada[indice] == lista_palabras_frase[posicion_palabra_frase - 1]:

                if not lista_palabras_entrada[indice+1] in diccionario_apariciones:
                    diccionario_apariciones[lista_palabras_entrada[indice+1]] = 1 
                        
                else:
                    diccionario_apariciones[lista_palabras_entrada[indice+1]] += 1

    return diccionario_apariciones



def encontrarPalabra(diccionario_apariciones):

    valores_diccionario = list(diccionario_apariciones.values()) #Creo una lista de los valores
    palabras_diccionario = list(diccionario_apariciones.keys()) #Y una de sus llaves que son las palabras

    mayor = 0
    posicion_palabra_diccionario = 0

    for indice in range(len(valores_diccionario)): #Busco cual es la posicion del mayor valor, que se corresponde a la posicion de la palabra
                
        if valores_diccionario[indice] > mayor:
            mayor = valores_diccionario[indice]
            posicion_palabra_diccionario = indice 
    
    return palabras_diccionario[posicion_palabra_diccionario] #La palabra con mayores apariciones es encontrada



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

        diccionario_apariciones = crearDiccionario(posicion_palabra_frase,lista_palabras_entrada,lista_palabras_frase)
            
        #El diccionario ya se completo, ahora queda ver cual es la palabra con mayor aparicion y reemplazar '_' por la palabra
            
        palabra_encontrada = encontrarPalabra(diccionario_apariciones) #La palabra fue encontrada

        #Queda reemplazar '_' por la palabra y escribir la frase en el archivo

        lista_palabras_frase[posicion_palabra_frase] = palabra_encontrada #Reemplazo por la palabra encontrada

        frase_formada = ' '.join(lista_palabras_frase) + '\n' #Junto las palabras de la frase para formar un string con salto de linea

        archivo_salida.write(frase_formada) #Finalmente se escribe en el archivo
        
    archivo_entrada.close()
    archivo_frases.close()
    archivo_salida.close()
                


            
        
        