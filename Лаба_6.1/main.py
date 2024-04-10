import PySimpleGUI as sg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv


def is_number(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False


def convert_to_normal_format(file_path):

    list_of_floats = []

    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        data_list = []
        for row in csv_reader:
            data_list.append(row)

    for row in data_list:
        for item in row:
            if is_number(item):
                list_of_floats.append(float(item))

    x = []
    y = []

    for i in range(1, len(data_list)):
        x.append(data_list[i][0])
        y.append(int(data_list[i][1]))

    xlabel = data_list[0][0]
    ylabel = data_list[0][1]
    return x, y, xlabel, ylabel


def display_graphic(plt_type):
    plt.figure(figsize=(11, 8))
    if plt_type == 'plot':
        plt.plot(x, y, label=xlabel)
    elif plt_type == 'scatter':
        plt.scatter(x, y, label=xlabel)
    elif plt_type == 'bar':
        plt.bar(x, y, label=xlabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(ylabel)
    plt.legend()
    plt.show()

sg.theme("GreenMono")
layout = [
    [sg.T("")],
    [
        sg.Text("Выберите файл: "),
        sg.Input(),
        sg.FileBrowse("Обзор", key="-IN-", file_types=(("CSV Files", "*.csv"),)),
    ],
    [sg.Button("Загрузить значения")],
    [sg.Button("Линейный", disabled=True), sg.Button("Scatterplot", disabled=True), sg.Button("Столбчатый", disabled=True)]
]

window = sg.Window("Визуализация CSV", layout, size=(600, 200))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Загрузить значения":
        csv_file_path = values["-IN-"]
        x, y, xlabel, ylabel = convert_to_normal_format(csv_file_path)
        window['Загрузить значения'].update(disabled=True)
        window['Линейный'].update(disabled=False)
        window['Scatterplot'].update(disabled=False)
        window['Столбчатый'].update(disabled=False)
        
    elif event == "Линейный" and x and y:
        display_graphic('plot')
    elif event == "Scatterplot" and x and y:
        display_graphic('scatter')
    elif event == "Столбчатый" and x and y:
        display_graphic('bar')
