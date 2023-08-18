# Chris's CPU Scheduling Simulator

Chris's CPU Scheduling Simulator is a user-friendly application that calculates average turnaround and waiting times for different CPU scheduling algorithms. It supports three major algorithms:

- **First-Come, First-Served (FCFS)**
- **Shortest Job First (SJF)**
- **Round Robin (RR)**

## How To Use

1. Clone or download this repository.
2. Ensure you have the necessary Python libraries installed:
   - `pandas`
   - `tkinter`
3. Run the application and you'll be greeted with a welcome page.
4. Click on "Get Started" to proceed to the main page.
5. To evaluate the metrics of your processes, upload an Excel file with the appropriate format. The results will be displayed instantly.

## Excel File Format

For the application to work correctly, the Excel file must adhere to a specific format:

- Columns needed: `arrival time`, `burst time`, and `time quantum(for RR)`.
- The column `time quantum(for RR)` is specifically used for the Round Robin algorithm. It should have a time quantum value in the first cell.

Please ensure your Excel file aligns with this format before uploading. Incorrect or missing data might lead to unexpected results.

## Licensing

This software is open-source and free to use. However, if you're planning to use or adapt it for your projects, please provide appropriate attribution. Also, ensure you understand the requirements and constraints of the libraries used.
