import tkinter as tk
from tkinter import ttk


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        vscrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        vscrollbar.pack(side="right", fill="y")

        hscrollbar = ttk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        hscrollbar.pack(side="bottom", fill="x")

        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="center")

        canvas.configure(yscrollcommand=vscrollbar.set)
        canvas.configure(xscrollcommand=hscrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)

root = tk.Tk()

frame = ScrollableFrame(root)

for i in range(50):
    ttk.Label(frame.scrollable_frame, text="Sample scrolling label ======================================================================================").pack()

frame.pack()
root.mainloop()