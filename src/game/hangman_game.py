import random

class HangmanGame:
    def __init__(self):
        """
        Construtor da classe HangmanGame.
        Inicializa a lista de palavras, seleciona uma palavra aleatória e define os conjuntos de letras corretas e erradas.
        Define o número máximo de tentativas.
        """
        # Lista de palavras disponíveis para o jogo
        self.words = ['CLUSTER', 'PREVISAO', 'RASTREIO', 'LEGISLACAO', 'CAMADA', 'APLICACAO', 'ALGORITMO', 
                        'FISICA', 'AUDITORIA', 'DOUTRINA', 'TRANSFORMACAO', 'CLIENTE', 'INFOGRAFICO', 'ALUNO', 
                        'CLIENTES', 'BALANCO', 'ARVORE', 'RELATORIOS', 'PARAMETRO', 'IMPOSTOS', 'INSTALACAO', 
                        'VENDAS', 'COMPUTACAO', 'CONTROLE', 'ESCOLA', 'PARCEIROS', 'USUARIOS', 'FINANCEIRO', 
                        'CANETA', 'REPUTACAO', 'PROCESSADOR', 'RESPONSABILIDADE', 'PROBABILIDADE', 'TATICAS', 
                        'INFORMACAO', 'CADEIRA', 'LOUSA', 'PROGRAMA', 'ARBITRAGEM', 'PUBLICA', 'SUPORTE', 
                        'ESTUDO', 'BIG', 'TRIBUTACAO', 'TABELAS', 'DOMINIO', 'PASTA', 'PAINEL', 'PRECISAO', 
                        'NEGOCIACOES', 'ESTRATEGIA', 'INOVACAO', 'FINANCEIRA', 'DATAGRAMAS', 'LINEAR', 'REDE', 
                        'ARQUIVO', 'CRIPTOGRAFIA', 'CONTROLADORIA', 'PREFERENCIA', 'REGISTRO', 'FISCAL', 'LAPIS', 
                        'METRICA', 'PADRAO', 'APONTADOR', 'QUADRO', 'ADVOCACIA', 'DATA', 'PROCESSOS', 
                        'DESENVOLVIMENTO', 'VALIDACAO', 'SUSTENTABILIDADE', 'FORCA', 'SATISFACAO', 'GRAFICOS', 
                        'BRANDING', 'LUCROS', 'DIRETORIO', 'TRANSFERENCIA', 'INDICADORES', 'TESTE', 'CONTABILIDADE', 
                        'TRANSPARENCIA', 'ATENDIMENTO', 'SERVIDOR', 'COMPUTADOR', 'ACURACIA', 'NUVEM', 'BARRAMENTO', 
                        'SALA', 'QUADROS', 'SINAL', 'SEGMENTACAO', 'DIAGRAMAS', 'NORMAS', 'MARKETING', 'PACOTE', 
                        'PROGRAMACAO', 'DADOS', 'PACOTES', 'DESVIO', 'CIRCUITOS', 'PROPAGANDA', 'ETICA', 'CADERNO', 
                        'ENSINO', 'AULA', 'CONTA', 'ENDERECO', 'LEITURA', 'EQUIPE', 'CORPORATIVA', 'MEMORIA', 'KPI', 
                        'AVALIACAO', 'FEEDBACK', 'SCANNER', 'RENTABILIDADE', 'ARTIFICIAL', 'VOIP', 'MEDIANA', 
                        'RESULTADOS', 'REGULACAO', 'FINANCAS', 'COLABORADORES', 'PRODUTO', 'NACIONAL', 'FINANCEIRAS', 
                        'RECEITAS', 'REFERENCIA', 'SISTEMA', 'LIVRO', 'USUARIO', 'SOCIAL', 'BITS', 'AGRUPAMENTO', 
                        'ACORDOS', 'CABO', 'PROTOTIPO', 'CONTRIBUICOES', 'REGULAMENTOS', 'VARIANCIA', 'CRESCIMENTO', 
                        'SOFTWARE', 'ENLACE', 'FLORESTA', 'MODELO', 'LOGIN', 'REGRESSAO', 'DIREITO', 'FUNCIONARIOS', 
                        'LOCAL', 'AMBIENTAL', 'SERVICO', 'PORTA', 'UPLOAD', 'SESSAO', 'PATRIMONIAL', 'MENSAGEM', 
                        'DIGITAL', 'ACOES', 'ESTRELA', 'PUBLICIDADE', 'APLICATIVO', 'FIREWALL', 'ENDIVIDAMENTO', 
                        'DOWNLOAD', 'ALEATORIA', 'METROPOLITANA', 'BACKUP', 'AMPLA', 'METRICAS', 'BATERIA', 
                        'TECLADO', 'PROTOCOLO', 'CIENCIA', 'LIDERANCA', 'IMAGEM', 'LANCAMENTO', 'ROTAS', 
                        'COMPLIANCE', 'SEGMENTOS', 'PRIVADA', 'CORRELACAO', 'ANALISE', 'ENERGIA', 'IMPLEMENTACAO', 
                        'PROFESSOR', 'MAPAS', 'TRANSPORTE', 'CONFORMIDADE', 'DECISAO', 'MESA', 'ACESSO', 'VPN', 
                        'ANEL', 'RELATORIO', 'TREINAMENTO', 'CLASSIFICACAO', 'FORNECEDORES', 'INVESTIMENTOS', 'ESCRITA', 
                        'IMPRESSORA', 'ANALISE', 'CADASTRO', 'GOVERNANCA', 'DEEP', 'LITIGIOS', 'VIRTUAL', 'EFICIENCIA', 
                        'APRESENTACAO', 'GESTAO', 'INTELIGENCIA', 'INTERNET', 'MERCADO', 'COMPETITIVIDADE', 'LOGISTICA', 
                        'INTERNACIONAL', 'CONTRATOS', 'MOUSE', 'SEGURANCA', 'PROCEDIMENTOS', 'ANTIVIRUS', 'INTRANET', 
                        'VARIAVEL', 'POLITICAS', 'TOPOLOGIA', 'ECONOMIA', 'LEARNING', 'METAS', 'UNIVERSIDADE', 'GLOBAL', 
                        'TELA', 'ESTATISTICA', 'SINTESE', 'CUSTOS', 'MONITORAMENTO', 'BLOCOS', 'MEDIA', 'TECNOLOGIA', 
                        'SOLVENCIA', 'MODA', 'DOCUMENTO', 'CONFIGURACAO', 'MONITOR'
                        ]
        # Filtra palavras que não contenham as letras proibidas
        self.words = [word for word in self.words if not any(c in word for c in "jhçyzx")]
        # Seleciona uma palavra aleatória da lista filtrada
        self.selected_word = random.choice(self.words)
        # Conjuntos para armazenar letras corretas e erradas adivinhadas pelo jogador
        self.correct_letters = set()
        self.wrong_letters = set()
        # Define o número máximo de tentativas
        self.max_attempts = 6

    def guess(self, letter):
        """
        Verifica se a letra adivinhada está na palavra selecionada.
        Adiciona a letra ao conjunto de letras corretas ou erradas, conforme apropriado.

        Parâmetros:
        letter (str): A letra adivinhada pelo jogador.
        """
        if letter in self.selected_word:
            self.correct_letters.add(letter)
        else:
            self.wrong_letters.add(letter)

    def display_word(self):
        """
        Gera uma string que representa a palavra com as letras adivinhadas até agora.
        Letras não adivinhadas são representadas por underscores (_).

        Retorna:
        str: A palavra com letras adivinhadas e underscores para letras não adivinhadas.
        """
        return ' '.join([letter if letter in self.correct_letters else '_' for letter in self.selected_word])

    def is_won(self):
        """
        Verifica se o jogador ganhou o jogo.

        Retorna:
        bool: True se o jogador adivinhou todas as letras da palavra, False caso contrário.
        """
        return set(self.selected_word).issubset(self.correct_letters)

    def is_lost(self):
        """
        Verifica se o jogador perdeu o jogo.

        Retorna:
        bool: True se o número de tentativas erradas atingiu o máximo permitido, False caso contrário.
        """
        return len(self.wrong_letters) >= self.max_attempts

    def remaining_attempts(self):
        """
        Calcula o número de tentativas restantes.

        Retorna:
        int: O número de tentativas restantes.
        """
        return self.max_attempts - len(self.wrong_letters)

    def get_wrong_letters(self):
        """
        Gera uma string com todas as letras erradas adivinhadas até agora.

        Retorna:
        str: As letras erradas separadas por espaços.
        """
        return ' '.join(self.wrong_letters)
