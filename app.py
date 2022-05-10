# Required packages importing
import os, streamlit as st
from streamlit_option_menu import option_menu
from pathlib import Path

st.set_page_config(layout="wide")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
#st.markdown(hide_streamlit_style, unsafe_allow_html=True)
filename = './/autogen//files//_configmap.tpl'

def streamlit_menu():
    # sidebar menu
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",  # required
            options=["Search"],  # required
            icons=["search"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
        )
    return selected

selected = streamlit_menu()

if selected == "Search":
    st.markdown(""" Message replacement in configmap files""")

    expander = st.expander("See explanation")
    expander.write("""
        This tool replaces msg1 & msg2 values in the _configmap.tpl \n
    """)
    with st.expander('Demo'):
        st.image('demo.png')       
         
    msg1 = st.text_input('MSG1', '')
    msg2 = st.text_area("MSG2")
    
    if st.button('Submit'):
        path = ".//autogen//data"
        # Check whether the specified path exists or not
        isExist = os.path.exists(path)
        if not isExist:  
            # Create a new directory because it does not exist 
            os.makedirs(path)
  
        with open(path + '//msg.txt', 'w') as file:
            file.write(msg2)
        
        path = Path(filename)

        if path.is_file():
            # Read in the file
            with open(filename, 'r') as file :
                filedata = file.read()
            # Replace the target string
            filedata = filedata.replace('$msg1', msg1)
            filedata = filedata.replace('$msg2', msg2)
            # Write the file out again
            with open(filename, 'w') as file:
                file.write(filedata)
            
        #st.balloons()
        else:
            st.write(f'configmap.tpl file does not exist.')
