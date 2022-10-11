from PIL import Image
import tkinter as tk

##window = tk.Tk()
def load_picture():
    image_name = input("enter image name")
    im = Image.open(image_name)
    return im.convert("RGB")

def save_as_format():
    image_format = input("enter Image format")
    image = load_picture()
    name = 'image.' + image_format
    print(name)
    image.save(name)

save_as_format()  
##tkimage = tk.PhotoImage(im)
##tk.Label(window, image=tkimage).grid()
##window.mainloop()
