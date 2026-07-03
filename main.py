import FreeSimpleGUI as sg
from zip_extractor import archive_extract
sg.theme('DarkAmber')

label_size = (18, 1)

layout = [[sg.Text("Plik ZIP do rozpakowania",size=label_size),sg.Input(), sg.FileBrowse("Wybierz", key="archive")],
          [sg.Text("Folder docelowy",size=label_size),sg.Input(),sg.FolderBrowse("Wybierz", key="folder")],
          [sg.Button("Wypakuj")],[sg.Text(key="output", text_color="green")]]

window = sg.Window("Aplikacja rozpakowująca", layout)

while True:
    event, values = window.read()
    archive_path = values["archive"]
    dir_path = values["folder"]
    if values["archive"] == "" or values["folder"] == "":
        window["output"].update(value= "Uzupełnij pola", text_color="red")
    else:
        try:
            archive_extract(archive_path, dir_path)
            window["output"].update(value="Zakończono rozpakowywanie",text_color="green")
        except ValueError:
            window["output"].update(value="Zły format pliku",text_color="red")
    if event == sg.WIN_CLOSED: break

