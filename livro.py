class Livro:
    def __init__(self, titulo, ISBN, editora, ano_publicacao, autores, id_exemplar):
        self.titulo = titulo
        self.ISBN = ISBN
        self.editora = editora
        self.ano_publicacao = ano_publicacao
        self.autores = autores
        self.id_exemplar = id_exemplar
        self.disponivel = True
