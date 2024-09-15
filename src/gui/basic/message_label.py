import customtkinter as ctk
from src.config.gui_config import *


class MessageLbl(ctk.CTkLabel):

    def __init__(
        self, parent, default_text, pad_x=0, pad_y=0, font_size=INPUT_FONT_SIZE
    ):
        self.text_variable = ctk.StringVar(value=default_text)
        super().__init__(
            master=parent,
            text=default_text,
            font=ctk.CTkFont(family=FONT, size=font_size),
            text_color=BLACK,
            padx=int(pad_x),
            pady=int(pad_y),
            textvariable=self.text_variable,
        )

    def set_text(self, text: str, mode: int = 0):
        """mode - INFO, WARNING, SUCCESS"""
        self.text_variable.set(text)
        if mode == WARNING:
            self.configure(text_color=WARNING_COLOR)
        if mode == INFO:
            self.configure(text_color=BLACK)
        if mode == SUCCESS:
            self.configure(text_color=SUCCESS_COLOR)
