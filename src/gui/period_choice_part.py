import customtkinter as ctk

from src.config.exceptions import *
from src.config.gui_config import *
from src.services.data_conversion import *

from src.gui.basic.button import CustomButton
from src.gui.basic.date_entry import CustomDateEntry
from src.gui.basic.message_label import MessageLbl
from src.gui.basic.smaller_lbl import SmallerLbl
from src.services.period_list import get_period_list


class PeriodChoicePart(ctk.CTkFrame):
    def __init__(self, parent, unsorted_data: list = []):
        super().__init__(master=parent, fg_color=DARK_GREEN)

        # data
        self.unstruct_data = unsorted_data
        self.period_data = []

        # layout
        self.columnconfigure(0, weight=1, uniform="f")
        self.columnconfigure(1, weight=2, uniform="f")

        self.rowconfigure((0, 1, 2, 3), weight=1, uniform="f")

        # widgets
        self.earlier_dateEntry = CustomDateEntry(self)
        self.later_dateEntry = CustomDateEntry(self)

        # events
        self.earlier_dateEntry.entry.bind("<<DateEntrySelected>>", self.validate_dates)
        self.later_dateEntry.entry.bind("<<DateEntrySelected>>", self.validate_dates)

        # properties
        self.early_ent_date = self.earlier_dateEntry.entry.get_date
        self.later_ent_date = self.later_dateEntry.entry.get_date

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
        self.inner_message_lbl = MessageLbl(
            self, default_text=PERIOD_MESSAGE_LBL_DEFAULT_TEXT, font_size=22
        )

        # placing
        self.query_btn.grid(column=0, columnspan=2, row=0, sticky="ew", padx=10, pady=5)

        self.earlier_txt_lbl.grid(column=0, row=1, sticky="e")
        self.earlier_dateEntry.grid(column=1, row=1, sticky="w", padx=30)

        self.later_txt_lbl.grid(column=0, row=2, sticky="e")
        self.later_dateEntry.grid(column=1, row=2, sticky="w", padx=30)

        self.inner_message_lbl.grid(column=0, columnspan=2, row=3, sticky="nsew")

        self.pack(expand=True, fill="both")

    def output(self) -> tuple:
        if len(self.period_data) == 0:
            raise NoPeriodChosenException
        dates = self.get_list_outer_dates()
        if dates[0] != dates[1]:
            return (
                f"{dates[1]} - {dates[0]}",
                self.period_data,
            )  # if period was chosen
        else:
            return (f"{dates[0]}", self.period_data)  # if one day was chosen

    def get_news_for_period(self):
        self.period_data = get_period_list(
            news_list=self.unstruct_data,
            start_date=self.early_ent_date(),
            end_date=self.later_ent_date(),
        )
        self.inner_message_lbl.set_text(text=self.get_result_msg(), mode=INFO)

    def get_result_msg(self):
        if len(self.period_data) <= 0:
            return PERIOD_TAB_NO_NEWS_FOR_PERIOD
        dates = self.get_list_outer_dates()
        if dates[1] != dates[0]:
            return f"{len(self.period_data)}{PERIOD_TAB_INNER_MSG_RESULT} период с {dates[1]} по {dates[0]}"
        else:
            return f"{len(self.period_data)}{PERIOD_TAB_INNER_MSG_RESULT} за {dates[0]}"

    def get_list_outer_dates(self) -> tuple:
        to_date = get_full_date_str(self.period_data[0]["Timestamp"])
        from_date = get_full_date_str(
            self.period_data[len(self.period_data) - 1]["Timestamp"]
        )
        return (to_date, from_date)

    def validate_dates(self, event):
        if (self.early_ent_date() > self.later_ent_date()) or (
            self.later_ent_date() < self.early_ent_date()
        ):
            self.color_border_red()
            self.disable_query_btn()
            self.inner_message_lbl.set_text(PERIOD_TAB_INCORRECT_DATES, WARNING)
            return
        else:
            self.delete_border()
            self.enable_query_btn()
            return

    def color_border_red(self):
        self.earlier_dateEntry.configure(fg_color=WARNING_COLOR)
        self.later_dateEntry.configure(fg_color=WARNING_COLOR)

    def delete_border(self):
        self.earlier_dateEntry.configure(fg_color="transparent")
        self.later_dateEntry.configure(fg_color="transparent")

    def enable_query_btn(self):
        if len(self.unstruct_data) > 0:
            self.query_btn.configure(state="normal")

    def disable_query_btn(self):
        self.query_btn.configure(state="disabled")
