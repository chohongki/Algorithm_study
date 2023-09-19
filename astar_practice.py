import heapq

class Node:
    def __init__(self, state, parent=None):
        self.state = state  # 현재 상태
        self.parent = parent  # 부모 노드
        self.g = 0  # 시작 노드부터의 경로 비용 (g(n))
        self.h = 0  # 휴리스틱 예측 비용 (h(n))
    
    def __lt__(self, other):
        # heapq 우선순위 큐에서 사용하기 위한 비교 연산자 정의
        return (self.g + self.h) < (other.g + other.h)

def astar(initial_state, goal_state, heuristic):
    open_set = []  # 열린 목록
    closed_set = set()  # 닫힌 목록

    start_node = Node(initial_state)
    start_node.g = 0
    start_node.h = heuristic(initial_state, goal_state)

    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal_state:
            # 목표 상태에 도달했을 때 경로를 추적하고 반환
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.state)

        for neighbor_state in get_neighbors(current_node.state):
            if neighbor_state in closed_set:
                continue
            
            neighbor_node = Node(neighbor_state, current_node)
            neighbor_node.g = current_node.g + 1
            neighbor_node.h = heuristic(neighbor_state, goal_state)

            if neighbor_node not in open_set:
                heapq.heappush(open_set, neighbor_node)

    return None  # 경로가 없을 경우

# 예제 휴리스틱 함수 (맨해튼 거리를 사용한 휴리스틱)
def manhattan_distance(state, goal_state):
    x1, y1 = state
    x2, y2 = goal_state
    return abs(x1 - x2) + abs(y1 - y2)

# 예제 이웃 생성 함수 (8방향 이동)
def get_neighbors(state):
    x, y = state
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            new_x, new_y = x + dx, y + dy
            neighbors.append((new_x, new_y))
    return neighbors

# 테스트
initial_state = (0, 0)
goal_state = (2, 4)
path = astar(initial_state, goal_state, manhattan_distance)
print(path)
