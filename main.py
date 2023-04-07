# Bud P. L. Patterson M. B.
# Autism Terminal
# April 3rd, 2023
import random

import arcade
from pyglet.math import Vec2
import os, sys

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)


WIDTH = 800
HEIGHT = 800
TITLE = "Autism Game"


codex = [
    # https://www.cdc.gov/ncbddd/autism/hcp-dsm.html
    """
    Autism according to the DSM 5 is defined by:
        Issues with social skills and communication,
        Trouble with social interaction, and body language
        Difficultys with understanding social norms
    """,
    # https://en.wikipedia.org/wiki/Causes_of_autism
    """
    Causes:
        Autism is a developmental disorder and the causes of it are not fully known,
        There is research that indicates that Autism may be hereditary
    """,
    # https://www.cdc.gov/ncbddd/autism/data.html
    """
    Prevalence:
        According to the CDC, about 1 in 36 children have Autism
    """,
    # https://en.wikipedia.org/wiki/Autism_spectrum#Management ; https://www.nichd.nih.gov/health/topics/autism/conditioninfo/treatments
    """
    Management:
        There is no cure nor treatment for Autism, however therpy and interventions can help and are suggested by the National Institute of Health
    """
]


class Autism_Creature(arcade.Sprite):

    def __init__(self):
        super(Autism_Creature, self).__init__(filename="creature.png", scale=.2)

    def on_update(self, delta_time: float = 1 / 60):
        pass



# class Autism_Tank(arcade.Sprite):
#     def __init__(self, filename: str, tint: tuple[int, int, int] = None):
#         super().__init__(filename=filename, scale=.2)
#         if tint:
#             self.color = tint
#
#     def on_update(self, delta_time: float = 1 / 60):
#         pass




class Window(arcade.Window):

    def __init__(self):
        super().__init__(width=WIDTH, height=HEIGHT, title=TITLE, resizable=True)

        #self.Creature = Autism_Creature()
        self.Creature = Autism_Creature()

        self.W = False
        self.S = False
        self.D = False
        self.A = False
        self.SPEED = 5

        self.CAM_GUI = arcade.Camera()
        self.CAM_SPRITES = arcade.Camera()
        self.CAMSPEED = .5

        self.GUI_text_objects = []

        # self.GUI_text_objects.append(
        #     #arcade.Text("Test", 0, 0, color=arcade.color.WHITE)
        # )

        self.pos_text = arcade.Text("", 0, 0, color=arcade.color.WHITE)

        self.WORLD_text_objects = [
            arcade.Text(
                "AUTISM", 0, 250, color=arcade.color.GRAY, font_size=120, font_name="Times New Roman", anchor_x="center"
            ),
            arcade.Text(
                codex[0], -20, 600, color=arcade.color.WHITE, anchor_x="right", multiline=True, width=500
            ),
            arcade.Text(
                codex[1], 20, 800, color=arcade.color.WHITE, anchor_x="left", multiline=True, width=500
            ),
            arcade.Text(
                codex[2], -20, 1000, color=arcade.color.WHITE, anchor_x="right", multiline=True, width=500
            ),
            arcade.Text(
                codex[3], 20, 1200, color=arcade.color.WHITE, anchor_x="left", multiline=True, width=500
            ),

        ]




        self.shapes = arcade.ShapeElementList()

        self.shapes.append(
            arcade.create_line(0, 400, 0, 1200, arcade.color.GOLD, line_width=5)
        )





    def on_draw(self):
        self.clear()


        self.CAM_SPRITES.use()
        for line in self.WORLD_text_objects:
            line.draw()
        self.shapes.draw()
        self.Creature.draw()

        self.CAM_GUI.use()
        self.pos_text.draw()

        #Test




    def on_update(self, delta_time: float):
        if self.W:
            self.Creature.center_y += self.SPEED
        if self.S:
            self.Creature.center_y -= self.SPEED
        if self.D:
            self.Creature.center_x += self.SPEED
        if self.A:
            self.Creature.center_x -= self.SPEED

        self.scroll_to_player()
        self.pos_text.text = f"{self.Creature.center_x}, {self.Creature.center_y}"


    def scroll_to_player(self):
        position = Vec2(self.Creature.center_x - self.width / 2,
                        self.Creature.center_y - self.height / 2)
        self.CAM_SPRITES.move_to(position, self.CAMSPEED)


    def on_resize(self, width, height):
        self.CAM_SPRITES.resize(int(width), int(height))
        self.CAM_GUI.resize(int(width), int(height))
        super().on_resize(width, height)


    def on_key_press(self, symbol: int, modifiers: int):

        if symbol == arcade.key.W:
            self.W = True
        if symbol == arcade.key.A:
            self.A = True
        if symbol == arcade.key.D:
            self.D = True
        if symbol == arcade.key.S:
            self.S = True





    def on_key_release(self, symbol: int, modifiers: int):

        if symbol == arcade.key.W:
            self.W = False
        if symbol == arcade.key.A:
            self.A = False
        if symbol == arcade.key.D:
            self.D = False
        if symbol == arcade.key.S:
            self.S = False





game = Window()


game.run()







