import zipfile

def archive_extract(archive_path, dir_path):
    if zipfile.is_zipfile(archive_path):
        with zipfile.ZipFile(archive_path) as zf:
            zf.extractall(dir_path)
    else:
        raise ValueError("To nie jest archiwum!")
