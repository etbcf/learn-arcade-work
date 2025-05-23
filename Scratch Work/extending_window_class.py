#!/usr/bin/env python3

from dataclasses import dataclass

import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


@dataclass
class Vector2:
    x: int
    y: int


class Ball:
    def __init__(
        self,
        position: Vector2,
        velocity: Vector2,
        radius: float,
        color: tuple[int, int, int, int],
    ) -> None:
        """Constructor."""
        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position.x
        self.position_y = position.y
        self.change_x = velocity.x
        self.change_y = velocity.y
        self.radius = radius
        self.color = color

    def draw(self) -> None:
        """Draw the balls with the instance variables we have."""
        arcade.draw_circle_filled(
            self.position_x,
            self.position_y,
            self.radius,
            self.color,
        )

    def on_update(self) -> None:
        """Code to control the ball's movement."""
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1


class MyGame(arcade.Window):
    """My window class."""

    def __init__(self, width: int, height: int, title: str) -> None:
        """Constructor."""
        # Call the parent class's init function
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create a list for the balls
        self.ball_list = []

        # Add three balls to the list

        # Create our ball
        self.ball = Ball(Vector2(50, 50), Vector2(3, 3), 15, arcade.color.AUBURN)
        self.ball_list.append(self.ball)

        self.ball = Ball(
            Vector2(100, 150),
            Vector2(2, 3),
            15,
            arcade.color.PURPLE_MOUNTAIN_MAJESTY,
        )
        self.ball_list.append(self.ball)

        self.ball = Ball(
            Vector2(150, 250),
            Vector2(-3, -1),
            15,
            arcade.color.FOREST_GREEN,
        )
        self.ball_list.append(self.ball)

    def on_draw(self) -> None:
        """Called whenever we need to draw the window."""
        self.clear()

        # Use a "for" loop to pull each ball from the list, then call the draw
        # method on the ball.
        for ball in self.ball_list:
            ball.draw()

    def on_update(self, delta_time) -> None:
        """Called to update our objects. Happens approximately 60 times per second."""
        # Use a "for" loop to pull each ball from the list, then call the update
        # method on the ball.
        for ball in self.ball_list:
            ball.on_update()


def main() -> None:
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    arcade.run()


main()
