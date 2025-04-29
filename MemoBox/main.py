import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import os


FILE_NAME = "saved_items.txt"

class MemoBoxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MemoBox")
        self.root.geometry("800x600")
        #self.root.configure(bg="#f0f0f0")
        self.root.configure(bg="lightblue")

        # Main Frame for entry and buttons
        self.main_frame = tk.Frame(root, bg="lightblue")
        #self.main_frame.pack(pady=20, fill="x")
        self.main_frame.pack(pady=20, padx=10)


        # Data Entry
        tk.Label(self.main_frame, text="Enter Data:", bg="lightblue", font=("Arial", 12,"bold")).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.data_entry = tk.Entry(self.main_frame, width=40, font=("Arial", 12))
        self.data_entry.grid(row=0, column=1, padx=10, pady=5)

        # Description Entry
        tk.Label(self.main_frame, text="Enter Description:", bg="lightblue", font=("Arial", 12,"bold")).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.desc_entry = tk.Entry(self.main_frame, width=40, font=("Arial", 12))
        self.desc_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons Frame
        self.button_frame = tk.Frame(self.main_frame, bg="lightblue")
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=10)


        rounded_button = ttk.Button(
            self.button_frame,
            text="Save",
            command=self.save_item,
            style="TButton"
        )
        rounded_button.pack(side="left", padx=5, pady=5)

        # Configure rounded button style
        style = ttk.Style()
        style.configure("TButton", padding=10, relief="flat", background="#4CAF50", font=("Arial", 12, "bold"))



        #tk.Button(self.button_frame, text="Save", command=self.save_item, bg="#4CAF50", fg="white", font=("Arial", 12), padx=10).pack(side="left", padx=5)
        tk.Button(
            self.button_frame,
            text="Save",
            command=self.save_item,
            bg="#4CAF50",     # Green background
            fg="white",       # White text color
            font=("Arial", 12, "bold"),  # Bold font
            padx=15,          # Extra padding (horizontal)
            pady=5,           # Extra padding (vertical)
            relief="raised",  # 3D button effect
            bd=3,             # Border thickness
            cursor="hand2",   # Changes cursor to a hand on hover
            width=12,         # Sets button width
            height=2,         # Sets button height
            highlightbackground="#3e8e41"  # Darker green outline (Mac support)
        ).pack(side="left", padx=5, pady=5)
        
        tk.Button(self.button_frame, text="Show Saved Items", command=self.show_items, bg="#008CBA", fg="white", font=("Arial", 12), padx=10).pack(side="left", padx=5)
        tk.Button(self.button_frame, text="Rewrite", command=self.rewrite_item, bg="#FFA500", fg="white", font=("Arial", 12), padx=10).pack(side="left", padx=5)
        tk.Button(self.button_frame, text="Delete", command=self.delete_item, bg="#f44336", fg="white", font=("Arial", 12), padx=10).pack(side="left", padx=5)
        tk.Button(self.button_frame, text="Clear Display", command=self.clear_display, bg="#9E9E9E", fg="white", font=("Arial", 12), padx=10).pack(side="left", padx=5)

        # Scrollable Canvas for squares display
        self.canvas = tk.Canvas(root, bg="#eee8aa")
        self.canvas.pack(side="left", fill="both", expand=True, padx=20)  # Added horizontal padding

        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create an inner frame inside the canvas
        self.inner_frame = tk.Frame(self.canvas, bg="#f08080",
                                    highlightthickness=3,  # Thickness of the borderhighlightbackground="black"  
                                    highlightbackground="black" # Color of the border
                                    )
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        # Bind events to update the scroll region and adjust squares when resized
        self.inner_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.show_items()  # Redraw squares dynamically when the canvas is resized

    def save_item(self):
        data = self.data_entry.get()
        description = self.desc_entry.get()
        if not data:
            messagebox.showwarning("Input Error", "Please enter data.")
            return
        
        with open(FILE_NAME, "a") as file:
            file.write(f"{data} | {description}\n")
        
        messagebox.showinfo("Success", "Item saved successfully!")
        self.data_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.show_items()

    def show_items(self):
        # Clear current squares
        for widget in self.inner_frame.winfo_children():
            widget.destroy()

        if not os.path.exists(FILE_NAME):
            tk.Label(self.inner_frame, text="No items saved yet.", bg="#f0f0f0", font=("Arial", 12)).pack(pady=10)
            return

        with open(FILE_NAME, "r") as file:
            items = file.readlines()

        if not items:
            tk.Label(self.inner_frame, text="No saved items.", bg="#f0f0f0", font=("Arial", 12)).pack(pady=10)
            return

        # Determine number of columns based on canvas width, accounting for padding
        canvas_width = self.canvas.winfo_width()
        min_square_width = 200  # Desired square width (including internal padding)
        columns = max(1, (canvas_width - 40) // min_square_width)  # 40 for extra padding on both sides

        for idx, line in enumerate(items):
            data, _, description = line.partition(" | ")
            square = tk.Frame(self.inner_frame, width=min_square_width - 20, height=100, bg="white", relief="raised", bd=2)
            square.grid(row=idx // columns, column=idx % columns, padx=10, pady=10)
            square.grid_propagate(False)

            tk.Label(square, text=f"Data: {data.strip()}", bg="white", font=("Arial", 10)).pack(pady=(10, 0))
            tk.Label(square, text=f"Desc: {description.strip()}", bg="white", font=("Arial", 10)).pack(pady=(5, 10))

    def clear_display(self):
        for widget in self.inner_frame.winfo_children():
            widget.destroy()

    def rewrite_item(self):
        if not os.path.exists(FILE_NAME):
            messagebox.showwarning("No Data", "No items to rewrite.")
            return
        with open(FILE_NAME, "r") as file:
            items = file.readlines()

        if not items:
            messagebox.showwarning("No Data", "No items to rewrite.")
            return

        index = simpledialog.askinteger("Rewrite Item", "Enter the item number to rewrite:")
        if index is None or index < 1 or index > len(items):
            messagebox.showerror("Invalid Input", "Invalid item number.")
            return

        new_data = simpledialog.askstring("Rewrite Item", "Enter new data:")
        if new_data is None:
            return
        new_desc = simpledialog.askstring("Rewrite Item", "Enter new description:")
        if new_desc is None:
            new_desc = ""

        items[index - 1] = f"{new_data} | {new_desc}\n"
        with open(FILE_NAME, "w") as file:
            file.writelines(items)

        messagebox.showinfo("Success", "Item rewritten successfully!")
        self.show_items()

    def delete_item(self):
        if not os.path.exists(FILE_NAME):
            messagebox.showwarning("No Data", "No items to delete.")
            return
        with open(FILE_NAME, "r") as file:
            items = file.readlines()

        if not items:
            messagebox.showwarning("No Data", "No items to delete.")
            return

        index = simpledialog.askinteger("Delete Item", "Enter the item number to delete:")
        if index is None or index < 1 or index > len(items):
            messagebox.showerror("Invalid Input", "Invalid item number.")
            return

        del items[index - 1]
        with open(FILE_NAME, "w") as file:
            file.writelines(items)

        messagebox.showinfo("Success", "Item deleted successfully!")
        self.show_items()

if __name__ == "__main__":
    root = tk.Tk()
    app = MemoBoxApp(root)
    root.mainloop()
