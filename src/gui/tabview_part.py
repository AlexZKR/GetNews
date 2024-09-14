import customtkinter as ctk

from src.config.exceptions import NoInternetException
from src.config.gui_config import *
from src.get_data.parse_json import get_mon_ru_str, get_total_results, parseRawData, sort_by_month
from src.gui.table_part import TablePart

# https://customtkinter.tomschimansky.com/documentation/widgets/tabview


class TabViewPart(ctk.CTkTabview):
    def __init__(self, parent, msg_lbl_command, save_btn_cmd):
        super().__init__(master=parent, fg_color=DARK_GREEN)

        # from app
        self.set_msg_lbl_text = msg_lbl_command
        self.control_save_btn_cmd = save_btn_cmd

        # tabs
        self.months_tab = self.add("Months")
        self.period_tab = self.add("Period")

        # data
        self.unstructured_news_data = None

        self.cards_of_period = None  # cards of period chosen by user on tab_2
        self.cards_by_months = (
            None  # cards structured in dicts[months] for table display
        )
        self.table_display_data = []
        # months tab

        self.table_part = TablePart(self.months_tab, self.get_news_data)

        self.grid(column=0, row=1, sticky="nsew")

    def get_news_data(self):
        try:
            self.unstructured_news_data = parseRawData()
            self.set_msg_lbl_text(get_total_results(self.unstructured_news_data))
            self.cards_by_months = sort_by_month(self.unstructured_news_data)
            self.fill_table()
            self.control_save_btn_cmd(switch_on=True)
        except Exception as e:
            if isinstance(e, NoInternetException):
                self.set_msg_lbl_text(NO_INTERNET_CONNECTION)
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
