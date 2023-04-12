import tkinter as tk
import endpointSim as eps
import midpointSim as mps
import radiusSim as rs
import method4Sim as m4

#runs simulations and gets inputs from initial GUI
def submit():
    numTrials = int(trialsInput.get())
    method = option.get()
    root.destroy()
    if method == "Endpoint":
        simulation = eps.endpointSim(numTrials)
    elif method == "Midpoint":
        simulation = mps.midpointSim(numTrials)
    elif method == "Radius":
        simulation = rs.radiusSim(numTrials)
    elif method == "Method 4":
        simulation = m4.method4Sim(numTrials)

#creates new GUI window and GUI elements
root = tk.Tk()
window = tk.Canvas(root,width=520,height=560)
root.title("Bertrand Paradox Simulation")
root.geometry("520x600")
window.pack(expand="YES",fill ="both")

label = tk.Label(window, text="Bertrand Paradox Simulation")
label.grid(row=0, column=0, padx=10, pady=10)

trialsLabel = tk.Label(window, text="Enter the number of trials:")
trialsLabel.grid(row=2, column=0,pady=10)

methodLabel = tk.Label(window, text="Choose what method that will be used:")
methodLabel.grid(row=3, column=0, pady=10)

trialsInput = tk.Entry(window)
trialsInput.grid(row=2, column=1)

options = ["Endpoint", 
           "Midpoint", 
           "Radius", 
           "Method 4"]
option = tk.StringVar()
option.set( "Endpoint" )

methodDrop = tk.OptionMenu( window, option, *options )
methodDrop.grid(row=3, column=1)

submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.grid(row=4, column=0,padx=10,pady=10)

tk.mainloop()