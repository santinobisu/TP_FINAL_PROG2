#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include "../funciones_aux/funciones.c"

void volcarATexto_testing(){
    char t1[50] = "Fito_Paez";
    assert(volcarATexto(t1) == 1);

    char t2[50] = "Sapo";
    assert(volcarATexto(t2) == -1);
}

void escribirArchivo_testing(){
    char resultado_esperado[] = "el amor despues del amor tal vez se parezca a este rayo de sol\ny ahora que busque y ahora que encontre el perfume que lleva el dolor\n";

    FILE *texto_a_leer = fopen("./Textos/Fito_Paez/elamordespuesdelamor.txt","r");
    FILE *texto_entrada = fopen("./Entradas/Fito_Paez.txt","w");

    escribirArchivo(texto_a_leer,texto_entrada);

    fclose(texto_a_leer);
    fclose(texto_entrada);

    FILE *texto_resultado = fopen("./Entradas/Fito_Paez.txt","r");
    char buffer[300];
    char resultado[300];

    while(fgets(buffer, sizeof(buffer), texto_resultado) != NULL)
    {
        strcat(resultado, buffer);
    }

    fclose(texto_resultado);

    assert(strcmp(resultado,resultado_esperado) == 0);
}

int main(){
    volcarATexto_testing();
    escribirArchivo_testing();
    printf("Testeos exitosos.\n");
    return 0;
}