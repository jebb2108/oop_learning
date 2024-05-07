# Создаем первый Dimmer Switch, включаем его и поднимаем уровень
# яркости дважды

from oo_dimmer_switch import DimmerSwitch

o_dimmer1 = DimmerSwitch('Dimmer1')
o_dimmer1.turn_on()
o_dimmer1.raise_level()
o_dimmer1.raise_level()

# Создаем второй Dimmer Switch, включаем его и поднимаем уровень
# яркости в три раза

o_dimmer2 = DimmerSwitch('Dimmer2')
o_dimmer2.turn_on()
o_dimmer2.raise_level()
o_dimmer2.raise_level()
o_dimmer2.raise_level()

# Создаем третий Dimmer Switch, используя настройки по умолчанию
o_dimmer3 = DimmerSwitch('Dimmer3')

# Просим каждый переключатель вывести свои показатели
o_dimmer1.show()
o_dimmer2.show()
o_dimmer3.show()
