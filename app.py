import customtkinter as ctk
from src.config.exceptions import NoInternetException, SavePathDoesNotExistException
from src.config.gui_config import *
from customtkinter import filedialog
import datetime

from src.gui.request_part import RequestPart
from src.gui.table_part import TablePart
from src.gui.save_path_part import SavePathPart
from src.gui.basic.button import CustomButton


from src.output_data.scraper_output import output_results
from src.get_data.parse_json import parseNewsData

try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass


class App(ctk.CTk):
    def __init__(self):

        # window setup
        super().__init__(fg_color=GREEN)
        self.title("")
        # self.iconbitmap()
        self.geometry("400x400")
        self.resizable(False, False)
        self.change_title_bar_color()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1, uniform="a")
        self.rowconfigure(1, weight=2, uniform="a")
        self.rowconfigure(2, weight=1, uniform="a")
        self.rowconfigure(3, weight=1, uniform="a")

        # ctk variables

        self.message_label = ctk.StringVar(value=". . .")
        self.save_path = ctk.StringVar(value="Путь для сохранения не выбран")
        self.add_save_folder = ctk.BooleanVar(value=True)

        # data
        self.news_data = None
        self.table_data = []

        # widgets
        self.request_part = RequestPart(
            self, btn_command=self.get_news_data, variable=self.message_label
        )
        self.table_part = TablePart(self)
        self.save_path_part = SavePathPart(
            self, self.save_path, self.get_save_path, self.add_save_folder
        )

        self.save_btn_part = CustomButton(
            self, btn_text="Сохранить", btn_command=self.on_save
        )
        self.save_btn_part.grid(column=0, row=3, sticky="ew", padx=40)

        self.mainloop()

    def get_save_path(self):
        self.save_path.set(filedialog.askdirectory())
        print(self.table_data)

    def change_title_bar_color(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = TITLE_HEX_COLOR
            windll.dwmapi.DwmSetWindowAttribute(
                HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int)
            )
        except:
            pass

    def on_closing(self):
        # Cancel any pending callbacks
        self.after_cancel(self.request_part)
        self.after_cancel(self.table_part)
        self.after_cancel(self.save_path_part)
        self.destroy()

    def get_news_data(self):
        try:
            self.news_data = parseNewsData()
            self.message_label.set(self.get_total_results(self.news_data))
            self.fill_table()
        except Exception as e:
            if isinstance(e, NoInternetException):
                self.message_label.set("Нет подключения к Интернету!")
            else:
                print(e)

    def fill_table(self):
        for k in self.news_data.keys():
            tmp = {}
            tmp["ru_date"] = self.parse_datestring(k).strftime("%B %Y")
            tmp["numeric_date"] = k
            tmp["count"] = len(self.news_data[k])
            tmp["to_save"] = False
            self.table_data.append(tmp)

            self.table_part.add_row(tmp)

    def get_total_results(self, data):
        total_results = sum(len(v) for v in data.values())
        if total_results <= 0:
            return f"Получено {total_results} новостных карточек. Что-то пошло не так"
        else:
            return f"Получено {total_results} новостных карточек"

    def parse_datestring(self, string):
        return datetime.datetime.strptime(string, "%m.%Y")

    def on_save(self):
        output = []
        for item in self.table_data:
            if item["to_save"] == True:
                output.append(self.news_data.get(item["numeric_date"]))
        if len(output) > 0:
            try:
                output_results(output, self.save_path, self.add_save_folder)
            except Exception as e:
                if isinstance(e, SavePathDoesNotExistException):
                    self.message_label.set("Путь для сохранения не существует!")
                else:
                    self.message_label.set(e)


App()
