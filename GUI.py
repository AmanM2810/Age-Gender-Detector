# Importing necessary liberaries
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image,ImageTk
import numpy as np
from tkinter import Button

# Initializing the GUI
top=tk.Tk()
top.geometry("800x600")
top.title("Age & Gender Detector")
top.configure(background="#CDCDCD")

# Defining Labels
label1=Label(top,background="#CDCDCD",font=("arial",15,"bold"))
label2=Label(top,background="#CDCDCD",font=("arial",15,"bold"))
sign_image=Label(top)

# Loading the model
from keras.models import load_model
model=load_model("Age_Gender_Detector.weights.keras")

# Definig the detect function to detect age and gender
def Detect(file_path):
    global label_packed
    image=Image.open(file_path)
    image=image.resize((48,48))
    image=np.expand_dims(image,axis=0)
    image=np.array(image)
    image=np.delete(image,0,1)
    image=np.resize(image,(48,48,3))
    print(image.shape)
    gender_f=["Male","Female"]
    image=np.array([image])/255
    pred=model.predict(image)
    age=int(np.round(pred[1][0]))
    gender=int(np.round(pred[0][0]))
    print("Predicted Age : " +str(age))
    print("predicted Gender : " + gender_f[gender])
    label1.configure(foreground="#011638",text=age)
    label2.configure(foreground="#011638",text=gender_f[gender])

# Defining the Show_detect button function
def Show_Detect_Button(file_path):
    Detect_b=Button(top,text="Detect Image",command=lambda: Detect(file_path),padx=10,pady=5)
    Detect_b.configure(background="#364156",foreground="white",font=("arial",10,"bold"))
    Detect_b.place(relx=0.79,rely=0.46)

# Uplode image function button
def uplode_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image=im
        label1.configure(text="")
        label2.configure(text="")
        Show_Detect_Button(file_path)
    except:
        pass

heading=Label(top,text="Age and Gender Detector",pady=20,font=("arial",20,"bold"))
heading.configure(background="#CDCDCD",foreground="#364156")
heading.pack()

sign_image.pack(side="bottom",expand=True)

label1.pack(side="bottom",expand=True)
label2.pack(side="bottom",expand=True)
upload=Button(top,text="Upload an Image",command=uplode_image,padx=10,pady=5)    
upload.configure(background="#364156",foreground="white",font=("arial",10,"bold"))
upload.pack(side="bottom",pady=50)

top.mainloop()