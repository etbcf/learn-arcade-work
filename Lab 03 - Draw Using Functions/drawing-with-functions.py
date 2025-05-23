#!/usr/bin/env python3

"""
In here, I will try to code the lab_02.py with functions.
"""

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_sand():
    """Draw the sand at the bottom third of the screen, it should be called after setting the background color."""
    arcade.draw_lrbt_rectangle_filled(
        0, SCREEN_WIDTH, 0, SCREEN_HEIGHT / 3, arcade.csscolor.BISQUE
    )


def draw_pyramid(x, y, scale):
    """Draw a pyramid centered at (x, y) with the given scale."""
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Right face (GOLD)
    arcade.draw_triangle_filled(
        x + 75 * scale, y + 25 * scale, x, y, x, y + 150 * scale, arcade.csscolor.GOLD
    )

    # Left face (GOLDENROD)
    arcade.draw_triangle_filled(
        x - 75 * scale,
        y + 25 * scale,
        x,
        y,
        x,
        y + 150 * scale,
        arcade.csscolor.GOLDENROD,
    )


def draw_clouds(x, y, scale):
    """Draw a cloud made of overlapping circles at position (x, y)."""

    # Main cluster of circles
    arcade.draw_circle_filled(x, y, 20 * scale, arcade.color.WHITE)
    arcade.draw_circle_filled(
        x + 25 * scale, y + 10 * scale, 20 * scale, arcade.color.WHITE
    )
    arcade.draw_circle_filled(x + 50 * scale, y, 20 * scale, arcade.color.WHITE)
    arcade.draw_circle_filled(
        x + 15 * scale, y - 10 * scale, 20 * scale, arcade.color.WHITE
    )
    arcade.draw_circle_filled(
        x + 40 * scale, y - 10 * scale, 20 * scale, arcade.color.WHITE
    )


def draw_sun(x, y, radius):
    """Draw the sun as a filled yellow circle at (x, y) with the given radius."""
    arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "The Pyramids")
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    # Start
    arcade.start_render()

    draw_sand()

    draw_sun(700, 450, 40)

    draw_clouds(200, 500, 1.0)
    draw_clouds(350, 520, 0.7)
    draw_clouds(100, 450, 1.3)

    draw_pyramid(600, 150, 0.6)  # smaller
    draw_pyramid(500, 100, 1.4)  # larger
    draw_pyramid(400, 50, 1.0)  # normal size

    # Draw a sun
    arcade.draw_circle_filled(700, 450, 40, arcade.color.YELLOW)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
