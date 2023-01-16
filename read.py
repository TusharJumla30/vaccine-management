import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_vaccine_data,view_person_data,view_hospital_data,view_inventory_data,view_doctor_data,view_location_data,view_supplies_data,view_vaccinates_data

def read_vaccine():
 result = view_vaccine_data()
 #st.write(result) 
 df = pd.DataFrame(result, columns=['V_name', 'V_company', 'V_cost']) 
 with st.expander("View all Vaccine"):
    st.dataframe(df)
 with st.expander("View all vaccine"):
    task_df = df['V_name'].value_counts().to_frame()
    task_df = task_df.reset_index()
    st.dataframe(task_df)
    p1 = px.pie(task_df, names='index', values='V_name')
    st.plotly_chart(p1)

def read_inventory():
 result = view_inventory_data()
 #st.write(result) 
 df = pd.DataFrame(result, columns=['I_id',' I_name', 'I_contactno','I_address']) 
 with st.expander("View all Inventory"):
    st.dataframe(df)
 with st.expander("Inventory"):
     task_df = df['I_id'].value_counts().to_frame()
     task_df = task_df.reset_index()
     st.dataframe(task_df)
     p1 = px.pie(task_df, names='index', values='I_id')
     st.plotly_chart(p1)

def read_person():
 result = view_person_data()
 #st.write(result) 
 df = pd.DataFrame(result, columns=['P_id','P_name','P_Gender','P_DOB','P_contactno','P_address','P_email']) 
 with st.expander("View all Person"):
    st.dataframe(df)
 with st.expander("Patients gender"):
    task_df = df['P_Gender'].value_counts().to_frame()
    task_df = task_df.reset_index()
    st.dataframe(task_df)
    p1 = px.pie(task_df, names='index', values='P_Gender')
    st.plotly_chart(p1)

def read_hospital():
 result = view_hospital_data()
 #st.write(result) 
 df = pd.DataFrame(result, columns=['H_id','H_name','H_pwd','H_contactno','H_type','H_address','H_email','H_vac','quant_rem']) 
 with st.expander("View hospital details"):
    st.dataframe(df)
 with st.expander("Hospitals list"):
    task_df = df['H_name'].value_counts().to_frame()
    task_df = task_df.reset_index()
    st.dataframe(task_df)
    p1 = px.pie(task_df, names='index', values='H_name')
    st.plotly_chart(p1)

def read_location():
 result = view_location_data()
 #st.write(result) 
 df = pd.DataFrame(result, columns=['pincode','area','state','city']) 
 with st.expander("View locations detail"):
    st.dataframe(df)
 with st.expander("Locations list"):
    task_df = df['pincode'].value_counts().to_frame()
    task_df = task_df.reset_index()
    st.dataframe(task_df)
    p1 = px.pie(task_df, names='index', values='pincode')
    st.plotly_chart(p1)

def read_vaccinates():
 result = view_vaccinates_data()
 #st.write(result) 
 df = pd.DataFrame(result, columns=['P','Hosp','Date_first','Date_last']) 
 with st.expander("View vaccinates details"):
    st.dataframe(df)
 with st.expander("Vaccinates list"):
    task_df = df['P'].value_counts().to_frame()
    task_df = task_df.reset_index()
    st.dataframe(task_df)
    p1 = px.pie(task_df, names='index', values='P')
    st.plotly_chart(p1)

def read_supplies():
 result = view_supplies_data()
 #st.write(result) 
 df = pd.DataFrame(result, columns=['S_id','S_hospital','S_inventory','S_quantity','S_time']) 
 with st.expander("View all supplies details"):
    st.dataframe(df)
 with st.expander("Supply list"):
    task_df = df['S_id'].value_counts().to_frame()
    task_df = task_df.reset_index()
    st.dataframe(task_df)
    p1 = px.pie(task_df, names='index', values='S_id')
    st.plotly_chart(p1)

def read_doctor():
 result = view_doctor_data()
 #st.write(result) 
 df = pd.DataFrame(result, columns=['D_id','D_dept']) 
 with st.expander("View Doctor details"):
    st.dataframe(df)
 with st.expander("Doctors list"):
    task_df = df['D_id'].value_counts().to_frame()
    task_df = task_df.reset_index()
    st.dataframe(task_df)
    p1 = px.pie(task_df, names='index', values='D_id')
    st.plotly_chart(p1)