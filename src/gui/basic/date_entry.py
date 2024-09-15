from tkcalendar import DateEntry
import customtkinter as ctk
from src.config.gui_config import *


class CustomDateEntry(ctk.CTkFrame):
    """It`s a tkcalendar dateEntry that is placed inside a frame. A de is squished by
    pady and padx so that underlying frame is visible. By default the frame is transparent,
    but by toggling its color you can i.g signal about an error (red border).

    signal_border-width - a value of pady,padx by which a dateEnrty is squised
    (in other words a width of a border)"""

    def __init__(
        self,
        parent,
        signal_border_width=3,
        font_size=CALENDAR_ENTRY_FONT_SIZE,
        variable=None,
    ):
        super().__init__(master=parent, fg_color="transparent", corner_radius=0)
        self.entry = DateEntry(
            master=self,
            locale="ru_RU",
            showweeknumbers=True,
            width=10,
            anchor="center",
            height=40,
            variable=variable,
            font=ctk.CTkFont(family=FONT, size=font_size),
            borderwidth=0,
        )
        
        self.entry.pack(
            expand=True, fill="both", padx=signal_border_width, pady=signal_border_width
        )
