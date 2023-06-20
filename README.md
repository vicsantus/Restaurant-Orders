# Boas-vindas ao repositório do Projeto Restaurant Orders!

## Contextualizando

O Restaurante Chapa Quente precisa de você para finalizar sua ferramenta de construção de cardápios. O restaurante necessita desta ferramenta para que possa, de maneira simples, gerar seus cardápios considerando possíveis restrições alimentares e também a disponibilidade dos ingredientes em estoque. Hoje, a gestão das receitas e de estoque do restaurante acontece de forma muito ineficiente através de arquivos csv e, por essa razão, as pessoas fundadoras do estabelecimento desejam melhorar esta gestão.

O projeto se trata de um gerenciador de csv, em python com algoritmos de leitura e manutenção de csv's. Ele simula ordems de um restaurante, onde na pasta models existem dois arquivos, um que simula os ingredientes, e o outro que simula pratos de comidas. E na pasta services existem 3 arquivos: menu_data simula faz o gerenciamento dos dados, menu_builder pega o cardápio e faz as ordems e inventory_control gerencia o inventario do restaurante.

Também foram feitos os testes utilizando PyTest do python. Cobrindo ingredientes e dish.

## Instalação

Instalação do projeto

```bash
  git clone git@github.com:vicsantus/Restaurant-Orders.git
  cd Restaurant-Orders
  python3 -m venv .venv && source .venv/bin/activate
  python3 -m pip install -r dev-requirements.txt
```

Para fazer o teste utilize a seguinte instrução dentro do ambiente .venv

```bash
  python3 -m pytest -s -vv
```
