from tkinter import*
from PIL import Image, ImageTk

def get_prediction(idx2word, i=0, save=False):
    orig_image, image = next(iter(generator))
    image = image.to(device)
    features = encoder(image).unsqueeze(1)
    output = decoder.sample(features)
    sentence = clean_sentence(output, idx2word)

def quitfrom():
    #quit()
    screen.destroy()
    
def generate():
    caption=get_prediction(generator.dataset.vocab.idx2word, i=i)
    caption="Caption:   "+caption 
    label.config(text=caption,fg='black',bg='white',font="Helvetica 16 bold")
    label.update_idletasks()

def main(file,root):
    global filepath
    global screen
    filepath=file
    screen=Toplevel(root)
    screen.title("Image Caption Generator")
    ff1=Frame(screen,bg="grey",borderwidth=6,relief=GROOVE)
    ff1.pack(side=TOP,fill=X)
    ff2=Frame(screen,bg="grey",borderwidth=6,relief=GROOVE)
    ff2.pack(side=TOP,fill=X)
    
    global ff4
    global label 
    ff4=Frame(screen,bg="grey",borderwidth=6,relief=GROOVE)
    ff4.pack(side=TOP,fill=X)
    ff3=Frame(screen,bg="grey",borderwidth=6,relief=GROOVE)
    ff3.pack(side=TOP,fill=X)
    Label(ff1,text="Welcome to Image Caption Generator",fg="red",bg="Green",font="Helvetica 16 bold").pack()
    img=Image.open(file)
    img=img.resize((500,400))
    photo=ImageTk.PhotoImage(img)
    Label(ff2,image=photo).pack() 
    label=Label(ff4,text="Caption",fg="blue",bg="gray",font="Helvetica 16 bold")
    label.pack()
    Button(ff3,text="Generate Caption",bg="yellow",command=generate,height=2,width=40,font="Helvetica 16 bold").pack(side=LEFT)
    Button(ff3,text='Quit',bg="red",command= quitfrom,height=2,width=20,font="Helvetica 16 bold").pack()
    screen.mainloop()


#main('/home/udaram/Desktop/Image Captioning/images/image1.jpeg')