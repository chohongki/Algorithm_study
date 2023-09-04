import heapq, sys, math
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel
from PyQt5.QtCore import Qt

INF = sys.maxsize
row = 0
col = 0
grid_data = [[]]

# QT Class
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
                label.setStyleSheet(f"background-color: {'black' if cell_value == 1 else 'white'};")
                grid_layout.addWidget(label, row, col)
                
                self.cell_labels[row][col] = label

    def checkCellVisited(self, now):
        row, col = now
        self.cell_labels[row][col].setStyleSheet(f"background-color: {'red'};")

# 노드 Class
class Node:
    def __init__(self, name, nbhd, f, g, h):
        self.name = name
        self.nbhd = nbhd
        self.f = f
        self.g = g
        self.h = h 
        self.visited = False
    
    def setF(self, f):
        self.f = f

    def setG(self, g):
        self.g = g
    
    def setH(self, h):
        self.h = h
    
    def setVisited(self):
        self.visited = True

# H값 산출
def calcHValue(now, dst):
    now_row, now_col = now
    dst_row, dst_col = dst
    return math.sqrt((now_row - dst_row) * (now_row - dst_row)
                     - (now_col, dst_col) * (now_col, dst_col))

# 주변 8블럭 중 갈 수 있는 블럭들 좌표 리스트 리턴
def retNBHD(r, c):
    global row, col
    lNBHD = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            if 0 < r + i < row and 0 < c + j < col and grid_data[r][c]:
                lNBHD.append((r + i, r + i))
    return lNBHD

# 탐색 마침 체크용
def isDestination(now, dst):
    return now == dst

# astar 알고리즘
def aStarSearch(window, src, dst):
    window.checkCellVisited(src)
    

def main():
    global row, col

    # 지도 데이터
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

    # QT 실행
    app = QApplication(sys.argv)
    window = GridWindow(grid_data)
    window.show()

    # 사전세팅
    row = len(grid_data)
    col = len(grid_data[0])

    nodes = [[0 for _ in range(col)] for _ in range(row)]

    # 출발, 도착지
    src = (0, 0)
    dst = (8, 0)

    # 노드 초기화
    for i in range(row):
        for j in range(col):
            nodes[i][j] = Node((i, j), retNBHD, INF, INF, INF)
    nodes[src[1]][src[0]].setF(0)
    nodes[src[1]][src[0]].setG(0)
    nodes[src[1]][src[0]].setH(0)

    aStarSearch(window, src, dst)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
