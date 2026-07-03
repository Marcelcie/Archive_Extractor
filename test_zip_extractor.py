import pytest
from unittest.mock import patch
from zip_extractor import archive_extract



@patch("zip_extractor.zipfile.ZipFile")

@patch("zip_extractor.zipfile.is_zipfile")
def test_archive_extract_sukces(mock_is_zipfile, mock_zipfile_class):
    mock_is_zipfile.return_value = True
    archive_extract("dobry_plik.zip", "udawany_folder")
    mock_is_zipfile.assert_called_once_with("dobry_plik.zip")