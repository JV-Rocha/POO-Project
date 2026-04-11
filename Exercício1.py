from abc import ABC, abstractmethod
from typing import Optional

# ====================== INTERFACE PRINCIPAL ======================
class Notifies(ABC):
    @abstractmethod
    def send(self, message: str, recipient: Optional[str] = None):
        pass


# ====================== IMPLEMENTAÇÕES CONCRETAS ======================
class Email(Notifies):
    def send(self, message: str, recipient: Optional[str] = None):
        print(f"[EMAIL] Enviado para {recipient or 'destinatário padrão'}: {message}")


class Push(Notifies):
    def send(self, message: str, recipient: Optional[str] = None):
        print(f"[PUSH] Enviado para {recipient or 'usuário'}: {message}")


# ====================== ADAPTER ======================
class LegacySMS:
    """Classe legada com interface incompatível (exemplo de serviço externo)"""
    
    def send_sms(self, phone: str, text: str):
        print(f"[LEGACY SMS] Enviado para {phone}: {text}")


class SMSAdapter(Notifies):
    """Adapter que converte a interface LegacySMS para a interface Notifies"""
    
    def __init__(self, legacy_sms: LegacySMS):
        self.legacy_sms = legacy_sms
    
    def send(self, message: str, recipient: Optional[str] = None):
        if not recipient:
            raise ValueError("SMS requer um número de telefone (recipient)")
        self.legacy_sms.send_sms(recipient, message)


# ====================== PROXY ======================
class NotificationProxy(Notifies):
    
    def __init__(self, real_notification: Notifies, user_role: str = "user"):
        self.real_notification = real_notification
        self.user_role = user_role
        self._attempts = 0
        self._max_attempts = 3
    
    def send(self, message: str, recipient: Optional[str] = None):
        self._attempts += 1
        
        # Validações e controles (Proxy)
        if self._attempts > self._max_attempts:
            print(f"[PROXY] Bloqueado: número máximo de tentativas ({self._max_attempts}) excedido.")
            return
        
        if not message or len(message.strip()) < 5:
            print("[PROXY] Erro: Mensagem muito curta ou vazia.")
            return
        
        if self.user_role == "guest" and isinstance(self.real_notification, (SMSAdapter, Email)):
            print("[PROXY] Acesso negado: Guests não podem enviar SMS ou Email.")
            return
        
        # Log
        print(f"[PROXY] Log: Tentativa {self._attempts} | Tipo: {type(self.real_notification).__name__} | Para: {recipient}")
        
        # Delega para o objeto real
        self.real_notification.send(message, recipient)


# ====================== FACTORY ATUALIZADA ======================
class NotifiesFactory:
    @staticmethod
    def create(notification_type: str, user_role: str = "user") -> Notifies:
        t = notification_type.lower()
        
        if t == "email":
            print("Factory criando Email...")
            real = Email()
            
        elif t == "push":
            print("Factory criando Push...")
            real = Push()
            
        elif t == "sms":
            print("Factory criando SMS (via Adapter)...")
            legacy_sms = LegacySMS()
            real = SMSAdapter(legacy_sms)
            
        else:
            raise ValueError(f"Tipo '{notification_type}' é inválido")
        
        # Envolve com Proxy para adicionar controles
        return NotificationProxy(real, user_role=user_role)


# ====================== SINGLETON (App) ======================
class App:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Iniciando instância única do App...")
            cls._instance = super(App, cls).__new__(cls)
            cls._instance.app_name = "NotifySys"
            cls._instance.server = "production"
            cls._instance.max_retries = 3
        return cls._instance


# ====================== EXECUÇÃO ======================
if __name__ == "__main__":
    config = App()
    print(f"Aplicação iniciada: {config.app_name}\n")

    # Testes com Proxy + Adapter
    try:
        # Usuário normal
        n1 = NotifiesFactory.create("email", user_role="admin")
        n1.send("Bem-vindo ao sistema!", "joao@email.com")

        n2 = NotifiesFactory.create("sms", user_role="user")
        n2.send("Seu código é 8542", "+5511999999999")

        n3 = NotifiesFactory.create("push", user_role="user")
        n3.send("Você tem uma nova mensagem!", "user123")

        print("\n--- Teste com usuário Guest ---")
        n4 = NotifiesFactory.create("sms", user_role="guest")
        n4.send("Mensagem proibida", "+5511888888888")

    except ValueError as e:
        print(f"Erro: {e}")
