from main import ohce_greeting
import pytest
from unittest.mock import patch
from datetime import datetime


@patch('main.datetime')
def test_ohce_greeting(mock_datetime):
    #Saludo mañana
    mock_datetime.now.returnvalue = datetime(2023, 10, 1, 9, 0, 0)
    assert ohce_greeting('Juan') == '¡Buenos días Juan!'