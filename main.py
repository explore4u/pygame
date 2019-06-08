#-*-coding:utf8;-*-
#qpy:pygame

import sys, os
import pygame
import random
from pygame.locals import *
	
cwd = os.getcwd()
asset_root = os.path.join(cwd, "assets")

pygame.init()
# Resolution is ignored on Android
surface = pygame.display.set_mode((640, 700))
# Only one built in font is available on Android
clock = pygame.time.Clock()
info = pygame.display.Info()
w, h = info.current_w, info.current_h

if not w or not h:
    sys.exit()    

def get_x(per):
    info = pygame.display.Info()
    w = info.current_w
    w = float(w)
    x = float(per)
    return (x/100)*w
    
def get_y(per):
    info = pygame.display.Info()
    h = info.current_h
    h = float (h)
    y = float(per)
    return (y/100)*h

class Player(pygame.sprite.Sprite):
    def __init__(self, *arg, **kwargs):
        super(Player, self).__init__(*arg, **kwargs)
        self.x = get_x(50)
        self.y = get_y(5)
        self.width = 50
        self.height = 28
        # self.surf = pygame.Surface((self.width, self.height))
        self.surf = pygame.image.load(os.path.join(asset_root, "tanks_tankGrey_body2.png"))
        self.surf = pygame.transform.scale(self.surf, (self.width, self.height))
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x, self.y)
        self.parent = None
        self.score = 0
        self.alive = True
        
    def render(self):
        if self.parent is not None:
            # self.surf.fill((25, 25, 25))
            self.parent.blit(self.surf, self.rect)
            
    def set_parent(self, parent):
        self.parent = parent
        
    def set_position(self, x=0, y=0):
        self.x = x
        self.y = y
        # self.surf = pygame.Surface((self.width, self.height))
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x, self.y)
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.x = get_x(random.choice(range(1, 100)))
        self.y = get_y(90)
        self.width = 20
        self.height = 20
        self.surf = pygame.image.load(random.choice( [
        	                                        os.path.join(asset_root, "tank_bullet3.png"), 
        	                                        os.path.join(asset_root, "tank_bullet4.png")
        	                            ]))
        self.surf = pygame.transform.scale(self.surf, (self.width, self.height))
        self.surf = pygame.transform.rotate(self.surf, 90)
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x, self.y)
        self.vel = 1
        self.reproduced = False
        r = random.choice(range(20, 200))
        g = random.choice(range(20, 200))
        b = random.choice(range(20, 200))
        self.color = (r, g, b)
        
    def render(self):
        if self.parent is not None:
            self.fire()
            # self.surf.fill(self.color)
            self.parent.blit(self.surf, self.rect)
            
    def set_parent(self, parent):
        self.parent = parent
        
    def set_position(self, x=0, y=0):
        self.x = x
        self.y = y
        self.surf = pygame.Surface((self.width, self.height))
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x, self.y)
        
    def fire(self):
        self.y -= self.vel
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x, self.y)
        
    def reproduce (self):
        if not self.reproduced:
            e = Enemy ()
            e.set_parent(self.parent)
            self.reproduced = True
            return e
        else:
            return None


p = Player ()
p.set_parent(surface)

e = Enemy ()
e.set_parent(surface)

enemies = pygame.sprite.Group()
enemies.add(e)


bg = random.choice([
	            pygame.image.load(os.path.join(asset_root, "BG.png")),
	            pygame.image.load(os.path.join(asset_root, "BG1.png")),
	            pygame.image.load(os.path.join(asset_root, "BG2.png"))

	            ])
bg = pygame.transform.scale(bg, (w, h))


def restart_game():
    globals()
    p.score = 0
    enemies.empty()
    p.alive = True
    # ...
    e = Enemy ()
    e.set_parent(surface)
    enemies.add(e)
        
def handle_event(event):
    globals()
    if event.type == MOUSEMOTION:
        if p.alive:
            p.set_position(event.pos[0], p.y)
    if event.type == MOUSEBUTTONDOWN:
        if not p.alive:
            restart_game()

def render():
    """render objects to screen"""
    globals()
    p.render()
    if p.alive:
        for enemy in enemies:
            enemy.render()
            if enemy.y < 0:
                enemy.kill()
    if pygame.sprite.spritecollide(p, enemies, False):
        p.alive = False
        sr_b.set_score("%i : you died. tap the screen to continue" %p.score)
                
def loop():
    globals()


while True:
    loop()
    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
        handle_event(ev)
    # Framelimiter
    clock.tick(80)
    surface.fill((255, 255, 255))
    surface.blit(bg, (0, 0))
    render()
    pygame.display.flip()
