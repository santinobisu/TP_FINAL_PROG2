
def encontrar_mayor_diccionario(dict):

    print(dict)

    keys_max_val = ""
    max_value = max(dict.values())

    for key, value in dict.items():
        if value == max_value:
            keys_max_val = key

    return keys_max_val

def main(nombre_persona):

    archivo_entrada = open("./Entradas/" + nombre_persona + ".txt","r")
    archivo_frases = open("./Frases/" + nombre_persona + ".txt", "r")
    archivo_salida = open("./Salidas/" + nombre_persona + ".txt","w")

    linea_frase = archivo_frases.readline() #te _ unos chinos en madrid\n

    while(linea_frase != ''):

        lista_palabras_frase = linea_frase.split()

        i = 0 # Posicion en lista_palabras

        j = 0 # Posicion de "_" que se va a guardar

        while(i < len(lista_palabras_frase)):
            if lista_palabras_frase[i] == "_":
                j = i
            i += 1

        if j == 0: # Caso "_" esta en la primera posicion

            diccionario_apariciones_palabras = {}

            linea_entrada = archivo_entrada.readline()

            while(linea_entrada != ''):

                lista_palabras_entrada = linea_entrada.split()

                for i in range(0,len(lista_palabras_entrada)):

                    if lista_palabras_entrada[i] == lista_palabras_frase[1]:

                        if not lista_palabras_entrada[i-1] in lista_llaves:
                            diccionario_apariciones_palabras[lista_palabras_entrada[i-1]] = 1                
                        else:
                            diccionario_apariciones_palabras[lista_palabras_entrada[i-1]] += 1

                linea_entrada = archivo_entrada.readline()
            
            #agarrar el mayor valor entre los valores del diccionario y reemplazar "_" por la llave del mayor valor

            lista_valores = list(diccionario_apariciones_palabras.values())
            lista_llaves = list(diccionario_apariciones_palabras.keys())

            mayor = 0
            posicion = 0

            for indice in range(0,len(lista_valores)):
                if lista_valores[indice] > mayor:
                    mayor = lista_valores[indice]
                    posicion = indice

            palabra_encontrada = lista_llaves[posicion]

            lista_palabras_frase[0] = palabra_encontrada

            s = ' '.join(lista_palabras_frase) + '\n' # Junto toda la lista en un string junto con el salto de linea

            #queda escribir el string en el nuevo archivo

            archivo_salida.write(s)

            
        elif j == (len(lista_palabras_frase) - 1): # Caso "_" esta en la ultima posicion

            diccionario_apariciones_palabras = {}

            linea_entrada = archivo_entrada.readline()
            
            while(linea_entrada != ''):

                lista_palabras_entrada = linea_entrada.split()

                for i in range(0,len(lista_palabras_entrada)):

                    if lista_palabras_entrada[i] == lista_palabras_frase[-2]:

                        if not lista_palabras_entrada[i+1] in diccionario_apariciones_palabras.keys():
                            diccionario_apariciones_palabras[lista_palabras_entrada[i+1]] = 1
                        else:
                            diccionario_apariciones_palabras[lista_palabras_entrada[i+1]] += 1
               
                linea_entrada = archivo_entrada.readline()

            #agarrar el mayor valor entre los valores del diccionario y reemplazar "_" por la llave del mayor valor

            lista_valores = list(diccionario_apariciones_palabras.values())
            lista_llaves = list(diccionario_apariciones_palabras.keys())

            mayor = 0
            posicion = 0

            for indice in range(0,len(lista_valores)):
                if lista_valores[indice] > mayor:
                    mayor = lista_valores[indice]
                    posicion = indice

            palabra_encontrada = lista_llaves[posicion]

            lista_palabras_frase[-1] = palabra_encontrada

            s = ' '.join(lista_palabras_frase) + '\n' # Junto toda la lista en un string junto con el salto de linea

            #queda escribir el string en el nuevo archivo

            archivo_salida.write(s)


        else: # Caso "_" no esta ni en la primera ni en la ultima posicion

            diccionario_apariciones_palabras = {}

            linea_entrada = archivo_entrada.readline()

            while(linea_entrada != ''):

                lista_palabras_entrada = linea_entrada.split()

                for i in range(0,len(lista_palabras_entrada)):

                    if lista_palabras_entrada[i] == lista_palabras_frase[j+1]:

                        if not lista_palabras_entrada[i-1] in diccionario_apariciones_palabras.keys():
                            diccionario_apariciones_palabras[lista_palabras_entrada[i-1]] = 1
                        else:
                            diccionario_apariciones_palabras[lista_palabras_entrada[i-1]] += 1
                    
                    elif lista_palabras_entrada[i] == lista_palabras_frase[j-1]:

                        if not lista_palabras_entrada[i+1] in diccionario_apariciones_palabras.keys():
                            diccionario_apariciones_palabras[lista_palabras_entrada[i+1]] = 1
                        else:
                            diccionario_apariciones_palabras[lista_palabras_entrada[i+1]] += 1
                                      
                linea_entrada = archivo_entrada.readline()

            #agarrar el mayor valor entre los valores del diccionario y reemplazar "_" por la llave del mayor valor

            palabra_encontrada = encontrar_mayor_diccionario(diccionario_apariciones_palabras)

            print(palabra_encontrada)

            lista_palabras_frase[j] = palabra_encontrada

            s = ' '.join(lista_palabras_frase) + '\n' # Junto toda la lista en un string junto con el salto de linea

            #queda escribir el string en el nuevo archivo

            archivo_salida.write(s)

    archivo_entrada.close()
    archivo_frases.close()
    archivo_salida.close()