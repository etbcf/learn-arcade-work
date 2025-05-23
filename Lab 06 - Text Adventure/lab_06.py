import arcade

def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rect_filled(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rect_filled(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rect_filled(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rect_filled(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rect_filled(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rect_filled(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rect_filled(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rect_filled(1050, 450, 300, 300, arcade.color.BLACK)

def draw_section_1():
    for row in range(30):
        for column in range(30):
            x = 0  # Instead of zero, calculate the proper x location using 'column'
            y = 0  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rect_filled(x, y, 5, 5, arcade.color.WHITE)


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()

    arcade.finish_render()

    arcade.run()


main()
