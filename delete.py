import pandas as pd 
import streamlit as st
from database import view_only_Vaccine_name,view_vaccine_data,view_doctor_data,view_only_Doctor_id,view_vaccinates_data,view_hospital_data,view_inventory_data,view_location_data,view_person_data,view_supplies_data
from database import delete_data_doctor,delete_data_hospital,delete_data_inventory,delete_data_location,delete_data_person,delete_data_supplies,delete_data_vaccinates,delete_data_Vaccine
from database import view_only_Doctor_id,view_only_Hospital_id,view_only_inventory_id,view_only_Location_pin,view_only_person_id,view_only_Supply_id,view_only_Vaccinates_id,view_only_Vaccine_name

def delete_vaccine():
    result = view_vaccine_data()
    df = pd.DataFrame(result, columns=['Vaccine Name', 'Vaccine Company', 'Vaccine Cost']) 
    with st.expander("Current data"):
        st.dataframe(df)
    list_of_vaccines = [i[0] for i in view_only_Vaccine_name()] 
    selected_vaccine = st.selectbox("Task to Delete", list_of_vaccines) 
    st.warning("Do you want to delete ::{}".format(selected_vaccine)) 
    if st.button("Delete Vaccine"):
        delete_data_Vaccine(selected_vaccine)
        st.success("That Vaccine has been deleted successfully")
    new_result = view_vaccine_data()
    df2 = pd.DataFrame(new_result, columns=['Vaccine Name', 'Vaccine Company', 'Vaccine Cost']) 
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_doctor():
    result = view_doctor_data()
    df = pd.DataFrame(result, columns=['Doctor ID', 'Doctor Department']) 
    with st.expander("Current data"):
        st.dataframe(df)
    list_of_doctors = [i[0] for i in view_only_Doctor_id()] 
    selected_doctor = st.selectbox("Task to Delete", list_of_doctors) 
    st.warning("Do you want to delete ::{}".format(selected_doctor)) 
    if st.button("Delete Doctor"):
        delete_data_doctor(selected_doctor)
        st.success("Doctor ID has been deleted successfully")
    new_result = view_doctor_data()
    df2 = pd.DataFrame(new_result, columns=['Doctor ID', 'Doctor Department']) 
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_Vaccinates():
    result = view_vaccinates_data()
    df = pd.DataFrame(result, columns=['Patient ID','Hospital ID','Date of first Dose','Date of last Dose']) 
    with st.expander("Current data"):
        st.dataframe(df)
    list_of_vaccinates = [i[0] for i in view_only_Vaccinates_id()] 
    selected_vaccinates = st.selectbox("Task to Delete", list_of_vaccinates) 
    st.warning("Do you want to delete ::{}".format(selected_vaccinates)) 
    if st.button("Delete"):
        delete_data_vaccinates(selected_vaccinates)
        st.success(" deleted successfully")
    new_result = view_vaccinates_data()
    df2 = pd.DataFrame(new_result, columns=['Patient ID','Hospital ID','Date of first Dose','Date of last Dose']) 
    with st.expander("Updated data"):
        st.dataframe(df2)


def delete_Person():
    result = view_person_data()
    df = pd.DataFrame(result, columns=['Person ID','Person Name','Person Gender','Person DOB','Contact No','Address','Email ID']) 
    with st.expander("Current data"):
        st.dataframe(df)
    list_of_doctors = [i[0] for i in view_only_person_id()] 
    selected_doctor = st.selectbox("Task to Delete", list_of_doctors) 
    st.warning("Do you want to delete ::{}".format(selected_doctor)) 
    if st.button("Delete"):
        delete_data_person(selected_doctor)
        st.success("deleted successfully")
    new_result = view_person_data()
    df2 = pd.DataFrame(new_result, columns=['Person ID','Person Name','Person Gender','Person DOB','Contact No','Address','Email ID']) 
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_Supplies():
    result = view_supplies_data()
    df = pd.DataFrame(result, columns=['Supply ID', 'Hospital ID','Inventory','Quantity','Time Duration']) 
    with st.expander("Current data"):
        st.dataframe(df)
    list_of_doctors = [i[0] for i in view_only_Supply_id()] 
    selected_doctor = st.selectbox("Task to Delete", list_of_doctors) 
    st.warning("Do you want to delete ::{}".format(selected_doctor)) 
    if st.button("Delete "):
        delete_data_supplies(selected_doctor)
        st.success("Doctor ID has been deleted successfully")
    new_result = view_supplies_data()
    df2 = pd.DataFrame(new_result, columns=['Supply ID', 'Hospital ID','Inventory','Quantity','Time Duration']) 
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_Hospital():
    result = view_hospital_data()
    df = pd.DataFrame(result, columns=['Hospital ID', 'Name','PWD','Contact No','Type','Address','Email','Vaccine','Quantity Remaining']) 
    with st.expander("Current data"):
        st.dataframe(df)
    list_of_doctors = [i[0] for i in view_only_Hospital_id()] 
    selected_doctor = st.selectbox("Task to Delete", list_of_doctors) 
    st.warning("Do you want to delete ::{}".format(selected_doctor)) 
    if st.button("Delete "):
        delete_data_hospital(selected_doctor)
        st.success("Deleted successfully")
    new_result = view_hospital_data()
    df2 = pd.DataFrame(new_result, columns=['Hospital ID', 'Name','PWD','Contact No','Type','Address','Email','Vaccine','Quantity Remaining']) 
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_Location():
    result = view_location_data()
    df = pd.DataFrame(result, columns=['Pincode', 'Area','State','City']) 
    with st.expander("Current data"):
        st.dataframe(df)
    list_of_doctors = [i[0] for i in view_only_Location_pin()] 
    selected_doctor = st.selectbox("Task to Delete", list_of_doctors) 
    st.warning("Do you want to delete ::{}".format(selected_doctor)) 
    if st.button("Delete"):
        delete_data_location(selected_doctor)
        st.success("Deleted successfully")
    new_result = view_location_data()
    df2 = pd.DataFrame(new_result, columns=['Pincode', 'Area','State','City']) 
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_Inventory():
    result = view_inventory_data()
    df = pd.DataFrame(result, columns=['Inventory ID','Name','Contact No','Address']) 
    with st.expander("Current data"):
        st.dataframe(df)
    list_of_doctors = [i[0] for i in view_only_inventory_id()] 
    selected_doctor = st.selectbox("Task to Delete", list_of_doctors) 
    st.warning("Do you want to delete ::{}".format(selected_doctor)) 
    if st.button("Delete"):
        delete_data_inventory(selected_doctor)
        st.success("Deleted successfully")
    new_result = view_inventory_data()
    df2 = pd.DataFrame(new_result, columns=['Inventory ID','Name','Contact No','Address']) 
    with st.expander("Updated data"):
        st.dataframe(df2)