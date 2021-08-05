#imports
import arcade
from arcade.color import BLACK, GREEN, RED, SKY_BLUE, YELLOW

import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "ROCKET KIWI"
MOVEMENT_SPEED = 8
SPRITE_SCALING_BOX  = 0.1

class Kiwi(arcade.Sprite):
    def __init__(self, image):
        scaling_factor = 0.1

        super().__init__(image, scaling_factor)
    
    def update(self):
        if self.center_y > SCREEN_HEIGHT - 25:
            self.center_y = SCREEN_HEIGHT -25
        if self.center_y < 25:
            self.center_y = 25
        if self.center_x > SCREEN_WIDTH -25:
            self.center_x = SCREEN_WIDTH -25
        #if self.center_x < 25:
        #    self.center_x = 25

        self.game_over()

    def game_over(self):
        if self.center_x < -20:
            arcade.get_window().show_view(MenuScreen())


    

class MenuScreen(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show(self):
        arcade.set_background_color(RED)
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("MENU" , SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.BLACK, font_size = 50, anchor_x="center")
        arcade.draw_text("Click here to start...", SCREEN_WIDTH/2 + 10, SCREEN_HEIGHT/2 - 50, arcade.color.BLACK, font_size = 20, anchor_x="center")

    def on_mouse_press(self, x, y, button, modifiers):
        game_view = GamePlay()
        game_view.setup()
        game_view.on_draw()
        self.window.show_view(game_view)

class GamePlay(arcade.View):

    def __init__(self):
        super().__init__()
        self.player_list = None
        self.wall_list = None  
        self.kiwi_sprite = None
        self.physics_engine = None
        self.window.set_mouse_visible(False)
        self.kiwi_sprite = Kiwi('Images/kiwi_default.png')

        self.background_sprites = None

          
    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.kiwi_sprite.center_x = SCREEN_WIDTH/2
        self.kiwi_sprite.center_y = SCREEN_HEIGHT/2

        self.player_list.append(self.kiwi_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(self.kiwi_sprite, self.wall_list)

        self.background_sprites = arcade.SpriteList()

        

        # place boxes continually in sequence
        for x in range(0, 800, 100):
            wall = arcade.Sprite("images/box.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 500
            self.wall_list.append(wall)

        

            #manualy place a tree

        self.background_sprites
        wall = arcade.Sprite("Images/nikau_tree.png", 0.25)
        wall.center_x = 300
        wall.center_y = 285
        self.wall_list.append(wall)

        # place boxes at specified co-ordinates   
    ''' coordinate_list = [[400, 500],
                           [470, 500],
                           [400, 570],
                          [470, 570]]

        for coordinate in coordinate_list:
            wall = arcade.Sprite("images/box.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)'''



    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0 ,800, 200, 0, GREEN)
        arcade.draw_lrtb_rectangle_filled(550,625,250,200, BLACK)
        self.wall_list.draw()
        self.player_list.draw()
        arcade.set_background_color(SKY_BLUE)
        self.kiwi_sprite.draw()





    def on_update(self, delta_time):
        self.kiwi_sprite.update()
        self.physics_engine.update()

        for wall in self.wall_list:
            wall.center_x -= 5
            if wall.center_x < -50:
                wall.kill()
                sprites = ["images/box.png", ]
                new_wall = arcade.Sprite(random.choice(sprites), SPRITE_SCALING_BOX)
                new_wall.center_x = 850
                new_wall.center_y = random.randint(0, SCREEN_HEIGHT)
                self.wall_list.append(new_wall)

        # print(delta_time**-1)

            

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.kiwi_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.kiwi_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.kiwi_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.kiwi_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.kiwi_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.kiwi_sprite.change_x = 0

        

 

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = MenuScreen()
    window.show_view(start_view)
    arcade.run()

main()