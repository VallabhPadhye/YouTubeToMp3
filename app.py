import youtube_dl
import streamlit as st

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

st.title("YouTube to MP3 Downloader")

url = st.text_input("Enter the URL of the YouTube video:")
if url:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            st.success("Download complete!")
        except:
            st.error("An error occurred during the download. Please try again.")
