from abc import ABC, abstractmethod


class Bebida(ABC):
    @abstractmethod
    def get_descricao(self) -> str:
        pass

    @abstractmethod
    def custo(self) -> float:
        pass


# ==================== BEBIDAS BASE ====================
class CafeExpresso(Bebida):
    def get_descricao(self) -> str:
        return "Café Expresso"
    def custo(self) -> float:
        return 6.00


class Cappuccino(Bebida):
    def get_descricao(self) -> str:
        return "Cappuccino"
    def custo(self) -> float:
        return 8.50


class Cha(Bebida):
    def get_descricao(self) -> str:
        return "Chá"
    def custo(self) -> float:
        return 5.00


# ==================== DECORADORES ====================
class Decorador(Bebida):
    def __init__(self, bebida: Bebida):
        self.bebida = bebida

    def get_descricao(self) -> str:
        return self.bebida.get_descricao()

    def custo(self) -> float:
        return self.bebida.custo()


class Leite(Decorador):
    def get_descricao(self) -> str:
        return f"{self.bebida.get_descricao()}, Leite"
    def custo(self) -> float:
        return self.bebida.custo() + 2.50


class Chantilly(Decorador):
    def get_descricao(self) -> str:
        return f"{self.bebida.get_descricao()}, Chantilly"
    def custo(self) -> float:
        return self.bebida.custo() + 3.00


class Canela(Decorador):
    def get_descricao(self) -> str:
        return f"{self.bebida.get_descricao()}, Canela"
    def custo(self) -> float:
        return self.bebida.custo() + 1.00


class CaldaDeChocolate(Decorador):
    def get_descricao(self) -> str:
        return f"{self.bebida.get_descricao()}, Calda de Chocolate"
    def custo(self) -> float:
        return self.bebida.custo() + 2.80


# ====================== USO ======================
if __name__ == "__main__":
    # Pedido 1: Expresso com Leite e Chantilly
    bebida1 = CafeExpresso()
    bebida1 = Leite(bebida1)
    bebida1 = Chantilly(bebida1)
    print(f"{bebida1.get_descricao()}")
    print(f"Total: R$ {bebida1.custo():.2f}\n")

    # Pedido 2: Cappuccino com Canela e Calda de Chocolate
    bebida2 = Cappuccino()
    bebida2 = Canela(bebida2)
    bebida2 = CaldaDeChocolate(bebida2)
    print(f"{bebida2.get_descricao()}")
    print(f"Total: R$ {bebida2.custo():.2f}\n")

    # Pedido 3: Chá com Leite e Canela
    bebida3 = Cha()
    bebida3 = Leite(bebida3)
    bebida3 = Canela(bebida3)
    print(f"{bebida3.get_descricao()}")
    print(f"Total: R$ {bebida3.custo():.2f}")
