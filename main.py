import os
from PIL import Image
import PIL
import tkinter as tk
from tkinter import filedialog as fd
import tkinter.messagebox as mbox
from tkinter import ttk

window = tk.Tk()

class ImageConversion():
    """utility class for image loading and conversion"""
    def __init__(self):
        self.image = None
    
    def load_picture(self, image_name: str):
        """function to load image"""
        try:
            im = Image.open(image_name)
        except PIL.UnidentifiedImageError:
            return 'error'
        self.image = im.convert("RGB")

    def save_as_format(self, image_format: str):
        """function to save image"""
        name = 'image.' + image_format
        try:
            self.image.save(name)
        except AttributeError:
            return 'error'

        
class Interface(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Image Converter")
        self.parent['bg'] = 'red'
        self.bg = tk.PhotoImage(file='assets/new.png')
        self.bg = self.bg.subsample(2, 2)
        self.select_icon = tk.PhotoImage(file='assets/select.png')
        self.select_icon=  self.select_icon.subsample(5, 5)
        self.convert_icon = tk.PhotoImage(file='assets/convert.png')
        self.convert_icon=  self.convert_icon.subsample(5, 5)
        self.github_icon = tk.PhotoImage(file='assets/github.png')
        self.github_icon=  self.github_icon.subsample(3, 3)
        self.facebook_icon = tk.PhotoImage(file='assets/facebook.png')
        self.facebook_icon=  self.facebook_icon.subsample(3, 3)

        self.converter_object = ImageConversion()

        self.build_ui()
        
    def import_image(self, btn):
        """function to import image from disk"""
        filetype = (
            ('All Files ', '*.*'),
            ('image file ', '*.jpg'),
            ('portable network graphic', '*.png'),
            )
        file = fd.askopenfilename(title="Open file",
                                  initialdir=os.environ["HOME"],
                                  filetypes=filetype)
        result = self.converter_object.load_picture(file)
        if not result:
            mbox.showinfo("success", "Image Loaded Successfully")
            btn['state'] = 'active'
        else:
            mbox.showerror("Failed", "Unsupported file format")
    
    def credit_ui(self):
        credit_win = tk.Toplevel(self.parent, bg='white')
        credit_win.transient(self.parent)
        credit_win.grid()
        tk.Label(credit_win,
                 text="This Piece Of Software Was Created By",
                 font='helvetica 13', bg='white').grid(pady=10, padx=10)
        tk.Label(credit_win,
                 text="Dama Michael Yohanna", bg='white', fg='Navy',
                 font='helvetica 15 bold').grid()
        ttk.Separator(credit_win, orient='horizontal').grid(pady=5,padx=5, sticky='we')

        tk.Label(credit_win,
                 text="""An enthusiastic Python Programmer with\n knowledge of web development using django, \n Desktop app with tkinter and PyQt, and little of Data analysis \n and ML with pandas,  numpy and scikit-learn.""",
                 font='helvetica 13', bg='white').grid(padx=20)

        tk.Label(credit_win,
                 text="I am resiliant in nature and open to learning.",
                 font='helvetica 13', bg='white').grid()
        ttk.Separator(credit_win, orient='horizontal').grid(pady=5,padx=5, sticky='we')

        tk.Label(credit_win,
                 text="You can check on me on the below channels",
                 font='helvetica 13', bg='white').grid()
        link_frame = tk.Frame(credit_win, bg='white')
        link_frame.grid()
        tk.Label(link_frame, image=self.facebook_icon,
                 bg='white').grid(row=0, column=0,padx=10)
        tk.Label(link_frame, image=self.github_icon,
                 bg='white').grid(row=0, column=1, padx=10, pady=10)

    def help_ui(self):
        help_win = tk.Toplevel(self.parent, bg='white')
        help_win.transient(self.parent)
        help_win.grid()

        
    def build_ui(self):
        """ functiion to build ui """
        def convert_call_back(input_var, pop_win):
            image_format = input_var.get()
            result = self.converter_object.save_as_format(image_format)
            if not result: 
                mbox.showinfo("success", "Image Converted Successfully")
                convert['state'] = 'active'
                print(convert['state'])


            else:
                mbox.showerror("Failed", "Image Conversion Failed")

                 
             # blur out select and format button
            select['state'] = 'active'
            convert['state'] = 'active'
           
            pop_win.withdraw()
            


        def popup_win_callback():

            """onclick call back for format selection popup """
            # create a toplevel transient window to display popup
            pop_win = tk.Toplevel(self.parent, bg='white')
            pop_win.transient(self.parent)
            pop_win.grid()
            # create combobox for format selection
            input_var = tk.StringVar()
            image_format = ttk.Combobox(pop_win,state='readonly',textvariabl=input_var,
                         values=['jpg', 'png', 'ico'], font='matura 15',)
            image_format.set("Select Format")
            image_format.grid(pady=10, padx=10)
            # proceed button
            tk.Button(pop_win, text='Proceed', bg='white', relief='flat',
                      width=31, command=lambda x=input_var, y=pop_win:convert_call_back(x, y)).grid(row=1,  pady=10,)
            # blur out select and format button
            select['state'] = 'disabled'
            convert['state'] = 'disabled'
            
            
            
        ui_frame = tk.Frame(self.parent, bg="white", bd=2)
        ui_frame.grid()
        # create header frame inside of ui_frame
        header_frame = tk.Frame(ui_frame,bg='white' )
        header_frame.grid(row=0, sticky='w')
        tk.Label(header_frame,text='Legacy Tech', bg='white',fg='navy',
                 font='consalas 15 bold').grid(row=0, column=0,sticky='w', padx=50, pady=10)
        # --------------------------------------------
        s_frame = tk.Frame(header_frame,bg='#f6f6f6' )
        s_frame.grid(row=0, column=1, sticky='ns')
        help_btn = tk.Button(s_frame, text='Help', bg='white', relief='flat',
                             command=self.help_ui)
        help_btn.grid(row=0, column=1,  padx=10,)
        credit_btn = tk.Button(s_frame, text='Credit', bg='white', relief='flat',
                               command=self.credit_ui)
        credit_btn.grid(row=0, column=2,  padx=10,pady=10)
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
        
        convert = tk.Button(btn_frame, image=self.convert_icon, text="Convert Image",
                  bg="navy",fg='white', compound='left',
                  font="Helvetica 15 bold",
                  command=popup_win_callback)
        convert.grid(row=0, column=1,)
        convert['state'] = 'disabled'
        select = tk.Button(btn_frame, image=self.select_icon, text='Select',
                  font='Helvetica 15 bold', compound='left',
                  bg="navy",fg='#e7e7e7',
                  command=lambda x=convert:self.import_image(x))
        select.grid(row=0, column=0, pady=0, sticky='w')
        
        # create a right inner frame inside of body frame
        right_inner_frame = tk.Frame(body_frame, bg='#e7e7e7')
        right_inner_frame.grid(row=0, column=1,)
        tk.Label(right_inner_frame, image=self.bg, relief='flat').grid(padx=70, pady=50)

        #------------------------------------
        footer_frame = tk.Frame(ui_frame, bg='white')
        footer_frame.grid()
        tk.Label(footer_frame,text='Alright Reserved! @ Legacy Technology', bg='white',
                 font='consalas 11 bold').grid(row=0, column=0,sticky='w', padx=50, pady=10)

Interface(window)
##tkimage = tk.PhotoImage(im)
##tk.Label(window, image=tkimage).grid()
##window.mainloop()
