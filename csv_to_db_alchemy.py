from sqlalchemy import create_engine
import pandas as pd
import os
import json


ABSOLUTE_PATH = os.path.abspath(os.path.dirname(__file__))
# csv_path= ABSOLUTE_PATH + '\\' + 'csv\\mysql.csv'
csv_path=os.path.join(ABSOLUTE_PATH,"csv", "mysql.csv")
df_mysql = pd.read_csv(csv_path, sep='\t')
# print(df_mysql)
# config_json=ABSOLUTE_PATH + '\\' + 'config.json'
config_json=os.path.join(ABSOLUTE_PATH, "config.json")

with open(config_json) as config_file:
    data = json.load(config_file)

con_string= data['postgres_conn_string']
engine = create_engine(con_string)
# connection = engine.connect()

df_mysql.to_sql('advertisement', con=engine, index=False, if_exists='append')