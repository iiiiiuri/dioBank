from datetime import date

class Transacao:
    def registrar(self, conta):
        raise NotImplementedError("Este método deve ser sobrescrito nas subclasses")


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)
        conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)


class Conta:
    def __init__(self, cliente, numero, agencia):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def saldo(self):
        return self.saldo

    def nova_conta(cliente, numero, agencia):
        return Conta(cliente, numero, agencia)

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        return False

    def depositar(self, valor):
        self.saldo += valor
        return True


class ContaCorrente(Conta):
    def __init__(self, cliente, numero, agencia, limite, limite_saques):
        super().__init__(cliente, numero, agencia)
        self.limite = limite
        self.limite_saques = limite_saques


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


# Exemplo de uso
cliente1 = PessoaFisica(cpf="12345678900", nome="João", data_nascimento=date(1990, 1, 1), endereco="Rua A, 123")
conta1 = Conta(cliente1, numero=12345, agencia="001")
cliente1.adicionar_conta(conta1)

deposito = Deposito(valor=1000.0)
cliente1.realizar_transacao(conta1, deposito)

saque = Saque(valor=200.0)
cliente1.realizar_transacao(conta1, saque)

print(f"Saldo atual: {conta1.saldo}")
print(f"Transações: {[type(t).__name__ for t in conta1.historico.transacoes]}")


