"""
Sistema de Controle de Consumo de Água
Tema: ODS 6 - Água Potável e Saneamento
Este sistema permite o cadastro de usuários e monitoramento do consumo de água,
contribuindo para o uso consciente e sustentável dos recursos hídricos.
"""

from abc import ABC, abstractmethod
from datetime import datetime


class Pessoa(ABC):
    """
    Classe abstrata que representa uma pessoa no sistema.
    Implementa encapsulamento com atributo privado.
    """
    
    def __init__(self, nome):
        """
        Inicializa uma pessoa com nome.
        
        Args:
            nome (str): Nome da pessoa
        """
        self.__nome = nome
    
    @property
    def nome(self):
        """Retorna o nome da pessoa (encapsulamento)."""
        return self.__nome
    
    @abstractmethod
    def exibir_info(self):
        """Método abstrato para exibir informações (polimorfismo)."""
        pass


class Usuario(Pessoa):
    """
    Classe que representa um usuário residencial.
    Herda de Pessoa e implementa polimorfismo.
    Demonstra agregação com a lista de consumos.
    """
    
    def __init__(self, nome, tipo="Residencial"):
        """
        Inicializa um usuário.
        
        Args:
            nome (str): Nome do usuário
            tipo (str): Tipo de usuário (padrão: Residencial)
        """
        super().__init__(nome)
        self.__tipo = tipo
        self.__consumos = []  # Agregação: usuário possui consumos
    
    @property
    def tipo(self):
        """Retorna o tipo de usuário."""
        return self.__tipo
    
    @property
    def consumos(self):
        """Retorna a lista de consumos do usuário."""
        return self.__consumos
    
    def adicionar_consumo(self, consumo):
        """
        Adiciona um registro de consumo ao usuário.
        
        Args:
            consumo (Consumo): Objeto do tipo Consumo
        """
        self.__consumos.append(consumo)
    
    def exibir_info(self):
        """Implementação polimórfica: exibe informações do usuário."""
        return f"Usuário: {self.nome} | Tipo: {self.__tipo}"
    
    def calcular_total(self):
        """
        Calcula o consumo total de água do usuário.
        
        Returns:
            float: Total de litros consumidos
        """
        return sum(c.valor for c in self.__consumos)
    
    def obter_estatisticas(self):
        """
        Retorna estatísticas de consumo usando dicionário.
        
        Returns:
            dict: Dicionário com estatísticas de consumo
        """
        if len(self.__consumos) == 0:
            return {
                "total": 0,
                "media": 0,
                "quantidade_registros": 0,
                "maior_consumo": 0,
                "menor_consumo": 0
            }
        
        valores = [c.valor for c in self.__consumos]
        return {
            "total": sum(valores),
            "media": sum(valores) / len(valores),
            "quantidade_registros": len(valores),
            "maior_consumo": max(valores),
            "menor_consumo": min(valores)
        }


class UsuarioComercial(Usuario):
    """
    Classe que representa um usuário comercial (empresa).
    Demonstra herança multinível: Pessoa -> Usuario -> UsuarioComercial.
    """
    
    def __init__(self, nome, cnpj):
        """
        Inicializa um usuário comercial.
        
        Args:
            nome (str): Nome da empresa
            cnpj (str): CNPJ da empresa
        """
        super().__init__(nome, "Comercial")
        self.__cnpj = cnpj
    
    def exibir_info(self):
        """Implementação polimórfica específica para usuário comercial."""
        return f"Empresa: {self.nome} | CNPJ: {self.__cnpj} | Tipo: {self.tipo}"


class Consumo:
    """
    Classe que representa um registro de consumo de água.
    Encapsula informações sobre valor e data do consumo.
    """
    
    def __init__(self, valor, data=None):
        """
        Inicializa um registro de consumo.
        
        Args:
            valor (float): Quantidade de água consumida em litros
            data (datetime, optional): Data do consumo. Se None, usa data/hora atual
        """
        self.__valor = valor
        self.__data = data if data else datetime.now()
    
    @property
    def valor(self):
        """Retorna o valor do consumo em litros."""
        return self.__valor
    
    @property
    def data(self):
        """Retorna a data do registro."""
        return self.__data
    
    def __str__(self):
        """Representação em string do consumo."""
        return f"{self.__valor}L em {self.__data.strftime('%d/%m/%Y %H:%M')}"


class Alerta(ABC):
    """
    Classe abstrata para sistema de alertas de consumo.
    Base para implementação de diferentes tipos de alertas (polimorfismo).
    """
    
    def __init__(self, limite):
        """
        Inicializa um alerta com limite de consumo.
        
        Args:
            limite (float): Limite de consumo em litros
        """
        self._limite = limite  # Atributo protegido
    
    @abstractmethod
    def verificar(self, consumo):
        """
        Método abstrato para verificar se o consumo excede o limite.
        
        Args:
            consumo (float): Valor do consumo a ser verificado
        
        Returns:
            str ou None: Mensagem de alerta ou None se não houver alerta
        """
        pass


