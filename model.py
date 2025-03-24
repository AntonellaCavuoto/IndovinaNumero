import random


class Model(object):
    # contiene la logica del gioco
    def __init__(self):
        self._NMax = 100
        self._TMax = 6  # numero di vite massime
        self._T = self._TMax
        self._segreto = None  # numero da indovinare

    def reset(self):
        # questo metodo resetta il gioco in qualsiasi momento
        self._segreto = random.randint(0, self._NMax)
        self._T = self._TMax
        print(self._segreto)

    def play(self, guess):
        """
        Funzione che esegue uno step del gioco
        :param guess: int
        :return: 0 se ho vinto,
        1 se è più grande,
        -1 se è più piccolo,
        2 se ho perso e ho finito le vite
        """
        # da fuori ci arriva un tentativo, confrontiamo il tentativo con il segreto
        self._T -= 1  # decremento le vite
        if guess == self._segreto:
            return 0  # ho vinto

        if self._T == 0:  # ho perso definitivamente
            return 2

        if guess > self._segreto:
            return -1  # il segreto è più piccolo

        return 1  # il segreto è più grande

    @property
    def NMax(self):
        return self._NMax

    @property
    def TMax(self):
        return self._TMax


    @property
    def T(self):
        return self._T

    @property
    def segreto(self):
        return self._segreto


if __name__ == "__main__":
    m = Model()
    m.reset()
    print(m.play(80))
    print(m.play(50))
