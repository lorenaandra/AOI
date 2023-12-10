import pandas as pd
import psycopg2
from sqlalchemy import Column, MetaData, String, Table, create_engine
from urllib.parse import quote_plus

# PostgreSQL connection details
# (replace with your actual credentials)
db_user = 'postgres'
db_password = 'p@$$w0rd!'
db_host = 'localhost'
db_port = '5432'
db_name = 'AOI'

# Format the password for the connection string
password = quote_plus(db_password)

# Paths to your Excel files
researchers_path = 'datasets/users/researchers.xlsx'
articles_path = 'datasets/articles/excels_CS/articles.xlsx'

# Read Excel files into pandas DataFrames
researchers_df = pd.read_excel(researchers_path)
articles_df = pd.read_excel(articles_path)

# Create a connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

# Create a SQLAlchemy engine to push the data to the database
engine = create_engine(f'postgresql://{db_user}:{password}@{db_host}:{db_port}/{db_name}')

# Create tables if they don't exist and push DataFrames to PostgreSQL
researchers_df.to_sql('researchers_table', engine, if_exists='replace', index=False)
articles_df.to_sql('articles_table', engine, if_exists='replace', index=False)

# Create a cursor to execute SQL queries
cursor = conn.cursor()

# SQL update query
update_query = """
    UPDATE articles_table
    SET authors = REPLACE(REPLACE(authors, 'Authors:', ''), E'\\n', '')
    WHERE authors LIKE '%Authors:%' OR authors LIKE '%' || E'\\n' || '%'
"""

# chage Appreciated column type to Text in order to be able to store Appreciated values generated in InterestRecom.ipynb
update_column_type_query = "ALTER TABLE researchers_table ALTER COLUMN \"Appreciated\" TYPE TEXT;"
cursor.execute(update_column_type_query)

# Execute the update query
cursor.execute(update_query)

# Commit the changes to the database
conn.commit()

# Close the cursor and the connection
cursor.close()
conn.close()


