def 电脑出招(n, m):
    return min(n, m) if n <= m else n % (m + 1) or m

def 用户出招(n, m):
    棋子 = int(input('你要拿走多少个棋子？ '))
    while not (0 < 棋子 <= m) or 棋子 > n:
        print("哎呀！无效的移动！请再试一次。")
        棋子 = int(input("\n你要拿走多少个棋子？ "))
    return 棋子

def 游戏():
    n = int(input('请输入总棋子数： '))
    m = int(input('请输入每回合最多拿取的棋子数： '))
    while m < 1:
        print('每回合拿取的棋子数必须小于或等于总棋子数')
        m = int(input('请输入每回合最多拿取的棋子数： '))
    棋子 = 0
    回合 = 0
    if n % (m + 1) == 0:
        print('你先开始！')
        回合 = True
        while n > 0:
            玩家 = "你" if 回合 else "电脑"
            棋子 = 用户出招(n, m) if 回合 else 电脑出招(n, m)
            print(f"{玩家}拿走了 {棋子}")
            n -= 棋子
            print(f"还剩下 {n} 个棋子")
            回合 = not 回合  
        获胜者 = 2 if 回合 else 1
        print(f"游戏结束！{'电脑' if 获胜者 == 2 else '你'}赢了！\n")
        return 获胜者
    else:
        print("电脑先开始！")
        回合 = 2 
        while n > 0:
            玩家 = "电脑" if 回合 == 2 else "你"
            棋子 = 电脑出招(n, m) if 回合 == 2 else 用户出招(n, m)
            print(f"{玩家}拿走了 {棋子}")
            n -= 棋子
            print(f"还剩下 {n} 个棋子")
            回合 = 1 if 回合 == 2 else 2
        获胜者 = 2 if 回合 == 1 else 1
        print(f"游戏结束！{'电脑' if 获胜者 == 2 else '你'}赢了!")
        return 获胜者
    
def 锦标赛():
    轮次 = 1
    电脑得分 = 用户得分 = 0
    for 轮次 in range(1, 4):
        print("第", 轮次, "轮")
        if 游戏() == 1:
            用户得分 += 1
        else:
            电脑得分 += 1
    print("锦标赛结束！")
    print("得分：你", 用户得分, "X", 电脑得分, "电脑")
    
def 主函数():
    print("欢迎来到 NIM 游戏！")
    print("1 - 进行单局游戏")
    print("2 - 进行锦标赛")
    选择 = 获取选择()
    选项 = {
        1: ("你选择了单局游戏！", 游戏),
        2: ("你选择了锦标赛！", 锦标赛)
    }
    if 选择 in 选项:
        消息, 函数 = 选项[选择]
        print(消息)
        函数()
    else:
        print("无效选择。游戏将终止。")

def 获取选择():
    while True:
        try:
            选择 = int(input("选择： "))
            if 选择 in [1, 2]:
                return 选择
            else:
                print("请选择有效选项！")
                continue 
        except ValueError:
            print("请输⼊有效的数字。")
主函数()
