import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt5.QtCore import Qt
from PIL import Image

class WebPConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('WebP Converter')
        self.setGeometry(100, 100, 400, 300)
        self.setAcceptDrops(True)

        # Create interface
        self.layout = QVBoxLayout()
        self.label = QLabel('Drag and drop images or a folder here\nor use the button below')
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        self.button = QPushButton('Select Folder')
        self.button.clicked.connect(self.select_folder)
        self.layout.addWidget(self.button)

        self.status_label = QLabel('')
        self.status_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.status_label)

        self.setLayout(self.layout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        for url in urls:
            path = url.toLocalFile()
            if os.path.isdir(path):
                self.convert_folder(path)
            elif os.path.isfile(path) and path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                self.convert_image(path)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folder:
            self.convert_folder(folder)

    def convert_image(self, input_path):
        try:
            output_path = os.path.splitext(input_path)[0] + '.webp'
            with Image.open(input_path) as img:
                img.save(output_path, 'webp')
            self.status_label.setText(f'Converted: {os.path.basename(input_path)}')
        except Exception as e:
            self.status_label.setText(f'Error: {e}')

    def convert_folder(self, folder_path):
        converted = 0
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                input_path = os.path.join(folder_path, filename)
                self.convert_image(input_path)
                converted += 1
        if converted > 0:
            self.status_label.setText(f'Converted {converted} images')
        else:
            self.status_label.setText('No supported images found')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WebPConverter()
    window.show()
    sys.exit(app.exec_())