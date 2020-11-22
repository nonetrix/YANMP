import random, time, os, threading
from tinytag import TinyTag
from pydub import AudioSegment
from pydub.playback import play
from threading import Thread

#MusicFolder = "./testfolder"
MusicFolder = "/home/nonetrix/games/music"

class PlayerThread(Thread):
    def run(self):
        if SongSelected.endswith('.mp3'):  
            play(AudioSegment.from_mp3(SongSelected))
        if SongSelected.endswith('.wav'):  
            play(AudioSegment.from_wav(SongSelected))
        if SongSelected.endswith('.ogg'):  
            play(AudioSegment.from_ogg(SongSelected))
        else:
            print("error bad file format")
            
class PrinterTread(Thread):
    def run(self):
        while True:
            print("now playing", SongSelected)
            time.sleep(1)

t = PlayerThread(args=("SongSelected"))
t2 = PrinterTread(args=("SongSelected"))

while True:
    if t.is_alive() is False:
        SongSelected = MusicFolder + "/" + random.choice(os.listdir(MusicFolder))
        t = PlayerThread(args=("SongSelected"))
        t.start()
    if t2.is_alive() is False:
        t2 = PrinterTread(args=("SongSelected"))
        t2.start()
