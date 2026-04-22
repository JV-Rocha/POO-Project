from abc import ABC, abstractmethod

# Interface
class Game(ABC):
    @abstractmethod
    def play(self):
        pass

# Implementações
class IndieGame(Game):
    def play(self):
        return "Jogando Hollow Knight

class AAAGame(Game):
    def play(self):
        return "Jogando Overwatch"

# Factory
class GameFactory:
    @staticmethod
    def create_game(tipo):
        if tipo == "indie":
            return IndieGame()
        elif tipo == "aaa":
            return AAAGame()
        else:
            raise ValueError("Tipo inválido")


# Uso
game1 = GameFactory.create_game("indie")
game2 = GameFactory.create_game("aaa")

print(game1.play())
print(game2.play())
