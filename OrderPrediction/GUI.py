import streamlit as st
from LogReg import inference
from PIL import Image

st.set_page_config(page_title='Order Prediction', page_icon=':pizza:', layout='centered', initial_sidebar_state='auto')


model = inference()

st.sidebar.title('Select your preference')

Name = st.sidebar.text_input("Type in your Name")

Age = st.sidebar.text_input("Type in your age")


Gender = st.sidebar.selectbox(
    'Select your Gender',
    ('Male', 'Female', 'Others'),
    key='Gen'
)

Frequency = st.sidebar.selectbox(
    'Select how many times you order in a month',
    (0,2,4,6,'8 and above'),
    key='freq'
)

if Gender=='Male':
	Gender=0
elif Gender=='Female':
	Gender=1
else:
	Gender=2


if Age!='' and Name!='':
	Age = int(Age)
	if Frequency=='8 and above':
		Frequency=8
	out=model.pred(Age, Gender, Frequency)

	if out==1:
		st.title(Name + ' is **_most_** likely to order again :sunglasses:')
		image = Image.open('1.png')
		st.image(image)
	else:
		st.title(Name + ' is **_not_** likely to order again :neutral_face:')
		image = Image.open('0.png')
		st.image(image)
