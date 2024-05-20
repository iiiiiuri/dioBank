# Projeto Banco em Python

Este projeto é uma atividade prática desenvolvida para a plataforma Digital Innovation One (DIO). O objetivo é criar um sistema bancário simples utilizando a linguagem Python, que permite realizar operações de depósito, saque e exibir extrato.

## Funcionalidades

O sistema bancário possui as seguintes funcionalidades:

- **Depósito**: Permite ao usuário depositar um valor na conta, desde que o valor seja positivo.
- **Saque**: Permite ao usuário sacar um valor da conta, respeitando o limite diário de saques, o saldo disponível e o limite máximo por saque.
- **Exibir Extrato**: Exibe todas as transações realizadas na conta e o saldo atual.

## Como Utilizar

Para executar o projeto, siga os passos abaixo:

1. Certifique-se de ter o Python instalado em sua máquina.
2. Faça o download ou clone este repositório.
3. Abra o terminal na pasta onde o arquivo main.py está localizado.
4. Execute o comando `python main.py` para iniciar o sistema bancário.

## Menu de Operações

- **[d] Depositar**: Solicita o valor do depósito e adiciona ao saldo se o valor for válido.
- **[s] Sacar**: Solicita o valor do saque e subtrai do saldo se as condições forem atendidas (saldo suficiente, dentro do limite e número de saques diários não excedido).
- **[e] Extrato**: Exibe todas as transações realizadas e o saldo atual.
- **[q] Sair**: Encerra o programa.