import tkinter as tk
import midpoint as m
import output as o

labelString = ""
def DrawCircle(window2):
    window2.create_oval(50,50,350,350, outline="black")
def DrawLine(window2, x1, y1, x2, y2, color):
    x1New = 200 + (x1*150)
    y1New = 200 - (y1*150)
    x2New = 200 + (x2*150)
    y2New = 200 - (y2*150)
    if color == True:
        window2.create_line(x1New, y1New, x2New, y2New, fill="#000fff000", width=2)
    else:
        window2.create_line(x1New, y1New, x2New, y2New, fill="#fff000000", width=2)

def midpointSim(numTrials):
    global totalSuccess
    global currentIteration
    root2 = tk.Tk()
    root2.title("Bertrand Paradox: Midpoint Method Simulation")
    root2.geometry("400x400")
    window2 = tk.Canvas(root2,width=400,height=400)
    window2.pack(expand="YES",fill ="both")
    totalSuccess = 0
    currentIteration = 1
    DrawCircle(window2)    
    windowUpdater(root2, window2, numTrials)
    root2.mainloop()

def windowUpdater(root2, window2, numTrials):
    global totalSuccess
    global currentIteration
    sim = m.midpoint()
    color = sim.getSuccess()
    
    DrawLine(window2, sim.getX1(), sim.getY1(), sim.getX2(), sim.getY2(), color)
    totalSuccess = totalSuccess + sim.getSuccess()

    if currentIteration <= numTrials:
        currentIteration = 1+currentIteration
        root2.after(1, windowUpdater, root2, window2, numTrials)
    else:
        o.output("Midpoint",numTrials, totalSuccess)