class Curve:
    def __init__(self, curve_function, color, width):
        self.curve_function = curve_function
        self.color = color
        self.width = width

    def get_pointlist(self, x_interval):
        pointlist = []

        # Add one to the stop value of the range function. Otherwise if you have an x interval 0 < x < 10, it will
        # only generate points up to and including 9. Why is it so?
        for x in range(x_interval[0], (x_interval[1] + 1)):
            # print('Generated point ({}, {})'.format(x, self.curve_function(x)))
            pointlist.append((x, self.curve_function(x)))

        return pointlist
