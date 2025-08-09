# オンラインホワイトボードアプリ

リアルタイムで複数ユーザーが同時に描画できるオンラインホワイトボードアプリケーションです。

## 技術スタック

### サーバーサイド
- Node.js
- Express.js
- Socket.io
- Herokuにデプロイ

### クライアントサイド
- React
- TypeScript
- Socket.io Client
- Vercelにデプロイ

## 機能

- リアルタイム描画
- 色選択
- 線の太さ調整
- 画面クリア
- 複数ユーザー同時接続

## セットアップ

### サーバーサイド
```bash
cd server
npm install
npm run dev
```

### クライアントサイド
```bash
cd client
npm install
npm start
```

## デプロイ

### Herokuデプロイ（サーバー）
1. Herokuアカウント作成
2. Heroku CLIインストール
3. `cd server`
4. `heroku create your-whiteboard-server`
5. `heroku config:set CLIENT_URL=https://your-client-domain.vercel.app`
6. `git init && git add . && git commit -m "Initial commit"`
7. `git push heroku main`

### Vercelデプロイ（クライアント）
1. Vercelアカウント作成
2. `cd client`
3. `vercel --prod`
4. 環境変数 `REACT_APP_SERVER_URL` をHerokuのサーバーURLに設定

## 使い方

1. ブラウザでクライアントURLにアクセス
2. 色と線の太さを選択
3. マウスでキャンバス上を描画
4. 他のユーザーの描画もリアルタイムで表示