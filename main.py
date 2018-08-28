import sys
import pygame
from colors import colorDictionary as Color
from curve import Curve
from window import Window

pygame.init()

width, height = 640, 480

# xStart = 0
# xEnd = 20
# yStart = 0
# yEnd = 20
x_interval = (-3, 10)
y_interval = (-3, 10)

window = Window(width, height, x_interval, y_interval)


# Generates the graph
def generate_graph():
    # pygame.draw.lines(window, Color['black'], False, generate_pixels(), 1)
    first_curve = Curve(lambda x: x, Color['black'], 1)
    first_curve.draw(window)


# Generates the points based on input function
def generate_point():
    point_list = []
    for i in range(1000):
        i = i * 0.01
        x = i
        y = (x * x)
        point_list.append((x, y))
    return point_list


def parse_function(string_input):
    # Assuming string_input is a math function with one variable, x
    # 'eval()' interprets a string like actual code
    # https://stackoverflow.com/questions/40828921/parsing-a-string-input-into-a-lambda-function-python
    # https://stackoverflow.com/questions/9383740/what-does-pythons-eval-do
    # Lambda functions are useful when writing small anonymous functions
    # They're come in handy when writing math expressions as writing math
    # like a normal function wouldn't make much sense
    # https://www.w3schools.com/python/python_lambda.asp
    math_function = lambda x: eval(string_input)
    return math_function


# Main function
def main():
    while True:
        # generate_grid()
        # generate_axis()
        window.generate_grid()
        window.generate_axis()
        # print(window.new_point_to_pixel(10, None))
        # print(window.new_point_to_pixel(None, 0))
        # generate_graph()
        pygame.display.update()

        # Makes sure the program doesn't crash when quitting
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit(0)


main()
