import tkinter as tk

class uiListBoxApp:
    def __init__(self, master):
        self.master = master
        self.entry_text = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.master, textvariable=self.entry_text)
        self.entry.pack()

        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack()

        self.button_add = tk.Button(self.button_frame, text="Add", command=self.add_item)
        self.button_add.pack(side=tk.LEFT)

        self.button_clear = tk.Button(self.button_frame, text="Clear", command=self.clear_items)
        self.button_clear.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(self.master, height=5, yscrollcommand=self.scrollbar.set)
        self.listbox.pack()

        self.scrollbar.config(command=self.listbox.yview)

        self.listbox.bind("<<ListboxSelect>>", self.on_select)
        self.listbox.bind("<Double-1>", self.on_double_click)

    def add_item(self):
        text = self.entry_text.get()
        if not text:
            return
        self.listbox.insert(tk.END, text)
        self.entry_text.set("")

    def clear_items(self):
        self.listbox.delete(0, tk.END)

    def on_select(self, event):
        selected_item = self.listbox.get(self.listbox.curselection())
        print(selected_item)

    def on_double_click(self, event):
        selected_item = self.listbox.get(self.listbox.curselection())
        print("Double-clicked:", selected_item)
