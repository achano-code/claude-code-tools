import sys
from tennis_gui import main as gui_main
from tennis_game import TennisGame

def console_demo():
    print("=== テニスゲーム コンソール版デモ ===")
    game = TennisGame("太郎", "花子")
    print(f"テニスゲーム開始: {game.player1_name} vs {game.player2_name}")
    print(f"初期スコア: {game.get_score()}")
    
    game.win_ball("太郎")
    print(f"太郎が1ポイント: {game.get_score()}")
    
    game.win_ball("花子")
    print(f"花子が1ポイント: {game.get_score()}")
    
    game.win_ball("太郎")
    print(f"太郎が2ポイント目: {game.get_score()}")
    
    game.win_ball("太郎")
    print(f"太郎が3ポイント目: {game.get_score()}")
    
    game.win_ball("花子")
    game.win_ball("花子")
    game.win_ball("花子")
    print(f"花子が追いつく: {game.get_score()}")
    
    game.win_ball("太郎")
    print(f"太郎アドバンテージ: {game.get_score()}")
    
    game.win_ball("太郎")
    print(f"太郎勝利: {game.get_score()}")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--console":
        console_demo()
    else:
        print("テニスゲーム GUI版を起動中...")
        gui_main()

if __name__ == "__main__":
    main()