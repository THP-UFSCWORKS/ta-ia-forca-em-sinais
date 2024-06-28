import cv2  # Importa a biblioteca OpenCV para captura e processamento de vídeo
from ultralytics import YOLO  # Importa a biblioteca YOLO da Ultralytics para detecção de objetos

class SignDetectorRealTime:
    def __init__(self, model_path):
        """
        Construtor da classe SignDetectorRealTime.
        Inicializa o caminho do modelo e define variáveis para o modelo e os resultados.

        Parâmetros:
        model_path (str): Caminho para o modelo YOLO treinado.
        """
        self.model_path = model_path
        self.model = None
        self.results = None

    def load_model(self):
        """
        Carrega o modelo YOLO a partir do caminho fornecido.
        """
        self.model = YOLO(self.model_path)

    def predict(self, frame):
        """
        Realiza a predição no frame fornecido.

        Parâmetros:
        frame (numpy.ndarray): Frame de vídeo para realizar a predição.

        Retorna:
        list: Resultados da predição.
        """
        self.results = self.model(frame)
        return self.results

    def process_results(self, frame):
        """
        Processa e exibe os resultados da predição no frame de vídeo.
        Desenha caixas delimitadoras e rótulos no frame.

        Parâmetros:
        frame (numpy.ndarray): Frame de vídeo para processar os resultados.

        Retorna:
        numpy.ndarray: Frame de vídeo com as detecções desenhadas.
        """
        for result in self.results:
            boxes = result.boxes  # Caixas delimitadoras para outputs de detecção
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Coletar coordenadas da caixa delimitadora
                confidence = box.conf[0]  # Coletar a confiança da detecção
                class_id = box.cls[0]  # Coletar a classe da detecção
                label = f"{self.model.names[int(class_id)]}: {confidence:.2f}"
                # Desenhar a caixa delimitadora e o rótulo no frame
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # pylint: disable=no-member
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)  # pylint: disable=no-member
        return frame

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

# if __name__ == "__main__":
#     model_path = "../../data/train/weights/best.pt"  # Caminho para o modelo treinado

#     detector = SignDetectorRealTime(model_path)  # Cria uma instância do detector de sinais em tempo real
#     detector.load_model()  # Carrega o modelo YOLO

#     # Iniciar captura de vídeo
#     cap = cv2.VideoCapture(0)  # Use 0 para a webcam interna, ou forneça o caminho para um arquivo de vídeo

#     while cap.isOpened():
#         ret, frame = cap.read()  # Captura um frame de vídeo
#         if not ret:
#             break
        
#         # Fazer a predição no frame capturado
#         detector.predict(frame)
#         # Processar e exibir resultados no frame
#         frame = detector.process_results(frame)
        
#         # Mostrar o frame com as detecções
#         cv2.imshow('Real-time Detection', frame)

#         # Sair do loop se a tecla 'q' for pressionada
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Liberar a captura de vídeo e fechar as janelas
#     cap.release()
#     cv2.destroyAllWindows()
