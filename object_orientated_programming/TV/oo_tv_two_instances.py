from oo_tv import TV


def main():
    oTV1 = TV('Samsung', 'Family room')
    oTV2 = TV('Sony', 'Bedroom')
    #TV.__init__('test', 'Samsung', 'Family room')  #what it looks like under the hood

    oTV1.power()
    oTV2.power()

    oTV1.volume_up()
    oTV1.volume_up()

    oTV2.volume_up()
    oTV2.volume_up()
    oTV2.volume_up()
    oTV2.volume_up()
    oTV2.volume_up()

    oTV2.set_channel(44)
    oTV2.mute()

    oTV1.show_info()
    oTV2.show_info()


if __name__ == '__main__':
    main()
