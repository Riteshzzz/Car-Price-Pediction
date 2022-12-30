import pandas as pd
import streamlit as st
import pickle
import sklearn
import numpy as np
from streamlit_option_menu import option_menu
pipe=pickle.load(open('VotingRegressorModel.pkl','rb'))
df=pickle.load(open('Cars24data.pkl','rb'))

st.title('CARS PRICE PREDICTOR')

#Brand
Name=st.selectbox('Brand',df['Name'].unique())
#Model
Company=st.selectbox('Model',df['Company'].unique())
#City
City=st.selectbox('City',df['City'].unique())
#Year
Year=st.selectbox('Year',df['Year'].unique())
#KM DRIVEN
KM_Driven = st.number_input('KM_Drivern',format='%.5f')
#N0 0F OWNERS
No_of_Owners = st.number_input('No Of Owners',format='%.5f')
#FUEL TYPE
Fuel_Type = st.selectbox('Fuel_Type',df['Fuel_Type'].unique())
#CALCULATED SCORE
Calculated_Score = st.number_input('Calculated Score',format='%.5f')
#Original Price
#Original_Price = st.number_input('Original Price',format='%.5f')
#Discount
#Discount = st.number_input('Discount',format='%.5f')
#Button
if st.button('Predict Price'):
    query=pd.DataFrame({'Name':Name,'Company':Company,'City':City,'Year':Year,'KM_Driven':KM_Driven,'No._of_Owners':No_of_Owners,'Fuel_Type':Fuel_Type,'Calculated_Score':Calculated_Score},index=[0])
    #query=[[Name,Company,City,Year,KM_Driven,No_of_Owners,Fuel_Type,Calculated_Score,Original_Price,Discount]]
    #query=query.reshape(1,10)
    st.title(int(pipe.predict(query)))