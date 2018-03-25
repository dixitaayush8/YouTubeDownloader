from apiclient.discovery import build
import unicodedata
import webbrowser
import os
import sys

DEVELOPER_KEY = 'SECRET'
youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)


def getUserFirstChoice():
    someIn = str(raw_input('[1]: Download mp3\n[2]: Download mp4\n[0] Quit\nPress 0, 1, or 2: '))
    if (someIn == '0' or someIn == '1' or someIn == '2'):
        return someIn
    else:
        while(someIn != '0' or someIn != '1' or someIn != '2'):
            if (someIn == '0' or someIn == '1' or someIn == '2'):
                return someIn
            someIn = str(raw_input('[1]: Download mp3\n[2]: Download mp4\n[0] Quit\nPress 0, 1, or 2: '))
    return someIn

def getUserSecondChoice():
    someIn = str(raw_input('[1]: Download by URL\n[2]: Download by title\n[0] Quit\nPress 0, 1, or 2: '))
    if (someIn == '0' or someIn == '1' or someIn == '2'):
        return someIn
    else:
        while(someIn != '0' or someIn != '1' or someIn != '2'):
            if (someIn == '0' or someIn == '1' or someIn == '2'):
                return someIn
            someIn = str(raw_input('[1]: Download by URL\n[2]: Download by title\n[0] Quit\nPress 0, 1, or 2: '))
    return someIn

def theTitle():
    try:
        someIn = str(raw_input('Name of the title: '))
    except:
        someIn = str(raw_input('Try again: '))
    return someIn

def theUrl():
    someIn = str(raw_input('YouTube URL Link: '))
    if(someIn.find('youtube.com/watch?v=') != -1):
        return someIn
    else:
        while(someIn.find('youtube.com/watch?v=') == -1):
            if(someIn.find('youtube.com/watch?v=') != -1):
                return someIn
            someIn = str(raw_input('YouTube URL Link: ')) 
    return someIn

def downloadAudioByTitle():
    name = theTitle()
    if (name == 'quit'):
        print 'Have a nice day!'
        sys.exit(0)
    results = youtube.search().list(q=name,part='snippet', type='video', maxResults=1).execute()
    k = ''
    for i in results['items']:
        title = i['snippet']['title']
        k = unicodedata.normalize('NFKD', i['id']['videoId']).encode('ascii','ignore')
        print type(k)
        url = 'https://www.youtube.com/watch?v=' + i['id']['videoId']
        firstCommand = 'mkdir -p Audio'
        secondCommand = 'youtube-dl --embed-thumbnail --no-warnings --extract-audio --audio-format mp3 -o "Audio/%(title)s.%(ext)s" ' + url
        os.system(firstCommand)
        os.system(secondCommand)

def downloadAudioByUrl():
    url = theUrl()
    if(url == 'quit'):
        print 'Have a nice day!'
        sys.exit(0)
    firstCommand = 'mkdir -p Audio'
    secondCommand = 'youtube-dl --embed-thumbnail --no-warnings --extract-audio --audio-format mp3 -o "Audio/%(title)s.%(ext)s" ' + url
    os.system(firstCommand)
    os.system(secondCommand)

def downloadVideoByTitle():
    name = theTitle()
    if (name == 'quit'):
        print 'Have a nice day!'
        sys.exit(0)
    results = youtube.search().list(q=name,part='snippet', type='video', maxResults=1).execute()
    k = ''
    for i in results['items']:
        title = i['snippet']['title']
        k = unicodedata.normalize('NFKD', i['id']['videoId']).encode('ascii','ignore')
        print type(k)
        url = 'https://www.youtube.com/watch?v=' + i['id']['videoId']
        firstCommand = 'mkdir -p Video'
        secondCommand = 'youtube-dl --no-warnings --format mp4 -o "Video/%(title)s.%(ext)s" ' + url
        os.system(firstCommand)
        os.system(secondCommand)

def downloadVideoByUrl():
    url = theUrl()
    if (url == 'quit'):
        print 'Have a nice day!'
        sys.exit(0)
    firstCommand = 'mkdir -p Video'
    secondCommand = 'youtube-dl --no-warnings --format mp4 -o "Video/%(title)s.%(ext)s" ' + url
    os.system(firstCommand)
    os.system(secondCommand)

def main():
    firstChoice = getUserFirstChoice()
    if (firstChoice == '0'):
        print 'Have a nice day!'
        sys.exit(0)
    elif (firstChoice == '1'):
        secondChoice = getUserSecondChoice()
        if(secondChoice == '0'):
            print 'Have a nice day!'
            sys.exit(0)
        elif(secondChoice == '1'):
            downloadAudioByUrl()
        elif(secondChoice == '2'):
            downloadAudioByTitle()
    elif (firstChoice == '2'):
        secondChoice = getUserSecondChoice()
        if(secondChoice == '0'):
            print 'Have a nice day!'
            sys.exit(0)
        elif(secondChoice == '1'):
            downloadVideoByUrl()
        elif(secondChoice == '2'):
            downloadVideoByTitle()

main()
