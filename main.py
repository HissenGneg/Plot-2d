import sys, pygame
from colors import colorDictionary as Color
from curve import Curve

pygame.init()

width,height = 640, 480

window = pygame.display.set_mode((width, height))
window.fill(Color['white'])
pygame.display.update()

xScale = 64
yScale = 48
# xStart = 0
# xEnd = 10
# yStart = 0
# yEnd = 10

# def interval_to_scale():

# converts point to pixel location
def point_to_pixel(inputTuple):
    inputX = inputTuple[0]
    inputY = inputTuple[1]

    pointX = inputX * xScale
    pointY = (yScale * 10) - (inputY * yScale)
    return pointX, pointY


def generate_grid():
    # Generates grid pattern
    for i in range(10):
        xStart = i * xScale
        yStart = i * yScale
        pygame.draw.line(window, Color['blue'], (0,yStart), (width,yStart), 1)
        pygame.draw.line(window, Color['blue'], (xStart, 0), (xStart, height), 1)

        if i % 2 == 0:
            # Make markings for every second line.
            pygame.draw.line(window, Color['black'], (0,yStart), (5, yStart), 2)
            pygame.draw.line(window, Color['black'], (xStart, height), (xStart, height - 5), 2)

    pygame.draw.line(window, Color['black'], (0, 0), (0, height), 5)
    pygame.draw.line(window, Color['black'], (0, height), (width, height), 5)


# Generates the graph
def generate_graph():
    # pygame.draw.lines(window, Color['black'], False, generate_pixels(), 1)
    first_curve = Curve(lambda x: x + 1, Color['black'], 1)
    first_curve.draw(window)


# Generates the pixels used for the pygame.draw.lines(,,,x,) argument.
def generate_pixels():
    pointList = generate_point()
    pixelList = []
    for i in range(len(pointList)):
        pixelList.append(point_to_pixel(pointList[i]))
    return(pixelList)


# Generates the points based on input function
def generate_point():
    pointList = []
    for i in range(1000):
        i = i * 0.01
        x = i
        y = (x * x)
        pointList.append((x,y))
    return(pointList)


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
        #PLEASE LEAVE THIS CODE!!!
        generate_grid()
        generate_graph()
        pygame.display.update()

        #Makes sure the program does not crash
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit(0)


main()
