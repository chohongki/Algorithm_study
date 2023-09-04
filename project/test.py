import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel
from PyQt5.QtCore import Qt

class GridWindow(QMainWindow):
    def __init__(self, grid_data):
        super().__init__()

        self.setWindowTitle("Grid Example")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(central_widget)

        self.grid_data = grid_data
        self.cell_labels = [[0 for i in range(len(grid_data[0]))] for _ in range(len(grid_data))]


        for row in range(9):
            for col in range(10):
                cell_value = self.grid_data[row][col]
                label = QLabel()
                label.setAlignment(Qt.AlignCenter)
                label.setFixedSize(30, 30)
                label.setStyleSheet(f"background-color: {'white' if cell_value == 1 else 'gray'};")
                grid_layout.addWidget(label, row, col)
                
                self.cell_labels[row][col] = label

    def checkCellVisited(self, row, col):
        self.cell_labels[row][col].setStyleSheet(f"background-color: {'red'};")

def main():
    grid_data = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    ]

    app = QApplication(sys.argv)
    window = GridWindow(grid_data)
    window.show()
    window.checkCellVisited(5, 5)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
