import customtkinter as ctk

from src.config.exceptions import *
from src.config.gui_config import *
from src.get_data.parse_json import (
    get_mon_ru_str,
    get_total_results,
    parseRawData,
    sort_by_month,
)
from src.gui.period_choice_part import PeriodChoicePart
from src.gui.table_part import TablePart
from src.output_data.scraper_output import output_results

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

        self.cards_of_period = None  # cards of period chosen by user on tab_2
        self.cards_by_months = (
            None  # cards structured in dicts[months] for table display
        )
        self.table_display_data = []

        # months tab
        self.table_part = TablePart(self.months_tab, self.get_news_data)

        # period tab
        self.period_choice_part = PeriodChoicePart(self.period_tab)

        self.grid(column=0, row=1, sticky="nsew")

    def get_news_data(self):
        try:
            self.table_part.clear_table()
            self.unstructured_news_data = parseRawData()
            self.has_data = True
            self.set_msg_lbl_text(get_total_results(self.unstructured_news_data))
            self.cards_by_months = sort_by_month(self.unstructured_news_data)
            self.fill_table()
            self.control_save_btn_cmd()
        except Exception as e:
            if isinstance(e, NoInternetException):
                self.set_msg_lbl_text(NO_INTERNET_CONNECTION, WARNING)
            else:
                raise e

    def fill_table(self):

        for k in self.cards_by_months:
            tmp = {}
            tmp["ru_month"] = get_mon_ru_str(k)
            tmp["numeric_date"] = k
            tmp["count"] = len(self.cards_by_months[k])
            tmp["to_save"] = False
            self.table_display_data.append(tmp)

            self.table_part.add_row(tmp)

    def output_data(self) -> dict:
        """Returns:
        dict:
        """
        active_tab = self.get()
        if active_tab == MONTHS_TAB_NAME:
            month_chosen = self.filter_output()
            if len(month_chosen) == 0:
                raise NoMonthsChosenException
            return self.get_data_to_output(month_chosen)
        if active_tab == PERIOD_TAB_NAME:
            self.output_period()

    def get_data_to_output(self, month_chosen) -> dict:
        output = {}
        for k in self.cards_by_months:
            if k in month_chosen:
                output[k] = self.cards_by_months[k]
        return output

    def filter_output(self) -> list:
        """Returns month which were chosen by user"""
        months_chosen = []
        for item in self.table_display_data:
            if item["to_save"] == True:
                months_chosen.append(item["numeric_date"])
        return months_chosen
