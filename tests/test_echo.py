from main import ohce_echo
import pytest

def test_ohce_echo():
    # Test de la función ohce_echo
    assert ohce_echo('hola') == 'aloh'
    assert ohce_echo('mundo') == 'odnum'
    assert ohce_echo('Python') == 'nohtyP'
    assert ohce_echo('aibofobia') == 'aibofobia'