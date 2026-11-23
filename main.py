
from fastapi import FastAPI
import os
import psycopg
from dotenv import load_dotenv

load_dotenv()
print("Password loaded:", bool(os.getenv("DB_PASSWORD")))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to MyShop"}

def get_db_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

@app.get("/test-db")
def test_db():
    with get_db_connection() as conn:
        return {"message": "PostgreSQL connected successfully"}
@app.get("/products")
def get_products():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM products")
            rows = cur.fetchall()
            columns = [desc.name for desc in cur.description]
            return [dict(zip(columns, row)) for row in rows]
