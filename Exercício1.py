from abc import ABC, abstractmethod

# --- INTERFACE (Abstract Base Class) ---
class Notifies(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# --- IMPLEMENTAÇÕES ---
class Email(Notifies):
    def send(self, message: str):
        print(f"[EMAIL]: {message}")

class SMS(Notifies):
    def send(self, message: str):
        print(f"[SMS]: {message}")

class Push(Notifies):
    def send(self, message: str):
        print(f"[PUSH]: {message}")

# --- FACTORY ---
class NotifiesFactory:
    @staticmethod
    def create(notification_type: str) -> Notifies:
        t = notification_type.lower()
        if t == "email":
            print("Factory criando Email")
            return Email()
        elif t == "sms":
            print("Factory criando SMS")
            return SMS()
        elif t == "push":
            print("Factory criando Push")
            return Push()
        else:
            raise ValueError(f"Tipo '{notification_type}' é inválido")

# --- SINGLETON (App) ---
class App:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Iniciando instância única do App...")
            cls._instance = super(App, cls).__new__(cls)
            # Inicialização dos atributos
            cls._instance.app_name = "NotifySys"
            cls._instance.server = "server"
            cls._instance.max_retries = 3
        return cls._instance

# --- EXECUÇÃO (Main) ---
if __name__ == "__main__":
    # Testando o Singleton
    config = App() 
    print(f"Aplicação: {config.app_name}")

    # Testando a Factory
    try:
        n1 = NotifiesFactory.create("email")
        n1.send("Olá!")

        n2 = NotifiesFactory.create("sms")
        n2.send("Seu código chegou.")

        n3 = NotifiesFactory.create("push")
        n3.send("Nova notificação disponível!")
        
    except ValueError as e:
        print(f"Erro: {e}")
