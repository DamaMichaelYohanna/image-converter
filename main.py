import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk

window = tk.Tk()

class ImageConversion():
    """utility class for image loading and conversion"""
    def __init__(self):
        self.image = None
    
    def load_picture(self, image_name):
        """function to load image"""
        im = Image.open(image_name)
        print(im)
        self.image = im.convert("RGB")

    def save_as_format(self, image_format):
        """function to save image"""
        name = 'image.' + image_format
        print(name)
        print(self.image)
        self.image.save(name)

        
class Interface(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Image Converter")
        self.parent['bg'] = 'red'

        self.converter_object = ImageConversion()

        self.build_ui()
        
    def import_image(self):
        """function to import image from disk"""
        filetype = (
            ('All Files ', '*.*'),
            ('image file ', '*.jpg'),
            ('portable network graphic', '*.png'),
            )
        file = fd.askopenfilename(title="Open file",
                                  initialdir=os.environ["HOME"],
                                  filetypes=filetype)
        self.converter_object.load_picture(file)
    
        
    def build_ui(self):
        """ functiion to build ui """

        def convert_call_back():
            """onclick call back for convert button"""
            nonlocal input_var
            image_format = input_var.get()
            self.converter_object.save_as_format(image_format)
            
        ui_frame = tk.Frame(self.parent)
        ui_frame.grid()
        bg = tk.Label(ui_frame, text="hello world", font='Matura 26', bg="white")
        bg.grid(ipady=40)
        tk.Button(ui_frame, text='Select Image', font='Helvetica 15',width=23,
                  command=self.import_image).grid(pady=10)
        ttk.Separator(ui_frame, orient='horizontal').grid(pady=0,padx=10, sticky='we')
        input_var = tk.StringVar()
        image_format = ttk.Combobox(ui_frame,state='readonly',textvariabl=input_var,
                     values=['jpg', 'png', 'ico'], font='matura 15')
        image_format.set("Select Format")
        image_format.grid(pady=10, padx=10)
        tk.Button(ui_frame, text="Convert Image",
                  font="Helvetica 15", width=23,
                  command=convert_call_back).grid(pady=10)


Interface(window)
##tkimage = tk.PhotoImage(im)
##tk.Label(window, image=tkimage).grid()
##window.mainloop()
