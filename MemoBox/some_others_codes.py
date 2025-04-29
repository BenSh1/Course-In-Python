"""
import tkinter as tk
from tkinter import messagebox, scrolledtext, simpledialog
import os

FILE_NAME = "saved_items.txt"

class MemoBoxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MemoBox")
        self.root.geometry("700x500")
        self.root.configure(bg="#f0f0f0")

        # Main Frame
        self.main_frame = tk.Frame(root, bg="#f0f0f0")
        self.main_frame.pack(pady=20)

        # Data Entry
        tk.Label(self.main_frame, text="Enter Data:", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.data_entry = tk.Entry(self.main_frame, width=50, font=("Arial", 12))
        self.data_entry.grid(row=0, column=1, padx=10, pady=5)

        # Description Entry
        tk.Label(self.main_frame, text="Enter Description:", bg="#f0f0f0", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.desc_entry = tk.Entry(self.main_frame, width=50, font=("Arial", 12))
        self.desc_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons Frame
        self.button_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=10)

        tk.Button(self.button_frame, text="Save", command=self.save_item, bg="#4CAF50", fg="white", font=("Arial", 12), padx=10).pack(side="left", padx=5)
        tk.Button(self.button_frame, text="Show Saved Items", command=self.show_items, bg="#008CBA", fg="white", font=("Arial", 12), padx=10).pack(side="left", padx=5)
        tk.Button(self.button_frame, text="Rewrite", command=self.rewrite_item, bg="#FFA500", fg="white", font=("Arial", 12), padx=10).pack(side="left", padx=5)
        tk.Button(self.button_frame, text="Delete", command=self.delete_item, bg="#f44336", fg="white", font=("Arial", 12), padx=10).pack(side="left", padx=5)
        tk.Button(self.button_frame, text="Clear Display", command=self.clear_display, bg="#9E9E9E", fg="white", font=("Arial", 12), padx=10).pack(side="left", padx=5)

        
        # Display Area
        self.display_area = scrolledtext.ScrolledText(self.main_frame, height=15, width=70, font=("Arial", 12))
        self.display_area.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        




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
        if not os.path.exists(FILE_NAME):
            messagebox.showwarning("No Data", "No items saved yet.")
            return
        
        self.display_area.delete(1.0, tk.END)
        with open(FILE_NAME, "r") as file:
            items = file.readlines()
        
        if not items:
            self.display_area.insert(tk.END, "No saved items.")
        else:
            for idx, line in enumerate(items, start=1):
                self.display_area.insert(tk.END, f"{idx}. {line}")

    def clear_display(self):
        self.display_area.delete(1.0, tk.END)

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



"""

"""
import tkinter as tk
from tkinter import messagebox, simpledialog
import os

FILE_NAME = "saved_items.txt"

class MemoBoxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MemoBox")
        self.root.geometry("750x600")
        self.root.configure(bg="#f0f0f0")

        # Main Frame
        self.main_frame = tk.Frame(root, bg="#f0f0f0")
        self.main_frame.pack(pady=20)

        # Data Entry
        tk.Label(self.main_frame, text="Enter Data:", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.data_entry = tk.Entry(self.main_frame, width=50, font=("Arial", 12))
        self.data_entry.grid(row=0, column=1, padx=10, pady=5)

        # Description Entry
        tk.Label(self.main_frame, text="Enter Description:", bg="#f0f0f0", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.desc_entry = tk.Entry(self.main_frame, width=50, font=("Arial", 12))
        self.desc_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons Frame
        self.button_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=10)

        tk.Button(self.button_frame, text="Save", command=self.save_item, bg="#4CAF50", fg="white", font=("Arial", 12), padx=10).pack(side="left", padx=5)
        tk.Button(self.button_frame, text="Show Saved Items", command=self.show_items, bg="#008CBA", fg="white", font=("Arial", 12), padx=10).pack(side="left", padx=5)
        tk.Button(self.button_frame, text="Rewrite", command=self.rewrite_item, bg="#FFA500", fg="white", font=("Arial", 12), padx=10).pack(side="left", padx=5)
        tk.Button(self.button_frame, text="Delete", command=self.delete_item, bg="#f44336", fg="white", font=("Arial", 12), padx=10).pack(side="left", padx=5)
        tk.Button(self.button_frame, text="Clear Display", command=self.clear_display, bg="#9E9E9E", fg="white", font=("Arial", 12), padx=10).pack(side="left", padx=5)

        # Squares Display Frame
        self.squares_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.squares_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

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
        for widget in self.squares_frame.winfo_children():
            widget.destroy()
            
        if not os.path.exists(FILE_NAME):
            messagebox.showwarning("No Data", "No items saved yet.")
            return
        
        with open(FILE_NAME, "r") as file:
            items = file.readlines()
        
        if not items:
            tk.Label(self.squares_frame, text="No saved items.", bg="#f0f0f0", font=("Arial", 12)).pack()
            return
        
        # Create a grid of square containers (3 per row)
        columns = 3
        for idx, line in enumerate(items):
            data, _, description = line.partition(" | ")
            square = tk.Frame(self.squares_frame, width=200, height=100, bg="white", relief="raised", bd=2)
            square.grid(row=idx // columns, column=idx % columns, padx=10, pady=10)
            # Ensure the frame doesn't shrink to fit its contents
            square.grid_propagate(False)
            
            tk.Label(square, text=f"Data: {data.strip()}", bg="white", font=("Arial", 10)).pack(pady=(10,0))
            tk.Label(square, text=f"Desc: {description.strip()}", bg="white", font=("Arial", 10)).pack(pady=(5,10))
        
    def clear_display(self):
        for widget in self.squares_frame.winfo_children():
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
"""


