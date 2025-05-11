"""
This program tries to draw the pyramids of Egypt.
It was taken from https://learn.arcade.academy
"""

import arcade

# Open up a window.
# Set the window title to "The Pyramids"
# Set the and dimensions (width and height)
arcade.open_window(800, 600, "The Pyramids")

# Set the background color
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw the sand
arcade.draw_lrbt_rectangle_filled(0, 800, 0, 200, arcade.csscolor.BISQUE)

# --- Draw the Pyramids ---
# left base point - left right, left base point - up down
# right base point - left right, right base point - up down
# top - left right, top - up down
arcade.draw_triangle_filled(550, 180, 700, 180, 625, 300, arcade.csscolor.GOLD)

# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
