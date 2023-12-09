import sys
sys.path.append('../')
from funciones_aux.funciones import *
import pytest

def palabrasAlrededor_testing():

    assert palabrasAlrededor(['hola','_','adios','no'],1) == ['hola','adios']
    assert palabrasAlrededor(['soy','un','_','programador'],2) == ['soy']
    assert palabrasAlrededor(['yo','_','en','mi','Dios'],3) == ['Dios']
    assert palabrasAlrededor(['quiero','ser','_','gran','licenciado'],2) == ['quiero','licenciado']

def crearDiccionario_testing():

    assert crearDiccionario(0,["soy","santino","y","vos"],["_","santino"],1,10) == {'soy':10}
    assert crearDiccionario(1,['el','apellido','es','bisutti','y','su','nombre','santino'],['el','_','es','bisutti'],1,6) == {'apellido':12}
    assert crearDiccionario(5,['la','salud','de','mi','paciente','es','critica'],['su','estado','de','salud','es','_'],2,7) == {'de':7}

def encontrarPalabra_testing():

    assert encontrarPalabra(0,["soy","santino","y","vos"],["_","santino"],1,10) == 'soy'
    assert encontrarPalabra(2,['mi','apellido','es','bisutti'],['su','apellido','_','gardier'],1,6) == 'es'
    assert encontrarPalabra(5,['la','salud','de','mi','paciente','es','critica'],['su','estado','de','salud','es','_'],2,7) == 'de'


palabrasAlrededor_testing()
crearDiccionario_testing()
encontrarPalabra_testing()