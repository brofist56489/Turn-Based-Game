import pygame
import pygame.gfxdraw
from pygame.locals import *

import threading, time

WIDTH = 640
HEIGHT = int(WIDTH * 3 / 4)
TITLE = "Turn Based"

class Game():
    def __init__(self):
        self.__init_video()
        return
    
    def __init_video(self):
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT), HWSURFACE | DOUBLEBUF | RLEACCEL)
        pygame.display.set_caption(TITLE)
        return

    def tick(self):
        return
    
    def render(self):
        self.display.fill((0, 0, 0))

        pygame.gfxdraw.filled_circle(self.display, int(WIDTH / 2), int(HEIGHT / 2), int(WIDTH / 2), (255, 0, 0))

        pygame.display.flip()
        return
    
    def run(self):
        
        running = True
        lt = round(time.time() * 1000)
        ltr = lt
        delta = 0.0
        msPt = 1000.0/60.0
        ticks = frames = 0
        
        while(running):
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    running = False

            now = round(time.time() * 1000)
            delta += (now - lt) / msPt
            lt = now
            
            while(delta >= 1):
                self.tick()
                ticks += 1
                delta -= 1

            self.render()
            frames += 1

            ct = round(time.time() * 1000)
            if(ct - ltr >= 1000):
                ltr += 1000
                print(ticks, "tps,", frames, "fps")
                ticks = frames = 0

            if not running:
                pygame.quit()
        return