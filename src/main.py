# ===================== import ===================== #

import pygame
from tiles import TileMap
from spritesheet import Spritesheet
from player import Player

# ===================== Game ===================== #

class Game:

    '''
    bringing together all the important elements of the game
    includes the main loop through which everything runs
    '''

    def __init__(self):
        pygame.init()
        self.DISPLAY_W, self.DISPLAY_H = 1480, 270
        self.canvas = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.running = True
        self.clock = pygame.time.Clock()
        self.TARGET_FPS = 60

        self.spritesheet = Spritesheet('sprites/placeholder/spritesheet.png')
        self.player = Player()
     
        #tilemap        
        self.map = TileMap('sprites/placeholder/big_level.csv', self.spritesheet, (0,0))
        self.player.position.x, self.player.position.y = self.map.start_x, self.map.start_y
        
        #camera
        self.offset = pygame.math.Vector2()
        self.half_w = self.canvas.get_size()[0]//2
        self.half_h = self.canvas.get_size()[1]//2

    def handle_events(self):

        '''
        method to handle all event of the game (keys)
        '''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.LEFT_KEY = True
                elif event.key == pygame.K_RIGHT:
                    self.player.RIGHT_KEY = True
                elif event.key == pygame.K_SPACE:
                    self.player.jump()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.LEFT_KEY = False
                elif event.key == pygame.K_RIGHT:
                    self.player.RIGHT_KEY = False
                elif event.key == pygame.K_SPACE:
                    if self.player.is_jumping:
                        self.player.velocity.y *= .25
                        self.player.is_jumping = False
    
    def center_target_camera(self, target):
        position = Player.getcurrentposition(target)
        self.offset.x = position[0]
        self.offset.y = position[1]
    
    def update(self, dt):
        self.center_target_camera(self.player)
        self.map = TileMap('sprites/placeholder/big_level.csv', self.spritesheet, (self.offset.x + 50, 0))
        self.player.update(dt, self.map.tiles)

    def draw(self):

        '''
        rendering everything that is shown in the game 
        '''

        self.canvas.fill((0, 180, 240))
        self.map.draw_map(self.canvas)
        self.player.draw(self.canvas)
        self.window.blit(self.canvas, (0, 0))
        pygame.display.update()

    def run(self):

        '''
        game loop
        '''

        while self.running: # main loop
            dt = self.clock.tick(60) * .001 * self.TARGET_FPS         
            self.handle_events()
            self.update(dt)
            self.draw()

# ===================== run ===================== #

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
    
#TODO Do it so that the 'camera' correctly follows the player and not just halfway as it is now.
