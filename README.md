## FORCA EM SINAIS - PROJETO NACIONAL

[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)
[![Contributing](https://img.shields.io/badge/contributing-guide-orange)](CONTRIBUTING.md)

---

## Descrição

**Forca em Sinais** é um jogo interativo de forca onde os jogadores utilizam sinais de Libras (Língua Brasileira de Sinais) para adivinhar as letras da palavra secreta. O jogo utiliza visão computacional para detectar e reconhecer os sinais feitos pelo jogador. Vale ressaltar, que tal jogo foi desenvolvido, inicialmente, para a disciplina de Tópicos Avançados em Inteligência Artificail,do curso de Engenharia de Computação da UFSC.

## Índice

- [Instalação](#instalação)
- [Uso](#uso)
- [Visão Computacional e YOLOv5](#visão-computacional-e-yolov5)
- [Contribuindo](#contribuindo)
- [Licença](#licença)
- [Autores](#autores)
- [Agradecimentos](#agradecimentos)

## Instalação

### Pré-requisitos

- Python 3.6+
- Git
- [OpenCV](https://opencv.org/)
- [PyQt5](https://pypi.org/project/PyQt5/)
- [Ultralytics YOLO](https://github.com/ultralytics/yolov5)

### Passos de Instalação

1. Faça um fork do repositório:

   ```bash
   git clone https://github.com/seu-usuario/forca-em-sinais.git
   cd forca-em-sinais
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Para Windows: .venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Certifique-se de que você tem o modelo YOLO treinado em `src/data/train/weights/best.pt`. Se necessário, ajuste o caminho no código para corresponder à localização do seu modelo. Ajuste o caminho em `src/app/gui.py`.

5. Ajuste o caminho dos plugins do Qt no `main.py`:

   ```python
   import os
   # Trocar o path para o diretório onde estão os plugins do Qt
   os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "seu_caminho_aqui/forca_em_sinais/.venv/lib/python3.12/site-packages/cv2/qt/plugins"
   ```

## Uso

Para iniciar o jogo, execute o script `main.py`:

```bash
python src/main.py
```

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


