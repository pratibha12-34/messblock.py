import easyocr
import imageio as iio
import numpy as np
import pytesseract
import nltk.data
import time
from datetime import datetime as dt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from gtts import gTTS
import os
import ffmpeg
import pyaudio
import speech_recognition as sr
import moviepy.editor as mp
from better_profanity import profanity

video = mp.VideoFileClip("geeksforgeeks.mp4")
audio_file = video.audio
audio_file.write_audiofile("geeksforgeeks.wav")
r = sr.Recognizer()
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8):
        dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16)
        print("working")
        with sr.AudioFile("geeksforgeeks.wav") as source:
            data = r.record(source)
            text = r.recognize_google(data)

        with open("C:/Users/Vivek Agrawal/OneDrive/Documents/file1.txt",'r+') as file :
            if __name__=="__main__":
                custom_badwords=['rascal','Apathetic','bastard','asshole','bitch','brother fucker','bullshit','bollocks','wanker','dickhead','nigra','damn it','hell','bloody hell','shit as','farted']
                profanity.add_censor_words(custom_badwords)
                profanity.censor(custom_badwords)
                s=profanity.censor(text)
                print(profanity.censor(s))                    
                file.write(s)
                content=file.readline()                              
                analyzer=SentimentIntensityAnalyzer()
                polarity_scores=analyzer.polarity_scores(content)
                positive_score=polarity_scores['pos']
                negative_score=polarity_scores['neg']
                compound_score=polarity_scores['compound']
                audio=gTTS(text=text_t, lang="en", slow=False)
                audio.save("geeksforgeeks.mp3")
                os.system("start geeksforgeeks.mp3")

    if compound_score>0.5:
        print("positive message")
        break
    elif compound_score< -0.5:
        print("negative message")        
        break
    else:
        print("Thanku")
