"""module that handles the main game loop and orgnize everything for the game"""
# ===================== import ===================== #

import pygame
from PIL import Image, ImageSequence
from tile_map import TileMap
from player import Player
from inputs import KeyInput

from audio import MusicController

# ===================== Main ===================== #

class Game():
    """
    Class that fuses all of the subparts together for the game to be playable.
    """

    def __init__(self, screen_resolution :pygame.Vector2, current_level :str, background_image_path :str, current_character_skin_path :str, death_image_path :str, jump_image_path :str, tiles_path:list, key_input:KeyInput) -> None:
        pygame.mixer.pre_init(44100,16,3,4096)
        pygame.init()
        self.__screen_resolution:pygame.Vector2 = screen_resolution
        self.__tile_map:TileMap = TileMap(current_level,tiles_path)
        self.__hurt_map:list = self.__tile_map.hurt_map

        images:list[pygame.Surface] = self.load_gif(current_character_skin_path)
        death_images:list[pygame.Surface] =self.load_gif(death_image_path)
        jump_imgages:list[pygame.Surface] = self.load_gif(jump_image_path)
        self.__player:Player = Player(images=images, death_images= death_images, jump_images= jump_imgages)

        self.__all_sprites = pygame.sprite.Group()
        self.__all_sprites.add(self.__tile_map)
        self.__all_sprites.add(self.__player)
        self.__all_sprites.add(self.__player.vertical_collision_box)
        self.__all_sprites.add(self.__player.horizontal_collision_box)

        self.__background:pygame.Surface = pygame.image.load(background_image_path).convert()
        self.__background = pygame.transform.scale(self.__background,(self.__screen_resolution))
        self.__key_input:KeyInput = key_input
        self.__clock = pygame.time.Clock()

        self.__win:bool = False
        self.__hard_escape:bool = False

        self.__screen:pygame.Surface

    def running(self, screen: pygame.Surface) -> None:
        """
        Method to run the game.
        """

        running = True
        music_controller = MusicController("sprites/soundsAndMusic/inGameBackgroundMusic.wav")
        music_controller.play()


        while running:
            # input update
            self.__key_input.get_input()
            # condition to end the running process
            if self.__key_input.key_escape or self.__player.is_dead:
                self.__key_input.key_escape = False
                running = False

            if self.__key_input.key_hard_escape:
                self.__hard_escape = True
                running = False

            if self.__player.win:
                self.__win = True
                running = False

            self.frame_update(self.__key_input, screen)

            self.__clock.tick(60)

        self.reset_hurt_map()
        # after the loop is done, return to main menu
        music_controller.stop()

    @property
    def win(self) -> bool:
        return self.__win

    @property
    def hard_escape(self) -> bool:
        return self.__hard_escape

    def reset_hurt_map(self) -> None:
        """
        Method to reset the hurtmap.
        """

        self.__hurt_map = None

    def draw_game_frame(self) -> None:
        """
        Method to blit the game on the screen.
        """

        # camera - calculate the offset
        # more on the left site
        player_offset_x:int = self.__screen_resolution.x // 6 - self.__player.rect.centerx
        # center
        player_offset_y:int = self.__screen_resolution.y // 2 - self.__player.rect.centery

        # camera - move all sprites in the other direction
        for sprite in self.__all_sprites:
            sprite.rect.x += player_offset_x
            sprite.rect.y += player_offset_y

        # draws the current frame on the screen
        self.__screen.blit(self.__background, (0, 0))
        self.__all_sprites.draw(self.__screen)
        #TODO UI health
        #TODO UI score
        pygame.display.flip()

    def load_gif(self, filename:str) -> list[pygame.Surface]:
        """
        Extracting the individual frames from the GIF and storing them in a list
        """
        pil_image = Image.open(filename)
        frames:list[pygame.Surface] = []
        for frame in ImageSequence.Iterator(pil_image):
            frame = frame.convert('RGBA')
            pygame_image:pygame.Surface = pygame.image.fromstring(
                frame.tobytes(), frame.size, frame.mode).convert_alpha()
            frames.append(pygame_image)
        return frames

# ============== game loop ============== #

    def frame_update(self, key_input:KeyInput, screen:pygame.Surface) -> None:
        """
        Method that lets the game update.
        """

        # runs all of Game.py main functions
        self.__screen = screen
        self.__key_input = key_input
        self.__player.player_update(self.__key_input, self.__tile_map, self.__hurt_map)
        self.__tile_map.update_tilemap_position()
        self.draw_game_frame()
