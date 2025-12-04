
import streamlit as st

DATADIR = "app/data/"

def init():
    # All key initilisation
    if 'df_geos' not in st.session_state:
        st.session_state['df_geos'] = None
    if 'df_geos_xtra' not in st.session_state:
        st.session_state['df_geos_xtra'] = None    
    if 'df_atoms' not in st.session_state:
        st.session_state['df_atoms'] = None
    if "ls_structures" not in st.session_state:
        st.session_state["ls_structures"] = ["AF-P04637-F1-model_v6","1YCS"]
    if "ls_geos" not in st.session_state:
        st.session_state['ls_geos'] = ["C-1:N:CA:C","N:CA:C:N+1","N:O","N:N+1","N:CA:C"]
    if "ls_contacts" not in st.session_state:
        st.session_state['ls_contacts'] = ["CA[aa|20]:{CA@i}[dis|0.5><10,rid|>1,aa|20"]
    if "ls_criteria" not in st.session_state:
        st.session_state['ls_criteria'] = ['SG:{N}+2','SG:{SG@1}','SG:{SG@2}','SG:SG','SG:(N)','SG:N']
    if "str_structures" not in st.session_state:
        st.session_state['str_structures'] = "AF-P04637-F1-model_v6 1YCS"
