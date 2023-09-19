import threading
import time

# 첫 번째 스레드의 작업 함수
def countdown(n):
    for i in range(n, 0, -1):
        print(f"Countdown 1: {i}")
        # time.sleep(1)

# 두 번째 스레드의 작업 함수
def countdown_reverse(n):
    for i in range(1, n+1):
        print(f"Countdown 2: {i}")
        # time.sleep(1)

# 두 개의 스레드 생성
thread1 = threading.Thread(target=countdown, args=(5,))
thread2 = threading.Thread(target=countdown_reverse, args=(5,))

start_time = time.time()

countdown(100)
countdown_reverse(100)
# # 스레드 시작
# thread1.start()
# thread2.start()

# # 스레드 종료 대기
# thread1.join()
# thread2.join()

print("카운트 다운이 완료되었습니다.")
print("작업 시간 : ", (time.time() - start_time), "sec")
