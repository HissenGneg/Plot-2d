import sys
import pygame
from colors import colorDictionary as Color
from curve import Curve
from window import Window

pygame.init()

width, height = 640, 480

x_interval = (-5, 15)
y_interval = (-5, 15)

window = Window(width, height, x_interval, y_interval)


# Generates the graph
def generate_graph():
    # pygame.draw.lines(window, Color['black'], False, generate_pixels(), 1)
    first_curve = Curve(lambda x: x, Color['black'], 1)
    second_curve = Curve(lambda x: x ** 2, Color['red'], 1)
    third_curve = Curve(lambda x: 4 * (x ** 3) + 3 * (x ** 2) + 2 * x + 1, Color['green'], 1)
    window.draw_curve(first_curve)
    window.draw_curve(second_curve)
    window.draw_curve(third_curve)


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
        window.generate_grid()
        window.generate_axis()
        window.generate_number_lines()
        # print(window.new_point_to_pixel(10, None))
        # print(window.new_point_to_pixel(None, 0))
        generate_graph()
        pygame.display.update()

        # Makes sure the program doesn't crash when quitting
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit(0)


main()
