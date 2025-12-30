"""The module takes care of everything related to the player and their collisions"""

# ===================== import ===================== #

import threading
import pygame
from PIL import Image
from inputs import KeyInput
from tile_map import TileMap
from audio import GameSounds

# ===================== Player ===================== #

class Player(pygame.sprite.Sprite):
    """
    Class to handle the player and their attributes.
    """

    def __init__(self, images:list[pygame.Surface], death_images:list[pygame.Surface], jump_images:list[pygame.Surface]) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.__images:list[pygame.Surface] = images
        self.__image:pygame.Surface = self.__images[0]
        self.__rect:pygame.Rect = self.image.get_rect()
        # --- movement --- #
        self.__horizontal_collision_box:OffsetRect = OffsetRect((255,255,0),self)
        self.__vertical_collision_box:OffsetRect = OffsetRect((255,0,0),self)
        self.__is_on_ground:bool = False
        self.__acceleration:float = 0 # acceleration of the player (force with which the player moves)
        self.__friction:float = -.05  # deceleration to halt the player
        self.__gravity:int = 1        # mass of the player
        self.__speed:pygame.Vector2 = pygame.Vector2(0,0) # speed of the player

        # --- health --- #
        self.__hurt_map = None
        self.__health:int = 3

        # --- animation --- #
        self.__image_index_run:int = 0
        self.__run_animation_index:int = 0

        self.__jump_images:list[pygame.Surface] = jump_images
        self.__image_index_jump:int = 0
        self.__jump_animation_index:int = 0
        self.__jump_move_last_key:str = "right"


        self.__death_images:list[pygame.Surface] = death_images
        self.__image_index_death:int = 0
        self.__death_animation_index:int = 0

        self.__is_dead:bool = False

        #sounds
        self.__sound_controller:GameSounds = GameSounds("sprites/soundsAndMusic/Jump.wav")
        self.__win:bool = False

    @property
    def image(self) -> pygame.Surface:
        return self.__image

    @property
    def rect(self) -> pygame.Rect:
        return self.__rect

    @property
    def horizontal_collision_box(self):
        return self.__vertical_collision_box

    @property
    def vertical_collision_box(self):
        return self.__horizontal_collision_box

# ============== horizontal player movement ============== #

    def horizontal_movement(self, key_input: KeyInput, tile_map :TileMap) -> None:
        """
        Method to handle horizontal movement of the player.
        """

        self.__acceleration = 0

        if key_input.key_left:
            self.__acceleration -= .3
            if self.__run_animation_index == 5:
                self.run_animation("left")
                self.__run_animation_index = 0

            self.__jump_move_last_key = "left"
            self.__run_animation_index += 1

        if key_input.key_right:
            self.__acceleration += .3
            if self.__run_animation_index == 5:
                self.run_animation("right")
                self.__run_animation_index = 0

            self.__run_animation_index += 1
            self.__jump_move_last_key = "right"


        self.__speed.x += self.__acceleration               #   F = m * a  |  m = 1  -->  F = a
        self.__speed.x += self.__friction * self.__speed.x  #   a * µ = a

        if abs(self.__speed.x) < .1:
            self.__speed.x = 0

        self.max_horizontal_speed(4)
        self.horizontal_collision_check(tile_map)
        self.rect.x += self.__speed.x

    def max_horizontal_speed(self, max_speed: int) -> int:
        """
        Method to limit the speed to an input value.
        """

        if self.__speed.x < 0:
            return max(self.__speed.x, -max_speed)

        else:
            return min(self.__speed.x, max_speed)

    def horizontal_collision_check(self, tile_map:TileMap) -> None:
        """
        Method to handle horizontal collisions.
        """

        if pygame.sprite.collide_mask(self.__vertical_collision_box, tile_map):

            if self.__speed.x > 0:

                while pygame.sprite.collide_mask(self.__vertical_collision_box, tile_map):
                    self.__speed.x = -1
                    self.rect.x += self.__speed.x
                    self.collision_box_update()

                self.__speed.x = 0

            if self.__speed.x < 0:

                while pygame.sprite.collide_mask(self.__vertical_collision_box, tile_map):

                    self.__speed.x = 1
                    self.rect.x += self.__speed.x
                    self.collision_box_update()

                self.__speed.x = 0

# ============== vertical player movement ============== #

    def vertical_movement(self, key_input:KeyInput, tile_map:TileMap) -> None:
        """
        Method to handle vertical movement of the player.
        """
        #jump sound
        if key_input.key_space_pressed and self.__is_on_ground:
            #play jump sound
            self.__sound_controller.playJumpSound()
            key_input.key_space_pressed = False

        # jump
        if key_input.key_space:
            if self.__is_on_ground:
                self.__speed.y -= 8
                self.__is_on_ground = False

        # movement
        self.__speed.y += self.__gravity

        if not self.__speed.y > 0:
            #when I wrote this, only God and I understood what I was doing

            # This handles cases when both jumping and running are pressed simultaneously,
            # and when only jumping is pressed, to ensure the player faces in the correct direction
            self.__jump_animation_index +=1
            if self.__jump_animation_index == 4 :
                if key_input.key_left:
                    self.jump_animation("left")
                    self.__jump_move_last_key = "left"

                elif key_input.key_right :
                    self.jump_animation("right")
                    self.__jump_move_last_key = "right"

                elif self.__jump_move_last_key == "left":
                    self.jump_animation("left")
                    self.__jump_move_last_key = "left"

                elif self.__jump_move_last_key == "right":
                    self.jump_animation("right")
                    self.__jump_move_last_key = "right"

                self.__jump_animation_index = 0
                #now, God only knows


        if self.__speed.y > 0:
            self.__speed.y += self.__friction * self.__speed.y * 2.5

        self.vertical_collision_check(tile_map)
        self.rect.y += self.__speed.y

    def vertical_collision_check(self, tile_map:TileMap) -> None:
        """
        Method to handle vertical collisions.
        """

        if self.__is_on_ground:
            self.__speed.y = 0
            self.rect.y += self.__speed.y
            self.collision_box_update()

            if not pygame.sprite.collide_mask(self.__horizontal_collision_box, tile_map):
                self.__is_on_ground = False
            return

        if pygame.sprite.collide_mask(self.__horizontal_collision_box, tile_map):
            self.__is_on_ground = True

