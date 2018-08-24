import sys, pygame
pygame.init()

white = (255,255,255)
black = (0,0,0)
blue = (135,206,250)

width,height = 640,480

window = pygame.display.set_mode((width,height))
window.fill(white)
pygame.display.update()

xScale = 64
yScale = 48

#converts point to pixel location
def point_to_pixel(inputTuple):
    inputX = inputTuple[0]
    inputY = inputTuple[1]

    pointX = inputX * xScale
    pointY = (yScale * 10) - (inputY * yScale)
    return (pointX,pointY)


def generate_grid():
    #Generates grid pattern
    for i in range(10):
        xStart = i * xScale
        yStart = i * yScale
        pygame.draw.line(window,blue,(0,yStart),(width,yStart), 1)
        pygame.draw.line(window,blue,(xStart, 0),(xStart, height), 1)

        if i % 2 == 0:
            # Make markings for every second line.
            pygame.draw.line(window,black,(0,yStart), (5, yStart), 2)
            pygame.draw.line(window,black,(xStart, height),(xStart, height - 5), 2)

    pygame.draw.line(window, black, (0, 0), (0, height), 5)
    pygame.draw.line(window, black, (0, height), (width, height), 5)

#Generates the graph
def generate_graph():
    pygame.draw.lines(window, black, False, generate_pixels(), 1)

#Generates the pixels used for the pygame.draw.lines(,,,x,) argument.
def generate_pixels():
    pointList = generate_point()
    pixelList = []
    for i in range(len(pointList)):
        pixelList.append(point_to_pixel(pointList[i]))
    return(pixelList)

#Generates the points based on input function
def generate_point():
    pointList = []
    for i in range(1000):
        i = i * 0.01
        x = i
        y = (x * x)
        pointList.append((x,y))
    return(pointList)

#def parse_function():
#(not yet completed)

#Main function
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

#Boiler plate to initialize main function
if __name__ == "__main__":
    main()
