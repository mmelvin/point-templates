import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

all_selections = {
    'Lufkin': [
        '# of meters',   
    ],
    'TotalFlow': [
        '# of meters',   
    ],
    'AutoPilot': [
        '# of meters',   
    ]
}

option = st.selectbox(
    "Device type?",
    all_selections.keys()
)

st.write("You selected:", option)