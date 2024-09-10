import customtkinter as ctk
from config.gui_config import *

from gui.request_part import RequestPart
from gui.table_part import TablePart
from gui.save_path_part import SavePathPart
from gui.basic.button import CustomButton

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

        # widgets
        self.request_part = RequestPart(self)
        self.table_part = TablePart(self)
        self.save_path_part = SavePathPart(self)

        self.save_btn_part = CustomButton(self, btn_text="Сохранить", btn_command=None)
        self.save_btn_part.grid(column=0, row=3, sticky="ew", padx=40)

        self.mainloop()

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


App()
