# 10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
# 1000미만의 자연수에서 3,5의 배수의 총합을 구하라.

# 내 아이디어: if문으로 sum +=i
# 강의 아이디어: 1. 내 아이디어 / 2. List에 모아서 sum 메소드

# tip1. 괄호를 명확히 치는 습관
# tip2. List는 메모리를 많이 먹음
# tip3. CodeGolf - 코드를 짧게 만드는 행위. 대회에서 쓰일법하지만 실전에선 가독성이 떨어진다.


# list1 = []
sum1 = 0

for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):
        # list1.append(i)
        sum1 += i

# print(sum(list1))
print(sum1)

