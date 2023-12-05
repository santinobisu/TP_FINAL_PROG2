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

    char comando_system[400];

    sprintf(comando_system,"cd ./Textos/%s && ls > ../../archivos.txt", argv[1]); // Copio el argumento recibido en un array de caracteres que sera la linea ejecutada en system
    system(comando_system); // Se ejecuta la linea almacenada en comando_system, en donde se guardan por cada linea los textos del nombre pasado como parametro

    FILE *lista_de_textos = fopen("archivos.txt","r");

    char direccion_archivo_entrada[400];
    char linea_archivo_texto[400];
    char direccion_texto[500]; // Los warnings se fueron al darle mas espacio a direccion_texto que a direccion_archivo_entrada

    while(fscanf(lista_de_textos,"%s",linea_archivo_texto) != EOF){

        char direccion_argumento[400]; 

        sprintf(direccion_texto,"./Textos/%s/%s",argv[1],linea_archivo_texto); // Direccion de un archivo de texto escrito en archivos.txt
        sprintf(direccion_archivo_entrada, "./Entradas/%s.txt",argv[1]); // Direccion del archivo a crearse

        FILE *texto = fopen(direccion_texto,"r"); // Se abre el archivo de texto
        FILE *entrada = fopen(direccion_archivo_entrada,"a"); // Se abre el archivo de entrada

        char linea_entrada[5000]; // Problema: El espacio es limitado

        int j = 0; // Posicion de linea_entrada
        char c = fgetc(texto);
        char caracter_anterior = '\0';

        while(c != EOF){

            if(c >= 97 && c <= 122){
                linea_entrada[j] = c;
                caracter_anterior = c;
                j += 1;
            }
            else if(c >= 65 && c <=90){
                linea_entrada[j] = c + 32;
                caracter_anterior = c + 32;
                j += 1;
            }
            else if(c == '.' && caracter_anterior != '.'){
                linea_entrada[j] = '\n';
                caracter_anterior = c;
                j += 1;
            }
            else if(c == '\n' && caracter_anterior != '.'){
                linea_entrada[j] = ' ';
                caracter_anterior = c;
                j += 1;
            }
            else if(c == ' ' && caracter_anterior != '\n' && caracter_anterior != '.'){
                linea_entrada[j] = ' ';
                caracter_anterior = c;
                j += 1;
            }
            else if (c >= 48 && c <= 57){
                linea_entrada[j] = c;
                caracter_anterior = c;
                j += 1;
            }

            c = fgetc(texto);
        }
    
    fputs(linea_entrada,entrada);
    fclose(texto);
    fclose(entrada);

    }
    
    fclose(lista_de_textos);

    return 0;
}

// Calamaro: Cuando hay un caracter especial(como ':' o ',') y un salto de linea 
// seguido se genera un doble espacio

// Canciones para ninos : Curado

// Diego Torres : Caracter extraño en linea 32

// Fabiana Cantilo : Fuga de un fragmento de cancion en otra

// Fito Paez : Curado

// Luis Spinetta : Caracter extraño al final del archivo (tal vez tenga que ver
// con que es el ultimo en procesarse)