import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk

window = tk.Tk()

class Interface(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Image Converter")
        self.parent['bg'] = 'red'

        self.build_ui()
        
    def import_image(self):
        """function to import image from disk"""
        file = fd.askopenfilename(title="Open file", initialdir=os.environ["HOME"])
        return file
        
    def build_ui(self):
        """ functiion to build ui """
        ui_frame = tk.Frame(self.parent)
        ui_frame.grid()
        tk.Button(ui_frame, text='hello friend',
                  command=self.import_image).grid()

class ImageConversion():
    """utility class for image loading and conversion"""
    self.image = None
    
    def load_picture(image_name):
        """function to load image"""
        im = Image.open(image_name)
        self.image = im.convert("RGB")

    def save_as_format(image_format):
        """function to save image"""
        name = 'image.' + image_format
        print(name)
        self.image.save(name)

Interface(window)
##tkimage = tk.PhotoImage(im)
##tk.Label(window, image=tkimage).grid()
##window.mainloop()
