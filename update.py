import pandas as pd
import streamlit as st
from database import get_location,get_vaccine,get_inventory,get_vaccinates,get_hospital,get_doctor,get_person,get_supplies
from database import view_doctor_data,view_hospital_data,view_inventory_data,view_location_data,view_person_data,view_supplies_data,view_vaccinates_data,view_vaccine_data
from database import view_only_Vaccine_name,view_only_Doctor_id,view_only_Hospital_id,view_only_inventory_id,view_only_Location_pin,view_only_person_id,view_only_Supply_id,view_only_Vaccinates_id
from database import edit_doctor_data,edit_hospital_data,edit_inventory_data,edit_location_data,edit_person_data,edit_supplies_data,edit_vaccinates_data,edit_vaccine_data
def update_location():
    result = view_location_data()
    df = pd.DataFrame(result, columns=['Pincode', 'Area', 'State', 'City'])
    with st.expander("Current Locations"):
        st.dataframe(df)
    list_of_trains = [i[0] for i in view_only_Location_pin()]
    selected_train = st.selectbox("Locations to Edit", list_of_trains)
    selected_result = get_location(selected_train)
    if selected_result:
        pincode = selected_result[0][0]
        area = selected_result[0][1]
        state = selected_result[0][2]
        city = selected_result[0][3]
        #destination = selected_result[0][4]
        #availability= selected_result[0][5]
        col1, col2 = st.columns(2)
        with col1:
            new_pincode = st.text_input("Pincode:", pincode)
            new_area = st.text_input("Area:", area)
        with col2:
            """new_dealer_city = st.selectbox(dealer_city, ["Bangalore", "Chennai", "Mumbai"])"""
            new_state = st.text_input("State:", state)
            new_city = st.text_input("City:", city)
        #with col3:
            #new_destination = st.text_input("Destination:", destination)
            #new_availability = st.text_input("Availability:", availability)
        if st.button("Update Location Data"):
            edit_location_data(new_pincode, new_area, new_state, new_city,pincode,area,state,city)
            st.success("Successfully updated:: {} to ::{}".format(pincode, new_pincode))
    result2 = view_location_data()
    df2 = pd.DataFrame(result2, columns=['Pincode', 'Area', 'State', 'City'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_Vaccine():
    result = view_vaccine_data()
    df = pd.DataFrame(result, columns=['V_name', 'V_company', 'V_cost'])
    with st.expander("Present Vaccine Details"):
        st.dataframe(df)
    list_of_trains = [i[0] for i in view_only_Vaccine_name()]
    selected_train = st.selectbox("Vaccines to Edit", list_of_trains)
    selected_result = get_vaccine(selected_train)
    if selected_result:
        V_name = selected_result[0][0]
        V_company = selected_result[0][1]
        V_cost = selected_result[0][2]
        #city = selected_result[0][3]
        #destination = selected_result[0][4]
        #availability= selected_result[0][5]
        col1, col2 = st.columns(2)
        with col1:
            new_V_name = st.text_input("Vaccine Name:", V_name)
            new_V_company = st.text_input("Company Name:", V_company)
        with col2:
            """new_dealer_city = st.selectbox(dealer_city, ["Bangalore", "Chennai", "Mumbai"])"""
            new_V_cost = st.text_input("Cost:", V_cost)
            #new_city = st.text_input("Source:", city)
        #with col3:
            #new_destination = st.text_input("Destination:", destination)
            #new_availability = st.text_input("Availability:", availability)
        if st.button("Update Vaccine Data"):
            edit_vaccine_data(new_V_name, new_V_company, new_V_cost, V_name,V_company,V_cost)
            st.success("Successfully updated:: {} to ::{}".format(V_name, new_V_name))
    result2 = view_vaccine_data()
    df2 = pd.DataFrame(result2, columns=['V_name', 'V_company', 'V_cost'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_Inventory():
    result = view_inventory_data()
    df = pd.DataFrame(result, columns=['I_id','I_name','I_contact','I_address'])
    with st.expander("Current Inventory"):
        st.dataframe(df)
    list_of_trains = [i[0] for i in view_only_inventory_id()]
    selected_train = st.selectbox("Inventory's to Edit", list_of_trains)
    selected_result = get_inventory(selected_train)
    if selected_result:
        I_id = selected_result[0][0]
        I_name = selected_result[0][1]
        I_contactno = selected_result[0][2]
        I_address = selected_result[0][3]
        #destination = selected_result[0][4]
        #availability= selected_result[0][5]
        col1, col2 = st.columns(2)
        with col1:
            new_I_id = st.text_input("Vaccine Name:", I_id)
            new_I_name = st.text_input("Company Name:", I_name)
        with col2:
            """new_dealer_city = st.selectbox(dealer_city, ["Bangalore", "Chennai", "Mumbai"])"""
            new_I_contactno = st.text_input("Contact:", I_contactno)
            new_I_address = st.text_input("address:", I_address)
        #with col3:
            #new_destination = st.text_input("Destination:", destination)
            #new_availability = st.text_input("Availability:", availability)
        if st.button("Update Vaccine Data"):
            edit_inventory_data(new_I_id, new_I_name, new_I_contactno, new_I_address,I_id, I_name, I_contactno, I_address)
            st.success("Successfully updated:: {} to ::{}".format(I_id,new_I_id))
    result2 = view_inventory_data()
    df2 = pd.DataFrame(result2, columns=['I_id','I_name','I_contact','I_address'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_Vaccinates():
    result = view_vaccinates_data()
    df = pd.DataFrame(result, columns=['P','Hosp','Date_first','Date_last'])
    with st.expander("Current Inventory"):
        st.dataframe(df)
    list_of_trains = [i[0] for i in view_only_Vaccinates_id()]
    selected_train = st.selectbox("Vaccinates to Edit", list_of_trains)
    selected_result = get_vaccinates(selected_train)
    if selected_result:
        P = selected_result[0][0]
        Hosp = selected_result[0][1]
        Date_first = selected_result[0][2]
        Date_last = selected_result[0][3]
        #destination = selected_result[0][4]
        #availability= selected_result[0][5]
        col1, col2 = st.columns(2)
        with col1:
            new_P = st.text_input("Patient Id:", P)
            new_Hosp = st.text_input("Hospital Id:", Hosp)
        with col2:
            """new_dealer_city = st.selectbox(dealer_city, ["Bangalore", "Chennai", "Mumbai"])"""
            new_Date_first = st.date_input("Date of first Dose:", Date_first)
            new_Date_last = st.date_input("Date of last Dose:", Date_last)
        #with col3:
            #new_destination = st.text_input("Destination:", destination)
            #new_availability = st.text_input("Availability:", availability)
        if st.button("Update Vaccine Data"):
            edit_vaccinates_data(new_P, new_Hosp, new_Date_first, new_Date_last,P,Hosp,Date_first,Date_last)
            st.success("Successfully updated:: {} to ::{}".format(P,new_P))
    result2 = view_vaccinates_data()
    df2 = pd.DataFrame(result2, columns=['P','Hosp','Date_first','Date_last'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_Hospital():
    result = view_hospital_data()
    df = pd.DataFrame(result, columns=['H_id','H_name','H_pwd','H_contactno','H_type','H_address','H_email','H_vac','quant_rem'])
    with st.expander("Current Hospital"):
        st.dataframe(df)
    list_of_trains = [i[0] for i in view_only_Hospital_id()]
    selected_train = st.selectbox("Hospitals to Edit", list_of_trains)
    selected_result = get_hospital(selected_train)
    if selected_result:
        H_id = selected_result[0][0]
        H_name = selected_result[0][1]
        H_pwd = selected_result[0][2]
        H_contactno = selected_result[0][3]
        H_type = selected_result[0][4]
        H_address= selected_result[0][5]
        H_email= selected_result[0][6]
        H_vac=selected_result[0][7]
        quant_rem=selected_result[0][8]
        col1, col2,col3 = st.columns(3)
        with col1:
            new_H_id = st.text_input("Hospital ID:", H_id)
            new_H_name = st.text_input("Hospital Name:", H_name)
            new_H_pwd = st.text_input("PWD:", H_pwd)
        with col2:
            """new_dealer_city = st.selectbox(dealer_city, ["Bangalore", "Chennai", "Mumbai"])"""
            new_H_contactno = st.text_input("Contact:", H_contactno)
            new_H_type = st.text_input("Type:", H_type)
            new_H_address =st.text_input("Address:",H_address)
        with col3:
            new_H_email = st.text_input("Email:", H_email)
            new_H_vac = st.text_input("Vaccencies:", H_vac)
            new_quant_rem = st.text_input("Vaccine Quantity Remaining:",quant_rem)
        if st.button("Update"):
            edit_hospital_data(new_H_id, new_H_name,new_H_pwd, new_H_contactno,new_H_type ,new_H_address,new_H_email,new_H_vac,new_quant_rem,H_id, H_name,H_pwd, H_contactno,H_type ,H_address,H_email,H_vac,quant_rem)
            st.success("Successfully updated:: {} to ::{}".format(H_id,new_H_id))
    result2 = view_hospital_data()
    df2 = pd.DataFrame(result2, columns=['H_id','H_name','H_pwd','H_contactno','H_type','H_address','H_email','H_vac','quant_rem'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_Doctor():
    result = view_doctor_data()
    df = pd.DataFrame(result, columns=['D_id','D_dept'])
    with st.expander("Current List"):
        st.dataframe(df)
    list_of_trains = [i[0] for i in view_only_Doctor_id()]
    selected_train = st.selectbox("Doctors to Edit", list_of_trains)
    selected_result = get_doctor(selected_train)
    if selected_result:
        D_id = selected_result[0][0]
        D_dept = selected_result[0][1]
        #I_contactno = selected_result[0][2]
        #I_address = selected_result[0][3]
        #destination = selected_result[0][4]
        #availability= selected_result[0][5]
        # col1 = st.columns(1)
        # with col1:
        new_D_id = st.text_input("Doctor ID:", D_id)
        new_D_dept = st.text_input("Doctor dept:", D_dept)
        #with col2:
            #"""new_dealer_city = st.selectbox(dealer_city, ["Bangalore", "Chennai", "Mumbai"])"""
            #new_I_contactno = st.text_input("Cost:", I_contactno)
            #new_I_address = st.text_input("Source:", I_address)
        #with col3:
            #new_destination = st.text_input("Destination:", destination)
            #new_availability = st.text_input("Availability:", availability)
        if st.button("Update"):
            edit_doctor_data(new_D_id, new_D_dept,D_id, D_dept)
            st.success("Successfully updated:: {} to ::{}".format(D_id,new_D_id))
    result2 = view_doctor_data()
    df2 = pd.DataFrame(result2, columns=['D_id','D_dept'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_Person():
    result = view_person_data()
    df = pd.DataFrame(result, columns=['P_id','P_name','P_Gender','P_DOB','P_contactno','P_address','P_email'])
    with st.expander("Current Person"):
        st.dataframe(df)
    list_of_trains = [i[0] for i in view_only_person_id()]
    selected_train = st.selectbox("Persons to Edit", list_of_trains)
    selected_result = get_person(selected_train)
    if selected_result:
        P_id = selected_result[0][0]
        P_name = selected_result[0][1]
        P_Gender = selected_result[0][2]
        P_DOB = selected_result[0][3]
        P_contactno = selected_result[0][4]
        P_address= selected_result[0][5]
        P_email=selected_result[0][6]
        col1, col2 = st.columns(2)
        with col1:
            new_P_id = st.text_input("Vaccine Name:", P_id)
            new_P_name = st.text_input("Company Name:", P_name)
            new_P_Gender=st.text_input("Gender:",P_Gender)
            new_P_DOB= st.date_input("Date of Birth:",P_DOB)
        with col2:
            """new_dealer_city = st.selectbox(dealer_city, ["Bangalore", "Chennai", "Mumbai"])"""
            new_P_contactno = st.text_input("Cost:", P_contactno)
            new_P_address = st.text_input("Source:", P_address)
            new_P_email=st.text_input("Email:",P_email)
        #with col3:
            #new_destination = st.text_input("Destination:", destination)
            #new_availability = st.text_input("Availability:", availability)
        if st.button("Update Vaccine Data"):
            edit_person_data(new_P_id, new_P_name,new_P_Gender,new_P_DOB,new_P_contactno, new_P_address,new_P_email,P_id,P_name,P_Gender,P_DOB,P_contactno,P_address,P_email,)
            st.success("Successfully updated:: {} to ::{}".format(P_id,new_P_id))
    result2 = view_person_data()
    df2 = pd.DataFrame(result2, columns=['P_id','P_name','P_Gender','P_DOB','P_contactno','P_address','P_email'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_Supplies():
    result = view_supplies_data()
    df = pd.DataFrame(result, columns=['S_id','S_hospital','S_inventory','S_quantity','S_time'])
    with st.expander("Current List"):
        st.dataframe(df)
    list_of_trains = [i[0] for i in view_only_Supply_id()]
    selected_train = st.selectbox("Suppliess to Edit", list_of_trains)
    selected_result = get_supplies(selected_train)
    if selected_result:
        S_id = selected_result[0][0]
        S_hospital = selected_result[0][1]
        S_inventory = selected_result[0][2]
        S_quantity = selected_result[0][3]
        S_time = selected_result[0][4]
        #availability= selected_result[0][5]
        col1, col2 = st.columns(2)
        with col1:
            new_S_id = st.text_input("Supply ID:", S_id)
            new_S_hospital = st.text_input("Hospital ID:", S_hospital)
            new_S_inventory= st.text_input("inventory",S_inventory)
        with col2:
            """new_dealer_city = st.selectbox(dealer_city, ["Bangalore", "Chennai", "Mumbai"])"""
            new_S_quantity = st.text_input("Quantity:", S_quantity)
            new_S_time = st.time_input("Time duration:", S_time)
        #with col3:
            #new_destination = st.text_input("Destination:", destination)
            #new_availability = st.text_input("Availability:", availability)
        if st.button("Update Vaccine Data"):
            edit_supplies_data(new_S_id,new_S_hospital,new_S_inventory,new_S_quantity,new_S_time, S_id,S_hospital,S_inventory,S_quantity,S_time)
            st.success("Successfully updated:: {} to ::{}".format(S_id,new_S_id))
    result2 = view_supplies_data()
    df2 = pd.DataFrame(result2, columns=['S_id','S_hospital','S_inventory','S_quantity','S_time'])
    with st.expander("Updated data"):
        st.dataframe(df2)
