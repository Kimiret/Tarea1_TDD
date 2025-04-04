from main import ohce_stop
import pytest

def test_ohce_stop():
    assert ohce_stop('Stop!') == True
    assert ohce_stop('stop') == False
    assert ohce_stop('Exit!') == False
    assert ohce_stop('') == False