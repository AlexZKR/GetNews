import customtkinter as ctk
from config.gui_config import *


class SavePathLbl(ctk.CTkLabel):

    def __init__(
        self,
        parent,
        lbl_text,
        variable,
        pad_x=0,
        pad_y=0,
    ):
        super().__init__(
            master=parent,
            text=lbl_text,
            font=ctk.CTkFont(family=FONT, size=SAVE_PATH_FONT_SIZE),
            text_color=BLACK,
            padx=pad_x,
            pady=pad_y,
            textvariable=variable,
        )
