import pytest
from tanslation import calculer_translation

@pytest.mark.parametrize("dict_coord, dict_trans,  resultat_attendu", [
    ({'Triangle1:': ['0,0', '2,0', '1,3']}, {'Triangle1:': ['2', '3']}, {'Triangle1:': ['2,3', '4,3', '3,6']}),
    ({}, {}, {}),
    ({'Triangle1:': ['0,0', '2,0', '1,3']}, {'Triangle1:': ['0', '0']}, {'Triangle1:': ['0,0', '2,0', '1,3']}),
    ({'Ligne:': ['0,0', '2,0']}, {'Ligne:': ['1', '1']}, {'Ligne:': ['1,1', '3,1']}),
    ( "Allo", 1, None),
])
def test_calculer_transaction(dict_coord, dict_trans, resultat_attendu):
    result = calculer_translation(dict_coord, dict_trans)
    assert result == resultat_attendu