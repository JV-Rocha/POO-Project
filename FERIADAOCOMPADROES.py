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
    
    def has_game(self, game_name):
        return game_name in self.library

# Proxy
class GameProxy:
    def __init__(self, game_name, game):
        self.game_name = game_name
        self.game = game
        self.client = GameClient()

    def play(self):
        if self.client.has_game(self.game_name):
            return self.game.play()
        else:
            raise ValueError("Game not found in library")

# Adapter 
class ExternalStoreAPI:
    def launch_game(self):
        return "Rodando jogo da loja externa"
    
class StoreAdapter(Game):
    def __init__(self, external_api):
        self.external_api = external_api

    def play(self):
        return self.external_api.launch_game()
    
# Decorator
class GameDecorator(Game):
    def __init__(self, game):
        self.game = game

class DLCDecorator(GameDecorator):
    def play(self):
        return self.game.play() + " com DLCs adicionais"
    
# Facade
class GameFacade:
    def __init__(self):
        self.client = GameClient()
        self.external_game = StoreAdapter(ExternalStoreAPI())

    def play_game(self, game_name):
        if external_game := self.external_game.play():
           return external_game
        elif self.client.has_game(game_name):
            return self.client.show_library()
       
    def buy_game(self, game_name):
        # Simula a compra de um jogo
        self.client.add_game(game_name)
        return f"Jogo '{game_name}' comprado e adicionado à biblioteca"

# Uso
game1 = GameFactory.create_game("indie")
game2 = GameFactory.create_game("aaa")

client1 = GameClient()
client1.add_game("Hollow Knight")
client2 = GameClient()

proxy = GameProxy("Hollow Knight", game1)

external_game = StoreAdapter(ExternalStoreAPI())

game3 = GameFactory.create_game("aaa")
game3 = DLCDecorator(game3)

hub = GameFacade()

game4 = hub.buy_game("Overwatch")

print(game1.play())
print(game2.play())

print(client2.show_library())

print(proxy.play())

print(external_game.play())

print(game3.play())

print(game4)
