import streamlit as st
import pandas as pd

templates = {
    'Lufkin': {
        'Register': ['0/1', '0/2', '0/3', '0/4'],
        'Tag': ['Casing Pressure', 'Tubing Pressure', 'Temperature', 'Flow'],
        'Meter': [1, 1, 1, 1],
    },
    'TotalFlow': {
        'Register': ['0/1', '0/2', '0/3', '0/4'],
        'Tag': ['Casing Pressure', 'Tubing Pressure', 'Temperature', 'Flow'],
        'Meter': [1, 1, 1, 1],
    },
    'AutoPilot': {
        'Register': ['0/1', '0/2', '0/3', '0/4'],
        'Tag': ['Casing Pressure', 'Tubing Pressure', 'Temperature', 'Flow'],
        'Meter': [1, 1, 1, 1],
    }
}

templates_df = pd.DataFrame.from_dict(templates)

st.title("Device Templates")

all_selections = {
    'Lufkin': [
        "# # of meters",
    ],
    'TotalFlow': [
        '# # of meters',   
    ],
    'AutoPilot': [
        '# # of meters',   
    ]
}

param2_enabled = False
def param2_enable(enabled = True):
    global param2_enabled
    param2_enabled = enabled

device_type = st.selectbox(
    "Device type?",
    all_selections.keys(),
    on_change = param2_enable(True),
    placeholder = "Select...",
)

#st.write("You selected:", device_type)

param2 = st.selectbox(
    all_selections[device_type][0],
    range(1,4),
    disabled = not param2_enabled,
    #on_change = lambda : st.write(param2)
)

#st.write(param2)

def csv_data(device):
    return pd.DataFrame(templates[device]).to_csv(index = False).encode('utf-8')

def csv_file_name(device, meter_count):
    return f"{device}_template_{meter_count}_meters.csv"

st.download_button(
    label = "Download data as CSV",
    data = csv_data(device_type),
    file_name = csv_file_name(device_type, param2),
    mime = "text/csv",
    disabled = not param2_enabled,
)