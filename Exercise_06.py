
class Tv:

    def __init__(self, channel, volume):
        if 1 <= channel <= 11:
            self.__channel = channel
        else:
            print('Invalid channel!')

        if 0 <= volume <= 100:
            self.__volume = volume
        else:
            print('Invalid volume!')

    def channel(self, channel):
        if 1 <= channel <= 11:
            self.__channel = channel
        else:
            print('Invalid channel!')

    def volume(self, value):
        if 0 <= value <= 100:
            self.__volume = value
        else:
            print('Invalid volume!')


tv1 = Tv(12, 12)
print(vars(tv1))
tv1.channel(7)
print(vars(tv1))
