import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime

class DiaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Diary App")

        self.entry_text = tk.Text(root, wrap="word", height=10, width=40)
        self.entry_text.pack(pady=10)

        save_button = tk.Button(root, text="Save Entry", command=self.save_entry)
        save_button.pack(pady=5)

        load_button = tk.Button(root, text="Load Entry", command=self.load_entry)
        load_button.pack(pady=5)

    def save_entry(self):
        entry_text = self.entry_text.get("1.0", tk.END).strip()

        if not entry_text:
            messagebox.showwarning("Warning", "Entry cannot be empty!")
            return

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"diary_entry_{timestamp}.txt"

        with open(filename, "w") as file:
            file.write(entry_text)

        messagebox.showinfo("Success", "Entry saved successfully!")

    def load_entry(self):
        filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        if not filename:
            return  # User canceled file dialog

        with open(filename, "r") as file:
            entry_text = file.read()

        self.entry_text.delete("1.0", tk.END)
        self.entry_text.insert(tk.END, entry_text)

        messagebox.showinfo("Success", "Entry loaded successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiaryApp(root)
    root.mainloop()
