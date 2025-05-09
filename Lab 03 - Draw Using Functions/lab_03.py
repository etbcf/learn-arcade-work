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

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)


snow_person1_x = {"x": 150}


def on_draw(delta_time):
    """Draw everything."""
    arcade.get_window().clear()

    draw_ground()
    # draw_snow_person(on_draw.snow_person1_x, 140)
    draw_snow_person(snow_person1_x["x"], 140)
    draw_snow_person(450, 180)

    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.
    # on_draw.snow_person1_x += 1
    snow_person1_x["x"] += 1


# on_draw.snow_person1_x = 150


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    # arcade.start_render()

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1 / 60)

    # Finish and run
    # arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