class AlertaSimples(Alerta):
    """Implementação de alerta simples para consumo moderadamente alto."""
    
    def verificar(self, consumo):
        """Verifica se o consumo está acima do limite."""
        if consumo > self._limite:
            return f"⚠️  CONSUMO ALTO: {consumo}L (Limite: {self._limite}L)"
        return None


class AlertaCritico(Alerta):
    """Implementação de alerta crítico para consumo muito alto."""
    
    def verificar(self, consumo):
        """Verifica se o consumo está 50% acima do limite."""
        if consumo > self._limite * 1.5:
            return f"🚨 CONSUMO CRÍTICO: {consumo}L (Limite: {self._limite}L)"
        return None


class GerenciadorConsumo:
    """
    Classe que gerencia usuários e alertas do sistema.
    Demonstra associação: usa objetos Usuario e Alerta sem possuí-los exclusivamente.
    """
    
    def __init__(self):
        """Inicializa o gerenciador com listas vazias."""
        self.__usuarios = []
        self.__alertas = [AlertaSimples(200), AlertaCritico(200)]
    
    def adicionar_usuario(self, usuario):
        """
        Adiciona um usuário ao sistema.
        
        Args:
            usuario (Usuario): Objeto do tipo Usuario ou UsuarioComercial
        """
        self.__usuarios.append(usuario)
    
    def buscar_usuario(self, nome):
        """
        Busca um usuário pelo nome.
        
        Args:
            nome (str): Nome do usuário a buscar
        
        Returns:
            Usuario ou None: Usuário encontrado ou None
        """
        for usuario in self.__usuarios:
            if usuario.nome.lower() == nome.lower():
                return usuario
        return None
    
    def listar_usuarios(self):
        """Retorna a lista de todos os usuários."""
        return self.__usuarios
    
    def verificar_alertas(self, usuario):
        """
        Verifica alertas de consumo para um usuário.
        
        Args:
            usuario (Usuario): Usuário a verificar
        
        Returns:
            list: Lista de mensagens de alerta
        """
        total = usuario.calcular_total()
        alertas_ativos = []
        for alerta in self.__alertas:
            msg = alerta.verificar(total)
            if msg:
                alertas_ativos.append(msg)
        return alertas_ativos
    
    def gerar_relatorio_geral(self):
        """
        Gera um relatório geral do sistema usando dicionários.
        
        Returns:
            dict: Dicionário com estatísticas gerais do sistema
        """
        if len(self.__usuarios) == 0:
            return {
                "total_usuarios": 0,
                "consumo_total_sistema": 0,
                "media_por_usuario": 0
            }
        
        consumo_total = sum(u.calcular_total() for u in self.__usuarios)
        return {
            "total_usuarios": len(self.__usuarios),
            "consumo_total_sistema": consumo_total,
            "media_por_usuario": consumo_total / len(self.__usuarios),
            "usuarios_com_alerta": sum(1 for u in self.__usuarios if len(self.verificar_alertas(u)) > 0)
        }


