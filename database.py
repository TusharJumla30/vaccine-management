import mysql.connector 
import streamlit as st
mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="", 
    database="vaccine_management"
)
c = mydb.cursor()

def create_table(): 
    c.execute('CREATE TABLE IF NOT EXISTS Location(pincode numeric(6) PRIMARY KEY, area varchar(30) NOT NULL, city varchar(20) NOT NULL, state varchar(20) NOT NULL);')
    c.execute('CREATE TABLE IF NOT EXISTS Inventory( I_id int PRIMARY KEY AUTO_INCREMENT, I_name varchar(20) NOT NULL, I_contactno numeric(10), I_address numeric(6) NOT NULL, FOREIGN KEY (I_address) REFERENCES Location(pincode) ON DELETE CASCADE ON UPDATE CASCADE);')
    c.execute('CREATE TABLE IF NOT EXISTS Vaccine( V_name varchar(20) PRIMARY KEY, V_company varchar(20) NOT NULL, V_cost float NOT NULL);')
    c.execute("CREATE TABLE IF NOT EXISTS Hospital(    H_id int AUTO_INCREMENT PRIMARY KEY,    H_name varchar(30) NOT NULL,    H_pwd varchar(200),    H_contactno numeric(10),    H_type char(1) NOT NULL CHECK (H_type='G' OR H_type='P'),    H_address numeric(6) NOT NULL,    H_email varchar(30),    H_vac varchar(20),    quant_rem int,    FOREIGN KEY (H_address) REFERENCES Location(pincode) ON DELETE CASCADE ON UPDATE CASCADE,    FOREIGN KEY (H_vac) REFERENCES Vaccine(V_name) ON DELETE CASCADE ON UPDATE CASCADE);")
    c.execute('CREATE TABLE IF NOT EXISTS Supplies( S_id int auto_increment primary key, S_hospital int,    S_inventory int,    S_quantity numeric,    S_time timestamp,    Foreign key (S_hospital) references hospital(h_id) on delete cascade on update cascade,    Foreign key (S_inventory) references inventory(i_id) on delete cascade on update cascade);')
    c.execute('CREATE TABLE IF NOT EXISTS Person(    P_id int PRIMARY KEY AUTO_INCREMENT,    P_name varchar(30) NOT NULL,    P_Gender char(20) NOT NULL,    P_DOB DATE NOT NULL,   P_contactno numeric(10),    P_address numeric(6),    P_email varchar(30),    FOREIGN KEY (P_address) REFERENCES Location(pincode) ON DELETE CASCADE ON UPDATE CASCADE);')
    c.execute('CREATE TABLE IF NOT EXISTS Doctor(    D_id int PRIMARY KEY,    D_dept varchar(20) NOT NULL,    FOREIGN KEY (D_id) REFERENCES Person(P_id) ON DELETE CASCADE ON UPDATE CASCADE);')
    c.execute('CREATE TABLE IF NOT EXISTS Vaccinates(    P int,    Hosp int,    Date_first DATE,    Date_second DATE,    PRIMARY KEY (P, Hosp),    FOREIGN KEY (P) REFERENCES Person(P_id)  ON DELETE CASCADE ON UPDATE CASCADE,    FOREIGN KEY (Hosp) REFERENCES Hospital(H_id)  ON DELETE CASCADE ON UPDATE CASCADE);')

def add_to_location(pincode,area,city,state): 
    c.execute('INSERT INTO location(pincode,area,city,state) VALUES (%s,%s,%s,%s)',(pincode,area,city,state)) 
    mydb.commit()

def add_to_inventory(I_id, I_name, I_contactno, I_address): 
    c.execute('INSERT INTO Inventory(I_id, I_name, I_contactno, I_address) VALUES (%s,%s,%s,%s)',(I_id, I_name, I_contactno, I_address )) 
    mydb.commit()

def add_to_vaccine(V_name, V_company, V_cost): 
    c.execute('INSERT INTO Vaccine(V_name, V_company, V_cost) VALUES (%s,%s,%s)',(V_name, V_company, V_cost)) 
    mydb.commit()

