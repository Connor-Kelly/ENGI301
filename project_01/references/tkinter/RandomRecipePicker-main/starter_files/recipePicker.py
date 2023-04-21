import tkinter as tk
from PIL import ImageTk

# initiallize app
root = tk.Tk()
root.title("Recipe Picker")
frame1 = tk.Frame(root, width = 500, height= 600, bg = "#1f223d")
frame1.grid(row=0, column=0)
root.eval("tk::PlaceWindow . center")



# run app
root.mainloop()
