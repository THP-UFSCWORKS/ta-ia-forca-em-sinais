## FORCA EM SINAIS - PROJETO NACIONAL

[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)
[![Contributing](https://img.shields.io/badge/contributing-guide-orange)](CONTRIBUTING.md)

---

## Descrição

**Forca em Sinais** é um jogo interativo de forca onde os jogadores utilizam sinais de Libras (Língua Brasileira de Sinais) para adivinhar as letras da palavra secreta. O jogo utiliza visão computacional para detectar e reconhecer os sinais feitos pelo jogador. Vale ressaltar, que tal jogo foi desenvolvido, inicialmente, para a disciplina de Tópicos Avançados em Inteligência Artificail,do curso de Engenharia de Computação da UFSC.

## Índice

- [Instalação](#instalação)
- [Uso com Docker](#uso-com-docker)
- [Visão Computacional e YOLOv5](#visão-computacional-e-yolov5)
- [Contribuindo](#contribuindo)
- [Licença](#licença)
- [Autores](#autores)
- [Agradecimentos](#agradecimentos)

## Instalação

Você pode rodar este projeto de duas formas:
- Manualmente, instalando Python e dependências (detalhado abaixo)
- **OU** com Docker Compose (recomendado)

### Instalação manual (modo alternativo)

### Pré-requisitos

- Python 3.6+
- Git
- [OpenCV](https://opencv.org/)
- [PyQt5](https://pypi.org/project/PyQt5/)
- [Ultralytics YOLO](https://github.com/ultralytics/yolov5)

### Passos de Instalação

```bash
git clone https://github.com/THP-UFSCWORKS/ta-ia-forca-em-sinais.git
cd forca-em-sinais

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
python src/main.py
```

> Certifique-se de ter o modelo YOLO em `src/data/train/weights/best.pt`

### Uso com Docker

### Pré-requisitos
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

#### 1. Clonar o projeto
```bash
git clone https://github.com/THP-UFSCWORKS/ta-ia-forca-em-sinais.git
cd forca-em-sinais
```

#### 2. Preparar ambiente (Linux)
```bash
xhost +local:docker
```

#### 3. Rodar com Docker Compose
```bash
docker-compose up --build  # Primeira vez
```
Depois, pode rodar apenas:
```bash
docker-compose up
```

### Para usuários Windows/macOS

Rodar interfaces gráficas com PyQt5 via Docker no Windows/macOS exige um servidor X. Siga os passos abaixo:

#### Passo 1: Instalar um servidor X
- Baixe e instale o [VcXsrv](https://sourceforge.net/projects/vcxsrv/) no Windows (ou [XQuartz](https://www.xquartz.org/) no macOS)

#### Passo 2: Iniciar o servidor X
- Abra o VcXsrv com as seguintes opções:
  - **Multiple windows**
  - **Start no client**
  - Marque a opção **Disable access control**

#### Passo 3: Criar ou editar o arquivo `.env` na raiz do projeto
```env
DISPLAY=host.docker.internal:0
MODEL_PATH=src/data/train/weights/best.pt
```

#### Passo 4: Executar o projeto
```bash
docker-compose up --build
```

> Observação: o acesso à câmera pode não funcionar nativamente no Windows. Para testes, você pode adaptar o código para usar um vídeo gravado em vez da câmera ao vivo.

---

### Controles do Jogo

- **Iniciar Jogo**: Começa uma nova partida de forca.
- **Sair**: Fecha a aplicação.
- **Pressionar 'Q'**: Fecha a janela do jogo.

### Regras do Jogo

1. O jogo seleciona uma palavra aleatória de uma lista predefinida.
2. O jogador deve fazer os sinais de Libras para adivinhar as letras da palavra.
3. Se a letra estiver correta, ela aparecerá na palavra.
4. Se a letra estiver incorreta, ela será adicionada à lista de letras usadas.
5. O jogo termina quando o jogador adivinha a palavra ou errar por 6 (seis) tentativas.

## Visão Computacional e YOLOv5

### Visão Computacional

A visão computacional é uma área da inteligência artificial que permite aos computadores interpretar e compreender o mundo visual. Utilizando técnicas de processamento de imagem, os sistemas de visão computacional podem realizar tarefas como reconhecimento de objetos, detecção de movimento e análise de imagem. No projeto **Forca em Sinais**, a visão computacional é utilizada para detectar e reconhecer os sinais de Libras feitos pelos jogadores, convertendo-os em letras que são usadas no jogo da forca.

### YOLOv5

O **YOLOv5** (You Only Look Once) é uma família de modelos de detecção de objetos desenvolvida pela Ultralytics. Ele é conhecido por sua precisão e eficiência em tempo real, tornando-o ideal para aplicações que exigem processamento rápido de imagens, como jogos interativos. No nosso projeto, utilizamos o YOLOv5 para treinar um modelo capaz de reconhecer sinais de Libras.

#### Como Funciona o YOLOv5

1. **Entrada de Imagem**: O modelo recebe uma imagem de entrada e a divide em uma grade.
2. **Predição de Caixa**: Em cada célula da grade, o modelo faz várias previsões de caixas delimitadoras, cada uma com uma pontuação de confiança e uma previsão de classe.
3. **Filtragem de Caixas**: As caixas com baixa confiança são descartadas, e as previsões restantes são refinadas para melhorar a precisão.
4. **Classificação e Localização**: O modelo retorna as classes dos objetos detectados e suas localizações precisas na imagem.

O YOLOv5 é treinado usando um conjunto de dados de sinais de Libras, permitindo que ele reconheça e categorize corretamente os diferentes sinais durante o jogo.

## Contribuindo

Contribuições são bem-vindas! Por favor, leia o [guia de contribuição](CONTRIBUTING.md) para mais detalhes sobre como começar.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Author

Veja a lista completa de [colaboradores](https://github.com/theHprogrammer/forca-em-sinais/graphs/contributors) que participaram deste projeto.

<table align="center">
    <tr>
        <td align="center">
            <a href="https://github.com/theHprogrammer">
                <img src="https://avatars.githubusercontent.com/u/79870881?v=4" width="150px;" alt="Helder's Image" />
                <br />
                <sub><b>Helder Henrique</b></sub>
            </a>
        </td>    
    </tr>
</table>
<h4 align="center">
   By: <a href="https://www.linkedin.com/in/theHprogrammer/" target="_blank"> Helder Henrique </a>
</h4>


