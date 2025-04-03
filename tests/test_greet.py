from main import ohce_greeting
import pytest
from unittest.mock import patch
from datetime import datetime


@patch('main.datetime')
def test_ohce_greeting(mock_datetime):

    #Saludo mañana con nombre Juan
    mock_datetime.now.returnvalue = datetime(2023, 10, 1, 9, 0, 0)
    assert ohce_greeting('Juan') == '¡Buenos días Juan!'

    #Saludo mañana con nombre Pedro
    mock_datetime.now.returnvalue = datetime(2023, 10, 1, 9, 0, 0)
    assert ohce_greeting('Pedro') == '¡Buenos días Pedro!'

    #Saludo mañana con nombre Luis
    mock_datetime.now.returnvalue = datetime(2023, 10, 1, 9, 0, 0)
    assert ohce_greeting('Luis') == '¡Buenos días Luis!'

    #Saludo Tarde con nombre Juan
    mock_datetime.now.returnvalue = datetime(2023, 10, 1, 15, 0, 0)
    assert ohce_greeting('Juan') == '¡Buenas tardes Juan!'

    #Saludo Tarde con nombre Pedro
    mock_datetime.now.returnvalue = datetime(2023, 10, 1, 15, 0, 0)
    assert ohce_greeting('Pedro') == '¡Buenas tardes Pedro!'

    #Saludo Tarde con nombre Luis
    mock_datetime.now.returnvalue = datetime(2023, 10, 1, 15, 0, 0)
    assert ohce_greeting('Luis') == '¡Buenas tardes Luis!'