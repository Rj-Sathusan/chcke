import streamlit as st
# import required modules
import mysql.connector
ok=st.secrets["db_username"]
# create connection object

# create connection object
mydb  = mysql.connector.connect(
  host="sql6.freemysqlhosting.net", user=ok,
  password="Q3Bq46Z4Vd", database="sql6474318")
  

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Try")

Result = mycursor.fetchall()
