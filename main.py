import streamlit as st
import pandas

st.set_page_config(layout="wide")

title = "The Best Company"
description = """
The word 'talent' has become a buzzword in our society. Everyone wants to have a talent, but many people do not know what that means. Some believe that talent is a natural ability that you were born with. Others think that talent is something you learn from an early age. Either way, people think that talent can help you reach your goals. However, talent is only useful when you use it. The primary problem with talent is that it can be misleading. A person may have talent for singing, but they will probably fail without proper training.
"""
heading1 = "Our Team"

st.title(title)
st.info(description)
st.subheader(heading1)

df = pandas.read_csv("data.csv", sep=",")

col1, empty_col1, col2, empty_col2, col3 = st.columns([1.5, 0.25, 1.5, 0.25, 1.5])

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"], width=150)

with col2:
    for index, row in df[5:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"], width=150)

with col3:
    for index, row in df[9:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"], width=150)