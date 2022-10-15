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
        self.bg = tk.PhotoImage(file='assets/bg1.png')
        self.bg = self.bg.subsample(5, 5)
        self.select_icon = tk.PhotoImage(file='assets/select.png')
        self.convert_icon = tk.PhotoImage(file='assets/convert.png')

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
##            nonlocal input_var
            image_format = input_var.get()
            self.converter_object.save_as_format(image_format)
            
        ui_frame = tk.Frame(self.parent, bg="white", bd=2)
        ui_frame.grid()
        # create header frame inside of ui_frame
        header_frame = tk.Frame(ui_frame,bg='white' )
        header_frame.grid(row=0)
##        tk.Label(header_frame, bg='white').grid()
        # create body frame to house all the main content
        body_frame = tk.Frame(ui_frame, bg='#e7e7e7')
        body_frame.grid(row=1, )
        # create a left inner frame inside of body frame
        left_inner_frame = tk.Frame(body_frame, bg='#e7e7e7')
        left_inner_frame.grid(row=0, column=0, sticky='we', padx=60)
        # -------------------------------------------------
        bg = tk.Label(left_inner_frame, text="Convert Image ", font='Matura 29 bold',
                      bg="#e7e7e7",fg='navy', relief='flat')
        bg.grid(ipadx=0, sticky='w')
        # more
        bg = tk.Label(left_inner_frame, text="Format With Ease", font='Matura 25 bold',
                      bg="#e7e7e7",fg='navy', relief='flat')
        bg.grid(sticky='w')
         # add horizontal line
        ttk.Separator(left_inner_frame, orient='horizontal').grid(pady=5,padx=5, sticky='we')
        # -------------------------------------------------
        # description frame
        desc_frame = tk.Frame(left_inner_frame,  bg='#e7e7e7')
        desc_frame.grid(sticky='w')
        tk.Label(desc_frame,
                 text='Convert your pictures to your desired',
                 bg='#e7e7e7', fg='navy').grid(pady=2,sticky='w')
        tk.Label(desc_frame,
                 text='format with ease and fast',
                 bg='#e7e7e7', fg='navy').grid(pady=2,sticky='w')
        # add horizontal line
        ttk.Separator(left_inner_frame, orient='horizontal').grid(pady=5,padx=5, sticky='we')

        btn_frame = tk.Frame(left_inner_frame,  bg='#e7e7e7')
        btn_frame.grid()
        
        
##        input_var = tk.StringVar()
##        image_format = ttk.Combobox(left_inner_frame,state='readonly',textvariabl=input_var,
##                     values=['jpg', 'png', 'ico'], font='matura 15',)
##        image_format.set("Select Format")
##        image_format.grid(pady=10, padx=10)
        tk.Button(btn_frame, image=self.select_icon, text='Select',
                  font='Helvetica 15 bold', compound='left',
                  bg="navy",fg='#e7e7e7',
                  command=self.import_image).grid(row=0, column=0, pady=0, sticky='w')
        tk.Button(btn_frame, image=self.convert_icon, text="Convert Image",
                  bg="navy",fg='white', compound='left',
                  font="Helvetica 15 bold",
                  command=convert_call_back).grid(row=0, column=1,)
        
        # create a right inner frame inside of body frame
        right_inner_frame = tk.Frame(body_frame)
        right_inner_frame.grid(row=0, column=1)
        tk.Label(right_inner_frame, image=self.bg, relief='flat').grid()

Interface(window)
##tkimage = tk.PhotoImage(im)
##tk.Label(window, image=tkimage).grid()
##window.mainloop()
