import numpy as np

def main():
    # 2차원 배열 생성
    array_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print("1. 2차원 배열: ")
    print(array_2d) # 2차원 배열 출력

    # 배열의 크기 확인
    print("\n2. 배열의 크기: ")
    print(array_2d.shape) # 배열의 크기 출력

    # 배열의 요소에 접근하기
    print("\n3. 배열의 요소에 접근: ")
    print("<행 출력>")
    print("첫번째 행: ", array_2d[0])
    print("두번째 행: ", array_2d[1])
    print("세번째 행: ", array_2d[2])

    print("<열 출력>")
    print("첫번째 열: ", array_2d[:, 0])
    print("두번째 열: ", array_2d[:, 1])
    print("세번째 열: ", array_2d[:, 2])

if __name__ == "__main__":
    main()