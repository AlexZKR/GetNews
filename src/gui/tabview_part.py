import customtkinter as ctk

from src.config.exceptions import *
from src.config.gui_config import *
from src.get_data.parse_json import (
    get_total_results,
    parseRawData,
)
from src.gui.period_choice_part import PeriodChoicePart
from src.gui.table_part import TablePart

# https://customtkinter.tomschimansky.com/documentation/widgets/tabview


class TabViewPart(ctk.CTkTabview):
    def __init__(self, parent, msg_lbl_command, save_btn_cmd):
        super().__init__(master=parent, fg_color=DARK_GREEN)

        # from app
        self.set_msg_lbl_text = msg_lbl_command
        self.control_save_btn_cmd = save_btn_cmd
        self.has_data = False
        # tabs
        self.period_tab = self.add(PERIOD_TAB_NAME)
        self.months_tab = self.add(MONTHS_TAB_NAME)

        # data
        self.unstructured_news_data = None

        # months tab
        self.table_part = TablePart(self.months_tab, self.get_data)
        # period tab
        self.period_choice_part = PeriodChoicePart(self.period_tab)

        self.grid(column=0, row=1, sticky="nsew")

    def get_data(self):
        try:
            self.table_part.clear_table()
            self.unstructured_news_data = parseRawData()
            self.has_data = True
            self.set_msg_lbl_text(get_total_results(self.unstructured_news_data))
            self.table_part.fill_table(self.unstructured_news_data)
            self.control_save_btn_cmd()
        except Exception as e:
            if isinstance(e, NoInternetException):
                self.set_msg_lbl_text(NO_INTERNET_CONNECTION, WARNING)
            else:
                raise e

    def output_data(self) -> dict:
        active_tab = self.get()
        if active_tab == MONTHS_TAB_NAME:
            return self.table_part.output()
        if active_tab == PERIOD_TAB_NAME:
            self.output_period()
