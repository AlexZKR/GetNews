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
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GREEN, command=None)

        # tabs
        self.period_tab = self.add(PERIOD_TAB_NAME)
        self.months_tab = self.add(MONTHS_TAB_NAME)

        # data
        self.unsorted_news_data = []

        # months tab
        self.table_part = TablePart(
            self.months_tab, unsorted_data=self.unsorted_news_data
        )
        # period tab
        self.period_choice_part = PeriodChoicePart(
            self.period_tab, unsorted_data=self.unsorted_news_data
        )

    def get_data(self) -> str:
        """Returns text for message lbl"""
        self.table_part.clear_table()
        self.unsorted_news_data.clear()
        self.unsorted_news_data.extend(parseRawData())

        self.table_part.enable_sort_btn()
        self.period_choice_part.enable_query_btn()

        return get_total_results(self.unsorted_news_data)

    # def on_tab_switch(self):
    #     active_tab = self.get()
    #     if active_tab == MONTHS_TAB_NAME:
    #         if not self.table_part.cards_by_months and self.unsorted_news_data:
    #             self.table_part.fill_table()
    #     if active_tab == PERIOD_TAB_NAME:
    #         pass

    def output_data(self) -> dict:
        active_tab = self.get()
        if active_tab == MONTHS_TAB_NAME:
            return self.table_part.output()
        if active_tab == PERIOD_TAB_NAME:
            self.output_period()
