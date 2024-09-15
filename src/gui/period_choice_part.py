import customtkinter as ctk
from src.config.gui_config import *


from src.gui.basic.button import CustomButton
from src.gui.basic.date_entry import CustomDateEntry
from src.gui.basic.message_label import MessageLbl
from src.gui.basic.smaller_lbl import SmallerLbl


class PeriodChoicePart(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GREEN)

        # layout
        self.columnconfigure(0, weight=1, uniform="f")
        self.columnconfigure(1, weight=2, uniform="f")

        self.rowconfigure((0, 1, 2, 3), weight=1, uniform="f")

        # ctk variables
        earlier = ctk.StringVar()
        later = ctk.StringVar()

        # widgets
        self.earlier_dateEntry = CustomDateEntry(self, variable=earlier)
        self.later_dateEntry = CustomDateEntry(self, variable=later)

        # labels
        self.header_lbl = MessageLbl(
            self, lbl_text=TAB_PERIOD_HEADING_TEXT, variable=None, font_size=21
        )
        self.earlier_txt_lbl = SmallerLbl(
            self, lbl_text=EARLIER_DATE_LBL, variable=None, font_size=20
        )
        self.later_txt_lbl = SmallerLbl(
            self, lbl_text=LATER_DATE_LBL, variable=None, font_size=20
        )
        self.query_btn = CustomButton(
            self, btn_text=PERIOD_TAB_QUERY_BTN_TEXT, btn_command=None
        )

        # placing
        self.header_lbl.grid(column=0, row=0, columnspan=2, sticky="nsew")
        self.earlier_txt_lbl.grid(column=0, row=1, sticky="e")
        self.earlier_dateEntry.grid(column=1, row=1, sticky="w", padx=30)
        self.later_txt_lbl.grid(column=0, row=2, sticky="e")
        self.later_dateEntry.grid(column=1, row=2, sticky="w", padx=30)
        self.query_btn.grid(column=0, columnspan=2, row=3, sticky="ew", padx=10, pady=5)
        self.pack(expand=True, fill="both")

        