n = int(input())

res = 0

while n > 0: # 여분의 설탕이 있다면
  if n % 5 == 0:
    res += n//5
    break # 탈출 없으면 초과 실행!
  n -= 3
  res += 1 # 5kg로 나눠 떨어질 때 까지 3kg 봉지를 하나씩 채운다.

  if n < 0:
    res = -1 # 딱 떨어지지 않는다면 -1 출력


print(res)

# 설탕이 5의 배수가 될때까지 3을 빼주는 것이 아이디어
# 실패 - 5kg로 가득 채우고 나머지가 생기면 3kg +1 5kg -1 하는 방법 => 3kg, 5kg 변수를 따로 관리해야 해서 복잡한 풀이다.
