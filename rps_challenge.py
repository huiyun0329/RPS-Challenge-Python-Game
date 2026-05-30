import random

# ----- 遊戲設定 -----
CHOICES = ["石頭", "布", "剪刀"]
user_score = 0
computer_score = 0
round_number = 0
total_rounds = 3  # 改為三戰兩勝制，節奏更快！

# ----- 顯示歡迎畫面 -----
def display_welcome():
    print("     🎮 歡迎來到剪刀石頭布大挑戰 🎮     ")
    print("📌 規則:")
    print("   🪨 石頭 贏 剪刀")
    print("   ✂️ 剪刀 贏 布")
    print("   📄 布 贏 石頭")
    print(f"\n🏆 賽制 : {total_rounds} 戰 {total_rounds//2 + 1} 勝")

# ----- 取得玩家選擇 -----
def get_user_choice():
    while True:
        user = input("\n👉 請輸入 石頭, 布, 或 剪刀: ").strip()
        if user in CHOICES:
            return user
        print("❌ 輸入錯誤！請確實輸入 石頭, 布 或 剪刀。")

# ----- 取得電腦選擇 -----
def get_computer_choice():
    print("\n🤖 電腦正在思考中...")
    return random.choice(CHOICES)

# ----- 判斷勝負邏輯 -----
def decide_winner(user, computer):
    global user_score, computer_score
    
    if user == computer:
        return "Tie"
    elif (
        (user == "石頭" and computer == "剪刀") or
        (user == "布" and computer == "石頭") or
        (user == "剪刀" and computer == "布")
    ):
        user_score += 1
        return "User"
    else:
        computer_score += 1
        return "Computer"

# ----- 顯示計分板 -----
def display_scoreboard():
    print("📊 目前比分")
    print(f"👤 你的分數 : {user_score}")
    print(f"🤖 電腦分數 : {computer_score}")

# ----- 顯示最終結果 -----
def display_final_result():
    print("\n" + "=" * 40)
    print("🏁 最終結果 🏁")
    print(f"👤 你的總分 : {user_score}")
    print(f"🤖 電腦總分 : {computer_score}")
    print("\n🎯 比賽總結")
    
    if user_score > computer_score:
        print("🎉 恭喜你獲得總冠軍！ 🎉")
        print("🏆 你成功擊敗了電腦！太神啦！")
    elif computer_score > user_score:
        print("🤖 電腦獲得了最終勝利！")
        print("😢 運氣不好，下次再挑戰吧！")
    else:
        print("🤝 雙方平手！")
        print("⚔️ 真是勢均力敵的精彩對決！")
    print("=" * 40 + "\n")


# ==========================================
#              遊戲主程式開始
# ==========================================

display_welcome()

while round_number < total_rounds:
    round_number += 1
    print(f"\n🎯 第 {round_number} 回合 / 共 {total_rounds} 回合")

    # 1. 玩家出拳
    user_choice = get_user_choice()
    
    # 2. 電腦出拳
    computer_choice = get_computer_choice()

    print(f"\n👤 你出了   : {user_choice}")
    print(f"🤖 電腦出了 : {computer_choice}")

    # 3. 判斷勝負
    winner = decide_winner(user_choice, computer_choice)

    # 4. 顯示該回合結果
    if winner == "Tie":
        print("\n⚖️ 這回合平手！")
    elif winner == "User":
        print("\n🎉 你贏了這回合！")
    else:
        print("\n😢 電腦贏了這回合！")

    # 5. 顯示計分板
    display_scoreboard()

# 遊戲結束，顯示總結
display_final_result()