"""
import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import math

FILE_NAME = "saved_items.txt"

class MemoBoxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MemoBox")
        self.root.geometry("750x600")
        self.root.configure(bg="#f0f0f0")

        # Main Frame for entry and buttons
        self.main_frame = tk.Frame(root, bg="#f0f0f0")
        self.main_frame.pack(pady=10, fill="x")

        # Data Entry
        tk.Label(self.main_frame, text="Enter Data:", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.data_entry = tk.Entry(self.main_frame, width=50, font=("Arial", 12))
        self.data_entry.grid(row=0, column=1, padx=10, pady=5)

        # Description Entry
        tk.Label(self.main_frame, text="Enter Description:", bg="#f0f0f0", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.desc_entry = tk.Entry(self.main_frame, width=50, font=("Arial", 12))
        self.desc_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons Frame
        self.button_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self.button_frame, text="Save", command=self.save_item, bg="#4CAF50", fg="white", font=("Arial", 12), padx=10).pack(side="left", padx=5)
        tk.Button(self.button_frame, text="Show Saved Items", command=self.show_items, bg="#008CBA", fg="white", font=("Arial", 12), padx=10).pack(side="left", padx=5)
        tk.Button(self.button_frame, text="Rewrite", command=self.rewrite_item, bg="#FFA500", fg="white", font=("Arial", 12), padx=10).pack(side="left", padx=5)
        tk.Button(self.button_frame, text="Delete", command=self.delete_item, bg="#f44336", fg="white", font=("Arial", 12), padx=10).pack(side="left", padx=5)
        tk.Button(self.button_frame, text="Clear Display", command=self.clear_display, bg="#9E9E9E", fg="white", font=("Arial", 12), padx=10).pack(side="left", padx=5)

        # Scrollable Canvas for squares display
        self.canvas = tk.Canvas(root, bg="#f0f0f0")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create an inner frame inside the canvas
        self.inner_frame = tk.Frame(self.canvas, bg="#f0f0f0")
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        # Bind the configure event to update scroll region and re-render grid when resized.
        self.inner_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

    def on_frame_configure(self, event):
        # Update scroll region to encompass the inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        # When canvas is resized, re-render the items to adapt to new width
        self.show_items()

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
        # Clear current squares from inner frame
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

        # Determine number of columns based on canvas width and desired square minimum width
        canvas_width = self.canvas.winfo_width()
        min_square_width = 220  # desired minimum width (including padding)
        columns = max(1, canvas_width // min_square_width)
        
        # Create a grid of square containers
        for idx, line in enumerate(items):
            data, _, description = line.partition(" | ")
            square = tk.Frame(self.inner_frame, width=min_square_width-20, height=100, bg="white", relief="raised", bd=2)
            square.grid(row=idx // columns, column=idx % columns, padx=10, pady=10)
            # Prevent the square from resizing based on its content
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

"""

