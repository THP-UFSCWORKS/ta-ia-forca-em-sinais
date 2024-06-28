from ultralytics import YOLO  # Importa a biblioteca YOLO da Ultralytics para detecção de objetos

class SignDetector:
    def __init__(self, model_path, image_path):
        """
        Construtor da classe SignDetector.
        Inicializa os caminhos do modelo e da imagem, e define variáveis para o modelo e os resultados.

        Parâmetros:
        model_path (str): Caminho para o modelo YOLO treinado.
        image_path (str): Caminho para a imagem de entrada a ser processada.
        """
        self.model_path = model_path
        self.image_path = image_path
        self.model = None
        self.results = None

    def load_model(self):
        """
        Carrega o modelo YOLO a partir do caminho fornecido.
        """
        self.model = YOLO(self.model_path)

    def predict(self):
        """
        Realiza a predição na imagem fornecida.

        Retorna:
        list: Resultados da predição.
        """
        self.results = self.model(self.image_path)
        return self.results

    def process_results(self):
        """
        Processa e exibe os resultados da predição.
        Para cada resultado, mostra as caixas delimitadoras, máscaras, pontos-chave, probabilidades e caixas orientadas.
        Salva a imagem resultante com as detecções.
        """
        for result in self.results:
            # boxes = result.boxes  # Caixas delimitadoras para outputs de detecção
            # masks = result.masks  # Máscaras de segmentação
            # keypoints = result.keypoints  # Pontos-chave para pose
            # probs = result.probs  # Probabilidades para classificação
            # obb = result.obb  # Caixas orientadas para outputs de OBB
            result.show()  # Exibe na tela
            result.save(filename="result.jpg")  # Salva no disco

    def export_model(self, export_format="onnx"):
        """
        Exporta o modelo para o formato especificado.

        Parâmetros:
        export_format (str): Formato para o qual o modelo será exportado (por exemplo, "onnx").

        Retorna:
        str: Caminho para o modelo exportado.
        """
        path = self.model.export(format=export_format)
        return path

if __name__ == "__main__":
    MODEL_PATH = "../../data/train/weights/best.pt"  # Caminho para o modelo treinado
    IMAGE_PATH = "../../data/images/v.jpeg"  # Caminho para a imagem de entrada

    detector = SignDetector(MODEL_PATH, IMAGE_PATH)  # Cria uma instância do detector de sinais
    detector.load_model()  # Carrega o modelo YOLO
    results = detector.predict()  # Realiza a predição na imagem
    detector.process_results()  # Processa e exibe os resultados
    onnx_path = detector.export_model()  # Exporta o modelo para o formato ONNX
    print(f"Model exported to {onnx_path}")  # Imprime o caminho do modelo exportado
