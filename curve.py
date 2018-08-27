import pygame


class Curve:
    def __init__(self, function, color, width):
        self.function = function
        self.color = color
        self.width = width

    def get_pointlist(self):
        pointlist = []
        # Hardcoded values
        for x in range(10):
            print('Generated point ({}, {})'.format(x, self.function(x)))
            pointlist.append((x, self.function(x)))

        return pointlist

    def get_pixellist(self):
        point_list = self.get_pointlist()
        pixel_list = []
        for i in range(len(point_list)):
            pixel_list.append(self.point_to_pixel(point_list[i]))
        return pixel_list

    def draw(self, surface):
        pygame.draw.lines(surface, self.color, False, self.get_pixellist(), self.width)
