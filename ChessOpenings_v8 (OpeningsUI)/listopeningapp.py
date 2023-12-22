import tkinter as tk
from tkinter import ttk
from cls_Openings import *

ChessOpenings = Openings()

class ListBoxApp:
    def __init__(self, master):
        self.master = master
        self.entry_text = tk.StringVar()
        self.sample_string = "1.e4 e5 2.Nf3 Nc6"
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.master, textvariable=self.entry_text)
        self.entry.pack()

        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack()

        self.btnAdd = tk.Button(self.button_frame, text="Add", command=self.btnAdd_click)
        self.btnAdd.pack(side=tk.LEFT)

        self.btnClear = tk.Button(self.button_frame, text="Clear", command=self.btnClear_click)
        self.btnClear.pack(side=tk.LEFT)

        self.btnSample = tk.Button(self.button_frame, text="Sample", command=self.btnSample_click)
        self.btnSample.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.treeview = ttk.Treeview(self.master, columns=("Column1", "Column2", "Column3"), selectmode=tk.BROWSE,
                                     show="headings", height=5, yscrollcommand=self.scrollbar.set)
        self.treeview.column("Column1", width=50, anchor=tk.CENTER)
        self.treeview.column("Column2", width=100, anchor=tk.W)
        self.treeview.column("Column3", width=300, anchor=tk.W)
        self.treeview.heading("Column1", text="Code")
        self.treeview.heading("Column2", text="Name")
        self.treeview.heading("Column3", text="Annotation")
        self.treeview.pack(fill=tk.BOTH, expand=True)

        self.scrollbar.config(command=self.treeview.yview)

        self.treeview.bind("<<TreeviewSelect>>", self.on_select)
        self.treeview.bind("<Double-1>", self.on_double_click)

    def btnAdd_click(self):
        pgn = self.entry_text.get()
        if not pgn:
            return
        # eco_list = ChessOpenings.get_continuations(pgn)
        # for eco in eco_list:
        #     self.treeview.insert("", tk.END, values=(eco, "Placeholder"))
        # self.entry_text.set("")

        eco_dict = ChessOpenings.get_continuations2(pgn)
        for each_key, each_value in eco_dict.items():
            self.treeview.insert("", tk.END, values=(each_value['ECO'], each_value['NAME'], each_key))
        self.entry_text.set("")


    def btnClear_click(self):
        self.treeview.delete(*self.treeview.get_children())

    def on_select(self, event):
        selected_item = self.treeview.selection()[0]
        values = self.treeview.item(selected_item)['values']
        if values:
            selected_value = values[0]
            print(selected_value)

    def on_double_click(self, event):
        selected_item = self.treeview.selection()[0]
        values = self.treeview.item(selected_item)['values']
        if values:
            selected_value = values[0]
            self.treeview.delete(*self.treeview.get_children())
            print("Double-clicked:", selected_value)

            filtered_openings = ChessOpenings.filter_opening_dict("ECO", selected_value)
            

            for each_key, each_value in filtered_openings.items():
                pgn = each_key
                self.treeview.insert("", tk.END, values=(each_value['ECO'], each_value['NAME'], each_key))
        self.entry_text.set("")

            # selected_value = values[2]
            # input(selected_value)
            # eco_dict = ChessOpenings.get_continuations2(selected_value)
            # for each_key, each_value in eco_dict.items():
            #     self.treeview.insert("", tk.END, values=(each_value['ECO'], each_value['NAME'], each_key))
            # self.entry_text.set("")

    def btnSample_click(self):
        self.entry.delete("0", tk.END)
        self.entry.insert(tk.END, self.sample_string)

    def run(self):
        self.master.mainloop()


# Create the main window
window = tk.Tk()
window.title("Chess")
window.geometry('800x400+0+0')

# Create an instance of the ListBoxApp class
app = ListBoxApp(window)

# Start the Tkinter event loop
app.run()
