from os import getcwd,chdir
from pytube import YouTube

# change current working directory
savecwd  = getcwd()
chdir(savecwd + "/Apps/Streaming/")
newcwd = getcwd()

print(newcwd)


url = 'https://www.youtube.com/watch?v=xxhET61yB1A'


def cb_dl_progress(stream, chunk:bytes, progress: int):
    
    with open("dl.txt","wb") as file:
        file.write(stream)
    #print("Stream: ", stream)
    #print("Chunk", chunk)
    print("Progress", progress)


def cb_dl_finished(stream, path:str):
    
    print("Stream: ", stream)
    print("Path: ", path)
    print("download has finished")


def mydownload(url :str, savepath:str,cb_progress,cb_finished):
    yt = YouTube(url,cb_progress,cb_finished)
    print(yt.title)
    trackname = yt.title + ".mp4"
    print("savepath: ", savepath)
    print("trackname: ", trackname)
    # Select a stream to be downloaded
    #stream = yt.streams.get_audio_only()
    stream = yt.streams.get_by_itag(18) #  video mp4
    #stream = yt.streams.get_by_itag(140) # Audio mp4 128kbps
    stream.download(savepath, trackname)


mydownload(url,newcwd,cb_dl_progress,cb_dl_finished)

#yt = YouTube(url)
#print(yt.title)
#print(yt.thumbnail_url)

# Displays all the available streams that can be downloaded...
#print(yt.streams)
'''
15 possible streams to be downloaded.
[<Stream: itag="17" mime_type="video/3gpp" res="144p" fps="6fps" vcodec="mp4v.20.3" acodec="mp4a.40.2" progressive="True" type="video">, 
 <Stream: itag="18" mime_type="video/mp4" res="360p" fps="25fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">, 
 <Stream: itag="135" mime_type="video/mp4" res="480p" fps="25fps" vcodec="avc1.4d401e" progressive="False" type="video">, 
 <Stream: itag="244" mime_type="video/webm" res="480p" fps="25fps" vcodec="vp9" progressive="False" type="video">, 
 <Stream: itag="134" mime_type="video/mp4" res="360p" fps="25fps" vcodec="avc1.4d4015" progressive="False" type="video">, 
 <Stream: itag="243" mime_type="video/webm" res="360p" fps="25fps" vcodec="vp9" progressive="False" type="video">, 
 <Stream: itag="133" mime_type="video/mp4" res="240p" fps="25fps" vcodec="avc1.4d400d" progressive="False" type="video">, 
 <Stream: itag="242" mime_type="video/webm" res="240p" fps="25fps" vcodec="vp9" progressive="False" type="video">, 
 <Stream: itag="160" mime_type="video/mp4" res="144p" fps="25fps" vcodec="avc1.4d400b" progressive="False" type="video">, 
 <Stream: itag="278" mime_type="video/webm" res="144p" fps="25fps" vcodec="vp9" progressive="False" type="video">, 
 <Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False" type="audio">, 
 <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">, 
 <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">, 
 <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">, 
 <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">]
 '''

# Progressive Downloads ( Progressive Streams) have lowes quality but audio and video comes in one track.
# No post processing after download is needed.
#print(yt.streams.filter(progressive=True))
'''
2 progressive streams are available to be downloaded
[<Stream: itag="17" mime_type="video/3gpp" res="144p" fps="6fps" vcodec="mp4v.20.3" acodec="mp4a.40.2" progressive="True" type="video">,
 <Stream: itag="18" mime_type="video/mp4" res="360p" fps="25fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">]
'''

# DASH ( Adaptative Streams.  Audio and Video are downloaded in separate files.
# After download the must be processed by a software like FFmpeg to join them.
#print(yt.streams.filter(adaptive=True))
'''
13 Adaptative streams are available to be downloaded
[<Stream: itag="135" mime_type="video/mp4" res="480p" fps="25fps" vcodec="avc1.4d401e" progressive="False" type="video">, 
 <Stream: itag="244" mime_type="video/webm" res="480p" fps="25fps" vcodec="vp9" progressive="False" type="video">, 
 <Stream: itag="134" mime_type="video/mp4" res="360p" fps="25fps" vcodec="avc1.4d4015" progressive="False" type="video">, 
 <Stream: itag="243" mime_type="video/webm" res="360p" fps="25fps" vcodec="vp9" progressive="False" type="video">, 
 <Stream: itag="133" mime_type="video/mp4" res="240p" fps="25fps" vcodec="avc1.4d400d" progressive="False" type="video">, 
 <Stream: itag="242" mime_type="video/webm" res="240p" fps="25fps" vcodec="vp9" progressive="False" type="video">, 
 <Stream: itag="160" mime_type="video/mp4" res="144p" fps="25fps" vcodec="avc1.4d400b" progressive="False" type="video">, 
 <Stream: itag="278" mime_type="video/webm" res="144p" fps="25fps" vcodec="vp9" progressive="False" type="video">, 
 <Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False" type="audio">, 
 <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">, 
 <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">, 
 <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">, 
 <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">]
'''

# Select a stream to be downloaded
#stream = yt.streams.get_audio_only()
#stream = yt.streams.get_by_itag(18) #  video mp4
#stream = yt.streams.get_by_itag(140) # Audio mp4 128kbps

# Initiate stream download
#stream.download()

chdir(savecwd)
print(getcwd())