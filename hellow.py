# import module
import streamlit as st
import mysql.connector
st.title("Hello GeeksForGeeks !!!")


mydb  = mysql.connector.connect(
  host="sql6.freemysqlhosting.net", user="sql6474318",
  password="Q3Bq46Z4Vd", database="sql6474318")
  

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Try")

Result = mycursor.fetchall()
st.write(Result)
