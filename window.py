import pygame
from colors import colorDictionary as Color


class Window:
    def __init__(self, width, height, x_interval, y_interval):
        self.width = width
        self.height = height
        self.x_interval = x_interval
        self.y_interval = y_interval
        print('Assigned intervals, x {} and y {}'.format(x_interval, y_interval))
        self.x_interval_length = self.x_interval[1] - self.x_interval[0]
        self.y_interval_length = self.y_interval[1] - self.y_interval[0]
        self.scale = self.__interval_to_scale()
        self.surface = self.create_surface()

    def __interval_to_scale(self):
        scale = (self.width / self.x_interval_length, self.height / self.y_interval_length)
        print('Generated scale {}'.format(scale))
        return scale

    def generate_grid(self):
        # Generates grid pattern
        # Generate vertical grid lines
        for x in range(self.x_interval[0], self.x_interval[1]):
            # Start drawing the lines from the top to bottom since pygame starts counting from the top left corner
            pygame.draw.line(
                self.surface,
                Color['blue'],
                self.new_point_to_pixel(x, self.y_interval[1]),
                self.new_point_to_pixel(x, self.y_interval[0]),
                1,
            )

        # Generate horizontal grid lines
        for y in range(self.y_interval[0], self.y_interval[1]):
            pygame.draw.line(
                self.surface,
                Color['blue'],
                self.new_point_to_pixel(self.x_interval[0], y),
                self.new_point_to_pixel(self.x_interval[1], y),
                1,
            )

    def generate_number_lines(self, line_height=0.5, line_width=3):
        line_height_for_one_side = (line_height / 2)
        # Generates the a line for all even x points
        for x in range(self.x_interval[0], self.x_interval[1]):
            if x % 2 == 0:
                pygame.draw.line(
                    self.surface,
                    Color['black'],
                    self.new_point_to_pixel(x, 0 + line_height_for_one_side),
                    self.new_point_to_pixel(x, 0 - line_height_for_one_side),
                    line_width,
                )

        for y in range(self.y_interval[0], self.y_interval[1]):
            if y % 2 == 0:
                pygame.draw.line(
                    self.surface,
                    Color['black'],
                    self.new_point_to_pixel(0 - line_height_for_one_side, y),
                    self.new_point_to_pixel(0 + line_height_for_one_side, y),
                    line_width,
                )

    # The axis should be drawn with the help of points in the window rather than pixels
    # Then use the point_to_pixel function to draw them with pygame
    # The axis should only be drawn in the interval
    def generate_axis(self):
        # Vertical line
        # Drawn from top to bottom of the screen
        # The x position is the same on both points
        # The first point has the y position of the end of the y_interval to pixels
        # The second point has the y position of the start of the y_interval to pixels
        vertical_start_position = self.new_point_to_pixel(0, self.y_interval[1])
        vertical_end_position = self.new_point_to_pixel(0, self.y_interval[0])
        pygame.draw.line(self.surface, Color['black'], vertical_start_position, vertical_end_position, 5)
        # print('Drawing vertical line from ' + str(vertical_start_position) + ' to ' + str(vertical_end_position))

        # Horizontal line
        # Drawn from left to right of the screen
        # The y position is the same on both points, 0 to pixels
        # The first point has the x position of the start of the x_interval to pixels
        # The second point has the x position of the end of the x_interval to pixels
        horizontal_start_position = self.new_point_to_pixel(self.x_interval[0], 0)
        horizontal_end_position = self.new_point_to_pixel(self.x_interval[1], 0)
        pygame.draw.line(self.surface, Color['black'], horizontal_start_position, horizontal_end_position, 5)
        # print(
        # 'Drawing horizontal line from ' + str(horizontal_start_position) + ' to ' + str(horizontal_end_position)
        # )

    def create_surface(self):
        surface = pygame.display.set_mode((self.width, self.height))
        surface.fill(Color['white'])
        pygame.display.update()
        return surface

    def new_point_to_pixel(self, point_x=None, point_y=None):
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
            pixel_x = self.new_point_to_pixel(point_x, None)
            pixel_y = self.new_point_to_pixel(None, point_y)
            # print('Returning pixels for point, x ' + str(pixel_x) + ' y ' + str(pixel_y))

            return pixel_x, pixel_y
        elif point_x is not None:
            # Only a x coordinate has been entered as parameter
            # pixel_x = abs(point_x - self.x_interval[0]) * self.scale[0]
            # The absolute value is not necessary for (point_x - self.x_interval[0]), because no x point in the
            # interval can cause the difference to be negative. (point_x - self.x_interval[0]) >= 0
            pixel_x = (point_x - self.x_interval[0]) * self.scale[0]
            # print('Returning pixel for just one x value, x ' + str(pixel_x))

            return pixel_x
        elif point_y is not None:
            # Only a y coordinate has been entered as parameter
            # The absolute value is necessary here because the length, (point_y - self.y_interval[1]), will be
            # negative for all y points except for the biggest y value in the interval
            # (point_y - self.y_interval[1]) <= 0
            if point_y > self.y_interval[1]:
                pixel_y = (self.y_interval[1] - point_y) * self.scale[1]
            else:
                pixel_y = abs(point_y - self.y_interval[1]) * self.scale[1]

            # print('Returning pixel for just one y value, y ' + str(pixel_y))
            return pixel_y

    def point_list_to_pixel_list(self, point_list):
        pixel_list = []

        for i in range(len(point_list)):
            # The point to pixel function expects two arguments one x and one y, you can't send it a tuple with both
            # Although that would be a good addition
            pixel_list.append(self.new_point_to_pixel(point_list[i][0], point_list[i][1]))

        return pixel_list

    def draw_curve(self, curve):
        pygame.draw.lines(
            self.surface,
            curve.color,
            False,
            self.point_list_to_pixel_list(curve.get_pointlist(self.x_interval, 100)),
            curve.width
        )
