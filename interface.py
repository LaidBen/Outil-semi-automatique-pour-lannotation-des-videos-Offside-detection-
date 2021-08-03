import Offside_detection as OF
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import PIL.Image, PIL.ImageTk
import cv2

global path
class Interface:
    path=None
    # path =".\\vid88.mp4"
    def open_file(self):
         
        self.pause = False

        self.filename = filedialog.askopenfilename(title="Select file", filetypes=(("MP4 files", "*.mp4"),
                                                                                         ("WMV files", "*.wmv"), ("AVI files", "*.avi"),("MKV File", "*.mkv")))
        # print(self.filename)

        self.path = self.filename

        # Open the video file
        self.cap = cv2.VideoCapture(self.filename)

        #frame of canvas
        # self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        # self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        # self.canvas.config(width = self.width, height = self.height)
        
    def get_frame(self):   # get only one frame

        try:

            if self.cap.isOpened():
                ret, frame = self.cap.read()
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        except:
            messagebox.showerror(title='Video file not found', message='Please select a video file.')


    def play_video(self):

        # Get a frame from the video source, and go to the next frame automatically
        ret, frame = self.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = NW)

        if not self.pause:
            self.app.after(self.delay, self.play_video)

    def annotate(self):
        OF.main(self.path)


    def pause_video(self):
        self.pause = True    

    
    def __init__(self, app):
        global path 
        self.app = app
        self.app.iconbitmap("assets/icon2.ico")
        self.app.title("Esi-Annot")
        self.app.geometry('900x650')
        background_img = PhotoImage(file=f"assets/bg3.png")
        label1 = Label( self.app, image = background_img)
        label1.place(x = 0, y = 0)

        top_frame = Frame(self.app)
        top_frame.pack(side=TOP, pady=5) 
        bottom_frame = Frame(app)
        bottom_frame.pack(side=BOTTOM, pady=5)
        btbottom_frame = Frame(app)
        btbottom_frame.pack(side=BOTTOM, pady=0)

        self.canvas = Canvas(top_frame, width=700, height=450)
        self.canvas.pack()

        # Select Button
        btn_select=Button(bottom_frame, text="Select video file", width=15, command= self.open_file)
        btn_select.pack(side=LEFT)
           
        # Play Button
        self.btn_play=Button(bottom_frame, text="Play", width=15, command=self.play_video)
        self.btn_play.pack(side=LEFT)
           
        #exit Button
        self.btn_end = Button(bottom_frame, text="exit",width=15, command= exit)
        self.btn_end.pack(side=LEFT)
        
        #Scan Button
        self.btn_annot = Button(btbottom_frame, text="Annotate",width=30, command=self.annotate) #exit
        self.btn_annot.grid(row=0,column=0)
        self.delay = 15 #ms
        self.app.mainloop()
        # main(path)
#create window
global path
Interface(Tk())