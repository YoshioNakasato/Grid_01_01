import streamlit as st
import numpy     as np
import pandas    as pd

#タイトル
st.title('STREAMLIT　超入門')

#テキスト
st.write('DtataFrame')

#データフレーム
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

#データフレームの表示　列にてソート(降順、昇順が操作できる)
#st.write(df)
# st.dataframe(df)でも同じように表示することができる
# width, heightといった引数で体裁を整えることができる
# st.dataframe(df, width=100, height=100)
# ピクセル単位で縦横の大きさを指定した

# ハイライト：列の中の数字で最大値のところにハイライト
#st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)


# テーブル表示　静的なテーブル(表)を作成したい時
st.table(df)

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy     as np
import pandas    as pd
```
"""

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns =  ['A', 'B', 'C']
)
df2
# 折れ線グラフ
st.line_chart(df2)
st.area_chart(df2)
# 棒グラフ
st.bar_chart(df2)

#おまけ
import altair as alt
c = alt.Chart(df2).mark_circle().encode(
    x='A', y='B', size='C', color='C', tooltip=['A', 'B', 'C']
)
st.altair_chart(c, use_container_width=True)

#マップのプロット
df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50]+[35.69, 139.70],
    columns =  ['lat', 'lon']
)
df3
st.map(df3)

# 画像表示
from PIL import Image

st.write('Display Image')
#写真データの参照先はsmaple.pyファイルと同じ階層にあるもの
img = Image.open('sample.jpeg')
st.image(img, caption='Photo', use_column_width=True)
