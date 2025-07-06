import tkinter as tk
from tkinter import scrolledtext, messagebox

# Simulated interpreter logic
def run_colag_code(code):
    # In actual future: Parse and interpret Colag syntax
    if "print(" in code:
        return eval(code.split("print(", 1)[1].rsplit(")", 1)[0])
    return "🚧 Colag interpreter not implemented yet!"

# Run button handler
def execute_code():
    code = code_input.get("1.0", tk.END)
    try:
        result = run_colag_code(code)
        output_box.config(state='normal')
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"Output:\n{result}")
        output_box.config(state='disabled')
    except Exception as e:
        messagebox.showerror("Execution Error", str(e))

# UI Setup
app = tk.Tk()
app.title("Colag Language IDE - Prototype")
app.geometry("700x500")
app.configure(bg="#f9f9f9")

# Heading
tk.Label(app, text="🧪 Colag Language Interface (v0.1)", font=("Arial", 16, "bold"), bg="#f9f9f9").pack(pady=10)

# Code Input Area
tk.Label(app, text="Write your Colag Code below:", font=("Arial", 12), bg="#f9f9f9").pack()
code_input = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=80, height=10, font=("Courier", 11))
code_input.pack(pady=5)

# Run Button
tk.Button(app, text="▶ Run Code", command=execute_code, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=10)

# Output Box
tk.Label(app, text="Output:", font=("Arial", 12, "bold"), bg="#f9f9f9").pack()
output_box = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=80, height=6, font=("Courier", 11), state='disabled')
output_box.pack(pady=5)

# Main loop
app.mainloop()
