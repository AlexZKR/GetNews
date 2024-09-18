import customtkinter as ctk
from src.config.exceptions import *
from src.config.gui_config import *

import os, sys

from src.gui.upper_info_part import UpperInfoPart
from src.gui.tabview_part import TabViewPart
from src.gui.save_path_part import SavePathPart

from src.output_data.scraper_output import output_results


try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass


def resource_path(relative_path):
    try:
        base_path = sys._MEI90522
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=GREEN)
        self.configure_window()

        # window layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1, uniform="a")
        self.rowconfigure(1, weight=2, uniform="a")
        self.rowconfigure(2, weight=1, uniform="a")

        # window widgets

        self.upper_info_part = UpperInfoPart(
            self,
            get_data_cmd=self.on_get,
        )
        self.noteBook = TabViewPart(self)
        self.save_path_part = SavePathPart(self, self.on_save)

        # window widgets layout
        self.upper_info_part.grid(column=0, row=0, sticky="nsew", padx=20, pady=10)
        self.noteBook.grid(column=0, row=1, sticky="nsew")
        self.save_path_part.grid(column=0, row=2, sticky="ew", padx=15, pady=10)

        self.mainloop()

    def configure_window(self):
        self.iconbitmap(resource_path("img\\icon.ico"))
        self.geometry("420x540")
        self.title("Get News 3.5")
        self.resizable(False, False)
        self.change_title_bar_color()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def change_title_bar_color(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = TITLE_HEX_COLOR
            windll.dwmapi.DwmSetWindowAttribute(
                HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int)
            )
        except:
            pass

    def on_closing(self):
        # Cancel any pending callbacks
        self.after_cancel(self.noteBook)
        self.after_cancel(self.save_path_part)
        self.destroy()

    def on_get(self):
        try:
            result_message = self.noteBook.get_data()
            self.upper_info_part.message_lbl.set_text(text=result_message, mode=INFO)
            self.save_path_part.has_data = True
        except Exception as e:
            if isinstance(e, NoInternetException):
                self.upper_info_part.message_lbl.set_text(
                    NO_INTERNET_CONNECTION, WARNING
                )
            else:
                raise e

    def on_save(self):
        try:
            to_output = self.noteBook.output_data()
            output_results(
                to_output,
                self.save_path_part.save_path.get(),
                self.save_path_part.add_save_folder.get(),
            )
            self.upper_info_part.message_lbl.set_text(SUCCESS_MESSAGE, mode=SUCCESS)
        except Exception as e:
            if isinstance(e, SavePathDoesNotExistException):
                self.upper_info_part.message_lbl.set_text(
                    text=SAVE_PATH_DOES_NOT_EXIST, mode=WARNING
                )
                self.save_path_part.control_save_btn()
                return
            if isinstance(e, NoMonthsChosenException):
                self.upper_info_part.message_lbl.set_text(
                    text=NO_MONTHS_CHOSEN, mode=WARNING
                )
                self.save_path_part.control_save_btn()
                return
            else:
                self.upper_info_part.message_lbl.set_text(e, mode=WARNING)
                raise (e)


App()
