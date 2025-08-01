# キーボードからの受け取りについて

# キーボードからの入力を受け取るときは、input()関数を使います。
# 例えば、CUIアプリケーションで名前とか受け取りたいときに使えます。

# 例: ユーザーから名前を受け取る
name = input("あなたの名前を入力してください: ")

# 例: メールアドレスを受け取る
email = input("メールアドレスを入力してください: ")

# 例: こんにちは！〇〇さんと表示する

print("こんにちは！" + name + "さん")

# 例: メールアドレスを表示する
print("あなたのメールアドレスは " + email + " です。")

# コンソールで実際に動かしてみよう

# 因みにこの緑の文字はコメント文といいます
# コメント文はプログラムの実行には影響しません
# #をつけるとコメント文になります
# コメント文はコードの説明やメモとして使います

# 次にインデントについてです。
# インデントはコードのブロックを示すために使います。
# まだやってないけどif文で例を見てみましょう
# 例: if文のインデント

name = input("あなたの名前を入力してください: ")

if name == "Alice":
    print("こんにちは、Aliceさん!")
else:
    print("who are you?")

# この例では、if文の中のコードはインデントされています。
# インデントは通常、スペース4つ分を使います。

# 因みにpythonの拡張子は.pyです。
# なので、ファイル名は3-1.pyのようにします。