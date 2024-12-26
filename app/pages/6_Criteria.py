import streamlit as st
import shared.simple_plotsheet as shared_plot
import shared.structure_explorer as se
import shared.dataframe_maker as dm
import shared.geo_plotter as gp

DATADIR = "app/data/"

st.set_page_config(
        page_title="prometry",
        page_icon="app/static/plot.png",
        layout="wide",
)

st.header("Prometry - Criteria playsheet")
st.caption('''
           "something about disulfide bonds"''')

st.write("""Edit the structures and the geometric definitions to find geometric information for your chosen structures. 
         The criteria search is explained on the help pages.""")

geos = "N:CA:C:N+1 C-1:N:CA:C N:O N:N+1 N:CA:C"

if True:
        ls_structures, ls_crits = se.explorer(use_geos="criteria")
        st.write("---")
        df = dm.maker_geos(ls_structures, ls_crits)
        st.write("---")
        gp.geo_plot(df)
                
st.divider()
st.caption("""---""")
