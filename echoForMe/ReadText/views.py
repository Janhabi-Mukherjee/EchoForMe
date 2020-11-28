from django.shortcuts import render

# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio
from datetime import datetime
import os 
import vlc

#web scraping libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# For time lag between Heading and Content
import time

# Create your views here.

def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

def normaltext(request):
    return render(request, 'readtext.html')

def textToAudioNormalText(request):
    print("---------------------------Processing text-----------------------------------")
    # Language in which you want to convert 
    language = 'en'
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    alldata = request.POST
    text_to_read = alldata.get("text_to_read")
    print(type(text_to_read))
    myobj = gTTS(text=text_to_read, lang=language, slow=False) 
      
    # Saving the converted audio in a mp3 file , changing file name everytime
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "/home/radhika/Desktop/hack1/django_projects/echoForMe/ReadText/AudioFiles/audio"+date_string+".mp3"
    myobj.save(filename) 
      
    # Playing the converted file
    p = vlc.MediaPlayer(filename)
    p.play()

    return render(request, 'readtext.html')

def texttoAudioNews(request):
    print("-----------------------Processing news------------------------------------")
    language = 'en'
    opts=webdriver.ChromeOptions()
    opts.headless=True
    driver = webdriver.Chrome(ChromeDriverManager().install() ,options=opts)
    # Page to access top News from TimesOfIndia
    driver.get("https://timesofindia.indiatimes.com/videos/top-videos")

    content = driver.page_source
    soup = BeautifulSoup(content,features="html.parser")

    # Finding the url for the latest news
    for a in soup.findAll('div',attrs={'class':'_3sL7K'}):
        url = a.find('a',href=True,attrs={'class':'_2tgB-'})

    headings=[] #List to store heading of the news
    contents=[] #List to store content of the news

    # Using the find url for extracting news and heading 
    driver.get(url["href"])
    content = driver.page_source
    soup = BeautifulSoup(content,features="html.parser")
    for a in soup.findAll('div',attrs={'class':'_2GHni'}):
        heading=a.find('h1')
        content=a.find('p',attrs={'class':'_159Jb'})

    myobjHeading = gTTS(text=heading.text, lang=language, slow=False)
    myobjContent = gTTS(text=content.text, lang=language, slow=False)

    date_string = datetime.now().strftime("%d%m%Y%H%M%S")

    # Saving the converted audio in mp3 format
    filename1 = "/home/radhika/Desktop/hack1/django_projects/echoForMe/ReadText/AudioFiles/heading"+date_string+".mp3"
    filename2 = "/home/radhika/Desktop/hack1/django_projects/echoForMe/ReadText/AudioFiles/content"+date_string+".mp3"
    myobjHeading.save(filename1)
    myobjContent.save(filename2)

    # For calling out the Heading Tag and Content tag
    headingMp3 = "/home/radhika/Desktop/hack1/django_projects/echoForMe/ReadText/AudioFiles/heading.mp3"
    contentMp3 = "/home/radhika/Desktop/hack1/django_projects/echoForMe/ReadText/AudioFiles/content.mp3"

    # Playing the converted file
    # Playing the title " The Heading"
    p = vlc.MediaPlayer(headingMp3)
    p.play()

    # Sleep for 2 sec
    time.sleep(2)

    # Playing the Heading Material
    p = vlc.MediaPlayer(filename1)
    p.play()

    # 8 sec time lag between heading and content 
    time.sleep(8)
    # Playing the title "Content" 
    p = vlc.MediaPlayer(contentMp3)
    p.play()

    # Sleep for 2 sec
    time.sleep(2)
    # Playing The News Material
    p = vlc.MediaPlayer(filename2)
    p.play()
    
    return render(request, 'index.html')
