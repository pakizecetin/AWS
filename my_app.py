
import pickle
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title("This is a title")

st.text('This is a text')
st.markdown("Streamlit is **_really_ cool** :+1:")
st.markdown('# This is a markdown')
st.markdown('## This is a markdown')
st.header('This is a header')
st.subheader('This is a subheader')

#success-info-error

st.success('This is a success message!')
st.info('This is a purely info message')
st.error('This is an error')

st.help(range)

st.write('Hello') # pythondaki print islevini görüyor

#image
img = Image.open('images.jpeg')
st.image(img, caption='minnos')
st.image(img, caption='minnos', width=300)

#st.help(st.image)
#my_video = open("ml.mov",'rb')
#st.video(my_video)
st.video("https://www.youtube.com/watch?v=uHKfrz65KSU")

#checkbox

cbox = st.checkbox('Hide and Seek (bu bir checkbox')

if cbox:
    st.write('Hide')
else:
    st.write('Seek')


#radio button
status = st.radio('Select a color', ('blue', 'orange', 'yellow'))
st.write('Your favourite color is', status)

#button
st.button('Button') # müsteri inputlari giriyor buttona basinca prediction cikiyor
if st.button('Press me'):
    st.success('Prediction is...')

# select box
occupation = st.selectbox(
    "Your Occupation", ["Programmer", "DataScientist", "Doctor"])

st.write('Your occupation is:', occupation)

# multiselction
multi_select = st.multiselect("Select multiple numbers", [1, 2, 3, 4, 5])

# slider ---> numeric feature secmek icin uygun
#st.slider("Select a number", min_value=5, max_value=70, value=30, step=5)
#st.slider("Select a number", min_value=10, max_value=70, value=30, step=5)
#st.slider("Select a number", 5, 70, 5) # sayilarin tipinin ayni olmasi lazim
          # integer sa hepsi integer floatsa hepsi float

option1 = st.slider("Select a number", min_value=5, max_value=70, value=30, step=5)
option2 = st.slider("Select a number", min_value=10,
                    max_value=70, value=30, step=5)
result = option1*option2
st.write("result is : ", result)

#text input
name = st.text_input("Enter your name", placeholder="Your name here")
if st.button('Submit'):
    st.write('Hello', name.title())


# code ---> psif kodu gercekten import etmiyor
st.code('import pandas as pd')
st.code('import pandas as pd\nimport numpy as np')

# echo ---> kodu gercekten import ediyor ve calistiriyor
with st.echo():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    df

# date input
import datetime
today = st.date_input('Enter the date')

# time input
time = st.time_input('Time is:')

# sidebar ---> inputlar sidebardan girilebilir
st.sidebar.title('sidebar title')

st.sidebar.header("Sidebar header")
a = st.sidebar.slider("input", 0, 5, 2, 1) # inputlarlar sidebardan
x = st.sidebar.slider("input2")
st.write("# sidebar input result") # sonuc ana ekranda cikiyor
st.success(a*x)

df = pd.read_csv("Advertising (1).csv", nrows=(100))
st.table(df.head())
st.write(df.head())
st.dataframe(df.head())

####deployment dosyasindaki modeli cekip prediction yaptiriyoruz simdi:
#Project Example
import pickle 
filename = 'my_model'
model = pickle.load(open(filename, 'rb'))


st.write(df.describe())

TV = st.sidebar.number_input("TV:", min_value=5, max_value=300)
radio = st.sidebar.number_input("radio:", min_value=1, max_value=50)
newspaper = st.sidebar.number_input("newspaper:", min_value=0, max_value=120)

my_dict = { # yukarida degiskene atadim, ben degistirdikce degisecek
    "TV": TV,
    "radio": radio,
    "newspaper": newspaper,
}

df = pd.DataFrame.from_dict([my_dict])
st.table(df)
if st.button("Predict"):
    pred = model.predict(df)
    st.write(pred[0])
#---------------------