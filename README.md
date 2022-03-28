# dorapi Alexa skill
dorapi を使って道具を検索し，Google画像検索で最上位の画像と共にお知らせするアレクサスキルです．

使用例:

```
自分: 「キーワードで道具を調べて」
```

```
Alexa: 「ようこそ、ドラピアイへ。ひみつ道具に関するキーワードを言ってみてください。」
```

```
自分: 「ドラえもん　<キーワード>」
```

```
Alexa: 「<キーワード> を検索した結果、<ひみつ道具名> が見つかりました。」
```

`.env` ファイルを直下に配置してください:
```
# 取得方法は https://github.com/paramraghavan/serverless-py-alexa-skill 等参照
AMAZON_VENDOR_ID=...
AMAZON_CLIENT_ID=...
AMAZON_CLIENT_SECRET=...
ALEXA_SKILL_ID=...
AWS_ACCOUNT=...

# Google Custom Search (取得方法は調べてください)
CSE_ID=...  # Custom Search Engine ID
GOOGLE_API_KEY=...  # Google API Key
```

# virtualenv
```
. ./skill_env/bin/activate
```

# デプロイ手順
- https://github.com/paramraghavan/serverless-py-alexa-skill

- https://www.serverless.com/blog/how-to-manage-your-alexa-skills-with-serverless

に従う．

以下の `--aws-profile` は `~/.aws/credentials` に登録されている profile に対応するものを指定する．

## Alexa skill 作成
```
npx serverless alexa create --name dorapi --locale ja_jp --type custom --aws-profile as-sqr
```

## intent syntax 確認
```
npx serverless alexa update --dryRun --aws-profile as-sqr
```

## manifest 更新

```
npx serverless alexa update --aws-profile as-sqr
```

## 作成した Alexa manifest 確認
```
npx serverless alexa manifests --name dorapi --aws-profile as-sqr
```

## モデル build
```
npx serverless alexa build --name dorapi --aws-profile as-sqr
```

## モデル確認
```
npx serverless alexa models --name dorapi --aws-profile as-sqr
```

## Lambda デプロイ
```
npx serverless deploy --aws-profile as-sqr
```
