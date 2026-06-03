import streamlit as st
import pandas as pd
import numpy as np
import random
from puzzles import beginner_puzzles
from puzzles import advanced_puzzles
from game import setup, move

if "diff" not in st.session_state:
    st.title("GridQuest")
    st.subheader("How To Play")
    st.markdown("""
        Welcome to **GridQuest**!
        Your goal is to move the player **P** from the start **S** to the end **E**.
        To move, type commands into the box and press **Enter**. 
        You can move in all four directions and diagonally.
        You can not go through walls **X**.
        
        If you play Advanced Mode, you can not visit boxes already visited, and you must collect all stars **🌟**.
        
        You have **1 minute** to solve as much puzzles as possible.
        You get **1 point** if you solve a puzzle and a **1 point bonus** for finding the shortest path.
                """)

    st.subheader("Select Difficulty")

    if st.button("Beginner"):
        st.session_state.diff = "beginner"
        st.rerun()

    if st.button("Advanced"):
        st.session_state.diff = "advanced"
        st.rerun()
    
    st.stop()

st.title("GridQuest")

#adv mode
if st.session_state.diff == "advanced":
    advmode = True
else:
    advmode = False

if "chosen" not in st.session_state:
    if st.session_state.diff == "beginner":
        st.session_state.chosen = random.choice(beginner_puzzles) #https://docs.streamlit.io/develop/concepts/architecture/session-state
    else:
        st.session_state.chosen = random.choice(advanced_puzzles)
chosen = st.session_state.chosen

if "array" not in st.session_state:
    st.session_state.array = setup(chosen)

rows = chosen["rows"]
cols = chosen["cols"]
S_row = chosen["S"][0]
S_col = chosen["S"][1]
E_row = chosen["E"][0]
E_col = chosen["E"][1]
X_pos = chosen["X"]
T_pos = chosen["T"]

if "Player_row" not in st.session_state: #init the start as P
    st.session_state.Player_row = S_row

if "Player_col" not in st.session_state:
    st.session_state.Player_col = S_col

#stars seccion
if "stcollected" not in st.session_state:
    st.session_state.stcollected = set()

if "totstars" not in st.session_state:
    st.session_state.totstars = set(tuple(x) for x in T_pos)

if advmode:
    if "blocksvisited" not in st.session_state:
        st.session_state.blocksvisited = set()

with st.form("cmds", clear_on_submit = True, enter_to_submit = True):
    urmove = st.text_input("Move with W/A/S/D/WD/SD/SA/WA")
    submit = st.form_submit_button("Enter")

if submit:
    st.session_state.msg = ""

    if advmode:
        st.session_state.blocksvisited.add((st.session_state.Player_row,st.session_state.Player_col))
        st.session_state.Player_row, st.session_state.Player_col,st.session_state.msg = move(st.session_state.Player_row, st.session_state.Player_col, urmove, st.session_state.array,st.session_state.blocksvisited)
    else:
        st.session_state.Player_row, st.session_state.Player_col,st.session_state.msg = move(st.session_state.Player_row, st.session_state.Player_col, urmove, st.session_state.array)

    if st.session_state.array[st.session_state.Player_row][st.session_state.Player_col] == "T":
        st.session_state.stcollected.add((st.session_state.Player_row, st.session_state.Player_col))

if "msg" in st.session_state and st.session_state.msg != "":
    st.warning(st.session_state.msg)

st.write(f"Stars: {len(st.session_state.stcollected)} / {len(st.session_state.totstars)}")

def celltext(r,c):
    if r == st.session_state.Player_row and c == st.session_state.Player_col:
        return "P"
    thingy = st.session_state.array[r][c]
    if thingy == 0:
        return "X"
    elif thingy == 1:
        return ""
    elif thingy == "E":
        return "E"
    elif thingy == "S":
        return "S"
    elif thingy == "T":
        return "🌟"

grid = f"""<div style=" display: grid; grid-template-columns: repeat({cols},50px); width: fit-content;">"""

for r in range(rows):
    for c in range(cols):
        txt = celltext(r,c)
        grid += f"""<div style=" width: 50px; height: 50px; border: 2px solid black; display: flex; align-items: center; justify-content: center; font-size: 24px;"> {txt} </div> """

grid += "</div>"

st.write(grid, unsafe_allow_html=True)

if st.session_state.Player_row == E_row and st.session_state.Player_col == E_col:
    if st.session_state.stcollected == st.session_state.totstars:
        st.success("you reached the end!", icon="✅")
    else:
        st.success("u did NOT get all", icon="❌")
