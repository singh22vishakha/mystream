import streamlit as st
st.set_page_config(page_title='my streamlit',page_icon='random')
mymenu=st.sidebar.selectbox('My Menu',('Home','Fill form','Download'))
st.image ('https://onleitechnologies.com/wp-content/uploads/2021/12/cropped-Untitled_design__6_-removebg-preview-1.png')
st.title('Onlei Technologies')
st.header ('By Abhinav Shrivastava')
st.text ('This is a tutorial on Streamlit Library')
if (mymenu=='Home'):
    st.markdown('<center><h1>WELCOME</h1></center>',unsafe_allow_html=True)
    st.video ('https://www.youtube.com/watch?v=spZgfeZMc40')
elif (mymenu=='Fill form'):
    with st.form("My form"):
                 name=st.text_input('Enter name')
                 dob=st.date_input("Choose Date of Birth")
                 marks=st.slider('Choose Marks')
                 k=st.form_submit_button("Submit Form")
                 if k:
                    st.write('name=',name,'DOB:',dob,'Marks:',marks)
elif (mymenu=='Download'):
    st.header ("Downloads")
    st.download_button('Download Now','Hello this is the downloaded data', 'onlei.txt')