# ============== update ============== #

    def player_update(self, key_input:KeyInput, tile_map:TileMap, hurt_map_rect:pygame.Rect) -> None:
        """
        Method to update all player related events.
        """

        if self.__hurt_map is None:
            self.__hurt_map = hurt_map_rect

        if tile_map.rect.x <= -4300:
            self.__win = True


        if tile_map.rect.y <= -100:
            # Since the player isn't moving visibly, but rather the tilemap is,
            # the Rect position of the tilemap is simply checked against its position.
            # Then, when the position, in this case -100, is reached, the player is considered dead.
            if self.__death_animation_index == 3:
                self.death_animation()
                self.__death_animation_index = 0

            if self.__image_index_death >= len(self.__death_images):
                self.__is_dead = True

            self.__death_animation_index += 1

        #self.horizontalMovement(__keyInput, __tileMap)
        #self.verticalMovement(__keyInput, __tileMap)
        thread_horizontal_movement = threading.Thread(target=self.horizontal_movement,args=(key_input, tile_map))
        thread_vertical_movement = threading.Thread(target=self.vertical_movement, args=(key_input, tile_map))

        thread_horizontal_movement.start()
        thread_vertical_movement.start()

        thread_horizontal_movement.join()
        thread_vertical_movement.join()

        self.collision_box_update()


    def collision_box_update(self):
        """
        Method to update all collision related events.
        """
        self.__vertical_collision_box.box_update(self, self.__speed.x, -8)
        self.__horizontal_collision_box.box_update(self, 0, self.__speed.y + 3)

# ============== damage and health ============== #

    @property
    def is_dead(self) -> bool:
        return self.__is_dead

    @property
    def win(self):
        return self.__win


# ===================== Animation ===================== #

    def run_animation(self, direction:str) -> None:
        """
        run animatio of the character, diffrent direction needs difrent animations
        """
        if direction == "left" and self.__is_on_ground:
            self.__image_index_run += 1
            # This line assigns the current image to be displayed from a list of images based on the index, ensuring it loops through the images if the index exceeds the length of the list
            self.__image = self.__images[self.__image_index_run % len(self.__images)]
            #flip the player in the opposite direction when the player moves left
            self.__image = pygame.transform.flip(self.image, True, False)
        elif direction == "right" and self.__is_on_ground:
            self.__image_index_run += 1
            self.__image = self.__images[self.__image_index_run % len(self.__images)]
            self.__image = pygame.transform.flip(self.__image, False, False)

    def death_animation(self) -> None:
        """plays the death animation if the player dies"""
        self.__image_index_death += 1
        self.__image = self.__death_images[self.__image_index_death % len(self.__death_images)]

    def jump_animation(self, direction:str) -> None:
        """plays the single frames from the jump animation if the player jumps"""
        if direction == "left":
            self.__image_index_jump += 1
            self.__image = self.__jump_images[self.__image_index_jump % len(self.__jump_images)]
            self.__image = pygame.transform.flip(self.image, True, False)
        elif direction == "right":
            self.__image_index_jump += 1
            self.__image = self.__jump_images[self.__image_index_jump % len(self.__jump_images)]
            self.__image = pygame.transform.flip(self.image, False, False)

# ===================== Offsetrect ===================== #

class OffsetRect(pygame.sprite.Sprite):
    """
    Class that generates collision checkboxes for player movement, input: player.
    """

    def __init__(self, color:tuple, player: Player) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.__image:pygame.Surface = pygame.Surface((player.rect.w-20, player.rect.h), pygame.SRCALPHA)# To reduce the hitbox by 20 to ensure proper collision detection for the player despite the animations (and avoid situations like getting caught on the arms).
        self.__rect:pygame.Rect = self.__image.get_rect()
        self.__mask = pygame.mask.Mask((player.rect.w-20, player.rect.h), True)
        self.__rect.centerx, self.__rect.centery = player.rect.centerx, player.rect.centery
        self.__offset:pygame.Vector2 = pygame.Vector2(0, 0)
        #self.image.fill(color=color) #Ability to color the offset rects for debugging purposes

    @property
    def rect(self) -> pygame.Rect:
        return self.__rect

    @rect.setter
    def rect(self, rect: pygame.Rect):
        self.__rect = rect

    @property
    def image(self) -> Image:
        return self.__image

    @property
    def mask(self) -> pygame.mask.Mask:
        return self.__mask

    def set_offset(self, __x :int, __y :int) -> None:
        """
        Setter for box offset.s
        """
        self.__offset.x, self.__offset.y = __x, __y

    def update_position(self, player:Player) -> None:
        """
        Method to sync the collisionbox position to the current player position.
        """
        self.__rect.centerx, self.__rect.centery = (player.rect.centerx + self.__offset.x), (player.rect.centery + self.__offset.y)

    def box_update(self, player: Player, x: int, y :int) -> None:
        """
        Method to update all collision box attributes.
        """
        self.set_offset(x, y)
        self.update_position(player)
