# similar-words

文字列の類似度を計算します。
<p>文字が連続で一致している場合に一致率が高くなる仕様です。<br>
但し入力文字数が３文字以下の場合は１文字の一致を許容するため、<br>
関係ない文字が一致しやすくなります。<br>
4文字以上入力することで目的の文字列が一致しやすくなります。<br>
出力結果が１に近いほど一致率が高く、完全一致の場合は１になります。
</p>


<h2>使用方法</h2>

```bash
git clone https://github.com/takashi-koshiba/similar-words
cd similar-words/python/
python exampleCalcCost.py "文字列1" "文字列2"
```


<h2>実行例</h2>

<p>入力値：あいうえお</p>

| ターゲット文字列 | 一致率 |
| ------------- | ------------- |
|あいうえお| 1.0  |
|あいうえおあいうえお  | 0.2222 |
| あいう  | 0.3 |
| あいえお  | 0.0667 |
| あうお  | 0.0 |


<h2>実行例(入力値が3文字以下)</h2>

<p>入力値：あいう</p>

| ターゲット文字列 | 一致率 |
| ------------- | ------------- |
|あいう| 1.0  |
|あいうえお| 0.4  |
|あいうあいう| 0.2857142  |
|あいうえおあいうえお  | 0.1090909|
| あいえお  | 0.15|
| あうお  | 0.1111 |

<p></p>





