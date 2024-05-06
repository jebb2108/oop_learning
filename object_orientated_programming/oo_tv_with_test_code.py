""" Класс TV с тестовым кодом"""


class TV():
    def __init__(self):
        self.is_on = False
        self.is_muted = False
        # Некий список каналов по умолчанию
        self.channel_list = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.n_channels = len(self.channel_list)
        self.channel_index = 0
        self.volume_minimum = 0
        self.volume_maximum = 10
        self.volume = self.volume_maximum // 2

    def power(self):
        self.is_on = not self.is_on

    def volume_up(self):
        if not self.is_on:
            return
        if self.is_muted:
            self.is_muted = False

        if self.volume < self.volume_maximum:
            self.volume += 1

    def volume_down(self):
        if not self.is_on:
            return
        if self.is_muted:
            self.is_muted = False
        if self.volume > self.volume_minimum:
            self.volume -= 1

    def channel_up(self):
        if not self.is_on:
            return
        self.channel_index += 1
        if self.channel_index > self.n_channels:
            self.channel_index = 0

    def channel_down(self):
        if not self.is_on:
            return
        self.channel_index -= 1

        if self.channel_index < 0:
            self.channel_index = self.n_channels - 1

    def mute(self):
        if not self.is_on:
            return

        self.is_muted = not self.is_muted

    def set_channel(self, new_channel):
        if new_channel in self.channel_list:
            self.channel_index = self.channel_list.index(new_channel)

    def show_info(self):
        print()
        print('TV Status:')
        if self.is_on:
            print('  TV is: On')
            print('  Channel is:', self.channel_list[self.channel_index])
            if self.is_muted:
                print('Volume is:', self.volume, '(sound is muted)')
            else:
                print('Volume is:', self.volume)
        else:
            print('TV is: Off')

oTV = TV()

oTV.power()
oTV.show_info()

oTV.channel_up()
oTV.channel_up()
oTV.volume_up()
oTV.volume_up()
oTV.show_info()

oTV.power()
oTV.show_info()
oTV.power()
oTV.show_info()

oTV.volume_down()
oTV.mute()
oTV.show_info()

oTV.set_channel(11)
oTV.mute()
oTV.show_info()