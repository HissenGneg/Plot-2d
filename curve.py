class Curve:
    def __init__(self, curve_function, color, width):
        self.curve_function = curve_function
        self.color = color
        self.width = width

    def get_pointlist(self, x_interval, precision=1):
        '''
        The point precision works by multiplying the start and end of the interval. By doing so you're making
        the difference between the start and end bigger. By making the difference bigger you are allowing for
        more precision when generating the pointlist. More x values equals more points as the curve function
        is called for each x value.
        The index in the range between this multiplied interval can't simply be appended to the pointlist
        as the x values are too large. For example, if you are generating points for the
        interval 0 < x < 10, the multiplied interval with a precision of 10 would be 0 < x < 100.
        Anything beyond 10 is irrelevant to the user since that's what is the interval that's requested.
        Before appending the x and its y value to the pointlist you need to create a new variable where
        you reverse the changes you made when you multiplied the interval. This will normalize the
        interval back to its original state 0 < x < 10. By having an increased precision you will
        generate more x values between the x values in the interval. For example, the generated
        x values might look like: 0, 0.33, 0.66, 1, 1.33, 1.66, 2, etc.
        To reverse you multiply the multiplied interval index with (1 / precision) which removes
        the multiplication applied to the interval.
        :param x_interval: The interval of x values to generate points for
        :param precision: Set the point precision. The default value is 1 which will generate points for each
        x in the x interval. But with an increased precision more points are generated between each x value
        resulting in a better looking curve.
        :return: A list of points which are tuples
        '''
        pointlist = []
        x_start_with_precision = (x_interval[0] * precision)
        x_end_with_precision = ((x_interval[1] + 1) * precision)

        # Add one to the stop value of the range function. Otherwise if you have an x interval 0 < x < 10, it will
        # only generate points up to and including 9. Why is it so?
        for x in range(x_start_with_precision, x_end_with_precision):
            # print('Generated point ({}, {})'.format(x, self.curve_function(x)))
            point_x = x * (1 / precision)
            pointlist.append((point_x, self.curve_function(point_x)))

        return pointlist
