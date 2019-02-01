#yinweixian
#2/1/19

class television(object):
    def __init__(self):
        self.channel = 1
        self.volume = 0

    def changeChannel(self):
        upDown = input("would you like to increase the channel number or decrease the channel number? up/down")
        change = int(input("enter the number by which you wish to change the channel"))

        if upDown.startswith("u"):
            self.channel += change
        elif upDown.startswith("d"):
            self.channel -= change

        if self.channel > 27831:
            self.channel = 27831
        elif self.channel < 0:
            self.channel = 0

        print("you are now on channel",self.channel)





    def changeVolume(self):
        upDown = input("would you like to increase or decrease the volume? up/down")
        change = int(input("enter the number by which you wish to change the channel"))

        if upDown.startswith("u"):
            self.volume += change
        elif upDown.startswith("d"):
            self.volume -= change

        if self.volume > 100:
            self.volume = 100
        elif self.volume < 0:
            self.volume = 0

        print("the volume is now",self.volume)


def main():
    tv = television()
    choose = 5
    while choose != 0:
        choose = int(input("""you are watching tv if you would like to change the channel press 1
        or if you want to change the volume press 2."""))
        if choose == 1:
            tv.changeChannel()

        if choose == 2:
            tv.changeVolume()
main()