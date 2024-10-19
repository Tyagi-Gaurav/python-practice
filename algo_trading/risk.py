class Risk:
    def __init__(self, tp_atr_multiplier=1.2):
        self.__tp_atr_multiplier = tp_atr_multiplier

    def get_tp_atr_multiplier(self):
        return self.__tp_atr_multiplier
