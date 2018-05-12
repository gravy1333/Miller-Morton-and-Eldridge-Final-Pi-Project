class Player():
    def __init__(self, maxH = 10):
        self.currentH = maxH
        self.maxH = maxH

    @property
    def maxH(self):
        return self._maxH

    @maxH.setter
    def maxH(self, val):
        if (val > 0):
            self._maxH = val

    @property
    def currentH(self):
        return self._currentH

    @currentH.setter
    def currentH(self, val):
        if (abs(val) > self.currentH):
            self._currentH = 0

        elif (val >= self.maxH):
            self._currentH = self.maxH
            
        else:
            self._currentH += val

    def getHealthPercent(self):
        return (float(self.currentH) / self.maxH) * 100

    def __str__(self):
        return "{}/{}".format(self.currentH, self.maxH)
p1 = Player()
print p1.currentH
p1.currentH = 100
print p1.currentH
