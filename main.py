import pandas
import streamlit as st
from streamlit_extras.grid import grid

st.set_page_config(layout="wide")

# Squirrly, but trying to stop the "full screen" button from appearing as it doesn't align well in grids.
hide_full_screen = '''
<style>
p {font-size: 1.5rem;}
.element-container .st-emotion-cache-youdgo {visibility: hidden;}
</style>
'''
st.markdown(hide_full_screen, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.image('img/profile_photo.png', use_column_width=True)

with col2:
    st.title("Justin C. Fulton", anchor=False)
    content = """
I'm a software engineer, educator, content development professional, and administrator; leveraging expertise gained over 
many years of work in the education sector as well as advanced software design for insurance and real estate agencies. 
I began my career as a Title 1 English Teacher, taught first in Washington state, then in Arizona, and finally spent 
many years in the United Arab Emirates working as a teacher, web developer, and content creator. 
    When I came back to America, I furthered my studies by gaining a degree in Computer Science, and I dove further into 
design and software engineering. My passions and projects today are cloud networking and delving ever deeper into 
Machine Learning and Artificial Intelligence.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in GoLang and Python. Feel free to contact me!
"""
st.header(content2, divider="blue")

df = pandas.read_csv("data.csv", sep=";")

my_grid = grid(3, gap="large")

for index, row in df.iterrows():
    tile = my_grid.container()
    tile.header(row["title"], anchor=False)
    tile.write(row["description"])
    tile.image("img/" + row["image"], use_column_width='always')
    tile.write(f"[Source Code]({row['url']})")
