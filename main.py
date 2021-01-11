import streamlit as st
import numpy     as np
import pandas    as pd

#タイトル
st.title('Duration Curve')

data = pd.read_csv('choryu_h.csv')
info = pd.read_csv('grid_info_h.csv')

#データフレーム
df1 = pd.DataFrame({
    'Grid_Name'    : info.iloc[1][1:len(info.columns)],
    'Grid_Capacity': info.iloc[3][1:len(info.columns)]
})

# テーブル表示　静的なテーブル(表)を作成したい時
expander1 = st.beta_expander('Grid Information')
expander1.write.st.table(df1)
#st.table(df1)

# 折れ線グラフ
st.line_chart(data[data.columns[1]])


