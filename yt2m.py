import os
import sys
from tkinter import *
import yt_dlp
import webbrowser
from PIL import Image, ImageTk

def resource_path(relative_path):
    base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f'{width}x{height}+{x}+{y}')

window = Tk()
window['bg'] = '#2B2D31'
window.title('Y2M')

icon_path = resource_path("appicon.ico")
try:
    window.iconbitmap(icon_path)
except Exception as e:
    print(f"Failed to set icon: {e}")

window_width = 300
window_height = 360
window.resizable(width=False, height=False)
center_window(window, window_width, window_height)

#============= Audio Function ==============#

def download_mp3(youtube_url):
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info_dict = ydl.extract_info(youtube_url, download=False)
            video_title = info_dict.get('title', 'audio')
        
        # Путь к папке Downloads
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        output_file = os.path.join(downloads_folder, f"{video_title} [audio].webm")
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_file,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])

        # Переименование файла в .mp3 (без конвертации)
        renamed_file = output_file.replace(".webm", ".mp3")
        if os.path.exists(output_file):
            os.rename(output_file, renamed_file)
            error_label.config(text="Audio was successfully saved\nin downloads folder.", font=("Lucida Console", 11))
        else:
            error_label.config(text="Failed to locate the downloaded file.", font=("Lucida Console", 11))
    except Exception as e:
        error_label.config(text=f"Error: {e}", font=("Lucida Console", 11))


def on_download():
    youtube_link = inp_entry.get()
    if youtube_link:
        download_mp3(youtube_link)
    else:
        error_label.config(text=(f"Enter the link!"), font=("Lucida Console", 12))

def info_btn():
    frame_audio.pack_forget()
    frame_info.pack(fill=BOTH, expand=True)

#=============== Audio Page ===============#

frame_audio = Frame(window, bg='#2B2D31')
frame_audio.pack(fill=BOTH, expand=True)

title = Label(frame_audio, text='YouTube2Music',
              font=("Lucida Console", 20), bg='#2B2D31', fg='white')
title.place(relx=0.5, y=30, anchor='n')

txt_entry = Label(frame_audio, text='Enter the link',
                  font=("Lucida Console", 13), bg='#2B2D31', fg='white')
txt_entry.place(relx=0.5, y=120, anchor='n')

inp_entry = Entry(frame_audio, bg='#2F3136', fg='white', relief='flat', highlightthickness=0, borderwidth=0, insertbackground='white', font=("Lucida Console", 10))
inp_entry.place(relx=0.5, y=147, anchor='n', width=182, height=30)

btn_dwlnd = Button(frame_audio, text='Download', bg='#7289DA', fg='white', relief='flat', highlightthickness=0, borderwidth=0, font=("Lucida Console", 16), command=on_download)
btn_dwlnd.place(relx=0.5, y=220, anchor='n')

btn_info = Button(frame_audio, text='info', bg='#2B2D31', fg='white', relief='flat', highlightthickness=0, borderwidth=0, font=("Lucida Console", 12), command=info_btn)
btn_info.place(relx=0.5, y=330, anchor='n')

error_label = Label(frame_audio, text='',
                    font=("Lucida Console", 12), bg='#2B2D31', fg='#a70606')
error_label.place(relx=0.5, y=280, anchor='n')

#=============== Info Functions ===============#

def back_btn():
    frame_info.pack_forget()
    frame_audio.pack(fill=BOTH, expand=True)

def github():
    webbrowser.open("https://github.com/pythonCBK/y2music/")

#=============== Info Page ===============#

frame_info = Frame(window, bg='#2B2D31')

title = Label(frame_info, text='Information',
              font=("Lucida Console", 24), bg='#2B2D31', fg='white')
title.place(relx=0.5, y=30, anchor='n')

txt_information = Label(frame_info, 
                        text='Hello! Thank you for\ndownloading Y2M! My app is\ncompletely free and open\nsource. You can find the\nsource code, more information,\nand support on my GitHub page.\nFeel free to ask anything!', 
                        font=("Lucida Console", 11), bg='#2B2D31', fg='white')
txt_information.place(relx=0.5, y=100, anchor='n')

github_image = Image.open(resource_path("github_logo.png"))
github_image = github_image.resize((160, 65), Image.LANCZOS)
github_photo = ImageTk.PhotoImage(github_image)

btn_github = Button(frame_info, image=github_photo, bg='#2B2D31', relief='flat', command=github)
btn_github.place(relx=0.5, y=230, anchor='n')

txt_upd = Label(frame_info, text='ver. 1.1', font=("Lucida Console", 11), bg='#2B2D31', fg='white')
txt_upd.place(relx=0.15, y=333, anchor='n')

txt_information = Label(frame_info, text='By CBK', font=("Lucida Console", 11), bg='#2B2D31', fg='white')
txt_information.place(relx=0.85, y=332, anchor='n')

btn_back = Button(frame_info, text='back', bg='#2B2D31', fg='white', relief='flat', highlightthickness=0, borderwidth=0, font=("Lucida Console", 13), command=back_btn)
btn_back.place(relx=0.5, y=330, anchor='n')

window.mainloop()
