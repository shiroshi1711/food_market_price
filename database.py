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

engine = create_engine(DATABASE_URL)


def save_to_database(dataframe, table_name):

    if dataframe.empty:
        print(f"No data to insert into {table_name} (all rows filtered out).")
        return
    
    records = dataframe.to_dict(orient="records")

    query = text(f"""
        INSERT INTO {table_name}
        (variant_id, variant_name, unit, date, region, price)
        VALUES
        (:variant_id, :variant_name, :unit, :date, :region, :price)

        ON CONFLICT (variant_id, date, region)
        DO UPDATE SET
            variant_name = EXCLUDED.variant_name,
            unit = EXCLUDED.unit,
            price = EXCLUDED.price;
    """)

    with engine.begin() as connection:
        connection.execute(query, records)