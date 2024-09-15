import customtkinter as ctk
from src.config.exceptions import NoMonthsChosenException
from src.config.gui_config import *

from src.get_data.parse_json import get_mon_ru_str, sort_by_month
from src.gui.basic.button import CustomButton


from .basic.table_header_lbl import TableHeaderLbl
from .basic.table_row import TableRow


class TablePart(ctk.CTkFrame):
    def __init__(self, parent, unsorted_data):
        super().__init__(master=parent, fg_color=DARK_GREEN)

        # data
        self.unsorted_data = unsorted_data
        self.cards_by_months = {}
        self.table_display_data = []

        # layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1, uniform="a")
        self.rowconfigure(1, weight=2, uniform="a")

        # frames
        self.header_frame = ctk.CTkFrame(
            self, fg_color=TABLE_HEADER_ROW, corner_radius=0
        )
        # header row frame
        self.upper_row_frame = ctk.CTkFrame(
            self.header_frame, fg_color=TABLE_HEADER_ROW, corner_radius=0
        )
        # headings
        save_chck_row_heading = TableHeaderLbl(
            self.upper_row_frame, lbl_text="Сохранить"
        )
        period_row_heading = TableHeaderLbl(self.upper_row_frame, lbl_text="Период")
        count_row_heading = TableHeaderLbl(self.upper_row_frame, lbl_text="Количество")

        # headings layout
        save_chck_row_heading.pack(side="left", anchor="n", expand=True)
        period_row_heading.pack(side="left", anchor="n", expand=True)
        count_row_heading.pack(side="left", anchor="n", expand=True)

        # widgets
        self.sort_btn = CustomButton(
            self.header_frame,
            btn_text=TABLE_FILL_BTN_TEXT,
            btn_command=self.fill_table,
            state="disabled",
        )

        # table part layout
        self.header_frame.grid(column=0, row=0, sticky="new", ipady=1)
        self.sort_btn.pack(expand=True, fill="both", padx=10, pady=5)
        self.upper_row_frame.pack(expand=True, fill="x")

        # rows
        self.rows = []
        self.row_count = 0

        self.pack(expand=True, fill="both")

    def enable_sort_btn(self):
        self.sort_btn.configure(state="normal")

    def fill_table(self):
        self.cards_by_months = sort_by_month(self.unsorted_data)
        for k in self.cards_by_months:
            tmp = {}
            tmp["ru_month"] = get_mon_ru_str(k)
            tmp["numeric_date"] = k
            tmp["count"] = len(self.cards_by_months[k])
            tmp["to_save"] = False
            self.table_display_data.append(tmp)

            self.add_row(tmp)

    def clear_table(self):
        for row in self.rows:
            row.exterminate()
        self.row_count = 0
        self.rows.clear()

        self.cards_by_months.clear()
        self.table_display_data.clear()

    def output(self) -> dict:
        output = {}
        month_chosen = self.get_months_chosen()
        for k in self.cards_by_months:
            if k in month_chosen:
                output[k] = self.cards_by_months[k]
        return output

    def get_months_chosen(self) -> list:
        """Returns month which were chosen by user"""
        months_chosen = []
        for item in self.table_display_data:
            if item["to_save"] == True:
                months_chosen.append(item["numeric_date"])
        if len(months_chosen) == 0:
            raise NoMonthsChosenException
        return months_chosen

    def add_row(self, data: dict):
        self.row_count += 1
        row_color = self.get_row_color()

        self.rowconfigure(self.row_count, weight=1, uniform="r", pad=0)
        self.rows.append(
            TableRow(self, row_num=self.row_count, data=data, row_color=row_color)
        )

    def get_row_color(self):
        if self.row_count % 2 == 0:
            return TABLE_ROW_ALT_COLOR
        else:
            return DARK_GREEN
