import streamlit as st
import pandas as pd
import mysql.connector 
from database import query,No_query
mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="", 
    database="vaccine_management"
)
c = mydb.cursor()

def Customize_query():
    c_query = st.text_input("Enter any Query:")
    if st.button('Execute'):
        x=query(c_query)
        st.success("Executed successfully") 
        if(x):
            st.dataframe(x) 
                  

def Customize_query_N():
    No_c_query=st.text_input("Enter your query:")
    if st.button('Execute'):
        No_query(No_c_query)
        st.success("Executed Successfully") 
