import customtkinter as ctk


from .basic.table_header_lbl import TableHeaderLbl
from .basic.table_row import TableRow

from src.config.gui_config import *


class TablePart(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GREEN)

        # layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1, uniform="a")

        # headings

        header_frame = ctk.CTkFrame(self, fg_color=TABLE_HEADER_ROW, corner_radius=0)

        save_chck_row_heading = TableHeaderLbl(header_frame, lbl_text="Сохранить")
        period_row_heading = TableHeaderLbl(header_frame, lbl_text="Период")
        count_row_heading = TableHeaderLbl(header_frame, lbl_text="Количество")

        header_frame.grid(column=0, row=0, sticky="new", ipady=1)

        save_chck_row_heading.pack(side="left", anchor="n", expand=True)
        period_row_heading.pack(side="left", anchor="n", expand=True)
        count_row_heading.pack(side="left", anchor="n", expand=True)

        # save_chck_row_heading.grid(column=0, row=0, sticky="n")
        # period_row_heading.grid(column=1, row=0, sticky="n")
        # count_row_heading.grid(column=2, row=0, sticky="n")

        # rows
        self.rows = []
        self.row_count = 0

        self.grid(column=0, row=1, sticky="nsew", padx=15)

    def add_row(self, data: dict):
        self.row_count += 1
        self.rowconfigure(self.row_count, weight=1, uniform="a")
        self.rows.append(TableRow(self, row_num=self.row_count, data=data))
