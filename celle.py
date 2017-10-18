class Celle:
# Constructor
    def __init__(self):
        self._state = False


    def settDoed(self):
        self._state = False


    def settLevende(self):
        self._state = True


    def erLevende(self):
        if self._state:
            return True
        else:
            return False


    def hentStatusTegn(self):
        if self._state:
            return "O"
        else:
            return "."
