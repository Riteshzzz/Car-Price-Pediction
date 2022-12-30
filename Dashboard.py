import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import plotly
import plotly.express as px
st.title('ANALYSIS TOOL')
#Add Sidebar
st.sidebar.subheader('Visualization Setting')
#SetupFile Upload
uploaded_file=st.sidebar.file_uploader(label='Upload your csv or Excel File',type=['csv','xlsx'])

global df
if uploaded_file is not None:
    print()
    print()

    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)
try:
    st.write(df)
    numeric_columns = list(df.select_dtypes([float, int]).columns)
    catagorical_columns=list(df.select_dtypes([object]).columns)
except Exception as e:
    print(e)
    st.write('Please Upload The File To The Application')


#Add Select widget to The Sidebar
chart_select = st.sidebar.selectbox(label='Select the Chart Type For Numerical',
                                    options=['Scatterplots','Histogram'])
if chart_select=='Scatterplots':
    st.sidebar.subheader('Scatterplots Settings')
    try:
        x_values=st.sidebar.selectbox('X axis',options=numeric_columns)
        y_values=st.sidebar.selectbox('Y axis',options=numeric_columns)
        plot=px.scatter(data_frame=df,x=x_values,y=y_values)
        st.plotly_chart(plot)

    except Exception as e:
        print(e)
if chart_select=='Histogram':
    st.sidebar.subheader('Histogram Settings')
    try:
        x_values=st.sidebar.selectbox('X axis',options=numeric_columns)
        y_values=st.sidebar.selectbox('Y axis',options=numeric_columns)
        plot=px.histogram(data_frame=df,x=x_values,y=y_values)
        st.plotly_chart(plot)

    except Exception as e:
        print(e)

# if chart_select=='Boxplot':
#     st.sidebar.subheader('Boxplots Settings')
#     try:
#         x_values=st.sidebar.selectbox('X axis',options=numeric_columns)
#         y_values=st.sidebar.selectbox('Y axis',options=numeric_columns)
#         plot=px.box(data_frame=df,x=x_values,y=y_values)
#         st.plotly_chart(plot)
#     except Exception as e:
#         print(e)
if chart_select=='Barplot':
    st.sidebar.subheader('Barplots Settings')
    try:
        x_values=st.sidebar.selectbox('X axis',options=numeric_columns)
        y_values=st.sidebar.selectbox('Y axis',options=numeric_columns)
        plot3=px.violin(data_frame=df,x=x_values,y=y_values)
        st.plotly_chart(plot3)
    except Exception as e:
        print(e)




chart_select = st.sidebar.selectbox(label='Select the Chart Type For Catagorical',
                                    options=['Piechart'])
if chart_select=='Piechart':
    st.sidebar.subheader('Piechart Settings')
    try:
        Values=st.sidebar.selectbox('Values',options=catagorical_columns)
        plot1=px.pie(data_frame=df,names=Values)
        st.plotly_chart(plot1)

    except Exception as e:
        print(e)

