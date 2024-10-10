import tkinter
import customtkinter
from pytube import YouTube

def download_video():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link)
        video = yt_object.streams.get_highest_resolution()
        video.download()
    except:
        print("ERROR")
    print("Download Complete")

# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# create frame
root = customtkinter.CTk()
root.geometry("720x480")
root.title("Youtube Video Downloader")

# adding UI
title = customtkinter.CTkLabel(root, text="Insert a YouTube link:")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(root, width=500, height=30, textvariable=url_var)
link.pack()

download = customtkinter.CTkButton(root, text="Download", command=download_video)
download.pack(padx=10, pady=10)

# run the program
root.mainloop()


