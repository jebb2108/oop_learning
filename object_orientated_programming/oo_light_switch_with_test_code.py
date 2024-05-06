# oo_light_switch

class LightSwitch():
    def __init__(self):
        self.switch_is_on = False

    def turn_on(self):
        self.switch_is_on = True
        return self.switch_is_on

    def turn_off(self):
        self.switch_is_on = False
        return self.switch_is_on

    def show(self):
        print(self.switch_is_on)

my_switch = LightSwitch()

my_switch.turn_on()
my_switch.show()
my_switch.turn_off()
my_switch.show()