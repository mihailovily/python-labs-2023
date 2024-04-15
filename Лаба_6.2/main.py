from pathlib import Path
import PySimpleGUI as sg


def popup_saver():
    sg.theme("GreenMono")


    layout = [
        [
            sg.Button("CSV"),
            sg.Button("HTML"),
            sg.Button("TXT")
        ]
    ]

    window = sg.Window("Saving", layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == "CSV":
            return '.csv'
        elif event == "HTML":
            return '.html'
        elif event == "TXT":
            return '.txt'

    window.close()


def popup_editor(filename, text):
    layout = [
        [sg.Button("Save"), sg.Button("Close")],
        [sg.Multiline(text, size=(15, 5), key="-text-", font="Helvitica 13")],
        [
            sg.CB("Bold", key="-bold-", change_submits=True),
            sg.CB("Italics", key="-italics-", change_submits=True),
            sg.CB("Underline", key="-underline-", change_submits=True),
        ],
        [
            sg.Slider(
                (6, 50),
                default_value=12,
                size=(14, 20),
                orientation="h",
                key="-slider-",
                change_submits=True,
            ),
            sg.Text("Font size"),
        ],
    ]
    window = sg.Window("Text Editor", layout)
    text_elem = window["-text-"]
    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Exit"):
            break
        elif event == "Save":
            filename = "test" + popup_saver()
            with open(filename, "w", encoding="utf-8") as f:
                test = values["-text-"]
                print(test)
                f.write(test)
                f.close()
        elif event == "Close":
            break
        font_string = "Helvitica "
        font_string += str(int(values["-slider-"]))
        if values["-bold-"]:
            font_string += " bold"
        if values["-italics-"]:
            font_string += " italic"
        if values["-underline-"]:
            font_string += " underline"
        text_elem.update(font=font_string)

    window.close()


sg.theme("GreenMono")

layout = [
    [
        sg.Input(key="-INPUT-"),
        sg.FileBrowse(file_types=(("TXT Files", "*.txt"), ("ALL Files", "*.*"))),
        sg.Button("Open"),
    ]
]

window = sg.Window("Choose file", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Open":
        filename = values["-INPUT-"]
        if Path(filename).is_file():
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    text = f.read()
                popup_editor(filename, text)
            except Exception as e:
                print("Error: ", e)

window.close()
