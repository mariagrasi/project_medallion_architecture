import pandas as pd
import psycopg2
from psycopg2 import sql
from io import StringIO
import os

from dotenv import load_dotenv

load_dotenv()

class PostgresDB:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        self.conn.autocommit = False

    def close(self):
        self.conn.close()

    # -------------------------------
    # CREATE TABLE
    # -------------------------------
    def create_table_from_df(self, table_name: str, df: pd.DataFrame):
        with self.conn.cursor() as cursor:
            columns_sql = []

            for col, dtype in df.dtypes.items():
                if pd.api.types.is_integer_dtype(dtype):
                    col_type = sql.SQL("INTEGER")
                elif pd.api.types.is_float_dtype(dtype):
                    col_type = sql.SQL("DOUBLE PRECISION")
                elif pd.api.types.is_bool_dtype(dtype):
                    col_type = sql.SQL("BOOLEAN")
                elif pd.api.types.is_datetime64_any_dtype(dtype):
                    col_type = sql.SQL("TIMESTAMP")
                else:
                    col_type = sql.SQL("TEXT")

                columns_sql.append(
                    sql.SQL("{} {}").format(
                        sql.Identifier(col),
                        col_type
                    )
                )

            query = sql.SQL("""
                CREATE TABLE IF NOT EXISTS {} (
                    {}
                )
            """).format(
                sql.Identifier(table_name),
                sql.SQL(", ").join(columns_sql)
            )

            cursor.execute(query)
            self.conn.commit()

    # -------------------------------
    # COPY FROM DataFrame
    # -------------------------------
    def copy_from_dataframe(self, table_name: str, df: pd.DataFrame):
        buffer = StringIO()

        df.to_csv(
            buffer,
            index=False,
            header=False,
            sep='\t',
            na_rep='\\N'
        )
        buffer.seek(0)

        with self.conn.cursor() as cursor:
            copy_sql = sql.SQL("""
                COPY {} ({})
                FROM STDIN WITH (FORMAT CSV, DELIMITER E'\t', NULL '\\N')
            """).format(
                sql.Identifier(table_name),
                sql.SQL(', ').join(map(sql.Identifier, df.columns))
            )

            cursor.copy_expert(copy_sql, buffer)
            self.conn.commit()

