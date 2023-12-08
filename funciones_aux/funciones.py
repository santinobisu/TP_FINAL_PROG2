from random import randint


#palabrasAlrededor: List(String) Int -> List(String)

#palabrasAlrededor toma una lista de string y un entero, y mediante un algoritmo de busqueda
#encuentra el string '_' para tomar la/s palabras en el rango entero desde el indice de '_'
#(+ rango, - rango) y devuelve otra lista con las palabras encontradas en dicho rango.

#Entrada: ["hola","_","adios","no"] , 1    Salida: ["hola","adios"]

def palabrasAlrededor(list,rango): #Busco las palabras alrededor de '_'

    palabras = [] #Creo una lista donde se guardaran las palabras en un rango 

    for indice in range(len(list)):

        if list[indice] == '_' and indice == 0: #Caso '_' sea el primer elemento

            palabras.append(list[indice+rango])
            
        elif list[indice] == '_' and indice == (len(list) - 1): #Caso '_' sea el ultimo elemento

            palabras.append(list[indice-rango])

        elif list[indice] == '_': #Caso '_' este en el medio

            palabrasDelante = (len(list)-1)-indice
            palabrasAtras = indice

            if palabrasDelante < rango: #Si el rango es mayor a la cantidad de palabras adelante, se guarda la de atras

                palabras.append(list[indice-rango])

            elif palabrasAtras < rango: #Si el rango es mayor a la cantidad de palabras detras, se guarda la de delante

                palabras.append(list[indice+rango])

            else: #Si la cantidad de palabras de ambos lados esta dentro del rango, se guardan las dos

                palabras.append(list[indice-rango])
                palabras.append(list[indice+rango])
    
    return palabras


#crearDiccionario: Int List(String) List(String) Int Int -> Dict{String:Int}

#crearDiccionario toma un entero posicion que sera el indice de '_' en la 2da lista de palabras, una lista de palabras que siempre sera mayor a la segunda 
#lista, un entero que sera un rango y otro entero que sera un numero de probabilidad, y
#mediante una busqueda de las palabras alrededor de '_' en la primera lista de palabras, se verifican condiciones para agregar en un diccionario
#la palabra siguiente o anterior correspondiente en la primera lista de palabras, y su cantidad de apariciones para asi devolver el diccionario
#formado por llaves que son strings y apariciones que son enteros.

#Entrada: 0 , ["soy","santino","y","vos"] , ["_","santino"] , 1 , 10    Salida: {"soy":10} 

def crearDiccionario(posicion,entrada,frase,rango,probabilidad): #Creo un diccionario con las palabras y la cantidad de apariciones respecto a '_'

    diccionario_apariciones = {} #Creo un diccionario de la forma {"Palabra":Apariciones de la palabra}

    palabras = palabrasAlrededor(frase,rango) #Se crea la lista con las palabras alrededor de '_' dentro de un rango

    palabrasDelante = (len(frase)-1)-posicion
    palabrasAtras = posicion

    for palabra in palabras: #Itero sobre la lista de palabras alrededor de '_'

        for indice in range(len(entrada)): #Y comparo cada una con las palabras de Entrada

            if entrada[indice] == palabra and posicion == 0: #Caso se encuentre la palabra y '_' sea la primera palabra

                diccionario_apariciones[entrada[indice+1]] = diccionario_apariciones.get(entrada[indice+1], 0) + probabilidad
            
            elif entrada[indice] == palabra and posicion == len(frase)-1: #Caso se encuentre la palabra y '_' sea la ultima palabra

                diccionario_apariciones[entrada[indice-1]] = diccionario_apariciones.get(entrada[indice-1], 0) + probabilidad

            
            elif entrada[indice] == palabra and palabrasDelante < rango: #Caso se encuentre la palabra y el rango sea mayor a las palabras por delante de '_'

                diccionario_apariciones[entrada[indice+1]] = diccionario_apariciones.get(entrada[indice+1], 0) + probabilidad

            elif entrada[indice] == palabra and palabrasAtras < rango: #Caso se encuentre la palabra y el rango sea mayor a las palabras por detras de '_'

                diccionario_apariciones[entrada[indice-1]] = diccionario_apariciones.get(entrada[indice-1], 0) + probabilidad

            
            elif len(palabras) > 1 and entrada[indice] == palabras[0]: #Caso se encuentre la palabra y las palabras alrededor de '_' se encuentren en rango, tomando la palabra predecesora
                
                diccionario_apariciones[entrada[indice+1]] = diccionario_apariciones.get(entrada[indice+1], 0) + probabilidad

            elif len(palabras) > 1 and entrada[indice] == palabras[1]: #Caso se encuentre la palabra y las palabras alrededor de '_' se encuentren en rango, tomando la palabra consiguiente

                diccionario_apariciones[entrada[indice-1]] = diccionario_apariciones.get(entrada[indice-1], 0) + probabilidad
    
    return diccionario_apariciones


#encontrarPalabra: Int List(String) List(String) Int Int -> String

#encontrarPalabra toma un entero posicion que sera el indice de '_' en la 2da lista de palabras, una lista de palabras que siempre sera mayor a la segunda 
#lista, un entero que sera un rango y otro entero que sera un numero de probabilidad, y
#mediante un diccionario llamado con los argumentos pasados y la funcion crearDiccionario, se elije/n la/s palabra/s que 
#cumpla/n la condicion de ser la de mayor valor numerico (apariciones) / mediante una eleccion aleatoria entre ellas.

#Entrada: 0 , ["soy","santino","y","vos"] , ["_","santino"] , 1 , 10    Salida: "soy"

def encontrarPalabra(posicion,entrada,frase,rango,probabilidad): #Se encuentra una palabra que cumpla las condiciones para reemplazar '_' en funcion a las palabras de su alrededor

    diccionario = crearDiccionario(posicion,entrada,frase,rango,probabilidad) #Se crea el diccionario de apariciones

    lista_final = [] #Creo una lista en la que se pondran las palabras con mayor o igual apariciones

    valores_diccionario = list(diccionario.values()) #Se toman los valores de las llaves del diccionario y crea una lista con ellos

    while(len(valores_diccionario) == 0): #Ciclo en el que sea el caso que las palabras alrededor de '_' no sean encontradas, se aumente el rango y disminuya la probabilidad de la palabra
        rango += 1
        probabilidad -= 1

        diccionario = crearDiccionario(posicion,entrada,frase,rango,probabilidad)

        valores_diccionario = list(diccionario.values())

    palabras_diccionario = list(diccionario.keys()) #Una vez que valores_diccionario no este vacio, se crea una lista con las llaves del diccionario, que seran las palabras

    mayor = 0

    for valor in valores_diccionario: #Se halla el mayor valor en la lista de valores
                
        if valor > mayor:
            mayor = valor
    
    for indice in range(len(valores_diccionario)): #Se agrega a la lista final todos los valores mayores o iguales que cumplan la condicion de ser la palabra encontrada

        if valores_diccionario[indice] == mayor:
            lista_final += [palabras_diccionario[indice]]
    
    return  lista_final[randint(0,(len(lista_final)-1))] #Se escoje una de las palabras en lista_final al azar para ser la palabra encontrada