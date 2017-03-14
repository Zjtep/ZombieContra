import pygame as pg
from GameConstants import *

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.wall
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(COLOR_BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
class Water(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.water
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(COLOR_BLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
  

        
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
         self.groups = game.all_sprites
         pg.sprite.Sprite.__init__(self, self.groups)
         self.game = game
         self.image = pg.Surface((TILESIZE, TILESIZE))
         self.image.fill(COLOR_PURPLE)
         self.rect = self.image.get_rect()
         self.vx, self.vy = 0, 0
         self.x = x * TILESIZE
         self.y = y * TILESIZE
       
    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            print"left"
            self.vx = -PLAYER_SPEED

        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED
#     diagional movmeents
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.50
            self.vy *= 0.50       
            
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.wall, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.wall, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y   

    def update(self):
        
   
#         self.get_keys()
#         self.rect.x += self.vx
#         self.rect.y += self.vy

        self.rect.x = self.x
#         self.collide_with_walls('x')
        self.rect.y = self.y
#         self.collide_with_walls('y')
                
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT