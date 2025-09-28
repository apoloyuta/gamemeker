import streamlit as st
from player import Player
from battle import Enemy, fight
from explore import move
from quest import generate_quest
from items import gain_item

st.title("Eclipse of Eternity")

# 初期化
if "player" not in st.session_state:
    name = st.text_input("名前を入力")
    if st.button("開始"):
        st.session_state.player = Player(name)

if "player" in st.session_state:
    player = st.session_state.player
    st.write(f"現在地: {player.location} | HP: {player.hp} | レベル: {player.level} | 経験値: {player.experience}")

    col1, col2, col3, col4 = st.columns(4)

    if col1.button("探索"):
        quest = generate_quest(player)
        st.write(f"クエスト: {quest}")
        result = move(player)
        st.write(result)

    if col2.button("戦闘"):
        enemy = Enemy("ゴブリン", 30, 5)
        result = fight(player, enemy)
        st.write(result)
        if player.hp <= 0:
            st.error("💀 HPが0になりました。ゲームオーバー！")

    if col3.button("休む"):
        player.hp = min(player.hp + 20, 100)
        st.success("HPを20回復しました")

    if col4.button("アイテム獲得"):
        item = gain_item(player)
        st.write(f"アイテム獲得: {item.name} - {item.effect}")
