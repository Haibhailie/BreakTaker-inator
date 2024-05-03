import tkinter as tk
from tkinter import ttk
import sv_ttk

def main():
    app = tk.Tk()
    app.title('Take a Break Reminder')
    app.geometry('437x494')
    sv_ttk.set_theme("light")

    frame = ttk.Frame(app, padding="30 30 30 30")
    frame.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)

    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    tk.Label(frame, text="Take a break every", font=("Helvetica", 12)).grid(column=0, row=0, columnspan=3, sticky=tk.EW)

    def add_arrow_hover_effect(button):
        def on_enter(e):
            button['foreground'] = 'green'

        def on_leave(e):
            button['foreground'] = 'black'

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

    increment_button = tk.Button(frame, text="▲", bd=0, command=lambda: increase(number), font=("Helvetica", 24))
    increment_button.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)
    
    number = tk.StringVar(value='15')
    number_label = tk.Label(frame, textvariable=number, font=("Helvetica", 24))
    number_label.grid(column=1, row=2, sticky=tk.EW)
    
    decrement_button = tk.Button(frame, text="▼", bd=0, command=lambda: decrease(number), font=("Helvetica", 24))
    decrement_button.grid(column=1, row=3, sticky=tk.EW, padx=5, pady=5)

    add_arrow_hover_effect(increment_button)
    add_arrow_hover_effect(decrement_button)

    unit = tk.StringVar(value='Minutes')
    for i, text in enumerate(["Seconds", "Minutes", "Hours"], start=0):
        b = ttk.Button(frame, text=text, style="Transparent.TButton", command=lambda text=text: unit.set(text))
        b.grid(column=i, row=4, sticky=tk.EW, padx=8, pady=5)

    play_icon = tk.PhotoImage(file="./assets/icons/play.png")
    pause_icon = tk.PhotoImage(file="./assets/icons/pause.png")
    stop_icon = tk.PhotoImage(file="./assets/icons/stop.png")

    play_button = tk.Button(frame, image=play_icon, fg='white', bd=0, activebackground='black', activeforeground='white', command=lambda: start)
    play_button.image = play_icon  
    play_button.grid(column=0, row=5, sticky=tk.EW, padx=10, pady=10)

    pause_button = tk.Button(frame, image=pause_icon, fg='white', bd=0, activebackground='black', activeforeground='white', command=lambda: pause)
    pause_button.image = pause_icon  
    pause_button.grid(column=1, row=5, sticky=tk.EW, padx=10, pady=10)

    stop_button = tk.Button(frame, image=stop_icon, fg='white', bd=0, activebackground='black', activeforeground='white', command=lambda: stop)
    stop_button.image = stop_icon  
    stop_button.grid(column=2, row=5, sticky=tk.EW, padx=10, pady=10)

    app.mainloop()

def increase(number):
    value = int(number.get())
    number.set(value + 1)

def decrease(number):
    value = int(number.get())
    number.set(value - 1 if value > 0 else 0)

def start():
    print("Timer started")

def stop():
    print("Timer stopped")

def pause():
    print("Timer paused")

if __name__ == "__main__":
    main()
