import customtkinter as ctk

# Buttons des Hauptmenüs
class MainMenuButton(ctk.CTkButton):
    def __init__(self, parent, column, row, text, corner_radius,
                 padx, sticky, font, hover_color, command, image=None):
        super().__init__(
            master=parent,
            text=text,
            corner_radius=corner_radius,
            image=image,
            fg_color=("#f3f3f3", "#191919"),
            font=font,
            text_color=("black", "#5d5d5d"),
            hover_color=hover_color,
            command=command
        )
        self.grid(column=column, row=row, padx=padx, sticky=sticky)


# Übersetzer Buttons
class Button(ctk.CTkButton):
    def __init__(self, parent, text, func, col, row, fg_color, hover_color, text_color, font, height=40, image=None, state=ctk.NORMAL, corner_radius=0, sticky="ew"):
        super().__init__(
            master=parent,
            text=text,
            command=func,
            corner_radius=corner_radius,
            font=font,
            fg_color=fg_color,
            hover_color=hover_color,
            text_color=text_color,
            state=state,
            image=image,
            height=height
        )
        self.grid(column=col, row=row, sticky=sticky)
        

class CheckButton(ctk.CTkCheckBox):
        def __init__(self, parent, text, fg_color, checkbox_height, checkbox_width, border_width, border_color, hover_color):
            super().__init__(
                master=parent,
                text=text,
                fg_color=fg_color,
                checkbox_height=checkbox_height,
                checkbox_width=checkbox_width,
                border_width=border_width,
                border_color=border_color,
                hover_color=hover_color
            )
            self.pack(pady=5, anchor="w")


class ButtonPack(ctk.CTkButton):
    def __init__(self, parent, width, height, fg_color, hover_color, func, corner_radius, text, pady, anchor=None, side=None, image=None):
        super().__init__(
            master=parent,
            width=width,
            height=height,
            fg_color=fg_color,
            hover_color=hover_color,
            command=func,
            corner_radius=corner_radius,
            text=text,
            image=image
        )
        self.pack(pady=pady, anchor=anchor, side=side)

class ButtonPlace(ctk.CTkButton):
    def __init__(self, parent, width, height, fg_color, bg_color, hover_color, func, corner_radius, text, rely, relx, anchor, image=None):
        super().__init__(
            master=parent,
            width=width,
            height=height,
            fg_color=fg_color,
            bg_color=bg_color,
            hover_color=hover_color,
            command=func,
            corner_radius=corner_radius,
            text=text,
            image=image
        )
        self.place(rely=rely, relx=relx, anchor=anchor)


class ChoiceBox(ctk.CTkComboBox):
    def __init__(self, parent, column, columnspan, row, fg_color, border_width, values, font, width, height, sticky, padx, dropdown_fg_color, text_color, dropdown_font, variable):
        super().__init__(
            master=parent,
            fg_color=fg_color,
            border_width=border_width,
            values=values,
            font=font,
            width=width,
            height=height,
            dropdown_fg_color=dropdown_fg_color,
            text_color=text_color,
            dropdown_font=dropdown_font,
            variable=variable
        )
        self.grid(column=column, columnspan=columnspan, row=row, sticky=sticky, padx=padx)