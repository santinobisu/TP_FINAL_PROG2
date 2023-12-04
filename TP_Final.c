#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// El programa toma un argumento:
// argc es el numero de argumentos (sera uno solo)
// argv[0] es el nombre del programa, y mi argumento sera argv[1]
// que a la hora de ejecutarlo se llamara asi: ./mi_programa argumento


// fgets(buff,255,archivo) toma la linea hasta \n incluido
// fscanf(archivo,"%s",buff) toma una cadena hasta antes de un espacio o \n sin incluirlo


int main(int argc, char *argv[]){

    char comando_system[255];
    sprintf(comando_system,"cd ./Textos/%s && ls > ../../archivos.txt", argv[1]); // Copio el argumento recibido en un array de caracteres que sera la linea ejecutada en system
    system(comando_system); // Se ejecuta la linea almacenada en comando_system, en donde se guardan por cada linea los textos del nombre pasado como parametro

    FILE lista_de_textos = fopen("archivos.txt","r");
    char x;
    int i = 0;
    while(x != EOF){
        x = fgetc(lista_de_textos); // x es: un caracter / un \n / EOF
        if x == '\n'{ // CASO: x es \n y por ende tengo un nombre de un archivo

            i = 0;
        }
        else{ // CASO: x es un caracter y por ende se guarda en un array de caracteres
            
        }
    }
    return 0;
}