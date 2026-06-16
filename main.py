import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()

    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return

    try:
        yt = YouTube(url)

        title_label.config(text=f"Title: {yt.title}")

        save_path = filedialog.askdirectory()

        if save_path:
            stream = yt.streams.get_highest_resolution()
            stream.download(save_path)

            messagebox.showinfo(
                "Success",
                "Video Downloaded Successfully!"
            )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )

root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("600x350")

heading = tk.Label(
    root,
    text="YouTube Video Downloader",
    font=("Arial",18,"bold")
)
heading.pack(pady=20)

url_entry = tk.Entry(root,width=60)
url_entry.pack(pady=10)

download_btn = tk.Button(
    root,
    text="Download Video",
    command=download_video,
    width=20,
    bg="blue",
    fg="white"
)
download_btn.pack(pady=15)

title_label = tk.Label(root,text="")
title_label.pack()

root.mainloop()