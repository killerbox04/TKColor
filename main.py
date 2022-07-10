#Color Picker

import tkinter as tk
from tkinter import ttk
import time
import random

#Make color window a random color on startup
ranRGB = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
ranHex = '#%02x%02x%02x' % ranRGB

class main(tk.Tk):
    def __init__(self):
        super().__init__()

        #Window config
        self.title("Color Picker")
        self.resizable(width=False, height=False)

        #THIS NEEEEEEDS TO BE CHANGED TO A CANVACE
        #fuck your canvas
        #Color window
        self.colorWin = tk.Label(
                self,
                text = f"HEX:{ranHex}",
                height = 10,
                width = 17,
                bg = ranHex
                )
        
        self.colorWin.grid(
                row = 0,
                column = 0,
                padx = 5,
                pady = 5
                ) 
        
        #RGB Input Boxes
        #Red
        self.redBox = tk.Entry(
                self,
                bg = "red"
                )

        self.redBox.grid(
                row = 1, 
                column = 0,
                padx = 5,
                pady = 1
                )
        #Green

        self.greenBox = tk.Entry(
                self,
                bg = "green"
                )

        self.greenBox.grid(
                row = 2,
                column = 0,
                padx = 5,
                pady = 1
                )
        
        #Blue
        self.blueBox = tk.Entry(
                self,
                bg = "blue"
                )

        self.blueBox.grid(
                row = 3,
                column = 0, 
                padx = 5,
                pady = 1
                )


        #Apply Button - Applies RGB value to output square
        self.applyButton = tk.Button(
                self,
                text = "Apply",
                command = self.apply
                )
        
        self.applyButton.grid(
                row = 4,
                column = 0
                )

    def apply(self):
       #Get RGB vals, convert into a hex val, and finally assign the hex val to the color square
        try:
            R = int(self.redBox.get())
            G = int(self.greenBox.get())
            B = int(self.blueBox.get())
            rgb = (R, G, B)
            colorHex = '%02x%02x%02x' % rgb
            
            self.colorWin.config(text = f"HEX:#{colorHex}")
            self.colorWin.config(bg = f"#{colorHex}")
        
        except:
            print("Invalid input")


if __name__ == "__main__":

    app = main()
    app.mainloop()


