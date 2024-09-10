import customtkinter as ctk
from gui_settings import *

from .basic.button import CustomButton
from .basic.main_txt_label import MainTxtLbl


class RequestPart(ctk.CTkFrame):
    def __init__(self, parent, btn_command=None):
        super().__init__(master=parent, fg_color=GREEN)

        # widgets
        btn = CustomButton(
            self,
            btn_text="Выполнить запрос",
            btn_command=lambda: print("Выполнить запрос"),
        )
        lbl = MainTxtLbl(self, lbl_text="Данные о запросе", pad_y=10)
        # layout
        btn.pack()
        lbl.pack(expand=True, fill="x")
        self.grid(column=0, row=0)
