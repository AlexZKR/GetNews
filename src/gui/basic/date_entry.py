from tkcalendar import DateEntry
import customtkinter as ctk

from src.config.gui_config import *


class CustomDateEntry(DateEntry):
    def __init__(self, parent, font_size=CALENDAR_ENTRY_FONT_SIZE):
        super().__init__(
            master=parent,
            locale="ru_RU",
            showweeknumbers=True,
            width=10,
            anchor="center",
            height=40,
            font=ctk.CTkFont(family=FONT, size=font_size),
        )
