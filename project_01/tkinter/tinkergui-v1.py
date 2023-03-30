# %%
import customtkinter as ctk
import os
from PIL import Image
import tkinter
# import tkinter.messagebox
# import ctk

# %%
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# %%
main_width = 320
main_height = 240
text_standard = "#8d99ae"
bg_standard = "#8282c34"
bg_selected = "#cadcfa"
# standard_btn_vec = {"master":self.navigation_frame, "corner_radius":0, "height":40, "border_spacing":10, "fg_color":"transparent", "text_color":("gray10", "gray90"), "hover_color":("gray70", "gray30"), "anchor":"w"}
# root = ctk.CTk()
# root.title("Music Box GUI")
# root.geometry(f"{main_width}x{main_height}")
# root.columnconfigure(0, minsize=main_width)

# configure grid layout (4x4)
# self.grid_columnconfigure(1, weight=1)
# self.grid_columnconfigure((2, 3), weight=0)
# self.grid_rowconfigure((0, 1, 2), weight=1)

# %%
# pageFrame = ctk.CTkFrame(master=root, width=main_width, height=main_height/3)
# page_label = ctk.CTkLabel(master=pageFrame, text="Page")
# page_label.grid(row=0, column=0, padx= 20, pady=20)
# subpage_label = ctk.CTkLabel(master=pageFrame, text="Subpage")
# subpage_label.grid(row=0, column=1, padx= 20, pady=20)
# pageFrame.grid(row=0, column=0, padx=20, pady=20)

# %%

class pageFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        page_label = ctk.CTkLabel(master=self, text="Page")
        page_label.grid(row=0, column=0, padx= 20, pady=20, sticky="ew")
        
        subpage_label = ctk.CTkLabel(master=self, text="Subpage")
        subpage_label.grid(row=0, column=1, padx= 20, pady=20, sticky="ew")

# %%

class App(ctk.CTk):
    def __init__(self):
        standard_btn_vec = {"master":self.navigation_frame, "corner_radius":0, "height":40, "border_spacing":10, "fg_color":"transparent", "text_color":("gray10", "gray90"), "hover_color":("gray70", "gray30"), "anchor":"w"}
        super().__init__()
        self.geometry(f"{main_width}x{main_height}")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = pageFrame(master=self, width=main_width, height=main_height/3)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="  Image Example",
                                                             compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # self.home_button = ctk.CTkButton( standard_btn_vec | {"text":"Home", "command":self.home_button_event})
        # self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 2",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 3",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=(bg_selected) if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=(bg_selected) if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=(bg_selected) if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

# %%
app = App()
app.mainloop()


