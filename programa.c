#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// El programa toma un argumento:
// argc es el numero de argumentos (sera uno solo)
// argv[0] es el nombre del programa, y mi argumento sera argv[1]
// que a la hora de ejecutarlo se llamara asi: ./mi_programa argumento


int main(int argc, char *argv[]){

    char comando_system[255];

    sprintf(comando_system,"cd ./Textos/%s && ls > ../../archivos.txt", argv[1]); // Copio el argumento recibido en un array de caracteres que sera la linea ejecutada en system
    system(comando_system); // Se ejecuta la linea almacenada en comando_system, en donde se guardan por cada linea los textos del nombre pasado como parametro

    FILE *lista_de_textos = fopen("archivos.txt","r");

    char direccion_archivo_entrada[255];
    char linea_archivo_texto[255];
    char direccion_texto[300];

    while(fscanf(lista_de_textos,"%s",linea_archivo_texto) != EOF){

        char direccion_argumento[255]; 

        sprintf(direccion_texto,"./Textos/%s/%s",argv[1],linea_archivo_texto); // Direccion de un archivo de texto escrito en archivos.txt
        sprintf(direccion_archivo_entrada, "./Entradas/%s.txt",argv[1]); // Direccion del archivo a crearse

        FILE *texto = fopen(direccion_texto,"r"); // Se abre el archivo de texto
        FILE *entrada = fopen(direccion_archivo_entrada,"a"); // Se abre el archivo de entrada

        char c = fgetc(texto); // Se tomara caracter por caracter de el texto
        char caracter_anterior = '\0'; // Y se verificara cual es el caracter anterior para establecer condiciones en ciertos casos especificos

        while(c != EOF){

            if(c >= 97 && c <= 122){ // Caso el caracter es una letra del alfabeto minuscula
                fputc(c,entrada);
                caracter_anterior = c;
            }
            else if(c >= 65 && c <=90){ // Caso el caracter es una letra del alfabeto mayuscula
                fputc(c+32,entrada);
                caracter_anterior = c + 32;
            }
            else if(c == '.' && caracter_anterior != '.'){ // Caso el caracter sea un punto, es decir, el fin de una oracion
                fputc('\n',entrada);
                caracter_anterior = c;
            }
            else if(c == '\n' && caracter_anterior != '.'){ // Caso el caracter es un salto de linea, siempre y cuando no este precedido por un punto
                fputc(' ',entrada);
                caracter_anterior = c;
            }
            else if(c == ' ' && caracter_anterior != '\n' && caracter_anterior != '.'){ // Caso el caracter es un espacio, siempre y cuando no sea precedido por un salto de linea ni un punto
                fputc(' ',entrada);
                caracter_anterior = c;
            }
            else if (c >= 48 && c <= 57){ // Caso el caracter es un digito
                fputc(c,entrada);
                caracter_anterior = c;
            }

            c = fgetc(texto); // Actualizo al siguiente caracter
        }

    fclose(texto);
    fclose(entrada);

    }
    
    fclose(lista_de_textos);

    char programa_phython[255]; // Almacenara el comando que ejecutara el programa en python

    sprintf(programa_phython,"python3 programa.py %s",argv[1]); // Se copia el comando en el array de caracteres

    system(programa_phython); // Finalmente se ejecuta el programa de python

    return 0;
}
