import numpy as np

def main():
    # 2차원 배열 생성
    array_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print("1. 2차원 배열: ")
    print(array_2d) # 2차원 배열 출력

    # 배열의 크기 확인
    print("\n2. 배열의 크기: ")
    print(array_2d.shape) # 배열의 크기 출력

    # 배열의 요소에 접근
    print("\n3. 배열의 요소에 접근: ")
    print("<행 출력>")
    print("첫번째 행: ", array_2d[0])
    print("두번째 행: ", array_2d[1])
    print("세번째 행: ", array_2d[2])

    print("<열 출력>")
    print("첫번째 열: ", array_2d[:, 0])
    print("두번째 열: ", array_2d[:, 1])
    print("세번째 열: ", array_2d[:, 2])

    # 배열의 요소의 합, 평균, 최댓값, 최솟값, 표준 편차 계산
    print("\n4. 배열의 통계적 특성: ")
    print("요소의 합: ", np.sum(array_2d))
    print("평균 값: ", np.mean(array_2d))
    print("최댓값: ", np.max(array_2d))
    print("최솟값: ", np.min(array_2d))
    print("표준 편차: ", np.std(array_2d))

    # 배열의 모양 변경
    print("\n5. 배열의 모양 변경: ")
    reshaped_array = np.reshape(array_2d, (1, 9))  # 3x3 배열을 1x9 배열로 변경
    print("변경된 배열: ", reshaped_array)


if __name__ == "__main__":
    main()