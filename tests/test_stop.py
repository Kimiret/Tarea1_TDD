from main import ohce_stop
import pytest

def test_ohce_stop():
    assert ohce_stop('Stop!') == True