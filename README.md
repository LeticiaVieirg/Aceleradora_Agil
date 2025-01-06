# Inventory Management System

Este é um sistema de gerenciamento de inventário baseado em Python. Ele permite que você adicione, liste, atualize, exclua e pesquise produtos em um inventário, armazenando os dados em um arquivo JSON.

## Funcionalidades do Projeto

- **Adicionar Produto**: Adicione novos produtos ao inventário com nome, categoria, quantidade e preço.
- **Listar Produtos**: Veja todos os produtos disponíveis no inventário em um formato de tabela.
- **Atualizar Produto**: Atualize as informações de um produto existente, incluindo nome, categoria, quantidade e preço.
- **Excluir Produto**: Remova um produto do inventário com base no ID.
- **Pesquisar Produto**: Procure produtos por ID ou nome.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **JSON**: Armazenamento de dados.
- **Tabulate**: Biblioteca para exibir tabelas no terminal.

## Como Executar

1. **Pré-requisitos**:
   - Python 3.6 ou superior instalado.
   - Instale a biblioteca `tabulate` executando:
     ```bash
     pip install tabulate
     ```

2. **Clone o repositório**:
   ```bash
   git clone <   >
   cd <Aceleradora_Agil>
   ```

3. **Execute o programa**:
   ```bash
   python <main.py>.py
   ```

## Estrutura do Projeto

```
.
├── inventory.json         # Arquivo de dados do inventário (criado automaticamente).
├── main.py                # Código principal do sistema.
└── README.md              # Arquivo de documentação do projeto.
```

## Exemplo de Uso

### Menu Principal
```plaintext
Inventory Management System
1. Add Product
2. List Products
3. Update Product
4. Delete Product
5. Search Product
6. Exit
```

### Listagem de Produtos
```plaintext
+----+------------+----------+----------+-------+
| ID | Name       | Category | Quantity | Price |
+----+------------+----------+----------+-------+
| 1  | Notebook   | Eletrônico | 10      | 2500.0 |
| 2  | Headset    | Acessório | 15      | 150.0  |
+----+------------+----------+----------+-------+
```


## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

## Autor

- [Seu Nome](https://github.com/SeuPerfil)
