from pytube import YouTube
link="https://youtu.be/_NbT1VuD5n8"
yt_1=YouTube(link)

#print(yt_1.title)
#print(yt_1.thumbnail_url)

videos=yt_1.streams.all()
vid =list(enumerate(videos))
for i in vid:
    print(i)
print()
strm=int(input("enter: "))
videos[strm].download()
print("succesfully download")
