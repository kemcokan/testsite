#@title ## ブラウザでWebページを開く
import streamlit as st
import pandas as pd
import webbrowser

st.set_page_config(page_title='Amazon Search')
st.title('Amazon Search')
product = st.text_input('商品名')
# st.write(f'{product}')

low = st.number_input('以上')
heigh = st.number_input('以下')

#「&low-price=3000&high-price=5000」と2つ合わせて使うと、「3000円以上5000円以下の商品」といった範囲内で絞り込む
if st.button('Search'):
    url = f'https://www.amazon.co.jp/s?k={product}'

    if low > 0:
        url = url + f'&low-price={low}'
    
    if heigh > 0:
        url = url + f'&high-price={heigh}'

    # new = 動作
    # 0 = 同じウインドウで開く
    # 1 = 新しいウインドウで開く
    # 2 = 新しいタブで開く
    # 第3引数 autoraise: Trueなら、可能であればウィンドウが前面に表示されます。
    webbrowser.open(url, new=0, autoraise=True)


