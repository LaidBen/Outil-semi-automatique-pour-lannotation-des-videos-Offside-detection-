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
    def open_file(self):
        width, height=700, 450
         
        self.pause = False

        self.filename = filedialog.askopenfilename(title="Select file", filetypes=(("MP4 files", "*.mp4"),
                                                                                         ("WMV files", "*.wmv"), ("AVI files", "*.avi"),("MKV File", "*.mkv")))
        # print(self.filename)

        self.path = self.filename

        # Open the video file
        self.cap = cv2.VideoCapture(self.filename)
        
        # self.cap= cv2.resize(self.cap,(700,450))
        # frame = cv2.resize(frame, (800,600)) 
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

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
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame)) #.resize(700,450)
            self.canvas.create_image(0, 0, image = self.photo, anchor = NW)

        if not self.pause:
            self.app.after(self.delay, self.play_video)

    def annotate(self):
        OF.main(self.path)
    
    def __init__(self, app):
        global path 
        self.app = app
        self.app.iconbitmap("assets/icon2.ico")
        self.app.title("Esi-Annot")
        self.app.geometry('1000x675')
        self.app.resizable(False,False)
        background_img = PhotoImage(file=f"assets/bg1.png")
        label1 = Label( self.app, image = background_img)
        label1.place(x = -2, y = -5)


        bottom_frame = Frame(app)
        bottom_frame.pack(side=BOTTOM, pady=5)
        btbottom_frame = Frame(app)
        btbottom_frame.pack(side=BOTTOM, pady=5)
        top_frame = Frame(self.app)
        # top_frame.grid(row=1,column=1)#,padx=200, sticky=W + E + N + S
        top_frame.pack(side=TOP, padx=150 ,pady=100) 
        # top_frame.config(background="red")

        self.canvas = Canvas(top_frame, width=800, height=411)#
        # self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.canvas.pack()

        # Select Button
        img3 = PhotoImage(file = f"img3.png")
        btn_select= Button(image = img3,borderwidth = 0,highlightthickness = 0,command = self.open_file,relief = "flat")
        # btn_select=Button(bottom_frame, text="Select video file", width=15, command= self.open_file)
        # btn_select.pack(side=LEFT)
        btn_select.place(x=656, y=100)
        
           
        # Play Button
        self.btn_play=Button(bottom_frame, text="Play", width=15, command=self.play_video)
        img1 = PhotoImage(file = f"img1.png")
        self.btn_play= Button(image = img1,borderwidth = 0,highlightthickness = 0,command = self.play_video,relief = "flat")
        # self.btn_play.pack(side=LEFT)
        self.btn_play.place(x=350, y=610)

           
        #exit Button
        # self.btn_end = Button(bottom_frame, text="exit",width=15, command= exit)
        img2 = PhotoImage(file = f"img2.png")
        self.btn_end = Button(image = img2, borderwidth = 0, highlightthickness = 0,command = exit, relief = "flat")
        self.btn_end.place(x=505, y=610)
        
        #Scan Button
        img0 = PhotoImage(file = f"img0.png")
        # self.btn_annot = Button(btbottom_frame, text="Annotate",width=30, command=self.annotate) #exit
        self.btn_annot=Button(image = img0, borderwidth =0,highlightthickness = 0,command = self.annotate,relief = "flat")
        # self.btn_annot.pack(side=TOP)
        self.btn_annot.place(x=350, y=550)
        self.delay = 15 #ms
        self.app.mainloop()
#create window
Interface(Tk())