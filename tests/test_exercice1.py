from exercices.exercice1 import *

def test_tableau_minmax():
    tableau = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1] 
    resultat = rechercheMinMax(tableau) 
    assert resultat  == {'min': -2, 'max': 9} 

def test_tableau_vide():
    tableau = [] 
    resultat = rechercheMinMax(tableau) 
    assert resultat  == {'min': None, 'max': None} 