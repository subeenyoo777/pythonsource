# 확장자 py 인 것은 모두 "module"이다.


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


# [ __name__ ] : 외부에서 출력될 시 출력되면 안됨
if __name__ == "__main__":
    print(add(6, 5))
    print(sub(16, 6))
