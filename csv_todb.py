import psycopg2
import json
import os  
import numpy as np 
import pandas as pd 


ABSOLUTE_PATH = os.path.abspath(os.path.dirname(__file__))
csv_path= ABSOLUTE_PATH + '\\' + 'csv\\mysql.csv'

df = pd.read_csv(csv_path, sep='\t')



#clean header names, lower case letters, remove all wite spaces, replace -,/,\\,$

# replacements = {
#     'object': 'varchar',
#     'float64': 'float',
#     'int64': 'int',
#     'datatime64': 'timestamp',
#     'timedelta64[ns]': 'varchar'
# }

# col_str = ", ".join("{} {}".format(n,d) for (n,d) in zip(df.columns, df.dtypes.replace(replacements)))

# df.to_csv('mysql.csv' , header=df.columns, index=False, encoding = 'utf-8')

config_json=ABSOLUTE_PATH + '\\' + 'config.json'

with open(config_json) as config_file:
    data = json.load(config_file)
hostname = data['hostname']
username = data['username']
port_id = data['port_id']
pwd = data['pwd']
database = data['database']

conn=None 
cur=None
try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
        )

    cur = conn.cursor()

    create_script=""" CREATE TABLE IF NOT EXISTS mysql (
        id	bigint PRIMARY KEY,
        logtype	bigint,
        wp_type	bigint,
        campaign_id	bigint,
        banner_id bigint,	
        werbeplatz_id bigint,	
        peer_ip	bigint,
        userid bigint,
        timestamp bigint,
        proxy_ip bigint,
        time timestamp,
        network	bigint,
        browser	bigint,
        os	bigint,
        screen_res	bigint,
        country	bigint,
        state	bigint,
        delivered_as bigint,	
        city	bigint,
        connection bigint,
        fvers	bigint,
        gk	bigint,
        mdev bigint,	
        subreq	bigint,
        server_id	bigint,
        svz_id	varchar(20) NOT NULL,
        fraud_action 	bigint,
        fraud_detection_results	bigint,
        used_batch_media bigint
        )
     """
    copy_statment="""
    COPY mysql FROM STDIN WITH
        CSV
        HEADER
        DELIMITER AS ','
    """
 
    cur.execute(create_script)
    
    my_file=open(csv_path)
    
    cur.copy_expert(sql=copy_statment, file=my_file)
    cur.execute('grant select on table mysql to public')
    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()