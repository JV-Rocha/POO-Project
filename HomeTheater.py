class TV:
    def ligar(self):
        print("TV ligada")
    def desligar(self):
        print("TV desligada")
    def set_entrada(self, entrada: str):
        print(f"TV configurada para entrada: {entrada}")


class Projetor:
    def ligar(self):
        print("Projetor ligado")
    def desligar(self):
        print("Projetor desligado")
    def modo_cinema(self):
        print("Projetor em modo cinema")


class Receiver:
    def ligar(self):
        print("Receiver ligado")
    def desligar(self):
        print("Receiver desligado")
    def set_volume(self, volume: int):
        print(f"Volume ajustado para {volume}")


class PlayerDeMidia:
    def ligar(self):
        print("Player de mídia ligado")
    def desligar(self):
        print("Player de mídia desligado")
    def play(self, filme: str):
        print(f"Reproduzindo: {filme}")


class SistemaDeSom:
    def ligar(self):
        print("Sistema de som ligado")
    def desligar(self):
        print("Sistema de som desligado")


class LuzAmbiente:
    def ligar(self):
        print("Luz ambiente ligada")
    def desligar(self):
        print("Luz ambiente desligada (modo cinema)")


# ====================== FACHADA ======================
class HomeTheaterFacade:
    def __init__(self, tv: TV, projetor: Projetor, receiver: Receiver,
                 player: PlayerDeMidia, som: SistemaDeSom, luz: LuzAmbiente):
        self.tv = tv
        self.projetor = projetor
        self.receiver = receiver
        self.player = player
        self.som = som
        self.luz = luz

    def assistir_filme(self, filme: str):
        print("\nPreparando o Home Theater para assistir filme...")
        self.luz.desligar()
        self.projetor.ligar()
        self.projetor.modo_cinema()
        self.tv.ligar()
        self.tv.set_entrada("HDMI")
        self.receiver.ligar()
        self.receiver.set_volume(8)
        self.som.ligar()
        self.player.ligar()
        self.player.play(filme)
        print("Filme iniciado!\n")

    def ouvir_musica(self, musica: str):
        print("\nPreparando o Home Theater para ouvir música...")
        self.luz.ligar()
        self.projetor.desligar()
        self.tv.desligar()
        self.receiver.ligar()
        self.receiver.set_volume(12)
        self.som.ligar()
        self.player.ligar()
        self.player.play(musica)
        print("Música tocando!\n")

    def desligar_tudo(self):
        print("\nDesligando o sistema...")
        self.player.desligar()
        self.som.desligar()
        self.receiver.desligar()
        self.projetor.desligar()
        self.tv.desligar()
        self.luz.ligar()
        print("Sistema desligado.\n")


# ====================== USO ======================
if __name__ == "__main__":
    # Subsistemas
    tv = TV()
    projetor = Projetor()
    receiver = Receiver()
    player = PlayerDeMidia()
    som = SistemaDeSom()
    luz = LuzAmbiente()

    # Fachada (o cliente só precisa disso!)
    facade = HomeTheaterFacade(tv, projetor, receiver, player, som, luz)

    facade.assistir_filme("Duna - Parte Dois")
    facade.ouvir_musica("Bohemian Rhapsody - Queen")
    facade.desligar_tudo()
