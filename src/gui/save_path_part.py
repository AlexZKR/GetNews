import customtkinter as ctk
from src.config.gui_config import *


from .basic.button import CustomButton
from .basic.save_path_lbl import SavePathLbl


class SavePathPart(ctk.CTkFrame):
    def __init__(self, parent, save_path_var, btn_command, check_variable):
        super().__init__(master=parent, fg_color=DARK_GREEN)

        # layout
        self.columnconfigure((0, 1), weight=1, uniform="v")
        self.rowconfigure((0, 1), weight=1, uniform="v")

        # widgets
        self.dialog_btn = CustomButton(
            self, btn_command=btn_command, btn_text="Путь для сохранения", font_size=18
        )
        self.add_folder_checkbox = ctk.CTkCheckBox(
            self,
            text="Отдельная папка",
            variable=check_variable,
            text_color=BLACK,
            font=ctk.CTkFont(family=FONT, size=SAVE_PATH_FONT_SIZE),
            checkbox_height=20,
            checkbox_width=20,
            hover_color=GREEN,
        )
        self.save_path_lbl = SavePathLbl(self, lbl_text="", variable=save_path_var)

        self.dialog_btn.grid(row=0, column=0, sticky="nsew", ipady=40, padx=4, pady=2)
        self.add_folder_checkbox.grid(row=0, column=1, sticky="ns", ipady=40)
        self.save_path_lbl.grid(row=1, column=0, columnspan=2, sticky="nsew")

        self.grid(column=0, row=2, sticky="ew", padx=15, pady=10)
