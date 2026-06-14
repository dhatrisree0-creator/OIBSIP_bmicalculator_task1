import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        name = name_entry.get().strip()
        age = age_entry.get().strip()
        weight = float(weight_entry.get())
        height_input = float(height_entry.get())
        
        if not name:
            name = "User"
        if not age:
            age = "N/A"
            
        if height_input > 3.0:
            height_m = height_input / 100.0
        else:
            height_m = height_input
            
        bmi = weight / (height_m ** 2)
        
        if bmi < 18.5:
            category = "UNDERWEIGHT 🟡"
            bg_color = "#334155"
            fg_color = "#fef08a"  
        elif 18.5 <= bmi < 24.9:
            category = "NORMAL WEIGHT 🟢"
            bg_color = "#14532d"  
            fg_color = "#4ade80"  
        elif 25 <= bmi < 29.9:
            category = "OVERWEIGHT 🟠"
            bg_color = "#7c2d12"  
            fg_color = "#fdba74"  
        else:
            category = "OBESE 🔴"
            bg_color = "#7f1d1d"  
            fg_color = "#fca5a5" 
            
        results_card.config(bg=bg_color, highlightbackground=fg_color, highlightthickness=2)
        result_label.config(text=f"{name} (Age: {age}) — BMI: {bmi:.2f}", fg="#f8fafc", bg=bg_color)
        category_label.config(text=category, fg=fg_color, bg=bg_color)
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height!")

root = tk.Tk()
root.title("Vibrant BMI Tracker — Dark Mode")
root.geometry("420x620")
root.configure(bg="#0f172a")  

header_frame = tk.Frame(root, bg="#1e293b", height=90)
header_frame.pack(fill="x")
header_frame.pack_propagate(False)

title_lbl = tk.Label(header_frame, text="⚡ VIBRANT HEALTH CALCULATOR ⚡", font=("Helvetica", 13, "bold"), fg="#14b8a6", bg="#1e293b")
title_lbl.pack(pady=32)

main_frame = tk.Frame(root, bg="#0f172a")
main_frame.pack(pady=15, padx=40, fill="both", expand=True)

def create_input_field(parent, label_text, accent_color):
    lbl = tk.Label(parent, text=label_text, font=("Helvetica", 10, "bold"), fg=accent_color, bg="#0f172a")
    lbl.pack(anchor="w", pady=(10, 2))
    

    entry = tk.Entry(parent, font=("Helvetica", 12, "bold"), bg="#1e293b", fg="#f8fafc", 
                     insertbackground="#14b8a6", bd=1, relief="solid", highlightthickness=0)
    entry.pack(fill="x", ipady=6, pady=(0, 5))
    return entry

name_entry = create_input_field(main_frame, "👤 ENTER NAME", "#94a3b8")       
age_entry = create_input_field(main_frame, "📅 ENTER AGE", "#94a3b8")        
weight_entry = create_input_field(main_frame, "⚖️ WEIGHT (kg)", "#94a3b8")  
height_entry = create_input_field(main_frame, "📏 HEIGHT (cm or m)", "#94a3b8") 

calc_btn = tk.Button(
    main_frame, 
    text="GENERATE REPORT", 
    font=("Helvetica", 11, "bold"), 
    bg="#f43f5e",  
    fg="white", 
    activebackground="#be123c", 
    activeforeground="white",
    bd=0, 
    relief="flat",
    command=calculate_bmi,
    cursor="hand2"
)
calc_btn.pack(fill="x", ipady=10, pady=25)

results_card = tk.Frame(main_frame, bg="#1e293b", highlightbackground="#334155", highlightthickness=1)
results_card.pack(fill="x", ipady=18, pady=5)

result_label = tk.Label(results_card, text="Awaiting your metrics...", font=("Helvetica", 11, "italic"), fg="#94a3b8", bg="#1e293b")
result_label.pack(pady=(8, 2))

category_label = tk.Label(results_card, text="STATUS: IDLE", font=("Helvetica", 13, "bold"), fg="#64748b", bg="#1e293b")
category_label.pack(pady=(0, 8))

root.mainloop()