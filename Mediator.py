from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List


class Mediator(ABC):
    """interface"""

    @abstractmethod
    def register_user(self, user: "User") -> None:
        pass

    @abstractmethod
    def send_message(self, message: str, sender_name: str) -> None:
        pass


class GroupTextMediator(Mediator):
    """Mediador concreto"""

    def __init__(self) -> None:
        self.users: Dict[str, User] = {}

    def register_user(self, user: "User") -> None:
        self.users[user.name] = user
        user.mediator = self

    def send_message(self, message: str, sender_name: str) -> None:
        for name, user in self.users.items():
            if name != sender_name:
                user.receive_message(message, sender_name)


class User:
    """Participante do grupo"""
    def __init__(self, name: str) -> None:
        self.name = name
        self.mediator: Mediator | None = None
        self.inbox: List[str] = []

    def send_message(self, message: str) -> None:
        if self.mediator is None:
            raise RuntimeError(f"Usuário {self.name} não está registrado em nenhum mediator.")

        print(f"{self.name} enviando: {message}")
        self.mediator.send_message(message, self.name)

    def receive_message(self, message: str, sender_name: str) -> None:
        formatted = f"{sender_name} diz: {message}"
        self.inbox.append(formatted)
        print(f"{self.name} recebeu: {formatted}")


def main() -> None:
    mediator = GroupTextMediator()

    alice = User("Alice")
    bob = User("Bob")
    carla = User("Carla")

    mediator.register_user(alice)
    mediator.register_user(bob)
    mediator.register_user(carla)

    alice.send_message("Taaarde pessoal, bora estudar pra prova de ProjOO?")
    bob.send_message("boooora! vou mandar meu resumo aqui")
    carla.send_message("blz gente, to com muita dúvida, preciso de ajuda ;-;.")

    print("\n=== Caixa de entrada de cada usuário ===")
    for user in (alice, bob, carla):
        print(f"{user.name}: {user.inbox}")


if __name__ == "__main__":
    main()
