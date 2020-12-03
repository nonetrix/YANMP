import pygame.mixer, os, time, threading, curses, random
from tinytag import TinyTag

#MusicFolder = "./testfolder"
MusicFolder = "/home/nonetrix/games/music"

pause = 0

stdscr = curses.initscr()

def isPlaying(self):
        return pygame.mixer.music.get_busy()

def Keyboard(Keyboard):
        while True:
                time.sleep(1)
                
t1 = threading.Thread(target=Keyboard, args=(1,))
t1.start()

while True:
        SongSelected = MusicFolder + "/" + random.choice(os.listdir(MusicFolder))
        tag = TinyTag.get(SongSelected)
        pygame.mixer.init(frequency=tag.samplerate)
        pygame.mixer.music.load(SongSelected)
        stdscr.addstr(SongSelected)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
                time.sleep(1)
                stdscr.refresh()
                ch = stdscr.getch()
                if ch == ord('c'):
                        if pause == 1:
                            pygame.mixer.music.unpause()
                            pause = 0
                        else:
                            pygame.mixer.music.pause()
                            pause = 1
                if ch == ord('x'):
                    break
        stdscr.clear()
        pygame.mixer.quit()
