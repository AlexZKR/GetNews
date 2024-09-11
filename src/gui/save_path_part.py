import customtkinter as ctk
from config.gui_config import *


from .basic.button import CustomButton
from .basic.save_path_lbl import SavePathLbl


class SavePathPart(ctk.CTkFrame):
    def __init__(self, parent, save_path_var, btn_command):
        super().__init__(master=parent, fg_color=DARK_GREEN)

        # widgets
        self.dialog_btn = CustomButton(
            self, btn_command=btn_command, btn_text="Путь для сохранения", font_size=18
        )
        self.save_path_lbl = SavePathLbl(
            self, lbl_text="", variable=save_path_var
        )

        self.dialog_btn.pack(pady=5)
        self.save_path_lbl.pack()

        self.grid(column=0, row=2, sticky="ew", padx=15, pady=10)
