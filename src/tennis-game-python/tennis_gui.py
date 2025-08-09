import tkinter as tk
from tkinter import ttk, messagebox
from tennis_game import TennisGame

class TennisGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("テニスゲーム")
        self.root.geometry("500x400")
        self.root.resizable(True, True)
        
        self.game = TennisGame("プレイヤー1", "プレイヤー2")
        self.setup_ui()
        self.update_display()
    
    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        title_label = ttk.Label(main_frame, text="テニスゲーム", font=("Arial", 20, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        player_frame = ttk.Frame(main_frame)
        player_frame.grid(row=1, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E))
        player_frame.columnconfigure(0, weight=1)
        player_frame.columnconfigure(2, weight=1)
        
        ttk.Label(player_frame, text="プレイヤー名:", font=("Arial", 12)).grid(row=0, column=0, columnspan=3, pady=(0, 10))
        
        self.player1_entry = ttk.Entry(player_frame, width=15)
        self.player1_entry.grid(row=1, column=0, padx=(0, 10))
        self.player1_entry.insert(0, "プレイヤー1")
        
        ttk.Label(player_frame, text="VS", font=("Arial", 14, "bold")).grid(row=1, column=1, padx=10)
        
        self.player2_entry = ttk.Entry(player_frame, width=15)
        self.player2_entry.grid(row=1, column=2, padx=(10, 0))
        self.player2_entry.insert(0, "プレイヤー2")
        
        update_button = ttk.Button(player_frame, text="プレイヤー名を更新", command=self.update_player_names)
        update_button.grid(row=2, column=0, columnspan=3, pady=10)
        
        score_frame = ttk.LabelFrame(main_frame, text="スコア", padding="15")
        score_frame.grid(row=2, column=0, columnspan=3, pady=20, sticky=(tk.W, tk.E))
        score_frame.columnconfigure(0, weight=1)
        score_frame.columnconfigure(2, weight=1)
        
        self.player1_name_label = ttk.Label(score_frame, text="プレイヤー1", font=("Arial", 14, "bold"))
        self.player1_name_label.grid(row=0, column=0, pady=5)
        
        self.score_label = ttk.Label(score_frame, text="Love-Love", font=("Arial", 18, "bold"), foreground="blue")
        self.score_label.grid(row=0, column=1, padx=20, pady=5)
        
        self.player2_name_label = ttk.Label(score_frame, text="プレイヤー2", font=("Arial", 14, "bold"))
        self.player2_name_label.grid(row=0, column=2, pady=5)
        
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=3, pady=20)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        
        self.player1_button = ttk.Button(button_frame, text="プレイヤー1 得点", command=self.player1_scores)
        self.player1_button.grid(row=0, column=0, padx=(0, 10), ipadx=10, ipady=5)
        
        self.player2_button = ttk.Button(button_frame, text="プレイヤー2 得点", command=self.player2_scores)
        self.player2_button.grid(row=0, column=1, padx=(10, 0), ipadx=10, ipady=5)
        
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=4, column=0, columnspan=3, pady=10)
        
        reset_button = ttk.Button(control_frame, text="ゲームリセット", command=self.reset_game)
        reset_button.grid(row=0, column=0, padx=5)
        
        quit_button = ttk.Button(control_frame, text="終了", command=self.root.quit)
        quit_button.grid(row=0, column=1, padx=5)
        
        info_frame = ttk.LabelFrame(main_frame, text="ゲーム情報", padding="10")
        info_frame.grid(row=5, column=0, columnspan=3, pady=(20, 0), sticky=(tk.W, tk.E))
        
        self.info_text = tk.Text(info_frame, height=4, width=50, wrap=tk.WORD, state=tk.DISABLED)
        scrollbar = ttk.Scrollbar(info_frame, orient=tk.VERTICAL, command=self.info_text.yview)
        self.info_text.configure(yscrollcommand=scrollbar.set)
        
        self.info_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        info_frame.columnconfigure(0, weight=1)
        info_frame.rowconfigure(0, weight=1)
        
        initial_info = "テニスゲームへようこそ！\nプレイヤー名を設定してゲームを開始してください。\n"
        self.add_info(initial_info)
    
    def update_player_names(self):
        player1_name = self.player1_entry.get().strip() or "プレイヤー1"
        player2_name = self.player2_entry.get().strip() or "プレイヤー2"
        
        self.game = TennisGame(player1_name, player2_name)
        self.player1_name_label.config(text=player1_name)
        self.player2_name_label.config(text=player2_name)
        self.player1_button.config(text=f"{player1_name} 得点")
        self.player2_button.config(text=f"{player2_name} 得点")
        
        self.update_display()
        self.add_info(f"新しいゲーム: {player1_name} vs {player2_name}")
    
    def player1_scores(self):
        self.game.win_ball(self.game.player1_name)
        self.update_display()
        self.add_info(f"{self.game.player1_name} が得点！")
        self.check_game_end()
    
    def player2_scores(self):
        self.game.win_ball(self.game.player2_name)
        self.update_display()
        self.add_info(f"{self.game.player2_name} が得点！")
        self.check_game_end()
    
    def update_display(self):
        score = self.game.get_score()
        self.score_label.config(text=score)
        
        if "Win for" in score:
            self.score_label.config(foreground="red")
        elif "Advantage" in score:
            self.score_label.config(foreground="orange")
        elif score == "Deuce":
            self.score_label.config(foreground="purple")
        else:
            self.score_label.config(foreground="blue")
    
    def check_game_end(self):
        score = self.game.get_score()
        if "Win for" in score:
            winner = score.replace("Win for ", "")
            messagebox.showinfo("ゲーム終了", f"🎉 {winner} の勝利！\n\nおめでとうございます！")
            self.add_info(f"🏆 ゲーム終了: {winner} の勝利！")
    
    def reset_game(self):
        self.game = TennisGame(self.game.player1_name, self.game.player2_name)
        self.update_display()
        self.add_info("ゲームがリセットされました。")
    
    def add_info(self, message):
        self.info_text.config(state=tk.NORMAL)
        self.info_text.insert(tk.END, message + "\n")
        self.info_text.see(tk.END)
        self.info_text.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = TennisGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()