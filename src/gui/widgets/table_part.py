import customtkinter as ctk


from .basic.table_header_lbl import TableHeaderLbl
from .basic.main_txt_label import MainTxtLbl
from gui_settings import *


class TablePart(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GREEN)

        # layout
        self.columnconfigure((0, 1, 2), weight=1)
        self.rowconfigure(0, weight=1)

        # headings
        save_pic_row_heading = TableHeaderLbl(self, lbl_text="Сохранить")
        period_row_heading = TableHeaderLbl(self, lbl_text="Период")
        count_row_heading = TableHeaderLbl(self, lbl_text="Количество")

        save_pic_row_heading.grid(column=0, row=0, sticky="n")
        period_row_heading.grid(column=1, row=0, sticky="n")
        count_row_heading.grid(column=2, row=0, sticky="n")

        self.grid(column=0, row=1, sticky="nsew", padx=15)
