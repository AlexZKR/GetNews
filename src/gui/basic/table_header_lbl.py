import customtkinter as ctk
from src.config.gui_config import *


class TableHeaderLbl(ctk.CTkLabel):

    def __init__(
        self,
        parent,
        lbl_text,
        pad_x=0,
        pad_y=0,
    ):
        super().__init__(
            master=parent,
            text=lbl_text,
            font=ctk.CTkFont(family=FONT, size=TABLE_HEADING_FONT_SIZE),
            text_color=BLACK,
            bg_color='transparent',
            corner_radius=0,
            padx=pad_x,
            pady=pad_y,
        )
