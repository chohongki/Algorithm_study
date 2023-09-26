import multiprocessing
import time

# 각 프로세스가 실행할 작업 함수
def square(numbers, result, index):
    partial_sum = 0
    for num in numbers:
        partial_sum += num * num
    result[index] = partial_sum

if __name__ == "__main__":
    # 입력 데이터
    numbers = list(range(100_000_00))
    result = [0, 0]
    # 두 개의 프로세스 생성
    process1 = multiprocessing.Process(target=square, args=(numbers, result, 0))
    process2 = multiprocessing.Process(target=square, args=(numbers, result, 1))

    start_time = time.time()

    # square(numbers, result, 0)
    # square(numbers, result, 1)

    # 프로세스 시작
    process1.start()
    process2.start()

    # 프로세스 종료 대기
    process1.join()
    process2.join()

    # 결과 출력
    total_sum = result[0] + result[1]

    print("Total sum of squared numbers:", result)
    print("작업 시간 : ", (time.time() - start_time), "sec")
    # print(list(result))
