# テニスゲーム (Python)

古典的なテニスのスコアリングシステムを実装したPythonアプリケーションです。

## 機能

- 古典的なテニススコア (Love, Fifteen, Thirty, Forty)
- Deuce/Advantage の処理
- 勝利条件の判定
- GUI版とコンソール版の両方をサポート

## ファイル構成

```
tennis-game-python/
├── tennis_game.py      # メインのゲームロジック
├── tennis_gui.py       # GUI版アプリケーション
├── main.py            # エントリーポイント
├── test_tennis_game.py # ユニットテスト
└── README.md          # このファイル
```

## 実行方法

### GUI版（推奨）
```bash
python main.py
```

### コンソール版デモ
```bash
python main.py --console
```

### GUI版を直接実行
```bash
python tennis_gui.py
```

## GUI版の使い方

1. アプリケーションを起動
2. プレイヤー名を入力（オプション）
3. 「プレイヤー名を更新」ボタンをクリック
4. 各プレイヤーの得点ボタンをクリックしてゲームを進行
5. ゲーム終了時に勝者が表示される
6. 「ゲームリセット」で新しいゲームを開始

## テスト実行

```bash
python test_tennis_game.py
```

## スコアリングルール

- **0ポイント**: Love
- **1ポイント**: Fifteen
- **2ポイント**: Thirty  
- **3ポイント**: Forty
- **同点で3-3以上**: Deuce
- **Deuceから1ポイント差**: Advantage
- **2ポイント差で勝利**: Win

## 必要な環境

- Python 3.6以上
- tkinter（通常Pythonに標準で含まれています）