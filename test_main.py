import pytest
from unittest.mock import patch
import FreeSimpleGUI as sg
from main import main

@patch("main.sg.window")
def test_main_puste_pole(mock_window_class):
    mock_window = mock_window_class.return_value
    mock_window.read.side_effect = [
        ("Wypakuj",{"archive": "", "folder": ""}),
        (sg.WIN_CLOSED, None)
    ]


main()