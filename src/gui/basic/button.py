import customtkinter as ctk

from src.config.gui_config import *


class CustomButton(ctk.CTkButton):
    def __init__(
        self,
        parent,
        btn_text,
        btn_command,
        state="normal",
        font_size=INPUT_FONT_SIZE,
    ):
        super().__init__(
            master=parent,
            text=btn_text,
            command=btn_command,
            font=ctk.CTkFont(family=FONT, size=font_size),
            text_color=BLACK,
            fg_color=LIGHT_GRAY,
            hover_color=GRAY,
            corner_radius=BUTTON_CORNER_RADIUS,
            state=state,
        )
