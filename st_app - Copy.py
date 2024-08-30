import joblib

import streamlit as st
import pandas as pd

model = joblib.load('model_final.pkl')

st.set_page_config("Final Project (Used car Prediction)")

def home_page():
    # Display text
    st.title("Poland used car Price")
    st.header("Used car price prediction")

    st.image("http://media.comcar.co.uk/article/2016/May/image/25143-1463683879-Screen%20shot%202016-05-19%20at%2019.51.13-320.jpg")

    #DataFrames
    df = pd.DataFrame({'brand' : ['alfa-romeo','alfa-romeo','alfa-romeo'],
                       'Fuel type' : ['Benzyna','Benzyna','Benzyna'],
                   'mileage':[133760,133760,227000],
                   'gearbox':['manual','manual','manual'],
                   'price':[14700,14000,4500]})
    st.dataframe(df)

def start_prediction():
    #Inputs

    st.title('Price Prediction')
    year = st.number_input('Year')
    mileage = st.number_input('Enter mileage in (Km)')
    gearbox = st.radio("gearbox",['manual','automatic'])
    fuel_type = st.selectbox("Fuel Type",["Benzyna","Benzyna+LPG","Diesel","Hybryda"])
    brand = st.selectbox("Car brand",["alfa-romeo","aston-martin","audi","bentley",'bmw','cadillac',
                          "chevrolet","citroen","dacia","daewoo",'daihatsu','dodge',
                          "fiat","ford","honda",'hyundai','infiniti','isuzu',
                          "jaguar","jeep","kia",'lancia','land-rover','maserati',
                          "mazda","mercedes-benz","mini","mitsubishi",'nissan','opel','peugeot',
                          "porsche","renault","rover","saab",'seat','skoda','smart','toyota','volkswagen','volvo'

                         
                         ])


    st.button("predict",on_click = prdict,args = (mileage,year,gearbox,brand,fuel_type))
    
def prdict(mileage,year,gearbox,brand,fuel_type):
    arr = [0]*48
    arr[0] = mileage
    arr[1] = 0 if gearbox == 'manual' else 1
    arr[2] = year
    fuel_list = ["Benzyna","Benzyna+LPG","Diesel","Hybryda"]
    index = fuel_list.index(fuel_type)
    arr[index+3] = 1
    brand_list = ["alfa-romeo","aston-martin","audi","bentley",'bmw','cadillac',
                          "chevrolet","citroen","dacia","daewoo",'daihatsu','dodge',
                          "fiat","ford","honda",'hyundai','infiniti','isuzu',
                          "jaguar","jeep","kia",'lancia','land-rover','maserati',
                          "mazda","mercedes-benz","mini","mitsubishi",'nissan','opel','peugeot',
                          "porsche","renault","rover","saab",'seat','skoda','smart','toyota','volkswagen','volvo'
                         ]
    
    index = brand_list.index(brand)
    arr[index+7] = 1
    pred = model.predict([arr])
    
  
    results(pred[0],arr)
                          
def results(result,arr):
    st.title('Results')
    #st.markdown(arr)
    st.markdown('**Estimated Price in Pln:**')
    st.markdown(round(result,2))

    st.button('Make another prediction',on_click = start_prediction)
    
page = st.sidebar.selectbox("select page",['Home','Start prediction'])
if page == 'Home':
    home_page()
else:
    start_prediction()