"""
This is a sample program.

Multi-line comments are surround by three double-quotes.
"""

# Import the "arcade" library

import arcade

arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color((arcade.csscolor.SKY_BLUE))

# Get ready to draw
arcade.start_render()

# Drawing code goes here
# Draw a rectangle
# Left of 0, right of 599,
# Bottom of 0, top of 300
arcade.draw_lrbt_rectangle_filled(0, 599, 0, 300, arcade.csscolor.GREEN)

# Tree trunk
# Center of 100, 320
# Width of 20
# Height of 60
arcade.draw_lrbt_rectangle_filled(90, 110, 290, 350, arcade.csscolor.SIENNA)

# Tree top
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

# Another tree, with an ellipse for the top
arcade.draw_lrbt_rectangle_filled(190, 210, 290, 355, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)

# Another tree, with a trunk and arc for the top
# Arc is centered at (300, 340) with a width of 60 and height of 100.
# The starting angle is 0, and ending angle is 180
arcade.draw_lrbt_rectangle_filled(290, 310, 290, 360, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

# Another tree, with a trunk and triangle for the top
# Triangle is made of these points
# (400, 400), (370, 320), (430, 320)
arcade.draw_lrbt_rectangle_filled(395, 405, 290, 365, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)

# Draw a tree using a polygon with a list of points
arcade.draw_lrbt_rectangle_filled(490, 510, 290, 370, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(
    ((500, 400), (480, 360), (470, 320), (530, 320), (520, 360)),
    arcade.csscolor.DARK_GREEN,
)

# Draw a sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)

# Rays to the left, right, up, and down
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)

# Diagonal rays
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

arcade.draw_text("Arbor Day - Plant a Tree!", 150, 230, arcade.color.BLACK, 24)

# Finish drawing
arcade.finish_render()

# Keep the window open
arcade.run()
