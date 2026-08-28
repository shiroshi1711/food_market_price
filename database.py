from sqlalchemy import create_engine, text

from config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


DATABASE_URL = (
    f"postgresql+psycopg://"
    f"{DB_USER}:{DB_PASSWORD}@"
    f"{DB_HOST}:{DB_PORT}/"
    f"{DB_NAME}"
)

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "prepare_threshold": None
    }
)


def save_to_database(dataframe, table_name):

    if dataframe.empty:
        print(f"No data to insert into {table_name} (all rows filtered out).")
        return
    
    dataframe.to_sql(name= table_name,
                     con=engine,
                     if_exists='append',
                     index=False)

    print(f'Saved {len(dataframe)} rows into {table_name}!')