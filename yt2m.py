import os
from tkinter import *
import yt_dlp
import webbrowser
import sys
import threading

# Window
window = Tk()
window['bg'] = '#2B2D31'
window.title('Y2M')

# Icon
if hasattr(sys, '_MEIPASS'):
    icon_path = os.path.join(sys._MEIPASS, 'appicon.ico')
else:
    icon_path = "C:\\......\\yt2m 1.2\\appicon.ico" # <------------ Your path here

window.iconbitmap(icon_path)

# Window location
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f'{width}x{height}+{x}+{y}')

window_width = 280
window_height = 370
window.resizable(width=False, height=False)
center_window(window, window_width, window_height)

# Variables
format_choice = StringVar(value="audio")



# -------- Functions -------- #

# Open gitHub Page Function
def github():
    webbrowser.open("https://github.com/pythonCBK/y2music/")

# Back Button Function
def back_btn():
    error_label.config(text="")
    frame_info.pack_forget()
    frame_main.pack(fill=BOTH, expand=True)

# Info Button Function
def info_btn():
    frame_main.pack_forget()
    frame_info.pack(fill=BOTH, expand=True)

# Download function
def download():
    error_label.config(text="Please wait...")
    url = inp_entry.get()
    if not url:
        error_label.config(text="Enter the link!")
        return
    
    download_thread = threading.Thread(target=download_file, args=(url,))
    download_thread.start()

def download_file(url):
    format_choice_value = format_choice.get()

    if format_choice_value == "audio":
        ydl_opts = {
            'format': 'bestaudio/best',  
            'outtmpl': os.path.join(os.path.expanduser('~/Downloads'), '%(title)s.%(ext)s'),  
        }
    else: 
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  
            'outtmpl': os.path.join(os.path.expanduser('~/Downloads'), '%(title)s.%(ext)s'),
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        error_label.config(text="File was successfully saved\nin downloads folder.")
    except Exception as e:
        error_label.config(text=f"Error: {str(e)}")

def pink_mode(event=None):
    error_label.config(text="You found me :3\nPink mode acivated!", fg='#f869d2')
    btn_download.config(bg="#eb90d6")
    btn_github.config(fg="#eb90d6")

window.bind("<Control-Shift-C>", pink_mode)


# -------- Main Page -------- #

frame_main = Frame(window, bg='#2B2D31')
frame_main.pack(fill=BOTH, expand=True)

# ----- Up ----- #

# Title Back
fr_back = Frame(frame_main, bg='#26272b', width=300, height=60)
fr_back.place(relx=0.5, y=26, anchor='center')

# Title
title = Label(frame_main, text='YouTube2Music',
              font=("Lucida Console", 20, "bold"), bg='#26272b', fg='white')
title.place(relx=0.5, y=15, anchor='n')

# ----- Input Field ----- #

# Clean Function
def clean_entry():
    inp_entry.delete(0, 'end')

# Enter The Link Text
txt_entry = Label(frame_main, text='Enter the link',
                  font=("Lucida Console", 17), bg='#2B2D31', fg='white')
txt_entry.place(relx=0.5, y=85, anchor='n')

# Entry Field
inp_entry = Entry(frame_main, bg='#2F3136', fg='white', relief='flat',
                  highlightthickness=0, borderwidth=0, insertbackground='white',
                  font=("Lucida Console", 12))
inp_entry.place(relx=0.45, y=130, anchor='n', width=210, height=30)

# Clean Button
btn_clean = Button(frame_main, text='←', bg='#26272b', fg='white',
                   relief='flat', highlightthickness=0, borderwidth=0, font=("Lucida Console", 16), command=clean_entry)
btn_clean.place(relx=0.85, y=130, anchor='n', width=30, height=30)

# ----- Format Choise ----- #

# Audio Choice
audio_button = Radiobutton(window, text="Audio",
                           bg='#2B2D31', fg='white', relief='flat', highlightthickness=0,
                           borderwidth=0, font=("Lucida Console", 13), variable=format_choice, value="audio", selectcolor='#26272b')
audio_button.place(relx=0.32, y=180, anchor='n')

# Video Choice
video_button = Radiobutton(window, text="Video",
                           bg='#2B2D31', fg='white', relief='flat', highlightthickness=0,
                           borderwidth=0, font=("Lucida Console", 13), variable=format_choice, value="video", selectcolor='#26272b')
video_button.place(relx=0.68, y=180, anchor='n')

# ----- Down ----- #

# Download Button
btn_download = Button(frame_main, text='Download', bg='#7289DA', fg='white', relief='flat', highlightthickness=0, borderwidth=0, font=("Lucida Console", 16), command=download)
btn_download.place(relx=0.5, y=225, anchor='n')

# Error Label
error_label = Label(frame_main, text='',
                    font=("Lucida Console", 11), bg='#2B2D31', fg='#a70606')
error_label.place(relx=0.5, y=280, anchor='n')

# Info Button
btn_info = Button(frame_main, text='info', bg='#2B2D31', fg='white', relief='flat', highlightthickness=0, borderwidth=0, font=("Lucida Console", 12), command=info_btn)
btn_info.place(relx=0.5, y=345, anchor='n')



# -------- Info Page -------- #

frame_info = Frame(window, bg='#2B2D31')

# ----- Up ----- #

# Title Back
fr_back2 = Frame(frame_info, bg='#26272b', width=300, height=60)
fr_back2.place(relx=0.5, y=26, anchor='center') # Центрирование Frame по горизонтали

# Title
title_info = Label(frame_info, text='Information',
              font=("Lucida Console", 20, "bold"), bg='#26272b', fg='white')
title_info.place(relx=0.5, y=15, anchor='n')

# Info Text
txt_information = Label(frame_info, 
                        text='Hello! Thank you for\ndownloading Y2M! My app is\ncompletely free and open\nsource. You can find the\nsource code, more\ninformation, and support\non my GitHub page.\nFeel free to ask anything!', 
                        font=("Lucida Console", 12), bg='#2B2D31', fg='white')
txt_information.place(relx=0.5, y=90, anchor='n')

# GitHub Button
btn_github = Button(frame_info, text='GitHub', bg='#2B2D31', fg='white', relief='flat', highlightthickness=0, borderwidth=0, font=("Calibri", 45, "bold"), command=github)
btn_github.place(relx=0.5, y=255, anchor='n', width=180, height=50)

# Back Button
btn_back = Button(frame_info, text='back', bg='#2B2D31', fg='white', relief='flat', highlightthickness=0, borderwidth=0, font=("Lucida Console", 12), command=back_btn)
btn_back.place(relx=0.5, y=345, anchor='n')

# Version
txt_ver = Label(frame_info, text='ver. 1.2', font=("Lucida Console", 11), bg='#2B2D31', fg='white')
txt_ver.place(relx=0.17, y=345, anchor='n')

# Author
txt_author = Label(frame_info, text='by CBK', font=("Lucida Console", 11), bg='#2B2D31', fg='white')
txt_author.place(relx=0.85, y=345, anchor='n')




window.mainloop()
