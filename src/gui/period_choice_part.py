import datetime
import customtkinter as ctk
from datetime import datetime as dt, timezone

from src.config.exceptions import *
from src.config.gui_config import *

from src.gui.basic.button import CustomButton
from src.gui.basic.date_entry import CustomDateEntry
from src.gui.basic.message_label import MessageLbl
from src.gui.basic.smaller_lbl import SmallerLbl


class PeriodChoicePart(ctk.CTkFrame):
    def __init__(self, parent, unsorted_data: list):
        super().__init__(master=parent, fg_color=DARK_GREEN)

        # data
        self.unstruct_data = unsorted_data
        self.period_data = []
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

    def enable_query_btn(self):
        if len(self.unstruct_data) > 0:
            self.query_btn.configure(state="normal")

    def disable_query_btn(self):
        self.query_btn.configure(state="disabled")

    def get_news_for_period(self):
        earlier_date = self.earlier_dateEntry.entry.get_date()
        later_date = self.later_dateEntry.entry.get_date()

        earlier_index = self.get_first_index_by_date(later_date, self.unstruct_data)
        later_index = self.get_last_index_by_date(earlier_date, self.unstruct_data)
        self.period_data = self.unstruct_data[earlier_index : later_index + 1]
        text = self.get_result_msg()
        self.inner_message_lbl.set_text(text=text, mode=INFO)

    def get_result_msg(self):
        if len(self.period_data) <= 0:
            return PERIOD_TAB_NO_NEWS_FOR_PERIOD
        to_date = datetime.date.fromtimestamp(
            self.period_data[0]["Timestamp"]
        ).strftime("%d.%m.%Y")
        from_date = datetime.date.fromtimestamp(
            self.period_data[len(self.period_data) - 1]["Timestamp"]
        ).strftime("%d.%m.%Y")
        return f"{len(self.period_data)}{PERIOD_TAB_INNER_MSG_RESULT} с {from_date} по {to_date}"

    def get_first_index_by_date(self, date, list_of_dicts: list):
        # if selected date (validation occured earlier) is later than
        # the latest news date than return the latest news index
        # i.e. selected date is 18.09 (which is valid date)
        # but the latest news are 17.09, so the latest news is returned
        if datetime.date.fromtimestamp(list_of_dicts[0]["Timestamp"]) < date:
            return 0  # index of the first news
        for dict in list_of_dicts:
            news_d = datetime.date.fromtimestamp(dict["Timestamp"])
            if news_d == date:
                return list_of_dicts.index(dict)
        return -1

    def get_last_index_by_date(self, date, list_of_dicts: list):
        # if selected date (validation occured earlier) is earlier than
        # the earliest news date than return the earlies news index
        # i.e. selected date is 01.09 (which is valid date)
        # but the earliest news are 02.09, so the news from 02.09 are returned
        if (
            datetime.date.fromtimestamp(
                list_of_dicts[len(list_of_dicts) - 1]["Timestamp"]
            )
            > date
        ):
            return len(list_of_dicts)  # index of the first news

        for index, dict in enumerate(list_of_dicts):
            if datetime.date.fromtimestamp(dict["Timestamp"]) == date:
                if index + 1 > len(list_of_dicts):
                    return index  # this is the last dict of the list
                if (
                    datetime.date.fromtimestamp(list_of_dicts[index + 1]["Timestamp"])
                    != date
                ):
                    return index  # the next dict is of the next date, meaning this is the last news of the day
        return -1

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
            # self.inner_message_lbl.set_text(" ", INFO)
            return

    def color_border_red(self):
        self.earlier_dateEntry.configure(fg_color=WARNING_COLOR)
        self.later_dateEntry.configure(fg_color=WARNING_COLOR)

    def delete_border(self):
        self.earlier_dateEntry.configure(fg_color="transparent")
        self.later_dateEntry.configure(fg_color="transparent")