class SistemaMenu:
    """
    Classe principal que gerencia o menu e interações do sistema.
    Demonstra composição: SistemaMenu possui um GerenciadorConsumo.
    """
    
    def __init__(self):
        """Inicializa o sistema com um gerenciador de consumo."""
        self.__gerenciador = GerenciadorConsumo()  # Composição
    
    def mostrar_menu(self):
        """Exibe o menu principal com todas as opções disponíveis."""
        print("\n=== Controle de Consumo de Água ===")
        print("1 - Cadastrar Usuário Residencial")
        print("2 - Cadastrar Usuário Comercial")
        print("3 - Registrar Consumo de Água")
        print("4 - Ver Consumo Registrado")
        print("5 - Calcular Consumo Total")
        print("6 - Ver Alerta de Consumo")
        print("7 - Ver Estatísticas Detalhadas")
        print("8 - Relatório Geral do Sistema")
        print("9 - Sair")
    
    def cadastrar_usuario_residencial(self):
        """Cadastra um novo usuário residencial no sistema."""
        nome = input("Nome do usuário: ")
        usuario = Usuario(nome)
        self.__gerenciador.adicionar_usuario(usuario)
        print(f"{usuario.exibir_info()} cadastrado com sucesso!")
    
    def cadastrar_usuario_comercial(self):
        """Cadastra um novo usuário comercial (empresa) no sistema."""
        nome = input("Nome da empresa: ")
        cnpj = input("CNPJ: ")
        usuario = UsuarioComercial(nome, cnpj)
        self.__gerenciador.adicionar_usuario(usuario)
        print(f"{usuario.exibir_info()} cadastrado com sucesso!")
    
    def registrar_consumo(self):
        """Registra um novo consumo de água para um usuário existente."""
        usuarios = self.__gerenciador.listar_usuarios()
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado. Cadastre um usuário primeiro.")
            return
        
        print("\nUsuários disponíveis:")
        for i, usuario in enumerate(usuarios):
            print(f"{i + 1} - {usuario.exibir_info()}")
        
        # Validação de entrada com tratamento de exceção
        try:
            indice = int(input("Escolha o número do usuário: ")) - 1
            if indice < 0 or indice >= len(usuarios):
                print("Usuário inválido.")
                return
            
            valor = float(input("Informe o consumo em litros: "))
            if valor < 0:
                print("O consumo não pode ser negativo.")
                return
            
            consumo = Consumo(valor)
            usuarios[indice].adicionar_consumo(consumo)
            print(f"Consumo de {valor}L registrado para {usuarios[indice].nome}.")
        except ValueError:
            print("Erro: Digite um valor numérico válido.")
    
    def ver_consumo(self):
        """Exibe todos os consumos registrados no sistema."""
        usuarios = self.__gerenciador.listar_usuarios()
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.")
            return
        
        print("\nConsumos registrados:")
        for usuario in usuarios:
            print(f"\n{usuario.exibir_info()}")
            if len(usuario.consumos) == 0:
                print("  Nenhum consumo registrado")
            else:
                for consumo in usuario.consumos:
                    print(f"  - {consumo}")
    
    def calcular_consumo_total(self):
        """Calcula e exibe o consumo total de cada usuário."""
        usuarios = self.__gerenciador.listar_usuarios()
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.")
            return
        
        print("\nConsumo total por usuário:")
        for usuario in usuarios:
            total = usuario.calcular_total()
            print(f"{usuario.nome}: {total}L")
    
    def ver_alerta_consumo(self):
        """Verifica e exibe alertas de consumo excessivo."""
        usuarios = self.__gerenciador.listar_usuarios()
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.")
            return
        
        print("\nAlertas de consumo:")
        tem_alerta = False
        for usuario in usuarios:
            alertas = self.__gerenciador.verificar_alertas(usuario)
            if alertas:
                tem_alerta = True
                print(f"\n{usuario.nome}:")
                for alerta in alertas:
                    print(f"  {alerta}")
        
        if not tem_alerta:
            print("Nenhum alerta ativo. Consumo dentro do normal.")
    
    def ver_estatisticas_detalhadas(self):
        """Exibe estatísticas detalhadas usando dicionários."""
        usuarios = self.__gerenciador.listar_usuarios()
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.")
            return
        
        print("\n=== Estatísticas Detalhadas por Usuário ===")
        for usuario in usuarios:
            stats = usuario.obter_estatisticas()  # Retorna dicionário
            print(f"\n{usuario.nome}:")
            print(f"  Total consumido: {stats['total']}L")
            print(f"  Média de consumo: {stats['media']:.2f}L")
            print(f"  Quantidade de registros: {stats['quantidade_registros']}")
            if stats['quantidade_registros'] > 0:
                print(f"  Maior consumo: {stats['maior_consumo']}L")
                print(f"  Menor consumo: {stats['menor_consumo']}L")
    
    def ver_relatorio_geral(self):
        """Exibe relatório geral do sistema usando dicionários."""
        relatorio = self.__gerenciador.gerar_relatorio_geral()  # Retorna dicionário
        
        print("\n=== Relatório Geral do Sistema ===")
        print(f"Total de usuários: {relatorio['total_usuarios']}")
        print(f"Consumo total do sistema: {relatorio['consumo_total_sistema']}L")
        
        if relatorio['total_usuarios'] > 0:
            print(f"Média de consumo por usuário: {relatorio['media_por_usuario']:.2f}L")
            print(f"Usuários com alerta ativo: {relatorio['usuarios_com_alerta']}")
    
    def executar(self):
        """Loop principal do sistema com menu interativo."""
        opcao = 0
        
        # Loop while para manter o menu ativo
        while opcao != 9:
            self.mostrar_menu()
            try:
                opcao = int(input("\nEscolha uma opção: "))
                
                # Estrutura condicional (if/elif/else) para navegação no menu
                if opcao == 1:
                    self.cadastrar_usuario_residencial()
                
                elif opcao == 2:
                    self.cadastrar_usuario_comercial()
                
                elif opcao == 3:
                    self.registrar_consumo()
                
                elif opcao == 4:
                    self.ver_consumo()
                
                elif opcao == 5:
                    self.calcular_consumo_total()
                
                elif opcao == 6:
                    self.ver_alerta_consumo()
                
                elif opcao == 7:
                    self.ver_estatisticas_detalhadas()
                
                elif opcao == 8:
                    self.ver_relatorio_geral()
                
                elif opcao == 9:
                    print("Saindo do sistema...")
                
                else:
                    print("Opção inválida. Escolha entre 1 e 9.")
            
            except ValueError:
                # Tratamento de exceção para entradas inválidas
                print("Erro: Digite um número válido.")


def menu():
    """Função principal para iniciar o sistema."""
    sistema = SistemaMenu()
    sistema.executar()

 