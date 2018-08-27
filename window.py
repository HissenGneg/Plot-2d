import pygame
from colors import colorDictionary as Color


class Window:
    def __init__(self, width, height, x_interval, y_interval):
        self.width = width
        self.height = height
        self.x_interval = x_interval
        self.y_interval = y_interval
        self.x_interval_length = self.x_interval[1] - self.x_interval[0]
        self.y_interval_length = self.y_interval[1] - self.y_interval[0]
        self.scale = self.__interval_to_scale()
        self.surface = self.create_surface()

    def __interval_to_scale(self):
        scale = (self.width / self.x_interval_length, self.height / self.y_interval_length)
        return scale

    def generate_grid(self):
        # Generates grid pattern
        for x in range(self.x_interval[0], self.x_interval[1]):
            x_start = x * self.scale[0]
            y_start = x * self.scale[1]
            pygame.draw.line(self.surface, Color['blue'], (0, y_start), (self.width, y_start), 1)
            pygame.draw.line(self.surface, Color['blue'], (x_start, 0), (x_start, self.height), 1)

            if x % 2 == 0:
                # Make markings for every second line.
                pygame.draw.line(self.surface, Color['black'], (0, y_start), (5, y_start), 2)
                pygame.draw.line(self.surface, Color['black'], (x_start, self.height), (x_start, self.height - 5), 2)

    # The axis should be drawn with the help of points in the window rather than pixels
    # Then use the point_to_pixel function to draw them with pygame
    # The axis should only be drawn in the interval
    def generate_axis(self):
        # pygame.draw.line(self.surface, Color['black'], (0, 0), (0, height), 5)
        # Vertical line
        # Drawn from start to bottom of the screen
        # The x position is the same on both points
        # The first point has the y position of the end of the y_interval to pixels
        # The second point has the y position of the start of the y_interval to pixels
        vertical_start_position = (self.point_to_pixel(0), self.point_to_pixel(None, self.y_interval[1]))
        vertical_end_position = (self.point_to_pixel(0), self.point_to_pixel(None, self.y_interval[0]))
        pygame.draw.line(self.surface, Color['black'], vertical_start_position, vertical_end_position, 2)
        # print('Drawing vertical line from ' + str(vertical_start_position) + ' to ' + str(vertical_end_position))

        # pygame.draw.line(self.surface, Color['black'], (0, height), (width, height), 5)
        # Horizontal line
        # The y position is the same on both points, 0 to pixels
        # The first point has the x position of the start of the x_interval to pixels
        # The second point has the x position of the end of the x_interval to pixels
        horizontal_start_position = (self.point_to_pixel(self.x_interval[0]), self.point_to_pixel(None, 0))
        horizontal_end_position = (self.point_to_pixel(self.x_interval[1]), self.point_to_pixel(None, 0))
        pygame.draw.line(self.surface, Color['black'], horizontal_start_position, horizontal_end_position, 2)
        print('Drawing horizontal line from ' + str(horizontal_start_position) + ' to ' + str(horizontal_end_position))

    def create_surface(self):
        surface = pygame.display.set_mode((self.width, self.height))
        surface.fill(Color['white'])
        pygame.display.update()
        return surface

    def point_to_pixel(self, point_x=None, point_y=None):
        '''
        New implementation of the point to pixel function.
        Overloading functions in Python:
        https://stackoverflow.com/questions/7113032/overloaded-functions-in-python
        :param point_x: Optional
        :param point_y: Optional
        :return: If a single parameter is entered it returns a single number.
        If a point is entered as parameter the function returns a tuple.
        '''
        if point_x is None and point_y is None:
            # At least one parameter is required
            return
        elif point_x is not None and point_y is not None:
            # A point has been entered as parameter
            # pixel_x = point_x * self.scale[0]

            # The subtraction is necessary as pygame starts counting the y pixels from the top to bottom
            # The 10 was the previous hardcoded value as the y-axis was drawn from 0 to 10
            # pixel_y = (self.scale[1] * 10) - (point_y * self.scale[1])

            pixel_x = self.point_to_pixel(point_x, None)
            pixel_y = self.point_to_pixel(None, point_y)
            print('Returning pixels for point, x ' + str(pixel_x) + ' y ' + str(pixel_y))
            return pixel_x, pixel_y
        elif point_x is not None:
            # Only a x coordinate has been entered as parameter
            # You need to also consider that the x-axis might not be drawn at the left side of the screen
            # It might be drawn in the middle
            # pixel_x = x * self.scale[0]
            if point_x == 0:
                pixel_x = (self.x_interval_length / 2) * self.scale[0]
            # elif point_x > 0:
                # pixel_x = ((self.x_interval_length / 2) + point_x) * self.scale[0]
            # elif point_x < 0:
                # pixel_x = ((self.x_interval_length / 2) - point_x) * self.scale[0]
            else:
                pixel_x = ((self.x_interval_length / 2) + point_x) * self.scale[0]

            print('Returning pixel for just one x value, x ' + str(pixel_x))
            return pixel_x
        elif point_y is not None:
            # Only a y coordinate has been entered as parameter
            if point_y >= 0:
                pixel_y = (self.scale[1] * self.y_interval[1]) - (point_y * self.scale[1])
            else:
                pixel_y = (self.scale[1] * self.y_interval[1]) - (point_y * self.scale[1])

            print('Returning pixel for just one y value, y ' + str(pixel_y))
            return pixel_y
