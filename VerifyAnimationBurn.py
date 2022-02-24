import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
from Resources import XYZ_LogFile_Read
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from os.path import dirname
import sys

def BurningAnimation():
    root = Tk()
    logFileAddress = askopenfilename(initialdir=dirname(sys.argv[0]), filetypes = (("Csv files","*.csv"),("all files","*.*")))
    root.update()
    root.destroy()
    X, Y, Z = XYZ_LogFile_Read(logFileAddress)

    fig = plt.figure()
    ax1 = fig.add_subplot(111,projection='3d')
    t = np.linspace(0, max(Z), len(Z))

    ax1.set_xlim3d([min(X), max(X)])
    ax1.set_xlabel('X')

    ax1.set_ylim3d([min(Y), max(Y)])
    ax1.set_ylabel('Y')

    ax1.set_zlim3d([min(Z), max(Z)])
    ax1.set_zlabel('Z')
    ax1.set_title('CNC Machine Run')

    lines = []
    for i in range(len(Z)):
        head = i - 1
        head_slice = (t > t[i]) & (t < t[i]+.25)
        line1,  = ax1.plot(X[:i], Y[:i], Z[:i],
                        color='black')
        line1a, = ax1.plot(X[head_slice], Y[head_slice], Z[head_slice],
                        color='red', linewidth=2)
        line1e, = ax1.plot([X[head]], [Y[head]], [Z[head]],
                        color='red', marker='o', markeredgecolor='r')
        lines.append([line1,line1a,line1e])
        
    ani = animation.ArtistAnimation(fig, lines, interval=10)
    plt.show()