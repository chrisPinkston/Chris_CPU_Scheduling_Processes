import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage

# Calculate Average Turnaround Time and Average Waiting Time for FCFS
def calculate_fcfs(df):
    completion_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0

    for index, row in df.iterrows():
        completion_time = max(completion_time, row['arrival time']) + row['burst time']
        turnaround_time = completion_time - row['arrival time']
        waiting_time = turnaround_time - row['burst time']
        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time

    avg_turnaround_fcfs = total_turnaround_time / len(df)
    avg_waiting_fcfs = total_waiting_time / len(df)
    return avg_turnaround_fcfs, avg_waiting_fcfs

# Calculate Average Turnaround Time and Average Waiting Time for SJF
def calculate_sjf(df):
    df_sjf = df.sort_values(by='burst time')
    completion_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0

    for index, row in df_sjf.iterrows():
        completion_time = max(completion_time, row['arrival time']) + row['burst time']
        turnaround_time = completion_time - row['arrival time']
        waiting_time = turnaround_time - row['burst time']
        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time

    avg_turnaround_sjf = total_turnaround_time / len(df_sjf)
    avg_waiting_sjf = total_waiting_time / len(df_sjf)
    return avg_turnaround_sjf, avg_waiting_sjf


# Calculate Average Turnaround Time and Average Waiting Time for RR
def calculate_rr(df, time_quantum):
    df_rr = df.copy()
    completion_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0

    while not df_rr.empty:
        for index, row in df_rr.iterrows():
            if row['burst time'] <= time_quantum:
                completion_time = max(completion_time, row['arrival time']) + row['burst time']
                turnaround_time = completion_time - row['arrival time']
                waiting_time = turnaround_time - row['burst time']
                total_turnaround_time += turnaround_time
                total_waiting_time += waiting_time
                df_rr.drop(index, inplace=True)
            else:
                completion_time = max(completion_time, row['arrival time']) + time_quantum
                df_rr.at[index, 'burst time'] -= time_quantum

    avg_turnaround_rr = total_turnaround_time / len(df)
    avg_waiting_rr = total_waiting_time / len(df)
    return avg_turnaround_rr, avg_waiting_rr


# Function to calculate metrics
def calculate_metrics(result_label):
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        df = pd.read_excel(file_path)
        time_quantum_rr = df['time quantum(for RR)'][0]
        
        avg_turnaround_fcfs, avg_waiting_fcfs = calculate_fcfs(df)
        avg_turnaround_sjf, avg_waiting_sjf = calculate_sjf(df)
        avg_turnaround_rr, avg_waiting_rr = calculate_rr(df, time_quantum_rr)
        
        result_label.config(text=f"FCFS: Avg Turnaround Time = {avg_turnaround_fcfs:.2f}, Avg Waiting Time = {avg_waiting_fcfs:.2f}\n"
                                 f"SJF: Avg Turnaround Time = {avg_turnaround_sjf:.2f}, Avg Waiting Time = {avg_waiting_sjf:.2f}\n"
                                 f"RR: Avg Turnaround Time = {avg_turnaround_rr:.2f}, Avg Waiting Time = {avg_waiting_rr:.2f}")

# GUI Initialization
root = tk.Tk()
root.title("Chris's CPU Scheduling Application")

# Welcome Page
background_image = PhotoImage(file="capua.png")

image_width = root.winfo_screenwidth()  # Get the screen width
background_image = background_image.subsample(int(background_image.width() / image_width))

# Set up a Label to display the background image
background_label = tk.Label(root, image=background_image)
background_label.pack(fill="both", expand=True)

welcome_label = tk.Label(root, text="Welcome to Chris's CPU Scheduling Application", font=("Helvetica", 20))
welcome_label.pack(pady=30)
welcome_label.place(relx=0.5, rely=0.5, anchor="center")
start_button = tk.Button(root, text="Get Started", command=lambda: show_main_page())
start_button.pack()
start_button.place(relx=0.5, rely=0.75, anchor="center")

# Main Page
def show_main_page():
    background_label.pack_forget()
    welcome_label.place_forget()
    start_button.place_forget()
    title_label = tk.Label(root, text="Chris's CPU Scheduling Application", font=("Helvetica", 20), fg="green")
    title_label.pack(pady=25)

# Label for Turnaround Time definition
    turnaround_label = tk.Label(root, text="Turnaround Time: Total time taken for a process to complete its execution, from entering the system to finishing.", font=("Helvetica", 12))
    turnaround_label.pack(pady=5)
    
    # Label for Completion Time definition
    completion_label = tk.Label(root, text="Completion Time: The point in time when a process finishes its execution, sum of arrival time and turnaround time.", font=("Helvetica", 12))
    completion_label.pack(pady=5)
    
    # Label for Waiting Time definition
    waiting_label = tk.Label(root, text="Waiting Time: Total time a process spends waiting in the ready queue before execution, difference between turnaround and burst time.", font=("Helvetica", 12))
    waiting_label.pack(pady=5)
    
    # Label for Arrival Time definition
    arrival_label = tk.Label(root, text="Arrival Time: The point in time when a process enters the system and becomes available for execution.", font=("Helvetica", 12))
    arrival_label.pack(pady=5)

    # Label for FCFS definition
    arrival_label = tk.Label(root, text="First-Come, First-Served (FCFS) Scheduling:FCFS is a non-preemptive scheduling algorithm that schedules processes in the order they arrive in the ready queue. The process that arrives first gets executed first. It may result in a scenario known as the convoy effect, where a long process holds up shorter processes behind it.", font=("Helvetica", 12), wraplength=400)
    arrival_label.pack(pady=5)
    
    # Label for SJF definition
    arrival_label = tk.Label(root, text="Shortest Job First (SJF) Scheduling:SJF is a scheduling algorithm that prioritizes processes with the shortest burst time. It can be either preemptive or non-preemptive. SJF aims to minimize the average waiting time by executing the shortest jobs first, ensuring that shorter jobs are completed before longer ones.", font=("Helvetica", 12), wraplength=400)
    arrival_label.pack(pady=5)

    # Label for RR definition
    arrival_label = tk.Label(root, text="Round Robin (RR) Scheduling:RR is a preemptive scheduling algorithm that allocates a fixed time quantum to each process in a cyclic manner. When a process's time quantum expires, it is moved to the back of the queue, and the next process in line gets a turn. RR provides fairness and responsiveness and prevents long processes from monopolizing the CPU for extended periods.", font=("Helvetica", 12), wraplength=400)
    arrival_label.pack(pady=5)

    upload_button = tk.Button(root, text="Upload Excel File", command=lambda: calculate_metrics(result_label))
    upload_button.pack(pady=10)
    
    result_label = tk.Label(root, text="", font=("Helvetica", 12))
    result_label.pack(pady=20)

# Run GUI
root.geometry("800x600")
root.mainloop()

