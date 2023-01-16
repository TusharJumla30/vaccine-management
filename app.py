import streamlit as st
from create import create_vaccine,create_doctor,create_inventory,create_location,create_hospital,create_person,create_supplies,create_vaccinates
from database import create_table,show_patient_id,show_all_contacts_of_patients,show_vaccine_inuse,show_doctor_details,show_suplies_hosp_details,d_details,s_h_details
from delete import delete_doctor,delete_Hospital,delete_Inventory,delete_Location,delete_Person,delete_Supplies,delete_Vaccinates,delete_vaccine
from read import read_hospital,read_inventory,read_person,read_vaccine,read_doctor,read_location,read_supplies,read_vaccinates
from update import update_Doctor,update_Hospital,update_Inventory,update_location,update_Person,update_Supplies,update_Vaccinates,update_Vaccine
from query import Customize_query,Customize_query_N

def main():
 st.title("Vaccine Management")
 st.subheader("By:- Tushar J ")
 menu = ["Add","Edit","Remove","View","Custom query","Custom Operations","requirment"]
 choice = st.sidebar.selectbox("Menu", menu)
 create_table() 
 if choice == "Add":
    add=["Vaccine","Inventory","Hospital","Person","Location","Doctor","Vaccinates","Supplies"]
    l1 = st.sidebar.selectbox("ADD",add)
    #st.subheader("Enter  Details:")
    #create()
    if l1 == "Vaccine":
      st.subheader("Enter Details of Vaccine:")
      create_vaccine()
    elif l1 =="Inventory":
      st.subheader("Enter Details of Inventory:")
      create_inventory()
    elif l1=="Location":
      st.subheader("Enter Details of Location:")
      create_location()
    elif l1=="Doctor":
      st.subheader("Enter Details of Doctor:")
      create_doctor()
    elif l1=="Person":
      st.subheader("Enter Details of Person:")
      create_person()
    elif l1=="Supplies":
      st.subheader("Enter Details of Supplies:")
      create_supplies()
    elif l1=="Vaccinates":
      st.subheader("Enter Details of Vaccinates:")
      create_vaccinates()
    elif l1=="Hospital":
      st.subheader("Enter Details of Location:")
      create_hospital()
    else:
      st.subheader("About tasks")
 elif choice == "View":
    #st.subheader("View created tasks")
    #read()
    view=["Vaccine","Inventory","Hospital","Person","Location","Doctor","Vaccinates","Supplies"]
    l1 = st.sidebar.selectbox("View",view)
    #st.subheader("Enter  Details:")
    #create() 
    if l1 == "Vaccine":
      st.subheader("Enter Details of Vaccine:")
      read_vaccine()
    elif l1 =="Inventory":
      st.subheader("Enter Details of Inventory:")
      read_inventory()
    elif l1=="Hospital":
      st.subheader("Enter Details of Location:")
      read_hospital()
    elif l1=="Person":
      st.subheader("Enter Details of Doctor:")
      read_person()
    elif l1=="Supplies":
      st.subheader("Enter Details of Supplies:")
      read_supplies()
    elif l1=="Doctor":
      st.subheader("Enter Details of Doctor:")
      read_doctor()
    elif l1=="Vaccinates":
      st.subheader("Enter Details of Vaccinates:")
      read_vaccinates()
    elif l1=="Location":
      st.subheader("Enter Details of Location:")
      read_location()
    else:
      st.subheader("About tasks")

 elif choice == "Edit":
    #st.subheader("Update created tasks")
    #update()
    view=["Vaccine","Inventory","Hospital","Person","Location","Doctor","Vaccinates","Supplies"]
    l1 = st.sidebar.selectbox("Update",view)
    #st.subheader("Enter  Details:")
    #create()
    if l1 == "Vaccine":
      st.subheader("Enter Details of Vaccine:")
      update_Vaccine()
    elif l1 =="Inventory":
      st.subheader("Enter Details of Inventory:")
      update_Inventory()
    elif l1=="Hospital":
      st.subheader("Enter Details of Location:")
      update_Hospital()
    elif l1=="Person":
      st.subheader("Enter Details of Doctor:")
      update_Person()
    elif l1=="Supplies":
      st.subheader("Enter Details of Supplies:")
      update_Supplies()
    elif l1=="Doctor":
      st.subheader("Enter Details of Doctor:")
      update_Doctor()
    elif l1=="Vaccinates":
      st.subheader("Enter Details of Vaccinates:")
      update_Vaccinates()
    elif l1=="Location":
      st.subheader("Enter Details of Location:")
      update_location()
    else:
      st.subheader("About tasks")

 elif choice == "Remove":
    #st.subheader("Delete created tasks")
    #delete()
    view=["Vaccine","Inventory","Hospital","Person","Location","Doctor","Vaccinates","Supplies"]
    l1 = st.sidebar.selectbox("Delete",view)
    #st.subheader("Enter  Details:")
    #create()
    if l1 == "Vaccine":
      st.subheader("Enter Details of Vaccine:")
      delete_vaccine()
    elif l1 =="Inventory":
      st.subheader("Enter Details of Inventory:")
      delete_Inventory()
    elif l1=="Hospital":
      st.subheader("Enter Details of Location:")
      delete_Hospital()
    elif l1=="Person":
      st.subheader("Enter Details of Person:")
      delete_Person()
    elif l1=="Supplies":
      st.subheader("Enter Details of Supplies:")
      delete_Supplies()
    elif l1=="Doctor":
      st.subheader("Enter Details of Doctor:")
      delete_doctor()
    elif l1=="Vaccinates":
      st.subheader("Enter Details of Vaccinates:")
      delete_Vaccinates()
    elif l1=="Location":
      st.subheader("Enter Details of Location:")
      delete_Location()
    else:
      st.subheader("About tasks")
 elif choice=="Custom query":
     st.subheader("Customize your Queries:")
     req = st.selectbox("Kind of query:",["Output oriented","Non-Output oriented"])
     if req =="Output oriented":
      Customize_query()
     else:
      Customize_query_N()
 elif choice=="Custom Operations":
     st.subheader("Other Operations")
     set_option = st.selectbox("Set Operations:",["GET Patients ID","GET All contact details","GET ALL Vaccine in use"])
     #join_option = st.selectbox("Some Join Operation details:",["",""])
     if set_option == "GET Patients ID":
      if st.button('Execute'):
        x=show_patient_id()
        st.success("Executed successfully") 
        if(x):
            st.dataframe(x) 
     elif set_option == "GET All contact details":
      if st.button('Execute'):
        x=show_all_contacts_of_patients()
        st.success("Executed successfully") 
        if(x):
            st.dataframe(x) 
     elif set_option == "GET ALL Vaccine in use":
      if st.button('Execute'):
        x=show_vaccine_inuse()
        st.success("Executed successfully") 
        if(x):
            st.dataframe(x) 
    #  join_option = st.selectbox("Some Join Operation details:",["Doctor details","Supply details"])
    #  if join_option == "Doctor details":
    #   d_details()
    #  elif join_option == "Supply details":
    #   s_h_details()
 elif choice =="requirment":
      st.subheader("Other Reports")
      join_option = st.selectbox("Some Join Operation details:",["Doctor details","Supply details"])
      if join_option == "Doctor details":
       d_details()
      elif join_option == "Supply details":
       s_h_details()

 else:
    st.subheader("About tasks")
if __name__ == '__main__':
 main()