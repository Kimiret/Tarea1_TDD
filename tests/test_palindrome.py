from main import ohce_palindrome
import pytest

def test_ohce_palindrome():
    # Test de la función ohce_palindrome
    assert ohce_palindrome('aibofobia') == True
    assert ohce_palindrome('anitalavalatina') == True
    assert ohce_palindrome('hola mundo') == False