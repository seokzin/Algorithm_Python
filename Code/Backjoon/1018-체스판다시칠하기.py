n, m = map(int, input().split())
a = []
res = 64 # 색칠할 최소값 - 64(최대값)으로 초기화

for _ in range(n):
  board = input()
  a.append(board)

for i in range(n-7): # 시작 y좌표
  for j in range(m-7): # 시작 x좌표
    cnt = 0
    
    # 시작 좌표로부터 8*8 칸 탐색
    for y in range(i, i + 8):
      for x in range(j, j + 8):
        # A 그룹이며 검정색 + B 그룹이며 흰색
        if ((y+x) % 2 == 0 and a[y][x] == 'B') or ((y+x) % 2 == 1 and a[y][x] == 'W'): 
          cnt += 1
        
    # W판은 B판과 반전 관계니 64-cnt 하면 된다. 따로 구할 필요 X
    # (이전 최소값, B판 필요 cnt, W판 필요 cnt) 중 최소값으로 갱신
    res = min(res, cnt, 64-cnt)
    
print(res)