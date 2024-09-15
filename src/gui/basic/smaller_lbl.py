import customtkinter as ctk
from src.config.gui_config import *


class SmallerLbl(ctk.CTkLabel):

    def __init__(
        self,
        parent,
        lbl_text,
        variable,
        pad_x=0,
        pad_y=0,
        font_size=SAVE_PATH_FONT_SIZE,
    ):
        super().__init__(
            master=parent,
            text=lbl_text,
            font=ctk.CTkFont(family=FONT, size=font_size),
            text_color=BLACK,
            padx=pad_x,
            pady=pad_y,
            textvariable=variable,
        )
