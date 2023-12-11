import pandas as pd
import psycopg2
from sqlalchemy import Column, MetaData, String, Table, create_engine
from urllib.parse import quote_plus

# connection details
db_user = 'postgres'
db_password = 'admin'
db_host = 'localhost'
db_port = '5432'
db_name = 'AOI'

# format password
password = quote_plus(db_password)

# paths to excel files
researchers_path = 'datasets/users/researchers.xlsx'
articles_path = 'datasets/articles/excels_CS/articles.xlsx'

researchers_df = pd.read_excel(researchers_path)
articles_df = pd.read_excel(articles_path)

conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

# SQLAlchemy engine
engine = create_engine(f'postgresql://{db_user}:{password}@{db_host}:{db_port}/{db_name}')

# push DataFrames to PostgreSQL
researchers_df.to_sql('researchers_table', engine, if_exists='replace', index=False)
articles_df.to_sql('articles_table', engine, if_exists='replace', index=False)

cursor = conn.cursor()

# update query
update_query = """
    UPDATE articles_table
    SET authors = REPLACE(REPLACE(authors, 'Authors:', ''), E'\\n', '')
    WHERE authors LIKE '%Authors:%' OR authors LIKE '%' || E'\\n' || '%'
"""

# chage Appreciated column type to Text in order to be able to store Appreciated values generated in SimpleRecom.ipynb
update_column_type_query = "ALTER TABLE researchers_table ALTER COLUMN \"Appreciated\" TYPE TEXT;"
cursor.execute(update_column_type_query)

cursor.execute(update_query)
conn.commit()
cursor.close()
conn.close()
