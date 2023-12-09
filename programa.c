#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "./funciones_aux/funciones.c"

// El programa toma un argumento:
// argc es el numero de argumentos (sera uno solo)
// argv[0] es el nombre del programa, y mi argumento sera argv[1]
// que a la hora de ejecutarlo se llamara asi: ./mi_programa argumento


int main(int argc, char *argv[]){

    if(argc < 2){ // Se verifica que se haya pasado un argumento
        printf("Ingrese un parámetro al ejecutar el programa.\n");
        return -1;
    }

    if(volcarATexto(argv[1]) == -1){ // Se verifica que el directorio con el argumento pasado exista
        printf("El directorio con el argumento ingresado no existe.\n");
        return -1;
    }

    FILE *lista_de_textos = fopen("archivos.txt","r"); // Si el directorio anterior existia, se crea archivos.txt y se abre aca

    char linea_archivo_texto[255]; // Nombres de los archivos a procesarse
    char direcciones_entrada[300]; // Direcciones de archivos a usarse

    sprintf(direcciones_entrada, "./Entradas/%s.txt",argv[1]); // Direccion del archivo a crearse
    FILE *entrada = fopen(direcciones_entrada,"w"); // Se abre el archivo de entrada

    while(fscanf(lista_de_textos,"%s",linea_archivo_texto) != EOF){

        sprintf(direcciones_entrada,"./Textos/%s/%s",argv[1],linea_archivo_texto); // Direccion de un archivo de texto escrito en archivos.txt
    
        FILE *texto = fopen(direcciones_entrada,"r"); // Se abre el archivo de texto

        escribirArchivo(texto,entrada); // Se utiliza la funcion escribirArchivo, que se encarga de pasar el caracter a carater el texto en limpio a entrada

    fclose(texto); // Se cierra el archivo de texto que ya no se va a usar
    }

    fclose(entrada);
    
    fclose(lista_de_textos);

    char programa_phython[255]; // Almacenara el comando que ejecutara el programa en python

    sprintf(programa_phython,"python3 programa.py %s",argv[1]); // Se copia el comando en el array de caracteres

    system(programa_phython); // Finalmente se ejecuta el programa de python

    return 0;
}