# 必要ライブラリ
# pip install streamlit openai rich

import streamlit as st
import openai
from random import choice

# --- OpenAI APIキー ---
openai.api_key = "YOUR_API_KEY"

# --- プレイヤー初期情報 ---
player = {
    "name": "",
    "hp": 100,
    "level": 1,
    "inventory": [],
    "location": "村",
    "experience": 0
}

# --- マップ候補 ---
locations = ["森", "洞窟", "湖", "塔", "遺跡"]

# --- AI生成関数 ---
def generate_ai_response(prompt, max_tokens=250):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}],
        max_tokens=max_tokens
    )
    return response.choices[0].message.content.strip()

# --- 敵生成＆戦闘 ---
def encounter_enemy():
    enemy = choice(["ゴブリン", "オーク", "スケルトン", "魔獣"])
    prompt = f"プレイヤー({player['name']})が{player['location']}で{enemy}に遭遇。戦闘描写、攻撃パターン、ダメージ量を生成してください。"
    story = generate_ai_response(prompt)
    damage = 10 + player["level"] * 2
    player["hp"] -= damage
    loot_prompt = f"{enemy}を倒したらどんなアイテムが落ちるか生成してください。"
    loot = generate_ai_response(loot_prompt, max_tokens=50)
    player["inventory"].append(loot)
    exp_gain = 20 + player["level"] * 5
    player["experience"] += exp_gain
    return story, damage, loot, exp_gain

# --- サイドクエスト生成 ---
def generate_quest():
    prompt = f"プレイヤー({player['name']})が{player['location']}に到着。探索イベントやサイドクエストを生成してください。"
    quest = generate_ai_response(prompt)
    return quest

# --- レベルアップ判定 ---
def check_level_up():
    required_exp = player["level"] * 50
    if player["experience"] >= required_exp:
        player["level"] += 1
        player["hp"] = 100
        st.success(f"🎉 レベルアップ！レベル {player['level']} に到達しました。HP全回復！")
        player["experience"] -= required_exp

# --- Streamlit UI ---
st.title("🔥 最高生成AI RPG 完全版 🔥")

if "started" not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    player["name"] = st.text_input("あなたの名前を入力してください")
    if st.button("ゲーム開始"):
        st.session_state.started = True
else:
    st.write(f"現在地: {player['location']} | HP: {player['hp']} | レベル: {player['level']} | 経験値: {player['experience']}")
    col1, col2, col3, col4 = st.columns(4)
    
    if col1.button("探索"):
        story, damage, loot, exp_gain = encounter_enemy()
        st.markdown(f"**{story}**")
        st.markdown(f"[red]敵の攻撃でHP-{damage}[/red]")
        st.markdown(f"[green]アイテム獲得: {loot} | 経験値+{exp_gain}[/green]")
        check_level_up()
        
    if col2.button("休む"):
        heal = 20
        player["hp"] = min(player["hp"] + heal, 100)
        st.markdown(f"[green]休んでHP回復しました。HP+{heal}[/green]")

    if col3.button("インベントリ"):
        st.markdown(f"[blue]持ち物: {player['inventory']}[/blue]")

    if col4.button("移動"):
        player["location"] = choice(locations)
        st.markdown(f"[bold magenta]{player['location']}へ移動しました。[/bold magenta]")
        quest = generate_quest()
        st.markdown(f"**{quest}**")

    if player["hp"] <= 0:
        st.markdown("[bold red]💀 HPが0になりました。ゲームオーバーです。[/bold red]")
