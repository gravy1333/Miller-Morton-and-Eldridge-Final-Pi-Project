class Player():
    def __init__(self, maxH):
        #temp is here to fix player instanciation issue
        self.tempH = maxH
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
        if (self.tempH + val < 0):
            self._currentH = 0
            self.tempH = 0

        elif (self.tempH + val >= self.maxH):
            self._currentH = self.maxH
            self.tempH = self.maxH
        else:
            self._currentH += val
            self.tempH += val

    def getHealthPercent(self):
        return (float(self.currentH) / self.maxH) * 100

    def __str__(self):
        return "{} / {}".format(self.currentH, self.maxH)
