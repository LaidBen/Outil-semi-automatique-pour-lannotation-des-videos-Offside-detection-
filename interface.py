# import Offside_detection
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import PIL.Image, PIL.ImageTk
import cv2

global vidpath 
class Interface:
    
    def open_file(self):
        
        self.pause = False

        self.filename = filedialog.askopenfilename(title="Select file", filetypes=(("MP4 files", "*.mp4"),
                                                                                         ("WMV files", "*.wmv"), ("AVI files", "*.avi")))
        print(self.filename)

        vidpath = self.filename

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


    def pause_video(self):
        self.pause = True    

    
    def __init__(self, app):
        self.app = app
        self.app.title("Esi-Annot")
        # self.app.attributes('-fullscreen',True)
        self.app.geometry('900x650')
        background_img = PhotoImage(file=f"assets/bg3.png")
        label1 = Label( self.app, image = background_img)
        label1.place(x = 0, y = 0)

        top_frame = Frame(self.app)
        # top_frame.grid(row=0,column=0,rowspan=2,columnspan=3,sticky=W+E+N+S)
        top_frame.pack(side=TOP, pady=5) 
        bottom_frame = Frame(app)
        # top_frame.grid(row=3,column=1,rowspan=3,columnspan=5,sticky=W+E+N+S)
        bottom_frame.pack(side=BOTTOM, pady=5)
        btbottom_frame = Frame(app)
        # top_frame.grid(row=3,column=1,rowspan=3,columnspan=5,sticky=W+E+N+S)
        btbottom_frame.pack(side=BOTTOM, pady=0)

        self.canvas = Canvas(top_frame, width=700, height=450)
        self.canvas.pack()

        # Select Button
        btn_select=Button(bottom_frame, text="Select video file", width=15, command= self.open_file)
        btn_select.pack(side=LEFT)
        # btn_select.grid(row=0, column=0) 
           
        # Play Button
        self.btn_play=Button(bottom_frame, text="Play", width=15, command=self.play_video)
        self.btn_play.pack(side=LEFT)
        # self.btn_play.grid(row=0, column=1) 
           
        #exit Button
        self.btn_end = Button(bottom_frame, text="exit",width=15, command= exit)
        self.btn_end.pack(side=LEFT)
        # self.btn_end.grid(row=0,column=2)
        
        #Scan Button
        self.btn_annot = Button(btbottom_frame, text="Annotate",width=30, command= exit)
        # self.btn_annot.pack(side=BOTTOM)
        self.btn_annot.grid(row=0,column=0)

        # start_img = PhotoImage(file=f"assets/start.png")
        # start = Button(app, image=start_img, borderwidth=0, highlightthickness=0, relief="flat")
        # start.place(x=200,y=235)
        self.delay = 15 #ms
        self.app.mainloop()
        # main(path)
#create window
Interface(Tk())