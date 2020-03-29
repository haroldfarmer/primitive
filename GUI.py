from tkinter import *
import os

def window():
    root = Tk()
    myLabel = Label(root, text="Primitive")
    myLabel.pack()
    root.mainloop()
    os.system('primitive -i C:\\Users\\harol\\Desktop\\yaPal.jpg -o C:\\Users\\harol\\Desktop\\PythonGUI.png -n 100')
window()


#def window():
#       Creates window for the program

#TODO Req 1.0
#def helpButton()
#   Creates a help button

#TODO 1.1
#def export()
#   allow the user to export their finished
#   picture to the location of their choice 
#TODO 1.2
#def difficulty()
#   allows the user to select the number of geometric shapes to form
#   the image

#TODO 1.3
#def geometricShapes()
#   allows the user to select what geometric shape to form
#   the image

#TODO 1.4
#def display()
#   Shows the final form of the image

#TODO Req 1.5
#def file()
    #allows the user to select the photo they want
    #import easygui
    #file = easygui.fileopenbox()

   