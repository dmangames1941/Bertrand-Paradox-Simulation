import tkinter as tk

def output(method, numTrials, totalSuccess):
    root = tk.Tk()
    root.title("Bertrand Paradox Simulation Results")
    root.geometry("520x650")
    window = tk.Canvas(root,width=520,height=650)
    window.pack(expand="YES",fill ="both")

    label = tk.Label(window, text="Results")
    label.pack(side="top")

    resultLabel = tk.Label(window, text="Method: " + method + "\nNumber of Trials: " + str(numTrials) + "\nTotal Number of Success: " + str(totalSuccess) + "\nRelative Frequency of Success: " + str(totalSuccess/numTrials))
    resultLabel.pack()

    root.mainloop()