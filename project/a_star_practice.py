'''
해결 과제 :

1. g 산출 계산식 안맞음
2. openlist, closedlist 안쓴거에 대한 설명
3. 기타등등
'''

import heapq, sys, math
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest

INF = sys.maxsize
row = 0
col = 0
grid_data = [[]]
nodes = [[]]

# QT Class
class GridWindow(QMainWindow):
    def __init__(self, grid_data):
        super().__init__()

        self.setWindowTitle("A-Star Example")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(central_widget)

        self.grid_data = grid_data

        self.cell_labels = [[0 for i in range(len(grid_data[0]))] for _ in range(len(grid_data))]

        for r in range(len(grid_data)):
            for c in range(len(grid_data[0])):
                cell_value = self.grid_data[r][c]
                label = QLabel()
                label.setAlignment(Qt.AlignCenter)
                label.setFixedSize(30, 30)
                label.setStyleSheet(f"background-color: {'black' if cell_value == 1 else 'white'};")
                grid_layout.addWidget(label, r, c)
                
                self.cell_labels[r][c] = label

        # 버튼을 추가하여 클릭 이벤트 연결
        button = QPushButton("Find Path")
        button.clicked.connect(self.find_path)
        grid_layout.addWidget(button, len(grid_data), 0, 1, len(grid_data[0]))

    def checkCellVisited(self, now):
        r, c = now
        self.cell_labels[r][c].setStyleSheet(f"background-color: {'green'};")

    def find_path(self):
        src = (0, 0)
        dst = (8, 9)
        aStarSearch(self, self.grid_data, src, dst)

# 노드 Class
class Node:
    def __init__(self, name, f, g, h):
        self.name = name
        self.f = f
        self.g = g
        self.h = h 
        self.visited = False

    def setVisited(self):
        self.visited = True

    def isVisited(self):
        return self.visited

    # H값 산출
    def setFGH(self, f, g, h):
        self.f = f
        self.g = g
        self.h = h
        
    # F값 리턴
    def getF(self):
        return self.f

# 주변 8블럭 중 갈 수 있는 블럭들 좌표 리스트 리턴

def euclidian(before, next):
        before_row, before_col = before
        next_row, next_col = next
        return math.sqrt((before_row - next_row) * (before_row - next_row)
                        + (before_col - next_col) * (before_col - next_col))

# 탐색 마침 체크용
def isDestination(now, dst):
    return now == dst

# astar 알고리즘
def aStarSearch(window, grid_data, src, dst):
    # 사전세팅
    row = len(grid_data)
    col = len(grid_data[0])

    nodes = [[0 for _ in range(col)] for _ in range(row)]

    window.cell_labels[src[0]][src[1]].setStyleSheet(f"background-color: {'red'};")
    window.cell_labels[dst[0]][dst[1]].setStyleSheet(f"background-color: {'blue'};")

    # 노드 초기화
    for i in range(row):
        for j in range(col):
            nodes[i][j] = Node((i, j), INF, INF, INF)
    nodes[src[0]][src[1]].setFGH(0, 0, 0)

    queue = []
    heapq.heappush(queue, (0, src))

    while queue:
        now_distance, now_destination = heapq.heappop(queue)

        if now_destination == dst:
            return

        now_row, now_col = now_destination

        if nodes[now_row][now_col].isVisited():
            continue

        if nodes[now_row][now_col].getF() < now_distance:
            continue

        for new_vector in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_i, new_j = new_vector
            new_row = now_row + new_i
            new_col = now_col + new_j
            new_destination = (new_row, new_col)

            if not (0 < new_row < row and 0 < new_col < col and grid_data[new_row][new_col]):
                continue

            new_g = euclidian(src, new_destination)
            new_h = euclidian(new_destination, dst)
            new_f = new_g + new_h

            if new_f < nodes[new_row][new_col].getF():
                nodes[new_row][new_col].setFGH(new_f, new_g, new_h)
                heapq.heappush(queue, (new_f, new_destination))
                if new_destination != dst:
                    window.checkCellVisited(new_destination)
                QTest.qWait(100)
    

def main():
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

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
