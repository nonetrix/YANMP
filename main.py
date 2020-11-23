import random, time, os, pygame
from tinytag import TinyTag

#MusicFolder = "./testfolder"
MusicFolder = "/home/nonetrix/games/music"

while True:
        SongSelected = MusicFolder + "/" + random.choice(os.listdir(MusicFolder))
        tag = TinyTag.get(SongSelected)
        pygame.mixer.init(tag.samplerate)
        pygame.mixer.music.load(SongSelected)
        pygame.mixer.music.play()
        print("now playing", SongSelected)
        time.sleep(tag.duration)
