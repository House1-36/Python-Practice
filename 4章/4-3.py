# リストとタプル

# リストには、複数の要素を格納することができます。他にも、タプルや辞書、集合など他にも様々な複数の要素を格納できるものがたくさんあります。
# これらのような性質を持つものを総称してコレクションといいます。

# リストの復習

# もちろんリストもインスタンスなので、メソッドを持っています。

# 一個一個見ていきましょう

# appendメソッド

# appendメソッドは、リストに新たに要素を追加することができるメソッドです。
# 末尾に追加します。

# 例

a = [1, 2, 3, 4]

print(a)

a.append(5)

print(a)

# popメソッド

# popメソッドはリストの要素の末尾にある要素を取得し、削除します。

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

c = b.pop()

print(c)

print(b)

# reverseメソッド

# reverseメソッドは並び順を反対にできるメソッドです。

d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(d)

d.reverse()

print(d)

# indexメソッド

# indexメソッドは、要素のインデックスを取得できます。

e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(e.index(10))

# 他にもいろいろあるけど一旦まとめるだけ

# insert(i, x) 指定したインデックスiにxを挿入する
# remove(x) 最初に見つかった値がxのものを削除する
# clear() 全要素を削除する
# count() 要素にxが出現する回数を返す

# メソッド以外のリストの操作

# del文

# del文は、インデックスを指定して、指定した部分の要素を削除することができます。

f = ["abc", "def", "cdf"]

print(f)

del f[2]

print(f)

# リストの連結

# リストは以下のような方法で連結することができます。

List1 = [1, 2, 3]
List2 = [4, 5, 6]
List3 = List1 + List2

print(List1)
print(List2)
print(List3)

# in演算子を使う

# 文章と同じように、in演算子を使うと、リストの中に含まれているか調べてくれます

Language = ["PHP", "Java", "Python"]

if Language in "PHP":
    print("PHPが含まれています")
else:
    print("PHPが含まれていません")

# len関数を使う

# さっきと同じでlen関数は要素の数を数えることができます。

scores = [32, 42, 82, 17]

print(len(scores))

# sorted関数を使う

# sorted関数を使うと、数字は昇順に、英語はアルファベット順に直してくれます。

scores2 = [12, 82, 32, 64, 92]

scores3 = sorted(scores2)

print(scores3)

# 引数にrevers=Trueと入れると降順になる

# 内包表記

# 2の倍数など規則に沿ったものをリストにしたい場合は内包表記を使うと便利です。

# 2の何乗を求めるリスト

g = [2 ** n for n in range(1, 11)]
print(g)

# 2の倍数を求めるリスト

h = [2 * x for x in range(1, 11)]
print(h)

# if 条件式を入れると、抽出もできます。

market = ['apple', 'grape', 'orange', 'banana', 'avocado']
market1 = [s for s in market if s[0] == 'a']

print(market1)

# タプル

# タプルは値の要素を変更できないリストです。

# 曜日とかに使います。

das = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

# リストと同様インデックスで要素にアクセスできます。

print(das[0])

# アンパック代入

# タプルとか、リストは以下のように各変数に代入できます。

data = ['山田', '太郎', 'user@example.com']
firstname, secondname, email = data