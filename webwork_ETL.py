import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def format_webwork(file_name):
    df = pd.read_csv(file_name)
    #print(df)
    df.drop(columns=["Student ID", "Class Level"], inplace=True)
    df[["Last_Name", "First_Name"]] = df.iloc[:, 0].str.split(",", n=1, expand=True)
    df["First_Name"] = df["First_Name"].str.strip()
    df.drop(columns=[df.columns[0]], inplace=True)
    df["First_Name"] = df["First_Name"].str.split().str[0]
    df["#Username"] = df.iloc[:, 0].str.split("@").str[0]  # assuming 1st col is email
    df = df[["#Username", "Last_Name", "First_Name", df.columns[0]]]  # keep original email last
    df.rename(columns={df.columns[3]: "Preferred Email"}, inplace=True)
    df.insert(3, "Status", "")
    df.insert(4, "Comment", "")
    df.insert(5, "Section", "")
    df.insert(6, "Recitation", "")
    df["#Username_Duplicate"] = df["#Username"]
    df.insert(9, "Password", "")
    df.insert(10, "Permission", "")
    df.rename(columns={
        "Last_Name": "Last Name",
        "First_Name": "First Name", "#Username_Duplicate": "Username", "Preferred Email": "Email"
    }, inplace=True)
    df["Permission"] = 0
    return df

class WebWorkETLApp:

    def __init__(self, root):
        self.root = root
        self.root.title("WeBWorK Roster Formatter")
        self.root.geometry("570x220")
        self.root.resizable(False, False)

        # Variables
        self.input_file_path = tk.StringVar()

        # Build UI
        self._create_widgets()

    def _create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # File Selection Section
        label = ttk.Label(main_frame, text="Select CSV File to Format:")
        label.grid(row=0, column=0, columnspan=2, sticky=tk.W, pady=(0, 5))

        entry = ttk.Entry(
            main_frame, textvariable=self.input_file_path, width=45
        )
        entry.grid(row=1, column=0, padx=(0, 10), pady=(0, 20))

        browse_btn = ttk.Button(
            main_frame, text="Browse...", command=self.browse_file
        )
        browse_btn.grid(row=1, column=1, pady=(0, 20))

        # Action Section
        self.process_btn = ttk.Button(
            main_frame,
            text="Process & Save CSV",
            command=self.process_and_save,
        )
        self.process_btn.grid(row=2, column=0, columnspan=2, ipady=5)

        # Status Label
        self.status_label = ttk.Label(
            main_frame, text="", font=("Helvetica", 9, "italic")
        )
        self.status_label.grid(row=3, column=0, columnspan=2, pady=(15, 0))

    def browse_file(self):
        selected_file = filedialog.askopenfilename(
            title="Select Input CSV",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
        )
        if selected_file:
            self.input_file_path.set(selected_file)
            self.status_label.config(text="", foreground="black")

    def process_and_save(self):
        input_path = self.input_file_path.get()

        if not input_path:
            messagebox.showwarning(
                "Warning", "Please select an input CSV file first."
            )
            return

        if not os.path.exists(input_path):
            messagebox.showerror(
                "Error", "The selected input file does not exist."
            )
            return

        # Prompt user for output destination
        output_path = filedialog.asksaveasfilename(
            title="Save Output CSV As",
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
            initialfile="formatted_webwork_roster.csv",
        )

        if not output_path:
            return  # User canceled the save dialog

        try:
            # Run transformation and save
            formatted_df = format_webwork(input_path)
            formatted_df.to_csv(output_path, index=False)

            self.status_label.config(
                text="File processed and saved successfully!",
                foreground="green",
            )
            messagebox.showinfo("Success", f"File saved to:\n{output_path}")

        except Exception as e:
            self.status_label.config(text="Error occurred.", foreground="red")
            messagebox.showerror(
                "Processing Error", f"An error occurred:\n{str(e)}"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = WebWorkETLApp(root)
    root.mainloop()