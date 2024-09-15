import customtkinter as ctk
from src.config.gui_config import *


class MessageLbl(ctk.CTkLabel):

    def __init__(
        self, parent, lbl_text, variable, pad_x=0, pad_y=0, font_size=INPUT_FONT_SIZE
    ):
        super().__init__(
            master=parent,
            text=lbl_text,
            font=ctk.CTkFont(family=FONT, size=font_size),
            text_color=BLACK,
            padx=int(pad_x),
            pady=int(pad_y),
            textvariable=variable,
        )

        
