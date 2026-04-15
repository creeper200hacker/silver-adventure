class FlipFlopBell:
    def __init__(self):
        self._flip = True

    def ring(self):
        if self._flip:
            print("flip")
        else:
            print("flop")
        self._flip = not self._flip


# Пример 1
bell = FlipFlopBell()
bell.ring()  # flip
bell.ring()  # flop
bell.ring()  # flip
