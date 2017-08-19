from dolphin import DolphinGun

class Orca:
    def __init__(self):
        self.set_vals()
        self.gun = DolphinGun(30, self.bodyX, self.headrightY, 5)

    def set_vals(self):
        self.tailMidx = 20
        # following three have same x = tailMidx = 20
        self.tailMidy = 450
        self.tailTopY = 460
        self.tailBotY = 440
        # right x has the same y as tailMidY
        self.tailRightX = 37.3

        # body
        self.bodyH = 10
        self.bodyW = 26
        self.bodyX = 30
        self.bodyY = 446

        # head
        self.headMidX = 56
        # following three have same x = headMidX
        self.headMidY = 450
        self.headtopY = 460
        self.headbotY = 450
        self.headrightY = 450
        self.headrightx = 56 + 15
        self.vx = 0
        self.vy = 0

    def moveX(self, x_net):
        if self.bodyX > 800 | self.bodyX < 0:
            self.respawn()
        self.tailMidx += x_net
        self.tailRightX += x_net
        self.bodyX += x_net
        self.headMidX += x_net
        self.headrightx += x_net
        self.gun.x += x_net

    def moveY(self, y_net):
        if self.bodyY > 600 | self.bodyY < 0:
            self.respawn()
        self.tailMidy += y_net
        self.tailTopY += y_net
        self.tailBotY += y_net
        self.bodyY += y_net
        self.headMidY += y_net
        self.headtopY += y_net
        self.headbotY += y_net
        self.headrightY += y_net
        self.gun.y += y_net

    def vMove(self):
        self.moveX(self.vx)
        self.moveY(self.vy)


    def getVxVy(self):
        return self.vx, self.vy

    def respawn(self):
        self.set_vals()