def add_to_hospital(H_id,H_name,H_pwd,H_contactno,H_type,H_address,H_email,H_vac,quant_rem): 
    c.execute('INSERT INTO Hospital(H_id,H_name,H_pwd,H_contactno,H_type,H_address,H_email,H_vac,quant_rem) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(H_id,H_name,H_pwd,H_contactno,H_type,H_address,H_email,H_vac,quant_rem)) 
    mydb.commit()

def add_to_person(P_id,P_name,P_Gender,P_DOB,P_contactno,P_address,P_email): 
    c.execute('INSERT INTO Person(P_id,P_name,P_Gender,P_DOB,P_contactno,P_address,P_email) VALUES (%s,%s,%s,%s,%s,%s,%s)',(P_id,P_name,P_Gender,P_DOB,P_contactno,P_address,P_email)) 
    mydb.commit()

def add_to_doctor(D_id,D_dept): 
    c.execute('INSERT INTO Doctor(D_id,D_dept) VALUES (%s,%s)',(D_id,D_dept)) 
    mydb.commit()

def add_to_vaccinates(P,Hosp,Date_first,Date_last): 
    c.execute('INSERT INTO Vaccinates(P,Hosp,Date_first,Date_second) VALUES (%s,%s,%s,%s)',(P,Hosp,Date_first,Date_last)) 
    mydb.commit()

def add_to_supplies(S_id,S_hospital,S_inventory,S_quantity,S_time): 
    c.execute('INSERT INTO Supplies(S_id,S_hospital,S_inventory,S_quantity,S_time) VALUES (%s,%s,%s,%s,%s)',(S_id,S_hospital,S_inventory,S_quantity,S_time)) 
    mydb.commit()

def view_vaccine_data(): 
    c.execute('SELECT * FROM Vaccine') 
    data = c.fetchall()
    return data

def view_doctor_data(): 
    c.execute('SELECT * FROM Doctor') 
    data = c.fetchall()
    return data

def view_hospital_data(): 
    c.execute('SELECT * FROM Hospital') 
    data = c.fetchall()
    return data

def view_person_data(): 
    c.execute('SELECT * FROM Person') 
    data = c.fetchall()
    return data

def view_inventory_data(): 
    c.execute('SELECT * FROM Inventory') 
    data = c.fetchall()
    return data

def view_vaccinates_data(): 
    c.execute('SELECT * FROM Vaccinates') 
    data = c.fetchall()
    return data

def view_supplies_data(): 
    c.execute('SELECT * FROM Supplies') 
    data = c.fetchall()
    return data

def view_location_data(): 
    c.execute('SELECT * FROM Location') 
    data = c.fetchall()
    return data

def view_only_Vaccine_name(): 
    c.execute('SELECT V_name FROM Vaccine') 
    data = c.fetchall()
    return data

def view_only_Doctor_id(): 
    c.execute('SELECT D_id FROM Doctor') 
    data = c.fetchall()
    return data

def view_only_Vaccinates_id(): 
    c.execute('SELECT P,Hosp FROM Vaccinates') 
    data = c.fetchall()
    return data

def view_only_person_id(): 
    c.execute('SELECT P_id FROM Person') 
    data = c.fetchall()
    return data

def view_only_Supply_id(): 
    c.execute('SELECT S_id FROM Supplies') 
    data = c.fetchall()
    return data

def view_only_Hospital_id(): 
    c.execute('SELECT H_id FROM Hospital') 
    data = c.fetchall()
    return data

def view_only_Location_pin(): 
    c.execute('SELECT pincode FROM Location') 
    data = c.fetchall()
    return data

def view_only_inventory_id(): 
    c.execute('SELECT I_id FROM Inventory') 
    data = c.fetchall()
    return data

def get_train(train_no): 
    c.execute('SELECT * FROM TRAIN WHERE train_no="{}"'.format(train_no)) 
    data = c.fetchall()
    return data

def get_location(pincode): 
    c.execute('SELECT * FROM Location WHERE pincode="{}"'.format(pincode)) 
    data = c.fetchall()
    return data

def get_vaccine(V_name): 
    c.execute('SELECT * FROM Vaccine WHERE V_name="{}"'.format(V_name)) 
    data = c.fetchall()
    return data

def get_inventory(I_id): 
    c.execute('SELECT * FROM Inventory WHERE I_id="{}"'.format(I_id)) 
    data = c.fetchall()
    return data

def get_vaccinates(P): 
    c.execute('SELECT * FROM Vaccinates WHERE P="{}"'.format(P)) 
    data = c.fetchall()
    return data

def get_hospital(H_id): 
    c.execute('SELECT * FROM Hospital WHERE H_id="{}"'.format(H_id)) 
    data = c.fetchall()
    return data

def get_doctor(D_id): 
    c.execute('SELECT * FROM Doctor WHERE D_id="{}"'.format(D_id)) 
    data = c.fetchall()
    return data

def get_person(P_id): 
    c.execute('SELECT * FROM Person WHERE P_id="{}"'.format(P_id)) 
    data = c.fetchall()
    return data

def get_supplies(S_id): 
    c.execute('SELECT * FROM Supplies WHERE S_id="{}"'.format(S_id)) 
    data = c.fetchall()
    return data

def edit_train_data(new_train_no, new_train_name, new_train_type, new_source, new_destination,new_availability, Train_No, Train_name, train_type,source, destination, availability): 
    c.execute("UPDATE TRAIN SET train_no=%s, train_name=%s, train_type=%s, source=%s, destination=%s, availability=%s WHERE train_no=%s and train_name=%s and train_type=%s and source=%s and destination=%s and availability=%s", (new_train_no, new_train_name, new_train_type, new_source, new_destination,new_availability, Train_No, Train_name, train_type,source, destination, availability))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_location_data(new_pincode, new_area, new_state, new_city, Pincode, Area, State, City): 
    c.execute("UPDATE Location SET pincode=%s, area=%s, state=%s, city=%s WHERE pincode=%s and area=%s and state=%s and city=%s", (new_pincode, new_area, new_state, new_city, Pincode, Area, State, City))
    mydb.commit()
    # data = c.fetchall()
    # return data

def edit_vaccine_data(new_V_name, new_V_company, new_V_cost, V_name, V_company, V_cost): 
    c.execute("UPDATE Vaccine SET V_name=%s, V_company=%s, V_cost=%s WHERE V_name=%s and V_company=%s and V_cost=%s", (new_V_name, new_V_company, new_V_cost, V_name, V_company, V_cost))
    mydb.commit()
    # data = c.fetchall()
    # return data

def edit_vaccinates_data(new_P,new_Hosp,new_Date_first,new_Date_last,P,Hosp,Date_first,Date_last): 
    c.execute("UPDATE Vaccinates SET P=%s, Hosp=%s, Date_first=%s, Date_last=%s WHERE P=%s and Hosp=%s and Date_first=%s and Date_last=%s", (new_P,new_Hosp,new_Date_first,new_Date_last,P,Hosp,Date_first,Date_last))
    mydb.commit()
    # data = c.fetchall()
    # return data

def edit_person_data(new_P_id,new_P_name,new_P_Gender,new_P_DOB,new_P_contactno,new_P_address,new_P_email,P_id,P_name,P_Gender,P_DOB,P_contactno,P_address,P_email): 
    c.execute("UPDATE Person SET P_id=%s, P_name=%s, P_Gender=%s, P_DOB=%s, P_contactno=%s, P_address=%s, P_email=%s WHERE P_id=%s and P_name=%s and P_Gender=%s and P_DOB=%s and P_contactno=%s and P_address=%s and P_email=%s", (new_P_id,new_P_name,new_P_Gender,new_P_DOB,new_P_contactno,new_P_address,new_P_email,P_id,P_name,P_Gender,P_DOB,P_contactno,P_address,P_email))
    mydb.commit()
    # data = c.fetchall()
    # return data

def edit_doctor_data(new_D_id, new_D_dept, D_id, D_dept): 
    c.execute("UPDATE Doctor SET D_id=%s, D_dept=%s WHERE D_id=%s and D_dept=%s", (new_D_id, new_D_dept, D_id, D_dept))
    mydb.commit()
    # data = c.fetchall()
    # return data

def edit_supplies_data(new_S_id,new_S_hospital,new_S_inventory,new_S_quantity,new_S_time, S_id,S_hospital,S_inventory,S_quantity,S_time): 
    c.execute("UPDATE Supplies SET S_id=%s, S_hospital=%s, S_inventory=%s, S_quantity=%s, S_time=%s WHERE S_id=%s and S_hospital=%s and S_inventory=%s and S_quantity=%s and S_time=%s", (new_S_id,new_S_hospital,new_S_inventory,new_S_quantity,new_S_time, S_id,S_hospital,S_inventory,S_quantity,S_time))
    mydb.commit()
    # data = c.fetchall()
    # return data

def edit_hospital_data(new_H_id,new_H_name,new_H_pwd,new_H_contactno,new_H_type,new_H_address,new_H_email,new_H_vac,new_quant_rem,H_id,H_name,H_pwd,H_contactno,H_type,H_address,H_email,H_vac,quant_rem): 
    c.execute("UPDATE Hospital SET H_id=%s, H_name=%s, H_pwd=%s, H_contactno=%s, H_type=%s, H_address=%s,H_email=%s,H_vac=%s,quant_rem=%s WHERE H_id=%s and H_name=%s and H_pwd=%s and H_contactno=%s and H_type=%s and H_address=%s and H_email=%s and H_vac=%s and quant_rem=%s", (new_H_id,new_H_name,new_H_pwd,new_H_contactno,new_H_type,new_H_address,new_H_email,new_H_vac,new_quant_rem,H_id,H_name,H_pwd,H_contactno,H_type,H_address,H_email,H_vac,quant_rem))
    mydb.commit()
    # data = c.fetchall()
    # return data

def edit_inventory_data(new_I_id, new_I_name, new_I_contactno, new_I_address,I_id, I_name, I_contactno, I_address): 
    c.execute("UPDATE Inventory SET I_id=%s, I_name=%s, I_contactno=%s, I_address=%s WHERE I_id=%s and I_name=%s and I_contactno=%s and I_address=%s", (new_I_id, new_I_name, new_I_contactno, new_I_address,I_id, I_name, I_contactno, I_address))
    mydb.commit()
    # data = c.fetchall()
    # return data

def delete_data_Vaccine(V_name): 
    c.execute('DELETE FROM Vaccine WHERE V_name="{}"'.format(V_name)) 
    mydb.commit()

def delete_data_doctor(D_id): 
    c.execute('DELETE FROM Doctor WHERE D_id="{}"'.format(D_id)) 
    mydb.commit()

def delete_data_inventory(I_id): 
    c.execute('DELETE FROM Inventory WHERE I_id="{}"'.format(I_id)) 
    mydb.commit()

def delete_data_vaccinates(P,Hosp): 
    c.execute('DELETE FROM Vaccinates WHERE P="{}" and Hosp="{}"'.format(P,Hosp)) 
    mydb.commit()

def delete_data_person(P_id): 
    c.execute('DELETE FROM Person WHERE P_id="{}"'.format(P_id)) 
    mydb.commit()

def delete_data_supplies(S_id): 
    c.execute('DELETE FROM Supplies WHERE S_id="{}"'.format(S_id)) 
    mydb.commit()

def delete_data_hospital(H_id): 
    c.execute('DELETE FROM Hospital WHERE H_id="{}"'.format(H_id)) 
    mydb.commit()

def delete_data_location(pincode): 
    c.execute('DELETE FROM Location WHERE pincode="{}"'.format(pincode)) 
    mydb.commit()

def delete_data(train_no): 
    c.execute('DELETE FROM TRAIN WHERE train_no="{}"'.format(train_no)) 
    mydb.commit()

def query(command):
    c.execute(command)
    data = c.fetchall()
    mydb.commit()
    return data

def No_query(command):
    c.execute(command)
    mydb.commit()

def show_patient_id():
    c.execute('SELECT P from Vaccinates,hospital where Hosp=H_id and H_name="manipal" Union Select P from Vaccinates,hospital where Hosp=H_id and H_name="Victoria";')
    data=c.fetchall()
    mydb.commit()
    return data

def show_all_contacts_of_patients():
    c.execute('SELECT P_id,P_contactno from PERSON except(SELECT D_id,P_contactno FROM PERSON Natural JOIN DOCTOR WHERE D_id = P_id);')
    data=c.fetchall()
    mydb.commit()
    return data

def show_vaccine_inuse():
    c.execute('SELECT v_name from Vaccine INTERSECT SELECT h_vac from Hospital;')
    data=c.fetchall()
    mydb.commit()
    return data

def show_doctor_details():
    c.execute('SELECT D_id,P_name,D_dept,P_gender,P_contactno,p_address,P_email FROM PERSON Natural JOIN DOCTOR WHERE D_id = P_id;')
    data=c.fetchall()
    mydb.commit()
    return data

def show_suplies_hosp_details():
    c.execute('SELECT * FROM SUPPLIES LEFT OUTER JOIN HOSPITAL ON S_hospital = H_id;')
    data=c.fetchall()
    mydb.commit()
    return data

def d_details():
    if st.button('Execute'):
        x=show_doctor_details()
        st.success("Executed successfully") 
        if(x):
            st.dataframe(x)

def s_h_details():
    if st.button('Execute'):
        x=show_suplies_hosp_details()
        st.success("Executed successfully") 
        #if(x):
        st.dataframe(x)

