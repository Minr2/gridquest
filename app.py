import streamlit as st
import pandas as pd
import numpy as np
from puzzles import beginner_puzzles

st.title("GridQuest")

chosen = beginner_puzzles[0]
rows = chosen["rows"]
cols = chosen["cols"]
S_row = chosen["S"][0]
S_col = chosen["S"][1]
E_row = chosen["E"][0]
E_col = chosen["E"][1]
X_pos = chosen["X"]
T_pos = chosen["T"]

def celltext(r,c):
    if r == S_row and c == S_col:
        return "S"
    elif r == E_row and c == E_col:
        return "E"
    elif (r,c) in X_pos:
        return "X"
    elif (r,c) in T_pos:
        return "*"
    else:
        return ""

grid = f"""<div style=" display: grid; grid-template-columns: repeat({cols},50px); width: fit-content;">"""

for r in range(rows):
    for c in range(cols):
        txt = celltext(r,c)
        grid += f"""<div style=" width: 50px; height: 50px; border: 2px solid black; display: flex; align-items: center; justify-content: center; font-size: 24px;"> {txt} </div> """

grid += "</div>"

st.markdown(grid, unsafe_allow_html=True)

