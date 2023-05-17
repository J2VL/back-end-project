#system import
from enum import Enum 
from datetime import date
import sqlite3

#libs import
from fastapi import FastAPI
from pydantic import BaseModel


#local import
from database.initdatabase import execute_sql_queries

app = FastAPI()



@app.on_event("startup")
async def startup():
    app.db_connection = sqlite3.connect("mydatabase.db")
    cursor = app.db_connection.cursor()
    execute_sql_queries(cursor)
    app.db_connection.commit()
    # Si vous voulez utiliser des rows factory :
    # app.db_connection.row_factory = sqlite3.Row

@app.on_event("shutdown")
async def shutdown():
    app.db_connection.close()

@app.get("/")
async def root():
    cursor = app.db_connection.cursor()
    cursor.execute("SELECT * FROM Users")
    rows = cursor.fetchall()
    return {"data": rows}