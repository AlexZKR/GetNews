import customtkinter as ctk
from src.config.exceptions import *
from src.config.gui_config import *
from customtkinter import filedialog
import os, sys

from src.gui.basic.main_txt_label import MessageLbl
from src.gui.save_path_part import SavePathPart
from src.gui.basic.button import CustomButton


from src.gui.tabview_part import TabViewPart
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

        # window setup
        super().__init__(fg_color=GREEN)
        self.title("")
        self.iconbitmap(resource_path("img\\icon.ico"))
        self.geometry("420x550")
        self.title("Get News 3.0")
        self.resizable(False, False)
        self.change_title_bar_color()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1, uniform="a")
        self.rowconfigure(1, weight=4, uniform="a")
        self.rowconfigure(2, weight=1, uniform="a")
        self.rowconfigure(3, weight=1, uniform="a")

        # ctk variables

        self.message_txt = ctk.StringVar(value=MESSAGE_LBL_DEFAULT_TEXT)
        self.save_path = ctk.StringVar(value=SAVE_PATH_NOT_CHOSEN)
        self.add_save_folder = ctk.BooleanVar(value=True)

        # widgets
        self.message_lbl = MessageLbl(
            self, lbl_text="", pad_y=10, variable=self.message_txt
        )
        self.noteBook = TabViewPart(
            self,
            msg_lbl_command=self.set_message_lbl_text,
            save_btn_cmd=self.control_save_btn,
        )

        self.save_path_part = SavePathPart(
            self, self.save_path, self.get_save_path, self.add_save_folder
        )

        self.save_btn_part = CustomButton(
            self,
            btn_text=SAVE_RESULTS_BTN_TEXT,
            btn_command=self.on_save,
            state="disabled",
        )
        self.save_btn_part.grid(column=0, row=3, sticky="ew", padx=40)

        self.mainloop()

    def get_save_path(self):
        self.save_path.set(filedialog.askdirectory())
        self.control_save_btn(switch_on=True)

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

    def set_message_lbl_text(self, text: str, mode: int = 0):
        """mode - INFO, WARNING, SUCCESS"""
        self.message_txt.set(text)
        if mode == WARNING:
            self.message_lbl.configure(text_color=WARNING_COLOR)
        if mode == INFO:
            self.message_lbl.configure(text_color=BLACK)
        if mode == SUCCESS:
            self.message_lbl.configure(text_color=GREEN)

    def control_save_btn(self, switch_on=False):
        if switch_on is True and (
            self.save_path.get() != SAVE_PATH_NOT_CHOSEN
            and self.save_path.get() != SAVE_PATH_DOES_NOT_EXIST
        ):
            self.save_btn_part.configure(state="normal")
        else:
            self.save_btn_part.configure(state="disabled")

    def on_save(self):

        try:
            to_output = self.noteBook.output_data()
            output_results(to_output, self.save_path.get(), self.add_save_folder.get())
        except Exception as e:
            if isinstance(e, SavePathDoesNotExistException):
                self.set_message_lbl_text(SAVE_PATH_DOES_NOT_EXIST, mode=WARNING)
                self.control_save_btn(switch_on=False)
            if isinstance(e, NoMonthsChosenException):
                self.set_message_lbl_text(NO_MONTHS_CHOSEN, mode=WARNING)
                self.control_save_btn(switch_on=False)
            else:
                self.set_message_lbl_text(e, mode=WARNING)
                raise (e)


App()
