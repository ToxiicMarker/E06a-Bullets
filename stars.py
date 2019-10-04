"""
Simple Snow
Based primarily on: http://arcade.academy/examples/sprite_collect_coins_move_down.html

Contributed to Python Arcade Library by Nicholas Hartunian

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.snow
"""

import sys, logging, os, random, math, open_color, arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Stars"


class Singlestar(arcade.Sprite):
    """
    Each instance of this class represents a single snowflake.
    Based on drawing filled-circles.
    """

    def __init__(self):
        super().__init__("assets/snow.png", 0.1)
        self.center_y = random.randrange(0, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(0, SCREEN_WIDTH)
        self.dx = random.randint(0,5)
        self.dy = random.randint(0,5)

    def update(self):
        #singlestar.center_y -= singlestar.speed * delta_time
        self.center_x += self.dx
        self.center_y += self.dy
        if self.center_x >= SCREEN_WIDTH:
            self.reset_pos()
        if self.center_x <= 0:
            self.reset_pos()
        if self.center_y >= SCREEN_HEIGHT:
            self.reset_pos()
        if self.center_y <= 0:
            self.reset_pos()
        self.center_x -= random.randrange(20,40)

    def reset_pos(self):
        # Reset flake to random position above screen
        self.center_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(0, SCREEN_WIDTH)


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        :param width:
        :param height:
        """
        # Calls "__init__" of parent class (arcade.Window) to setup screen
        super().__init__(width, height, title)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        # Sprite lists
        self.star_list = arcade.Sprite("assets/snow.png", 1)
       
        

    def start_starfall(self):
        """ Set up snowfall and initialize variables. """
        self.star_list = arcade.SpriteList()

        for i in range(50):
            # Create snowflake instance
            singlestar = Singlestar()
            # Add snowflake to snowflake list
            self.star_list.append(singlestar)

        # Don't show the mouse pointer
        self.set_mouse_visible(False)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command is necessary before drawing
        arcade.start_render()

        # Draw the current position of each snowflake
        self.star_list.draw()

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        self.star_list.update()



def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.start_starfall()
    arcade.run()


if __name__ == "__main__":
    main()