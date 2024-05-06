class DimmerSwitch():
    def __init__(self):
        self.switch_is_on = False
        self.brightness = 0

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
        print('Switch is on?', self.switch_is_on)
        print('Brightness is:', self.brightness)


o_dimmer = DimmerSwitch()

o_dimmer.turn_on()
o_dimmer.raise_level()
o_dimmer.raise_level()
o_dimmer.raise_level()
o_dimmer.raise_level()
o_dimmer.raise_level()
o_dimmer.show()

o_dimmer.lower_level()
o_dimmer.lower_level()

o_dimmer.turn_off()
o_dimmer.show()

o_dimmer.turn_on()
o_dimmer.raise_level()
o_dimmer.raise_level()
o_dimmer.raise_level()
o_dimmer.show()