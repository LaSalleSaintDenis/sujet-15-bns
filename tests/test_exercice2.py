from exercices.exercice2 import *

import pytest

@pytest.fixture
def unPaquet():
    paquet = PaquetDeCarte()
    paquet.remplir()
    return paquet

@pytest.fixture
def uneCarte(unPaquet):
    return unPaquet.getCarteAt(20)

def test_carte_nom(uneCarte):
    assert uneCarte.getNom() == '7'


def test_carte_couleur(uneCarte):
    assert uneCarte.getCouleur() == 'coeur'

