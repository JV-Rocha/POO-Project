from abc import ABC, abstractmethod

# Interface
class Game(ABC):
    @abstractmethod
    def play(self):
        pass

# Implementações
class IndieGame(Game):
    def play(self):
        return "Jogando Hollow Knight"

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


# Singleton
class GameClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameClient, cls).__new__(cls)
            cls._instance.library = []
        return cls._instance
    
    def add_game(self, game):
        self.library.append(game)

    def show_library(self):
        return self.library

# Uso
game1 = GameFactory.create_game("indie")
game2 = GameFactory.create_game("aaa")

client1 = GameClient()
client1.add_game("Hollow Knight")
client2 = GameClient()

print(game1.play())
print(game2.play())

print(client2.show_library())
