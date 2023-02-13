import streamlit as st
import pandas as pd 
import plotly.express as px 

st.set_page_config(page_title='Excel Plotter')
st.title('Excel Plotter ')
st.subheader('Feed me with your Excel file')

uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx')
if uploaded_file :
    st.markdown('----')

    
    df=pd.read_excel(uploaded_file, engine='openpyxl')
    df = df.astype(str)
    st.dataframe(df)
    groupby_column=st.selectbox(
        'what would you like to analyse ? ', ('Name and Surname','Ward','Health Facility'),
    )

    output_columns=['Reach','Variance']
    df_grouped=df.groupby(by=[groupby_column],as_index=False)[output_columns].sum()
    st.dataframe(df_grouped)

    fig=px.bar(

        df_grouped,
        x=groupby_column,
        y='Reach',
        color='Variance',
        color_continuous_scale=['red','yellow', 'green'],
        template='plotly_white',
        title=f'<b> Reach & Variance by {groupby_column}</b>'
    )
    st.plotly_chart(fig)

