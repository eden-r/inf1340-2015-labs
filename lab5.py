#!/usr/bin/env python3

""" GUI for Name that Shape """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from name_that_shape import name_that_shape
import Tkinter
import tkMessageBox

"""
   Create a GUI for the Name That Shape program
   See name_shape_gui.png for specification
   Use the name_that_shape.py to perform computations
   For inputs that raise an error, pop up a modal dialog box
   For inputs that produce a shape name, display the string in the window
"""


class NameThatShapeGUI:


    def __init__(self):
        self.main_window = Tkinter.Tk()

        # create three frames to group widgets, create widgets
        self.top_frame = Tkinter.Frame(self.main_window)
        self.prompt_label = Tkinter.Label(self.top_frame, text='Enter the number of sides in the shape:')
        self.side_entry = Tkinter.Entry(self.top_frame, width=10)

        # middle frame
        self.mid_frame = Tkinter.Frame(self.main_window)
        self.name_label = Tkinter.Label(self.mid_frame, text='Name of Shape: ')

        # doing the output = use the label in a certain way so that it responds to content
        self.value = Tkinter.StringVar()
        self.value.set("")
        self.shape_name = Tkinter.Label(self.mid_frame, textvariable=self.value)


        # bottom frame
        self.bottom_frame = Tkinter.Frame(self.main_window)
        self.conv_button = Tkinter.Button(self.bottom_frame, text='Name', command=self.convert)
        self.quit_buttom = Tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)


        # pack the widgets
        self.prompt_label.pack(side='left')
        self.side_entry.pack(side='left')

        self.name_label.pack(side='left')
        self.shape_name.pack(side='left')

        self.conv_button.pack(side='left')
        self.quit_buttom.pack(side='left')

        # Pack the frames in the order they will appear
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()


        Tkinter.mainloop()

    def value_error_message(self):
        tkMessageBox.showinfo("Error", "\"" + self.side_entry.get() + "?\" I don't know a shape with that many sides")
    def type_error_message(self):
        tkMessageBox.showinfo("Error", "\"" + self.side_entry.get() + "\" is invalid input")

    def convert(self):
        # pop up a modal dialogue
        #tkMessageBox.showinfo("Response", self.side_entry.get())
        #self.value.set(self.side_entry.get())
        sides = self.side_entry.get()
        sides = str(sides)

        try:
            if sides.isdigit() or sides[0] is "-" and sides[1:].isdigit():
                sides = int(sides)
            else:
                raise TypeError
            if (sides > 10) or (sides < 3):
                raise ValueError
        except TypeError:
            self.type_error_message()
        except ValueError:
            self.value_error_message()

        self.value.set(name_that_shape(sides))



# Instantiating the object
ntsg = NameThatShapeGUI()
