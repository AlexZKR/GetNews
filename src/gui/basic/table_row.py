import customtkinter as ctk
from src.config.gui_config import *

from .table_row_lbl import TableRowLbl


class TableRow(ctk.CTkFrame):
    def __init__(self, parent, row_num, data):
        super().__init__(master=parent, fg_color=DARK_GREEN, corner_radius=0)
        self.data = data
        # layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1, uniform="d")
        self.columnconfigure(1, weight=1, uniform="d")
        self.columnconfigure(2, weight=1, uniform="d")

        # widgets
        checkbox = ctk.CTkCheckBox(
            self,
            text="",
            border_color=TABLE_HEADER_ROW,
            hover_color=GREEN,
            command=self.on_checked,
        )
        periodLbl = TableRowLbl(self, lbl_text=self.data["ru_month"])
        countLbl = TableRowLbl(self, lbl_text=self.data["count"])

        checkbox.grid(row=0, column=0, sticky="ns", padx=45)
        periodLbl.grid(row=0, column=1, sticky="n")
        countLbl.grid(row=0, column=2, sticky="n")

        self.grid(column=0, row=row_num, sticky="ew", ipady=5)

        # events
        bind_tag = f"row{row_num}_widgets"
        self.retag(bind_tag, self, checkbox, periodLbl, countLbl)
        self.bind_class(bind_tag, "<Enter>", self.on_hover)
        self.bind_class(bind_tag, "<Leave>", self.on_leave)

    def retag(self, tag, *args):
        """Add the given tag as the first bindtag for every widget passed in"""
        for widget in args:
            widget.bindtags((tag,) + widget.bindtags())

    def on_leave(self, *args):
        self.configure(fg_color=DARK_GREEN)

    def on_hover(self, *args):
        self.configure(fg_color=GRAY)

    def on_checked(self):
        if self.data["to_save"] == False:
            self.data["to_save"] = True
        else:
            self.data["to_save"] = False
