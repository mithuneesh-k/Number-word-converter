import customtkinter as ctk
from words_to_number import words_to_number
from number_to_words import number_to_words

# ---------- Setup ---------- #
ctk.set_appearance_mode("light")   # Light theme
ctk.set_default_color_theme("blue")  

app = ctk.CTk()
app.title("Number Converter")
app.geometry("700x500") 

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# ---------- Container Frame ---------- #
container = ctk.CTkFrame(app, corner_radius=15)
container.grid(row=0, column=0, sticky="nsew")

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

frames = {}

def show_frame(frame_name):
    frame = frames[frame_name]
    frame.tkraise()

# ---------- Home Page ---------- #
home_frame = ctk.CTkFrame(container)
home_frame.grid(row=0, column=0, sticky="nsew")

for i in range(5):
    home_frame.grid_rowconfigure(i, weight=1)
home_frame.grid_columnconfigure(0, weight=1)

title = ctk.CTkLabel(home_frame, text="Number Converter", font=("Segoe UI", 36, "bold"))
title.grid(row=0, column=0, pady=20)

btn1 = ctk.CTkButton(home_frame, text="Words → Number", width=220, height=50,
                     command=lambda: show_frame("words_to_num"))
btn1.grid(row=1, column=0, pady=10)

btn2 = ctk.CTkButton(home_frame, text="Number → Words", width=220, height=50,
                     command=lambda: show_frame("num_to_words"))
btn2.grid(row=2, column=0, pady=10)

frames["home"] = home_frame

# ---------- Words → Number Page ---------- #
words_to_num_frame = ctk.CTkFrame(container)
words_to_num_frame.grid(row=0, column=0, sticky="nsew")

for i in range(6):
    words_to_num_frame.grid_rowconfigure(i, weight=1)
words_to_num_frame.grid_columnconfigure(0, weight=1)

label1 = ctk.CTkLabel(words_to_num_frame, text="Enter Number in Words:", font=("Segoe UI", 20))
label1.grid(row=0, column=0)

words_entry = ctk.CTkEntry(words_to_num_frame, width=500, height=40, font=("Consolas", 18))
words_entry.grid(row=1, column=0)

words_result = ctk.CTkLabel(words_to_num_frame, text="", font=("Segoe UI", 22), text_color="#315FF7", wraplength=650, justify="center")
words_result.grid(row=2, column=0, padx=10)

def convert_words_to_num():
    try:
        val = words_entry.get().strip()
        result = words_to_number(val)
        words_result.configure(text=str(result), text_color="#3C83DF")
    except ValueError as e:
        words_result.configure(text=f"Error: {e}", text_color="red")

def copy_words_result():
    app.clipboard_clear()
    app.clipboard_append(words_result.cget("text"))

ctk.CTkButton(words_to_num_frame, text="Convert", width=150, command=convert_words_to_num).grid(row=3, column=0)
ctk.CTkButton(words_to_num_frame, text="Copy", width=150, fg_color="#2196F3",
              hover_color="#1976D2", command=copy_words_result).grid(row=4, column=0)
ctk.CTkButton(words_to_num_frame, text="← Back", width=150, fg_color="#9e9e9e",
              hover_color="#616161", command=lambda: show_frame("home")).grid(row=5, column=0)

frames["words_to_num"] = words_to_num_frame

# ---------- Number → Words Page ---------- #
num_to_words_frame = ctk.CTkFrame(container)
num_to_words_frame.grid(row=0, column=0, sticky="nsew")

for i in range(6):
    num_to_words_frame.grid_rowconfigure(i, weight=1)
num_to_words_frame.grid_columnconfigure(0, weight=1)

label2 = ctk.CTkLabel(num_to_words_frame, text="Enter Number:", font=("Segoe UI", 20))
label2.grid(row=0, column=0)

num_entry = ctk.CTkEntry(num_to_words_frame, width=500, height=40, font=("Consolas", 18))
num_entry.grid(row=1, column=0)

num_result = ctk.CTkLabel(num_to_words_frame, text="", font=("Segoe UI", 22), text_color="#3162E8", wraplength=650, justify="center")
num_result.grid(row=2, column=0, padx=10)

def convert_num_to_words():
    try:
        n = int(num_entry.get().strip())
        result = number_to_words(n)
        num_result.configure(text=result, text_color="#2F76E2")
    except ValueError:
        num_result.configure(text="Please enter a valid integer.", text_color="red")

def copy_num_result():
    app.clipboard_clear()
    app.clipboard_append(num_result.cget("text"))

ctk.CTkButton(num_to_words_frame, text="Convert", width=150, command=convert_num_to_words).grid(row=3, column=0)
ctk.CTkButton(num_to_words_frame, text="Copy", width=150, fg_color="#2196F3",
              hover_color="#1976D2", command=copy_num_result).grid(row=4, column=0)
ctk.CTkButton(num_to_words_frame, text="← Back", width=150, fg_color="#9e9e9e",
              hover_color="#616161", command=lambda: show_frame("home")).grid(row=5, column=0)

frames["num_to_words"] = num_to_words_frame

# ---------- Start ---------- #
show_frame("home")
app.mainloop()
