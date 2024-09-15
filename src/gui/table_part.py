import customtkinter as ctk
from src.config.gui_config import *

from src.gui.basic.button import CustomButton


from .basic.table_header_lbl import TableHeaderLbl
from .basic.table_row import TableRow



class TablePart(ctk.CTkFrame):
    def __init__(self, parent, btn_command):
        super().__init__(master=parent, fg_color=DARK_GREEN)

        # layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1, uniform="a")
        self.rowconfigure(1, weight=2, uniform="a")

        # frames
        self.header_frame = ctk.CTkFrame(
            self, fg_color=TABLE_HEADER_ROW, corner_radius=0
        )
        # header row frame
        self.upper_row_frame = ctk.CTkFrame(
            self.header_frame, fg_color=TABLE_HEADER_ROW, corner_radius=0
        )
        # headings
        save_chck_row_heading = TableHeaderLbl(
            self.upper_row_frame, lbl_text="Сохранить"
        )
        period_row_heading = TableHeaderLbl(self.upper_row_frame, lbl_text="Период")
        count_row_heading = TableHeaderLbl(self.upper_row_frame, lbl_text="Количество")
        # headings layout
        save_chck_row_heading.pack(side="left", anchor="n", expand=True)
        period_row_heading.pack(side="left", anchor="n", expand=True)
        count_row_heading.pack(side="left", anchor="n", expand=True)

        # widgets
        btn = CustomButton(
            self.header_frame,
            btn_text=QUERY_BTN_TEXT,
            btn_command=btn_command,
        )

        # table part layout
        self.header_frame.grid(column=0, row=0, sticky="new", ipady=1)
        btn.pack(expand=True, fill="both", padx=10, pady=5)
        self.upper_row_frame.pack(expand=True, fill="x")

        # rows
        self.rows = []
        self.row_count = 0

        self.pack(expand=True, fill="both")

    def add_row(self, data: dict):
        self.row_count += 1
        row_color = self.get_row_color()

        self.rowconfigure(self.row_count, weight=1, uniform="r", pad=0)
        self.rows.append(
            TableRow(self, row_num=self.row_count, data=data, row_color=row_color)
        )

    def clear_table(self):
        for row in self.rows:
            row.exterminate()
        self.row_count = 0
        self.rows.clear()

    def get_row_color(self):
        if self.row_count % 2 == 0:
            return TABLE_ROW_ALT_COLOR
        else:
            return DARK_GREEN
