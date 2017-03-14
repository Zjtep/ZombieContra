import pygame as pg
import sys
from os import path
from GameConstants import *
from Sprites import *

class Cursor_Control(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
#         self.image = pg.Surface((50, 50))
#         self.image.fill(COLOR_RED)
      
        self.image = pg.Surface((TILESIZE,TILESIZE), pg.SRCALPHA, 32)
        self.image.fill((23, 100, 255, 50))        
        
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
    def update_position(self,x,y):
#         print "wtf"
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE     
        
        
#         self.screen.blit(rect, (100,100))

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        
        pg.mouse.set_visible(0)

        

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.wall = pg.sprite.Group()
        self.water = pg.sprite.Group()
        self.mountain = pg.sprite.Group()
        self.cursor=Cursor_Control(self, 2,2)
        
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == '2':
                    Water(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                    
    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, COLOR_RED, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, COLOR_RED, (0, y), (WIDTH, y))

    def draw(self):
        
        mousePosition  = pg.mouse.get_pos()
#         print mousePosition[0]/32
#         print mousePosition[1]/32
        self.cursor.update_position(mousePosition[0]/TILESIZE,  mousePosition[1]/TILESIZE )        
        
        self.screen.fill(BACKGROUND_COLOR)
#         self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.draw_grid()
        
#         cursor_rect = pg.Surface((500,500), pg.SRCALPHA, 32)
#         cursor_rect.fill((23, 100, 255, 50))
#         self.screen.blit(cursor_rect, (100,100))
        
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
#                 if event.key == pg.K_LEFT:
#                     self.player.move(dx=-10)
#                 if event.key == pg.K_RIGHT:
#                     self.player.move(dx=10)
#                 if event.key == pg.K_UP:
#                     self.player.move(dy=-10)
#                 if event.key == pg.K_DOWN:
#                     self.player.move(dy=10)
#                     


       

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
