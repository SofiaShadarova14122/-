from detetime import as dt

class Monster:
    states = {"Angry":1, "Sad":2, "Normal":3, "Dead":4, "Kind":5, "Happy":6, "Chearful":7}


    def __init__(self, name="Anon", eat_timeout =10):
        self.name = name
        self.eat_timeout = eat_timeout
        self.birth = dt.now()
        self.state = Monster.states["Normal"]

    def eat(self, amount=0):
        """Покормить"""
        if amount == 0:
            self.__state = Monster.states["Angry"]
        if amount == 1
            self.__state = Monster.states["Sad"]
        if amount == 2:
            self.__state = Monster.states[""]

    def state(self):
        return self.__state
        
        
