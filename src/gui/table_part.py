import customtkinter as ctk

from src.gui.basic.button import CustomButton


from .basic.table_header_lbl import TableHeaderLbl
from .basic.table_row import TableRow

from src.config.gui_config import *


class TablePart(ctk.CTkFrame):
    def __init__(self, parent, btn_command):
        super().__init__(master=parent, fg_color=DARK_GREEN)

        # layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1, uniform="a")
        self.rowconfigure(1, weight=2, uniform="a")

        btn = CustomButton(
            self,
            btn_text=QUERY_BTN_TEXT,
            btn_command=btn_command,
        )
        btn.grid(column=0, row=0)
        # headings

        header_frame = ctk.CTkFrame(self, fg_color=TABLE_HEADER_ROW, corner_radius=0)

        save_chck_row_heading = TableHeaderLbl(header_frame, lbl_text="Сохранить")
        period_row_heading = TableHeaderLbl(header_frame, lbl_text="Период")
        count_row_heading = TableHeaderLbl(header_frame, lbl_text="Количество")

        header_frame.grid(column=0, row=1, sticky="new", ipady=1)

        save_chck_row_heading.pack(side="left", anchor="n", expand=True)
        period_row_heading.pack(side="left", anchor="n", expand=True)
        count_row_heading.pack(side="left", anchor="n", expand=True)

        # rows
        self.rows = []
        self.row_count = 0

        # self.grid(column=0, row=1, sticky="nsew")
        self.pack(expand=True, fill="both")

    def add_row(self, data: dict):
        self.row_count += 1
        self.rowconfigure(self.row_count, weight=1, uniform="r", pad=0)
        self.rows.append(TableRow(self, row_num=self.row_count, data=data))
