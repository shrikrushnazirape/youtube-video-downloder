import pytube 
link = str(input('Enter the link of video :- '))
youtube = pytube.YouTube(link)
stream = youtube.streams.first()
stream.download()
cout<<"Downloaded"