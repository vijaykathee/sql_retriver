import os
import sqlite3
import pandas as pd
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
filename =r"C:\python\sales.csv"
#
conn = sqlite3.connect('global_sales.db')
df = pd.read_csv(filename)
df.to_sql('sales_data', conn, if_exists='replace', index=False)
from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///C:/python/text2sql/global_sales.db")
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
chain = create_sql_query_chain(llm=llm,db=db)

response = chain.invoke({"question": "what are the city wise sales"})

cur = conn.cursor()
cur.execute(response)
query_res = cur.fetchall()
print(query_res)
