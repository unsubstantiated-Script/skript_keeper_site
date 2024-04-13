import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('img/profile_photo.png', use_column_width=True)

with col2:
    st.title("Justin C. Fulton")
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
