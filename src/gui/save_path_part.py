from tkinter import filedialog
import customtkinter as ctk
from src.config.gui_config import *


from .basic.button import CustomButton
from .basic.smaller_lbl import SmallerLbl


class SavePathPart(ctk.CTkFrame):
    def __init__(self, parent, btn_command):
        super().__init__(master=parent, fg_color=DARK_GREEN)

        # ctk variables
        self.has_data = False
        self.save_path = ctk.StringVar(value=SAVE_PATH_NOT_CHOSEN)
        self.add_save_folder = ctk.BooleanVar(value=True)

        # layout
        self.columnconfigure((0, 1), weight=1, uniform="v")
        self.rowconfigure((0, 1), weight=1, uniform="v")
        self.rowconfigure(
            2,
            weight=2,
            uniform="v",
        )

        # widgets
        self.dialog_btn = CustomButton(
            self,
            btn_command=self.get_save_path,
            btn_text=SAVE_PATH_BTN_TEXT,
            font_size=18,
        )
        self.add_folder_checkbox = ctk.CTkCheckBox(
            self,
            text=ADD_FOLDER_CHECBOX_TEXT,
            variable=self.add_save_folder,
            text_color=BLACK,
            font=ctk.CTkFont(family=FONT, size=SAVE_PATH_FONT_SIZE),
            checkbox_height=20,
            checkbox_width=20,
            hover_color=GREEN,
        )
        self.save_path_lbl = SmallerLbl(self, lbl_text="", variable=self.save_path)

        self.save_btn_part = CustomButton(
            self,
            btn_text=SAVE_RESULTS_BTN_TEXT,
            btn_command=btn_command,
            state="disabled",
            anchor="center",
        )

        self.dialog_btn.grid(row=0, column=0, sticky="nsew", ipady=40, padx=4, pady=2)
        self.add_folder_checkbox.grid(row=0, column=1, sticky="ns", ipady=40)
        self.save_path_lbl.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.save_btn_part.grid(
            column=0, row=2, columnspan=2, sticky="ew", padx=40, pady=10
        )

    def get_save_path(self):
        self.save_path.set(filedialog.askdirectory())
        self.control_save_btn()

    def control_save_btn(self):
        if (self.has_data is True) and (self.save_path.get() != SAVE_PATH_NOT_CHOSEN):
            self.save_btn_part.configure(state="normal")
        else:
            self.save_btn_part.configure(state="disabled")
