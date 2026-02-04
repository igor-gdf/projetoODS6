# 💧 Sistema de Controle de Consumo de Água

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-GPL--3.0-green.svg)](LICENSE)
[![ODS](https://img.shields.io/badge/ODS-6%20%C3%81gua%20Pot%C3%A1vel-00bcd4.svg)](https://brasil.un.org/pt-br/sdgs/6)

## 📋 Sobre o Projeto

Sistema desenvolvido para monitoramento e controle do consumo de água, alinhado com o **ODS 6 - Água Potável e Saneamento** da Agenda 2030 da ONU. O objetivo é conscientizar usuários sobre seu consumo hídrico e promover o uso sustentável da água.

### 🎯 Objetivos

- Registrar e monitorar o consumo de água de usuários residenciais e comerciais
- Alertar sobre consumos excessivos
- Fornecer estatísticas detalhadas para tomada de decisão
- Promover o uso consciente dos recursos hídricos

## 👥 Equipe

- **Desenvolvedores**: [Nomes dos membros da equipe]
- **Disciplina**: Programação Orientada a Objetos
- **Instituição**: [Nome da instituição]

## ✨ Funcionalidades

### Menu Principal (9 opções)

1. **Cadastrar Usuário Residencial** - Registro de usuários domésticos
2. **Cadastrar Usuário Comercial** - Registro de empresas com CNPJ
3. **Registrar Consumo de Água** - Adicionar leituras de consumo com data/hora
4. **Ver Consumo Registrado** - Listar todos os consumos por usuário
5. **Calcular Consumo Total** - Totalizar o consumo de cada usuário
6. **Ver Alerta de Consumo** - Verificar alertas de consumo alto/crítico
7. **Ver Estatísticas Detalhadas** - Análise completa com média, máximo e mínimo
8. **Relatório Geral do Sistema** - Visão geral de todos os usuários
9. **Sair** - Encerrar o sistema

## 🛠️ Tecnologias e Conceitos

### Linguagem
- **Python 3.8+**

### Bibliotecas Utilizadas
- `abc` - Classes e métodos abstratos
- `datetime` - Manipulação de datas e horários

### Conceitos de POO Implementados

#### ✅ Classes
- `Pessoa` (abstrata)
- `Usuario`
- `UsuarioComercial`
- `Consumo`
- `Alerta` (abstrata)
- `AlertaSimples`
- `AlertaCritico`
- `GerenciadorConsumo`
- `SistemaMenu`

#### ✅ Herança
- **Herança Simples**: `Usuario` herda de `Pessoa`
- **Herança Multinível**: `UsuarioComercial` herda de `Usuario` que herda de `Pessoa`
- **Herança com Classes Abstratas**: `AlertaSimples` e `AlertaCritico` herdam de `Alerta`

#### ✅ Encapsulamento
- Atributos privados com `__` (ex: `__nome`, `__consumos`, `__usuarios`)
- Uso de `@property` para controle de acesso
- Métodos públicos para manipulação controlada de dados

#### ✅ Polimorfismo
- Método `exibir_info()` implementado de forma diferente em `Usuario` e `UsuarioComercial`
- Método `verificar()` implementado de forma diferente em `AlertaSimples` e `AlertaCritico`

#### ✅ Associação
- `GerenciadorConsumo` trabalha com objetos `Usuario` e `Alerta` sem possuí-los exclusivamente

#### ✅ Agregação
- `Usuario` possui uma lista de objetos `Consumo`, mas os consumos podem existir independentemente

#### ✅ Composição
- `SistemaMenu` possui um `GerenciadorConsumo` que só existe enquanto o sistema existe

### Outros Conceitos Aplicados

- ✅ **Condicionais** (if/elif/else)
- ✅ **Laços de repetição** (for, while)
- ✅ **Funções** (métodos e função principal)
- ✅ **Listas** (armazenamento de usuários e consumos)
- ✅ **Dicionários** (estatísticas e relatórios)
- ✅ **Tratamento de exceções** (try/except ValueError)
- ✅ **Validação de entradas** (verificação de tipos e valores)

## 🚀 Como Executar

### Pré-requisitos
```bash
python --version  # Python 3.8 ou superior
```

### Instalação e Execução

1. Clone o repositório:
```bash
git clone https://github.com/naylacastro/projetoODS6.git
cd projetoODS6
```

2. Execute o programa:
```bash
python main.py
```

## 📊 Exemplo de Uso

```
=== Controle de Consumo de Água ===
1 - Cadastrar Usuário Residencial
2 - Cadastrar Usuário Comercial
3 - Registrar Consumo de Água
4 - Ver Consumo Registrado
5 - Calcular Consumo Total
6 - Ver Alerta de Consumo
7 - Ver Estatísticas Detalhadas
8 - Relatório Geral do Sistema
9 - Sair

Escolha uma opção: 1
Nome do usuário: João Silva
Usuário: João Silva | Tipo: Residencial cadastrado com sucesso!
```

## 📈 Sistema de Alertas

O sistema possui dois níveis de alerta:

- **⚠️ Alerta Simples**: Consumo acima de 200L
- **🚨 Alerta Crítico**: Consumo acima de 300L (150% do limite)

## 📝 Estrutura do Código

```
projetoODS6/
│
├── main.py           # Ponto de entrada do programa
├── sistema.py        # Código principal com todas as classes
├── README.md         # Este arquivo
└── __pycache__/      # Arquivos compilados Python
```

## 🤖 Uso de IA Generativa

Este projeto utilizou **GitHub Copilot** como ferramenta auxiliar para:

- ✅ Sugestão de docstrings e comentários
- ✅ Refatoração de código para melhor legibilidade
- ✅ Identificação de boas práticas em Python

**Importante**: Todos os conceitos de POO foram implementados manualmente com compreensão completa da equipe. A IA foi utilizada apenas como assistente de produtividade, não como substituto do aprendizado.

## 📚 Documentação Adicional

### Recursos sobre ODS 6
- [ONU Brasil - ODS 6](https://brasil.un.org/pt-br/sdgs/6)
- [Agenda 2030](https://brasil.un.org/pt-br/sdgs)

### Boas Práticas Python
- [PEP 8 - Style Guide](https://pep8.org/)
- [Python Docstrings](https://www.python.org/dev/peps/pep-0257/)

## 📄 Licença

Este projeto está sob a licença GPL-3.0. Veja o arquivo `LICENSE` para mais detalhes.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abrir um Pull Request

## 📞 Contato

- **Repositório**: [github.com/naylacastro/projetoODS6](https://github.com/naylacastro/projetoODS6)
- **Issues**: Para reportar bugs ou sugerir melhorias

---

💧 **Desenvolvido com foco em sustentabilidade e uso consciente da água**
