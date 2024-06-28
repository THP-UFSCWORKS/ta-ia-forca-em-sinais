# pylint: disable=no-name-in-module, import-error, invalid-name
from collections import Counter  # Import padrão deve vir antes dos imports de terceiros
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap, QImage
import cv2
from detection.sign_detector_realtime import SignDetectorRealTime
from game.hangman_game import HangmanGame

# Definindo uma classe auxiliar para a interface do usuário
class UIComponents:
    def __init__(self, parent):
        self.camera_label = QLabel(parent)
        self.word_label = QLabel(parent)
        self.used_letters_label = QLabel("Letras Usadas: ", parent)
        self.hangman_label = QLabel(parent)

# Definindo uma classe auxiliar para o jogo
class GameAttributes:
    def __init__(self):
        self.game = HangmanGame()
        self.prediction_window = []  # Janela deslizante para previsões
        self.window_size = 10  # Tamanho da janela deslizante
        self.class_mapping = {
            'D1': 'D',
            'D2': 'D',
            # Adicione outros mapeamentos conforme necessário
        }

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jogo da Forca com Sinais")
        self.setGeometry(100, 100, 800, 600)
        self.game_window = None  # Inicialize o atributo no __init__
        self.init_ui()

    def init_ui(self):
        """
        Inicializa a interface do usuário para a tela inicial.
        """
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.start_button = QPushButton("Iniciar Jogo", self)
        self.start_button.clicked.connect(self.start_game)
        self.layout.addWidget(self.start_button)

        self.exit_button = QPushButton("Sair", self)
        self.exit_button.clicked.connect(self.close)
        self.layout.addWidget(self.exit_button)

    def start_game(self):
        """
        Esconde a tela inicial e mostra a tela do jogo.
        """
        self.hide()
        self.game_window = GameWindow()  # Defina o atributo dentro do método
        self.game_window.show()

class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jogo da Forca com Sinais")
        self.setGeometry(100, 100, 800, 600)
        self.detector = SignDetectorRealTime("/home/thehprogrammer/Documentos/Creche/up_to_date/Semester_08/IA2/forca_em_sinais/data/train/weights/best.pt")  # Atualize este caminho conforme necessário
        self.detector.load_model()
        self.ui = UIComponents(self)
        self.game_attr = GameAttributes()
        self.init_ui()

    def init_ui(self):
        """
        Inicializa a interface do usuário para a tela do jogo.
        """
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Layout para câmera e forca
        self.layout.addWidget(self.ui.camera_label)
        self.layout.addWidget(self.ui.word_label)
        self.layout.addWidget(self.ui.used_letters_label)
        self.layout.addWidget(self.ui.hangman_label)

        # Iniciar captura de vídeo
        self.capture = cv2.VideoCapture(0)

        # Timer para atualização do frame
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def update_frame(self):
        """
        Atualiza o frame da câmera, faz a predição e processa os resultados.
        """
        ret, frame = self.capture.read()
        if ret:
            self.detector.predict(frame)
            frame = self.detector.process_results(frame)
            self.display_camera(frame)
            self.update_game()

    def display_camera(self, frame):
        """
        Converte o frame capturado para o formato correto e exibe na interface.
        
        Parâmetros:
        frame (numpy.ndarray): Frame de vídeo capturado da câmera.
        """
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_frame.shape
        bytes_per_line = ch * w
        convert_to_qt_format = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.ui.camera_label.setPixmap(QPixmap.fromImage(convert_to_qt_format))

    def update_game(self):
        """
        Atualiza o estado do jogo com base na predição estabilizada.
        """
        if self.detector.results:
            # Coleta as previsões
            for result in self.detector.results:
                boxes = result.boxes
                for box in boxes:
                    class_id = box.cls[0]
                    letter = self.detector.model.names[int(class_id)]
                    normalized_letter = self.game_attr.class_mapping.get(letter, letter)  # Normaliza a letra
                    self.game_attr.prediction_window.append(normalized_letter)
                    if len(self.game_attr.prediction_window) > self.game_attr.window_size:
                        self.game_attr.prediction_window.pop(0)

            # Averigua a letra mais frequente na janela deslizante
            if len(self.game_attr.prediction_window) == self.game_attr.window_size:
                most_common_letter = Counter(self.game_attr.prediction_window).most_common(1)[0][0]
                self.process_guess(most_common_letter)

    def process_guess(self, letter):
        """
        Processa a letra adivinhada, atualiza o estado do jogo e a interface do usuário.
        
        Parâmetros:
        letter (str): A letra adivinhada.
        """
        game = self.game_attr.game
        if letter not in game.correct_letters and letter not in game.wrong_letters:
            game.guess(letter)
            self.ui.word_label.setText(game.display_word())
            self.ui.used_letters_label.setText("Letras Usadas: " + game.get_wrong_letters())

            if game.is_won():
                self.show_message("Vitória!", "Você adivinhou a palavra!")
                self.reset_game()
            elif game.is_lost():
                self.show_message("Game Over", "A palavra era: " + game.selected_word)
                self.reset_game()

    def show_message(self, title, message):
        """
        Exibe uma mensagem ao usuário.
        
        Parâmetros:
        title (str): O título da mensagem.
        message (str): O conteúdo da mensagem.
        """
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

    def reset_game(self):
        """
        Reseta o jogo para uma nova partida.
        """
        self.game_attr = GameAttributes()
        self.ui.word_label.setText(self.game_attr.game.display_word())
        self.ui.used_letters_label.setText("Letras Usadas: ")
        self.game_attr.prediction_window.clear()

    def keyPressEvent(self, event):
        """
        Fecha a janela do jogo se a tecla 'Q' for pressionada.
        
        Parâmetros:
        event (QKeyEvent): Evento de tecla pressionada.
        """
        if event.key() == Qt.Key_Q:
            self.close()
