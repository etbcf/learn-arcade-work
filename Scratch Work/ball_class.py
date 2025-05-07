import arcade


class Ball:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.change_x = 2
        self.change_y = 1
        self.size = 10
        self.color = arcade.color.RED

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Ball Example")
        self.ball = Ball()
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        self.ball.draw()

    def on_update(self, delta_time):
        self.ball.move()


if __name__ == "__main__":
    game = MyGame()
    arcade.run()
