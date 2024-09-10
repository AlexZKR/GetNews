import customtkinter as ctk
from config.gui_config import *

from .basic.button import CustomButton
from .basic.main_txt_label import MainTxtLbl


class RequestPart(ctk.CTkFrame):
    def __init__(self, parent, variable=None, btn_command=None):
        super().__init__(master=parent, fg_color=GREEN)

        # widgets
        btn = CustomButton(
            self,
            btn_text="Выполнить запрос",
            btn_command=btn_command,
        )
        lbl = MainTxtLbl(self, lbl_text="Данные о запросе", pad_y=10, variable = variable)
        # layout
        btn.pack()
        lbl.pack(expand=True, fill="x")
        self.grid(column=0, row=0)
