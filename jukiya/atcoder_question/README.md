# AtCoderオリジナル環境の解説(というかメモ)

自分なりに使いやすいように変更しました。(恐らく多少のバグはあります)
online-judge-toolsについては下のReferenceを見てください
makeコマンドで動きます。

## get_question
https://atcoder.jp/contests/abs/tasks/abc086_a のようにcontestsの後ろと問題部分が一致していない場合に使えます

##### example
```bash
make get_question url="https://atcoder.jp/contests/abs/tasks/abc086_a" id="abc086_a"
```

## get_question_without_url
https://atcoder.jp/contests/typical90/tasks/typical90_d のようにcontestsの後ろの部分と問題部分(a~dは除く)が一致している場合に使用できます.

##### example
```bash
make get_question contest="typical90" id="d"
```

## run_test
online-judge-toolsの機能を使ってテストします。

##### example
```bash
make run_test id="abc086_a"
```

## run_test_without_url
online-judge-toolsの機能を使ってテストします。

##### example
```bash
make run_test contest="typical90" id="d"
```
## submit
online-judge-toolsを使用してコマンドで提出します

##### example
```bash
make submit url="https://atcoder.jp/contests/abs/tasks/abc086_a" id="abc086_a"
```

## submit_without_urk
online-judge-toolsを使用してコマンドで提出します

##### example
```bash
make submit contest="typical90" id="d"
```


# Reference
* online-judge-toolsのGithub
https://github.com/online-judge-tools/oj/blob/master/README.ja.md
* 過去のAtCoderの提出コードの取得
https://zenn.dev/tishii2479/articles/6b381fb86e0369
