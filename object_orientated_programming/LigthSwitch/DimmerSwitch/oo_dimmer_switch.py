class DimmerSwitch:
    def __init__(self, label):
        self.switch_is_on = False
        self.brightness = 0
        self.label = label

    def turn_on(self):
        self.switch_is_on = True

    def turn_off(self):
        self.switch_is_on = False

    def raise_level(self):
        if self.brightness < 10:
            self.brightness += 1

    def lower_level(self):
        if self.brightness > 0:
            self.brightness -= 1

    def show(self):
        print('Label:', self.label)
        print('Switch is on?', self.switch_is_on)
        print('Brightness is:', self.brightness)
        print()
