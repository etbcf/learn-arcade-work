"""
Drawing exercise...
"""

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_ground():
    """Draw the ground."""
    arcade.draw_lrbt_rectangle_filled(
        0, SCREEN_WIDTH, 0, SCREEN_HEIGHT / 3, arcade.color.AIR_SUPERIORITY_BLUE
    )


def draw_snow_person(x, y):
    """Draw a snow person."""
    arcade.draw_circle_filled(x, 140 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 220 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 280 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, 290 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 290 + y, 5, arcade.color.BLACK)


class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Snow Person")
        arcade.set_background_color(arcade.color.DARK_BLUE)

    def on_draw(self):
        """Draw everything."""
        self.clear()

        draw_ground()
        draw_snow_person(150, 140)
        draw_snow_person(450, 180)


def main():
    game = Game()
    arcade.run()


# Call the main function to get the program started.
main()
