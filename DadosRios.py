from abc import ABC, abstractmethod

# Subject (Sujeito)
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for obs in self._observers:
            obs.update(self)


# Interface Observer
class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass


# Classe que representa o monitoramento do Rio Amazonas
class MonitorRioAmazonas(Subject):
    def __init__(self):
        super().__init__()
        self._ura = 0
        self._pa = 0
        self._ph = 7
        self._temperatura = 0

    # getters
    def get_dados(self):
        return {
            "URA": self._ura,
            "PA": self._pa,
            "pH": self._ph,
            "Temperatura": self._temperatura
        }

    # setters
    def set_dados(self, ura, pa, ph, temperatura):
        self._ura = ura
        self._pa = pa
        self._ph = ph
        self._temperatura = temperatura
        self.notify_observers()


# ===== Universidades (Observers) =====

class UniversidadeUSP(Observer):
    def update(self, subject):
        dados = subject.get_dados()
        print("[USP] Dados recebidos:", dados)


class UniversidadeUFRJ(Observer):
    def update(self, subject):
        dados = subject.get_dados()
        print("[UFRJ] Análise ambiental:", dados)


class UniversidadeUFAM(Observer):
    def update(self, subject):
        dados = subject.get_dados()
        print("[UFAM] Monitoramento regional:", dados)


class UniversidadeUnicamp(Observer):
    def update(self, subject):
        dados = subject.get_dados()
        print("[Unicamp] Dados científicos:", dados)


class UniversidadeUnifesp(Observer):
    def update(self, subject):
        dados = subject.get_dados()
        print("[Unifesp] Relatório hídrico:", dados)


# ===== Main =====
if __name__ == "__main__":
    monitor = MonitorRioAmazonas()

    monitor.add_observer(UniversidadeUSP())
    monitor.add_observer(UniversidadeUFRJ())
    monitor.add_observer(UniversidadeUFAM())
    monitor.add_observer(UniversidadeUnicamp())
    monitor.add_observer(UniversidadeUnifesp())

    # dispara notificação
    monitor.set_dados(
        ura=85,
        pa=1013,
        ph=6.8,
        temperatura=28.5
    )
