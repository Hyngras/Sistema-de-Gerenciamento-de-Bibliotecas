**Sistema de Gerenciamento de Bibliotecas**

Esta atividade é mais uma aplicação do conteúdo abordado na disciplina de Técnicas Computacionais do Professor Fernando Sales. Consiste em um Sistema de Gerenciamento de Bibliotecas desenvolvido em Python, utilizando programação orientada a objetos (POO). O sistema tem como objetivo fornecer funcionalidades para o controle de livros, revistas, teses, usuários, empréstimos, multas e listas de espera em uma biblioteca.

### Funcionalidades Principais:

1. **Classes:**
   - **Livro:** Representa um livro na biblioteca, com informações como título, ISBN, editora, ano de publicação, autores e identificador único.
   - **Revista:** Representa uma revista na biblioteca, com informações como título, ISSN, autor, editora, ano, volume e identificador único.
   - **Tese:** Representa uma tese na biblioteca, com informações como título, autor, programa de pós-graduação, orientador, co-orientador e ano de publicação.
   - **Usuario:** Representa um usuário da biblioteca, com informações como nome, e-mail, telefone, filiação, data de nascimento, histórico de empréstimos e multas.
   - **Emprestimo:** Gerencia o processo de empréstimo de itens da biblioteca.
   - **Multa:** Controla as multas associadas a atrasos na devolução de itens.
   - **ListaEspera:** Mantém uma lista de espera para itens populares que estão todos emprestados.

2. **Funcionalidades de Usuário:**
   - Cada usuário tem permissões específicas com base em seu tipo (aluno de graduação, aluno de pós-graduação, professor, funcionário, gerente).
   - Limites de empréstimo e prazos variam conforme o tipo de usuário.

3. **Relatórios e Estatísticas:**
   - O sistema gera relatórios sobre os itens emprestados, os mais populares, listas de espera, entre outros.
   - Estatísticas mensais, semanais e diárias estão disponíveis.

### Como Executar o Projeto:

1. **Clone o Repositório:**
   ```bash
   git clone https://github.com/seu-usuario/Sistema-de-Gerenciamento-de-Bibliotecas.git
   ```

2. **Navegue para o Diretório:**
   ```bash
   cd Sistema-de-Gerenciamento-de-Bibliotecas
   ```

3. **Execute o Main:**
   ```bash
   python main.py
   ```

### Requisitos:

- Python 3.x

### Contribuições:

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) e enviar pull requests para melhorar o sistema.

### Autores:

- [Hyngrid Sousa e Silva]
- [Luana Lopes Santiago]
- [Matheus K]
- [Pedro A]

