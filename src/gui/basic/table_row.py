import customtkinter as ctk
from config.gui_config import *

from .table_row_lbl import TableRowLbl


class TableRow(ctk.CTkFrame):
    def __init__(self, parent, row_num, data):
        super().__init__(master=parent, fg_color=DARK_GREEN)

        # layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1, uniform="a")
        self.columnconfigure(1, weight=1, uniform="a")
        self.columnconfigure(2, weight=1, uniform="a")

        # widgets
        checkbox = ctk.CTkCheckBox(
            self,
            text="",
            border_color=TABLE_HEADER_ROW,
            hover_color=GREEN,
        )
        periodLbl = TableRowLbl(self, lbl_text=data["ru_date"])
        countLbl = TableRowLbl(self, lbl_text=data["count"])

        checkbox.grid(row=0, column=0, sticky="n", padx=45)
        periodLbl.grid(row=0, column=1, sticky="n")
        countLbl.grid(row=0, column=2, sticky="n")

        # checkbox.pack(side="left", anchor="n", expand=True)
        # periodLbl.pack(side="left", anchor="n", expand=True)
        # countLbl.pack(side="left", anchor="n", expand=True)

        self.grid(column=0, row=row_num, sticky="ew")
