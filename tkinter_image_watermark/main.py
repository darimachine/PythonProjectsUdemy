
from tkinter import *
from tkinter.filedialog import askopenfilename
import PIL.Image
from PIL import Image,ImageDraw,ImageFont,ImageTk
def upload_file():
    global img,filename
    f_types=[('Picture Files','*.jpg *.png')]
    filename = askopenfilename(multiple=True,filetypes=f_types)
    col=1
    row=3
    for f in filename:
        img = Image.open(f)
        width, height = img.size
        img_resized = img.resize((100, 100))
        img = ImageTk.PhotoImage(img_resized)
        e1=Label(window)

        e1.image=img
        e1['image']=img
        e1.grid(row=row, column=col)
        if col==3:
            row+=1
            col=1
        else:
            col+=1

def add_watermark():

    global filename
    text = 'darimachine'
    print(filename)
    logo = ('Type Here your Logo Path')
    logo_open = Image.open(logo)
    logo_open.thumbnail((100,100))
    for image in filename:
        opened_image = Image.open(image)
        width, height = opened_image.size
        draw = ImageDraw.Draw(opened_image)
        font_size = int(width/12)
        font = ImageFont.truetype('arial.ttf',font_size)
        x,y = int(width/2), int(height/2)
        draw.text((x,y),text,font=font,fill='#FFF',stroke_width=3,stroke_fill='#222',anchor='ms')
        opened_image.paste(logo_open)
        opened_image.show()
    print(filename)
    print(1)
window = Tk()
window.geometry('410x300')
window.title("Image uploading")
my_font1=('times',18,'bold')
l1 = Label(window,text="Upload Files & display",width=30,font=my_font1)
l1.grid(row=1,column=1,columnspan=4)
b1 = Button(window,text='Upload File',width=20,command=lambda:upload_file())
b1.grid(row=2,column=1,columnspan=4)
b2 = Button(window,text='Add Watermark',width=20,command=lambda:add_watermark())
b2.grid(row=20,column=1,columnspan=4)


window.mainloop()