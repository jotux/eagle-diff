#!/usr/bin/env python
import os, sys
import Image
import ImageTk
import ImageChops
import Tkinter
import subprocess

eagle_path = "C:/Program Files (x86)/EAGLE-6.1.0/bin/eagle.exe"

cmd = eagle_path + " -C \"export image b1.png 400;quit\" " + sys.argv[1]
subprocess.call(cmd)
cmd = eagle_path + " -C \"export image b2.png 400;quit\" " + sys.argv[2]
subprocess.call(cmd)

root = Tkinter.Tk()
root.resizable(0,0)

im_size = 640

image1 = Image.open('b1.png')
ratio = float(image1.size[0]) / float(image1.size[1])
image1 = image1.resize((im_size,int(im_size / ratio)), Image.ANTIALIAS)
tkimage1 = ImageTk.PhotoImage(image1)
image2 = Image.open('b2.png')
image2 = image2.resize((im_size,int(im_size / ratio)), Image.ANTIALIAS)
tkimage2 = ImageTk.PhotoImage(image2)
diff = ImageChops.difference(image1, image2)
diff = diff.resize((im_size,int(im_size / ratio)), Image.ANTIALIAS)
tk_diff = ImageTk.PhotoImage(diff)
overlay = ImageChops.screen(image1, image2)
overlay = overlay.resize((im_size,int(im_size / ratio)), Image.ANTIALIAS)
tk_overlay = ImageTk.PhotoImage(overlay)

root.geometry('%dx%d' % (image1.size[0] * 2,image1.size[1] * 2))
label_image1 = Tkinter.Label(root, image=tkimage1)
label_image2 = Tkinter.Label(root, image=tkimage2)
label_diff = Tkinter.Label(root, image=tk_diff)
label_overlay = Tkinter.Label(root, image=tk_overlay)

label_image1.place(x=0,y=0,width=im_size,height=int(im_size/ratio))
label_image2.place(x=im_size,y=0,width=im_size,height=int(im_size/ratio))
label_diff.place(x=0,y=int(im_size/ratio),width=im_size,height=int(im_size/ratio))
label_overlay.place(x=im_size,y=int(im_size/ratio),width=im_size,height=int(im_size/ratio))

root.title("Image diff")
root.mainloop()
os.system('del b1.png b2.png')
