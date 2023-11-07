import tkinter as tk
import threading
from socket import *


class DarkSouls:
    # Иницииализация приложения сервера
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('DarkSoulsDie?')
        self.win.geometry("256x256+200+100")
        self.win.config(bg='#D8BFD8')

        self.setup()
        self.start()

    # Логика работы сервера
    def _server_run(self):
        server = socket(AF_INET, SOCK_STREAM)
        server.bind(("127.0.0.1", 12345))
        server.listen()

        user, addr = server.accept()
        while True:
            self.update_text()

    # Создание рамки приложения
    def setup(self):
        self.frame = tk.Frame(self.win, background='#D8BFD8')
        self.frame.pack(fill=tk.BOTH, expand=True)

    def start(self):
        new_thread = threading.Thread(target=self._server_run)
        new_thread.start()

    # Реакция сервера на нажатие кнопки из клиентского приложения
    def update_text(self):
        text = tk.Label(self.win, width=9, height=4, background='#D8BFD8', text='YOU DIED', font="Times 35")
        text.place(relx=0.5, rely=0.5, anchor='center')

        # Попытка реализовать вечный двигатель(Не удалась успехом.)
        btn = tk.Button(self.win, text='Rlly?', font="Times 35", width=4, height=2, command=self.click, bg='#EE82EE')
        btn.place(relx=0.5, rely=0.5, side='bottom')
        btn.focus()

    def click(self):
        self.client.send(bytes("\00", 'ascii'))

    def run(app):
        app.win.mainloop()


if __name__ == "__main__":
    app = DarkSouls()
    app.run()
