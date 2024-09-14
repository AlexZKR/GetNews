import customtkinter as ctk
from src.config.gui_config import *


class MessageLbl(ctk.CTkLabel):

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
            font=ctk.CTkFont(family=FONT, size=INPUT_FONT_SIZE),
            text_color=BLACK,
            padx=pad_x,
            pady=pad_y,
            textvariable=variable,
        )
        
        self.grid(column=0, row=0)
