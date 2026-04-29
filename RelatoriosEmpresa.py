from abc import ABC, abstractmethod

# Interface do Visitante
class Visitor(ABC):
    @abstractmethod
    def visit_relatorio_produtos(self, relatorio):
        pass

    @abstractmethod
    def visit_relatorio_inadimplencia(self, relatorio):
        pass

# Elemento Base
class Relatorio(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

# Relatórios Concretos (Dados)
class RelatorioProdutos(Relatorio):
    def __init__(self, data_referencia, itens):
        self.data = data_referencia
        self.itens = itens

    def accept(self, visitor: Visitor):
        visitor.visit_relatorio_produtos(self)

class RelatorioInadimplencia(Relatorio):
    def __init__(self, mes, devedores):
        self.mes = mes
        self.devedores = devedores

    def accept(self, visitor: Visitor):
        visitor.visit_relatorio_inadimplencia(self)

# Novos Visitantes (Saídas)

class JSONVisitor(Visitor):
    """Simula a saída para APIs ou integrações de sistemas"""
    def visit_relatorio_produtos(self, rel):
        print(f"SAÍDA JSON")
        print(f'{{ "tipo": "vendas", "data": "{rel.data}", "itens": {rel.itens} }}\n')

    def visit_relatorio_inadimplencia(self, rel):
        print(f"SAÍDA JSON")
        print(f'{{ "tipo": "inadimplencia", "mes": "{rel.mes}", "lista": {rel.devedores} }}\n')

class CSVVisitor(Visitor):
    """Simula a saída formatada em colunas separadas por vírgula"""
    def visit_relatorio_produtos(self, rel):
        print(f"SAÍDA CSV")
        print(f"Data;Produto;Quantidade")
        for item in rel.itens:
            print(f"{rel.data};{item['nome']};{item['qtd']}")
        print()

    def visit_relatorio_inadimplencia(self, rel):
        print(f"SAÍDA CSV")
        print(f"Mes;Nome;Valor_Devido")
        for d in rel.devedores:
            print(f"{rel.mes};{d['nome']};{d['valor']}")
        print()

# Execução das novas simulações

if __name__ == "__main__":
    # 1. Preparando os dados dos novos relatórios
    vendas_maio = RelatorioProdutos("Maio/2026", [{"nome": "Cadeira Gamer", "qtd": 45}, {"nome": "Teclado", "qtd": 30}])
    devedores_junho = RelatorioInadimplencia("Junho/2026", [{"nome": "Loja ABC", "valor": 5000}, {"nome": "Tech Soluções", "valor": 12556}]) # [cite: 4]

    # 2. Criando os novos visitantes
    exportador_json = JSONVisitor()
    exportador_csv = CSVVisitor()

    # 3. Executando as simulações
    print("Simulando Relatório de Vendas em JSON:")
    vendas_maio.accept(exportador_json)

    print("Simulando Relatório de Inadimplência em CSV:")
    devedores_junho.accept(exportador_csv)
