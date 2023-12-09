#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int volcarATexto(char *argumento);
void escribirArchivo(FILE *texto, FILE *entrada);

// volcarATexto: char * -> int

// volcarATexto toma un argumento que sera un char pointer (es decir, un string), y
// se encarga de verificar si el directorio dentro de la carpeta Textos existe, en cuyo
// caso vuelca los contenidos de dicho directorio en un texto llamado "archivos.txt" y 
// devuelve 1, y en caso contrario devuelve -1.

// Entrada: "Fito_Paez"      Salida: 1
// Entrada: "Sapo"           Salida: -1 

int volcarATexto(char *argumento){

    char comando_system[255];
    sprintf(comando_system, "./Textos/%s",argumento);
    FILE *atexto = fopen(comando_system,"r");

    if (!atexto){
        return -1;
    }

    fclose(atexto);

    sprintf(comando_system, "cd ./Textos/%s && ls > ../../archivos.txt",argumento);

    system(comando_system);

    return 1;
}

// escribirArchivo: FILE FILE -> void

// escribirArchivo toma un achivo de texto escrito y un archivo de texto a escribir.
// Se encarga de tomar caracter a carater mediante una iteracion al archivo escrito
// y mediante condiciones pasar parseado a partir de ciertas condiciones todo el texto
// al archivo a escribir.

// Entrada: ./Textos/Andres_Calamaro.txt ./Entradas/Andres_Calamaro.txt    Salida: Void (Se realizan cambios internos en el archivo)

void escribirArchivo(FILE *texto, FILE *entrada){

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
}
