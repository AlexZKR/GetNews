import customtkinter as ctk
from src.config.exceptions import *
from src.config.gui_config import *

from datetime import datetime

from src.gui.basic.button import CustomButton
from src.gui.basic.date_entry import CustomDateEntry
from src.gui.basic.message_label import MessageLbl
from src.gui.basic.smaller_lbl import SmallerLbl


class PeriodChoicePart(ctk.CTkFrame):
    def __init__(self, parent, unsorted_data):
        super().__init__(master=parent, fg_color=DARK_GREEN)

        # data
        self.unsorted_data = unsorted_data

        # layout
        self.columnconfigure(0, weight=1, uniform="f")
        self.columnconfigure(1, weight=2, uniform="f")

        self.rowconfigure((0, 1, 2, 3), weight=1, uniform="f")

        # ctk variables
        self.earlier = ctk.StringVar()
        self.later = ctk.StringVar()

        # widgets
        self.earlier_dateEntry = CustomDateEntry(self, variable=self.earlier)
        self.later_dateEntry = CustomDateEntry(self, variable=self.later)

        # events
        self.earlier_dateEntry.entry.bind("<<DateEntrySelected>>", self.validate_dates)
        self.later_dateEntry.entry.bind("<<DateEntrySelected>>", self.validate_dates)

        # labels
        self.query_btn = CustomButton(
            self,
            btn_text=PERIOD_TAB_QUERY_BTN_TEXT,
            btn_command=self.get_news_for_period,
            state="disabled",
        )
        self.earlier_txt_lbl = SmallerLbl(
            self, lbl_text=EARLIER_DATE_LBL, variable=None, font_size=20
        )
        self.later_txt_lbl = SmallerLbl(
            self, lbl_text=LATER_DATE_LBL, variable=None, font_size=20
        )
        self.inner_message_lbl = MessageLbl(self, default_text="", font_size=22)

        # placing
        self.query_btn.grid(column=0, columnspan=2, row=0, sticky="ew", padx=10, pady=5)

        self.earlier_txt_lbl.grid(column=0, row=1, sticky="e")
        self.earlier_dateEntry.grid(column=1, row=1, sticky="w", padx=30)

        self.later_txt_lbl.grid(column=0, row=2, sticky="e")
        self.later_dateEntry.grid(column=1, row=2, sticky="w", padx=30)

        self.inner_message_lbl.grid(column=0, columnspan=2, row=3, sticky="nsew")

        self.pack(expand=True, fill="both")

    def enable_query_btn(self):
        if len(self.unsorted_data) > 0:
            self.query_btn.configure(state="normal")

    def disable_query_btn(self):
        self.query_btn.configure(state="disabled")

    def get_news_for_period(self):
        pass

    def validate_dates(self, _):
        earlier_date = self.earlier_dateEntry.entry.get_date()
        later_date = self.later_dateEntry.entry.get_date()
        if (earlier_date > later_date) or (later_date < earlier_date):
            self.color_border_red()
            self.disable_query_btn()
            self.inner_message_lbl.set_text(PERIOD_TAB_INCORRECT_DATES, WARNING)
            return
        else:
            self.delete_border()
            self.enable_query_btn()
            self.inner_message_lbl.set_text(" ", INFO)
            return

    def color_border_red(self):
        self.earlier_dateEntry.configure(fg_color=WARNING_COLOR)
        self.later_dateEntry.configure(fg_color=WARNING_COLOR)

    def delete_border(self):
        self.earlier_dateEntry.configure(fg_color="transparent")
        self.later_dateEntry.configure(fg_color="transparent")
