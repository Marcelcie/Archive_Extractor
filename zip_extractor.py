import zipfile
import rarfile


"""
Funkcja do sprawdzania czy pliki są formatu zip lub rar.
"""
rarfile.UNRAR_TOOL = r"UnRAR.exe"

def archive_extract(archive_path, dir_path):

    if zipfile.is_zipfile(archive_path):
        with zipfile.ZipFile(archive_path) as zf:
            zf.extractall(dir_path)

    elif rarfile.is_rarfile(archive_path):
        with rarfile.RarFile(archive_path) as rf:
            rf.extractall(dir_path)
    else:
        raise ValueError("Zły format pliku")
