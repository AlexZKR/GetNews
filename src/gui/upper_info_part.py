from src.config.gui_config import *
from src.config.gui_config import *
from src.gui.basic.button import CustomButton
from src.gui.basic.message_label import MessageLbl
import customtkinter as ctk


class UpperInfoPart(ctk.CTkFrame):
    def __init__(self, parent, get_data_cmd):
        super().__init__(master=parent, fg_color=GREEN)

        self.message_txt = ctk.StringVar(value=MAIN_MESSAGE_LBL_DEFAULT_TEXT)

        self.message_lbl = MessageLbl(
            self, default_text=MAIN_MESSAGE_LBL_DEFAULT_TEXT, pad_y=10
        )
        self.general_query_btn = CustomButton(
            self, btn_text=GENERAL_QUERY_BTN_TEXT, btn_command=get_data_cmd
        )
        self.general_query_btn.pack(expand=True, fill="x")
        self.message_lbl.pack(expand=True, fill="x")
