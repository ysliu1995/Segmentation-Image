import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class GUI:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Final Project")
        self.window.geometry("1200x400")
        self.Choose_btn = None
        self.Start_btn = None
        self.Suorce_img = None
        self.GroundTruth_img = None
        self.Result_img = None
        self.Suorce = None
        self.GroundTruth = None
        self.Result = None
        self.Result_pixel = None
        self.GroundTruth_pixel = None
        self.Intersection_pixel = None
        self.DC = None

    
    def LoadFile(self):
        self.window.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))
        #Source
        self.Suorce_img = cv2.imread(self.window.filename, cv2.COLOR_BGR2GRAY)
        self.Suorce_img = cv2.resize(self.Suorce_img, (256,256))
        imgtk1 = ImageTk.PhotoImage(image=Image.fromarray(self.Suorce_img)) 
        self.Source_img = tk.Label(self.window,
                                image = imgtk1,
                                width=256,
                                height=256)
        self.Source_img.place(x=40, y=80, anchor='nw')
        self.Source = tk.Label(self.window,
                        text = "Source",
                        width=15, 
                        height=2)
        self.Source.place(x=110, y=350, anchor='nw')

    def Main(self):

        self.Choose_btn = tk.Button(self.window, 
                        text='Choose the picture',      
                        width=15, 
                        height=2,
                        command=self.LoadFile)     
        self.Choose_btn.place(x=40, y=20, anchor='nw')
    

        self.Start_btn = tk.Button(self.window, 
                        text='Start',      
                        width=15, 
                        height=2)     
        self.Start_btn.place(x=180, y=20, anchor='nw')

        

        #GroundTruth
        self.GroundTruth_img = cv2.imread('Data/data01/image/image0081.png', cv2.COLOR_BGR2GRAY)
        self.GroundTruth_img = cv2.resize(self.GroundTruth_img, (256,256))
        imgtk2 = ImageTk.PhotoImage(image=Image.fromarray(self.GroundTruth_img)) 
        self.GroundTruth_lable = tk.Label(self.window,
                                image = imgtk2,
                                width=256,
                                height=256)
        self.GroundTruth_lable.place(x=320, y=80, anchor='nw')
        self.GroundTruth = tk.Label(self.window,
                        text = "GroundTruth",
                        width=15, 
                        height=2)
        self.GroundTruth.place(x=400, y=350, anchor='nw')

        #Result
        self.Result_img = cv2.imread('Data/data01/image/image0082.png', cv2.COLOR_BGR2GRAY)
        self.Result_img = cv2.resize(self.Result_img, (256,256))
        imgtk3 = ImageTk.PhotoImage(image=Image.fromarray(self.Result_img)) 
        self.Result_lable = tk.Label(self.window,
                                image = imgtk3,
                                width=256,
                                height=256)
        self.Result_lable.place(x=600, y=80, anchor='nw')
        self.Result = tk.Label(self.window,
                        text = "Result",
                        width=15, 
                        height=2)
        self.Result.place(x=680, y=350, anchor='nw')

        #report
        self.Result_pixel = tk.Label(self.window,
                        text = "Result(pixel) : ",
                        width=20, 
                        height=2,
                        anchor='e')
        self.Result_pixel.place(x=900, y=80, anchor='nw')
        self.GroundTruth_pixel = tk.Label(self.window,
                        text = "GroundTruth(pixel) : ",
                        width=20, 
                        height=2,
                        anchor='e')
        self.GroundTruth_pixel.place(x=900, y=120, anchor='nw')
        self.Intersection_pixel = tk.Label(self.window,
                        text = "Intersection(pixel) : ",
                        width=20, 
                        height=2,
                        anchor='e')
        self.Intersection_pixel.place(x=900, y=160, anchor='nw')
        self.DC = tk.Label(self.window,
                        text = "DC : ",
                        width=20, 
                        height=2,
                        anchor='e')
        self.DC.place(x=900, y=200, anchor='nw')



        self.window.mainloop()


if __name__ == '__main__':
    gui = GUI()
    gui.Main()
    