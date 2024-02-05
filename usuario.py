from datetime import datetime, timedelta

class Usuario:
    def __init__(self, nome, email, telefone, filiacao, data_nascimento, tipo_usuario):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.filiacao = filiacao
        self.data_nascimento = data_nascimento
        self.tipo_usuario = tipo_usuario
        self.livros_emprestados = []  # Lista para armazenar os livros emprestados
        self.multas = []  # Lista para armazenar as multas

    def emprestar_livro(self, livro):
        if len(self.livros_emprestados) < 5:  # Verifica se o usuário atingiu o limite de empréstimos
            data_retirada = datetime.now()
            data_devolucao = data_retirada + timedelta(days=7)  # Prazo de uma semana
            emprestimo = Emprestimo(livro, self, data_retirada, data_devolucao)
            self.livros_emprestados.append(emprestimo)
            livro.disponivel = False  # Atualiza o status do livro para não disponível
            return emprestimo
        else:
            return None  # Usuário atingiu o limite de empréstimos

    def devolver_livro(self, emprestimo):
        if emprestimo in self.livros_emprestados:
            data_devolucao_real = datetime.now()
            emprestimo.data_devolucao = data_devolucao_real
            dias_atraso = (data_devolucao_real - emprestimo.data_devolucao).days
            if dias_atraso > 0:
                multa_valor = dias_atraso * 2.50  # Valor da multa por dia
                multa = Multa(self, multa_valor, data_devolucao_real)
                self.multas.append(multa)
            self.livros_emprestados.remove(emprestimo)
            emprestimo.livro.disponivel = True  # Atualiza o status do livro para disponível
            return True
        else:
            return False  # Empréstimo não encontrado na lista

    def pagar_multa(self, multa):
        if multa in self.multas and multa.data_pagamento is None:
            multa.data_pagamento = datetime.now()
            return True
        else:
            return False  # Multa não encontrada na lista ou já foi paga

    def renovar_emprestimo(self, emprestimo):
        if emprestimo in self.livros_emprestados:
            emprestimo.data_devolucao += timedelta(days=7)  # Renovação por mais uma semana
            return True
        else:
            return False  # Empréstimo não encontrado na lista
