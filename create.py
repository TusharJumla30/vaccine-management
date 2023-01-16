import streamlit as st
from database import add_to_vaccine,add_to_inventory,add_to_hospital,add_to_doctor,add_to_location,add_to_person,add_to_vaccinates,add_to_supplies
import datetime
"""def write_into_vaccine():
    col1, col2 = st.columns(2)
    with col1:
        train_no = st.text_input("Train No:")
        train_name = st.text_input("Train Name:")
        train_type = st.text_input("Train Type:")
    with col2:
        
        source = st.text_input("Source:")
        destination = st.text_input("Destination:")
    availability = st.text_input("Availability:")
    if st.button("Add Train"):
        add_to_vaccine(V_name, V_company, V_cost)
        st.success("Successfully added train: {}".format(train_no))"""

def create_vaccine():
    col1, col2 = st.columns(2)
    with col1:
        #train_no = st.text_input("Train No:")
        V_name = st.text_input(" Name of Vaccine:")
        V_company = st.text_input("Vaccine Company Name:")
    with col2:
        """dealer_city = st.selectbox("City", ["Bangalore", "Chennai", "Mumbai"])"""
        V_cost = st.text_input("Cost:")
        #destination = st.text_input("Destination:")
    #availability = st.text_input("Availability:")
    if st.button("Add Vaccine"):
        add_to_vaccine(V_name, V_company, V_cost)
        st.success("Successfully added Vaccine: {}".format(V_name))

def create_inventory():
    col1, col2 = st.columns(2)
    with col1:
        #train_no = st.text_input("Train No:")
        I_id = st.text_input(" Inventory Id:")
        I_name = st.text_input("Inventory Name:")
    with col2:
        """dealer_city = st.selectbox("City", ["Bangalore", "Chennai", "Mumbai"])"""
        I_contactno = st.text_input("Contact No:")
        I_address = st.text_input("Address:")
        #destination = st.text_input("Destination:")
    #availability = st.text_input("Availability:")
    if st.button("Add to inventory"):
        add_to_inventory(I_id,I_name,I_contactno,I_address)
        st.success("Successfully added Inventory: {}".format(I_id))

def create_location():
    col1, col2 = st.columns(2)
    with col1:
        #train_no = st.text_input("Train No:")
        pincode = st.text_input("Pincode:")
        area = st.text_input("Area:")
    with col2:
        """dealer_city = st.selectbox("City", ["Bangalore", "Chennai", "Mumbai"])"""
        city = st.text_input("City:")
        state = st.text_input("State:")
    #availability = st.text_input("Availability:")
    if st.button("Add location"):
        add_to_location(pincode,area,city,state)
        st.success("Successfully added Location: {}".format(pincode,area))

def create_doctor():
    col1,col2 = st.columns(2)
    with col1:
        #train_no = st.text_input("Train No:")
        D_id = st.text_input("Doctor ID:")
       
    with col2:
        """dealer_city = st.selectbox("City", ["Bangalore", "Chennai", "Mumbai"])"""
        D_dept = st.text_input("Department:")
        #destination = st.text_input("Destination:")
    #availability = st.text_input("Availability:")
    if st.button("Add Doctor Details"):
        add_to_doctor(D_id,D_dept)
        st.success("Successfully added Doctor: {}".format(D_id))

def create_vaccinates():
    col1,col2 = st.columns(2)
    with col1:
        #train_no = st.text_input("Train No:")
        P = st.text_input("Patient ID:")
        Hosp = st.text_input("Hospital ID:")
    with col2:
        """dealer_city = st.selectbox("City", ["Bangalore", "Chennai", "Mumbai"])"""
        
        Date_first = st.date_input("Date of First Dose:")
        Date_last = st.date_input("Date Of Second Dose:")#,datetime.date(2000,1,1)
    if st.button("Add Details"):
        add_to_vaccinates(P,Hosp,Date_first,Date_last)
        st.success("Successfully added Vaccinate: {}".format(P,Hosp))

def create_hospital():
    col1,col2, = st.columns(2)
    with col1:
        #train_no = st.text_input("Train No:")
        H_id = st.text_input("Hospital ID:")
        H_name = st.text_input("Hospital Name:")
        H_pwd = st.text_input("Hospital pwd:")
        H_contactno = st.text_input("Hospital Contact No:")
    with col2:
        """dealer_city = st.selectbox("City", ["Bangalore", "Chennai", "Mumbai"])"""
        H_type = st.selectbox("Select Type of Hospital:",['G','P'])
        H_address = st.text_input("Address:")
        H_email = st.text_input("Email ID:")

    H_vac = st.text_input("Vaccencies:")
    quant_rem = st.text_input("Vaccines Remaining:")
    if st.button("Add Hospital Details"):
        add_to_hospital(H_id,H_name,H_pwd,H_contactno,H_type,H_address,H_email,H_vac,quant_rem)
        st.success("Successfully added Hospital: {}".format(H_id))

def create_person():
    col1,col2 = st.columns(2)
    with col1:
        #train_no = st.text_input("Train No:")
        P_id = st.text_input("Person ID:")
        P_name= st.text_input("Person Name:")
        #P_Gender= st.text_input("Sex:")
        P_Gender= st.selectbox("Sex:",["Male","Female","TransGender"])
        min_date=datetime.date(1950,1,1)
        max_date=datetime.date(2032,1,1)
        P_DOB= st.date_input("Date of Birth:",min_value=min_date,max_value=max_date)
    with col2:
        """dealer_city = st.selectbox("City", ["Bangalore", "Chennai", "Mumbai"])"""
        P_address = st.text_input("Address:")
        P_contactno= st.text_input("Contact No:")
        P_email = st.text_input("Email ID:")
    #availability = st.text_input("Availability:")
    if st.button("Add Person Details"):
        add_to_person(P_id,P_name,P_Gender,P_DOB,P_contactno,P_address,P_email)
        st.success("Successfully added Person: {}".format(P_id))

def create_supplies():
    col1,col2 = st.columns(2)
    with col1:
        #train_no = st.text_input("Train No:")
        S_id = st.text_input("Supply ID:")
        S_hospital= st.text_input("Hospital Id:")

    with col2:
        """dealer_city = st.selectbox("City", ["Bangalore", "Chennai", "Mumbai"])"""
        S_inventory = st.text_input("Inventory:")
        S_quantity = st.text_input("Quantity:")
        S_time= st.time_input("Time Duration:")
    #availability = st.text_input("Availability:")
    if st.button("Add Supply Details"):
        add_to_supplies(S_id,S_hospital,S_inventory,S_quantity,S_time)
        st.success("Successfully added Supplies: {}".format(S_id))
