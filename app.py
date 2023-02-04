import pafy
import streamlit as st

st.title("YouTube to MP3 Downloader")

url = st.text_input("Enter the URL of the YouTube video:")
if url:
    try:
        video = pafy.new(url)
        audio = video.getbestaudio(preftype="m4a")
        audio.download(filepath=f"{video.title}.mp3", remux_audio=True)
        st.success("Download complete!")
    except:
        st.error("An error occurred during the download. Please try again.")
