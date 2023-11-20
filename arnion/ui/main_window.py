import tkinter as tk


class MainWindow:
    # Конструктор
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('310x380')
        self.window.title('SPAN')

    # Запуск цикла
    def start_mainloop(self):
        self.window.mainloop()
