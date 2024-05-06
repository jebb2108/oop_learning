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

# Два экземпляра
my_switch1 = LightSwitch()
my_switch2 = LightSwitch()

print(type(my_switch1))


my_switch1.show()
my_switch2.show()
my_switch1.turn_on()

my_switch1.show()
my_switch2.show()
print()


s = 'abc'
print(type(s))

