from main import ohce_echo
import pytest

def test_ohce_echo():
    assert ohce_echo('hola') == 'aloh'