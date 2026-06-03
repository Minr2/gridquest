import streamlit as st
import pandas as pd
import numpy as np
import random
from puzzles import beginner_puzzles
from game import set, move

st.title("GridQuest")

if "chosen" not in st.session_state:
    st.session_state.chosen = random.choice(beginner_puzzles) #https://docs.streamlit.io/develop/concepts/architecture/session-state
chosen = st.session_state.chosen

if "array" not in st.session_state:
    st.session_state.array = set(chosen)

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
    st.session_state.Player_col = S_col

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

grid = f"""<div style=" display: grid; grid-template-columns: repeat({cols},50px); width: fit-content;">"""

for r in range(rows):
    for c in range(cols):
        txt = celltext(r,c)
        grid += f"""<div style=" width: 50px; height: 50px; border: 2px solid black; display: flex; align-items: center; justify-content: center; font-size: 24px;"> {txt} </div> """

grid += "</div>"

st.write(grid, unsafe_allow_html=True)

with st.form("cmds", clear_on_submit = True, enter_to_submit = True):
    urmove = st.text_input("Move with W/A/S/D/WD/SD/SA/WA")
    submit = st.form_submit_button("Enter")

if submit:
    st.session_state.Player_row, st.session_state.Player_col = move(st.session_state.Player_row, st.session_state.Player_col, urmove, st.session_state.array)
    st.rerun()

if st.session_state.Player_row == E_row and st.session_state.Player_col == E_col:
    st.success("you reached the end!", icon="✅")