# 文字列の操作

# 先ほど紹介したメソッドで、実際に文字列の操作をしてみましょう

## 小文字への変換

# 小文字に変換するにはlower()メソッドを使います。

a = "HELLO PYTHON"

print(a.lower())    # 出力: hello python

## 大文字への変換

# さっきも使ったupper()メソッドを使います。

b = "hello python"

print(b.upper())    # 出力: HELLO PYTHON

## 文字列の検索

# 文字列が含まれる位置を調べるには、find()メソッドを使います。

c = "hello python"

print(c.find("python")) # 出力: 6

# 文字列が含まれない場合は-1を返します。
print(c.find("java"))   # 出力: -1

## 文字列の分割

# ※競技プログラミングやるときに、めっちゃ使う

# 文字列を分割するにはsplit()メソッドを使います。

c = "2021-01-01"

print(c.split("-")) # 出力: ['2021', '01', '01']

## 文字列の置換

# 文字列の一部を置換するにはreplace()メソッドを使います。

d = "hello JavaScript"

print(d.replace("JavaScript", "python")) # 出力: hello python

# 置換する文字列が見つからない場合は元の文字列を返します。

## formatメソッドによる文字列の整形

# format()メソッドを使うと、文字列の中に変数を埋め込むことができます。
# さっき習ったsplitメソッドを使ってみましょう

e = "2021-01-01"
f = e.split("-")
print("今日は{}年{}月{}日です。".format(f[0], f[1], f[2]))  # 出力: 今日は2021年01月01日です。

# 他にも書式の設定もできたりします

## in演算子による文字列の検索

# in演算子を使うと、文字列が含まれているかどうかを簡単にチェックできます。

g = "hello python"

if "o" in g:
    print("文字列に'o'が含まれています")  # 出力: 文字列に'o'が含まれています
else:
    print("文字列に'o'は含まれていません")

# Hello pythonからHi Javaにするとどうなるでしょうか

g = "Hi Java"

if "o" in g:
    print("文字列にoが含まれています")
else:
    print("文字列にoが含まれていません")

# こんな感じでoが含まれなくなるとin演算子はFalseを返します