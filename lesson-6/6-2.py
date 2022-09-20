class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        print('Create a new road')

    def coating(self):
        weigth_1_m = 25
        tickness = 5
        coating = self._length * self._width * weigth_1_m * tickness / 1000
        print(f'Need {coating} ton of asphalt for the building')


new_road1 = Road(5000, 20)
new_road1.coating()
