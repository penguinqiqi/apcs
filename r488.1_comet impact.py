R, C, D = map(int, input().split())

# 建立地圖 (R x C)，初始高度為 D
grid = [[D for _ in range(C)] for _ in range(R)]

# 讀取 K 隻恐龍座標
K = int(input())
dinosaurs = []
for _ in range(K):
    dinosaurs.append(list(map(int, input().split())))

# 恐龍狀態：我們用一個 list 紀錄哪些恐龍是清醒的 (True)
is_awake = [True] * K

M = int(input())
for _ in range(M):
    a, b, s, d = map(int, input().split())
    
    # 計算撞擊邊界        (因邊長固定為奇數 且中心佔一格 所以-1)
    offset = (s - 1) // 2
    r_start, r_end = max(0, a - offset), min(R - 1, a + offset) #max min 控制邊界不超出地圖
    c_start, c_end = max(0, b - offset), min(C - 1, b + offset)
    #舉例:邊長 S = 5 offset = (5 - 1) // 2 = 2
    #列：從 a - 2 到 a + 2（總共包含 a-2, a-1, a, a+1, a+2 ）。 也就是 a-offset 跟 a+offset


    # 檢查範圍內是否有清醒的恐龍
    has_awake_dino = False
    for i in range(K):
        if is_awake[i]:
            dr, dc = dinosaurs[i]
            if r_start <= dr <= r_end and c_start <= dc <= c_end:
                has_awake_dino = True
                is_awake[i] = False # 恐龍暈眩
    
    # 如果範圍內沒有清醒恐龍，地面高度減少 d
    if not has_awake_dino:
        for r in range(r_start, r_end + 1):
            for c in range(c_start, c_end + 1):
                grid[r][c] -= d

max_h = -float('inf')
min_h = float('inf')
for r in range(R):
    for c in range(C):
        if grid[r][c] > max_h: max_h = grid[r][c]
        if grid[r][c] < min_h: min_h = grid[r][c]

awake_count = sum(is_awake)
print(f"{max_h} {min_h} {awake_count}")