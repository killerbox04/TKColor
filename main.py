#Color Picker

import tkinter as tk
from tkinter import ttk
import time


class main(tk.Tk):
    def __init__(self):
        super().__init__()

        #Window config
        self.title("Color Picker")
        self.resizable(width=False, height=False)

        #THIS NEEEEEEDS TO BE CHANGED TO A CANVACE
        #Or does it, its not causing a problem its.
        #Its like using a jet engine to blow leaves away
        #Yeah it works but I mean, its a little goofy
        #Color window
        self.colorWin = tk.Label(
                self,
                text = "",
                height = 10,
                width = 17,
                bg = "#65A8E1"
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
                self
                )

        self.redBox.grid(
                row = 1, 
                column = 0,
                padx = 5,
                pady = 1
                )
        #Green

        self.greenBox = tk.Entry(
                self
                )

        self.greenBox.grid(
                row = 2,
                column = 0,
                padx = 5,
                pady = 1
                )
        
        #Blue
        self.blueBox = tk.Entry(
                self
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
            
            self.colorWin.config(bg = f"#{colorHex}")
        
        except:
            


        pass


if __name__ == "__main__":
    app = main()
    app.mainloop()


