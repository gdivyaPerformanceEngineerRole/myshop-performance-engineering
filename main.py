from fastapi import FastAPI, HTTPException
import os
from pydantic import BaseModel, Field
from psycopg_pool import ConnectionPool
from contextlib import asynccontextmanager
from dotenv import load_dotenv

load_dotenv()

# Database connection pool
pool = ConnectionPool(
    kwargs={
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
        "dbname": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD")
    },
    min_size=2,
    max_size=10,
    timeout=30,
    open=False
)

# Application startup and shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    pool.open()
    try:
        pool.wait()
        yield
    finally:
        pool.close()

app = FastAPI(lifespan=lifespan)

# Borrow a database connection
def get_db_connection():
    return pool.connection()

@app.get("/")
def home():
    return {"message": "Welcome to MyShop"}

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

@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM products WHERE product_id = %s",
                (product_id,)
            )
            row = cur.fetchone()
            if row is None:
                raise HTTPException(
                    status_code=404,
                    detail="Product not found"
                )
            columns = [desc.name for desc in cur.description]
            return dict(zip(columns, row))

@app.get("/search")
def search_products(keyword: str):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM products WHERE name ILIKE %s",
                (f"%{keyword}%",)
            )
            products = cur.fetchall()

    return products
class CartItem(BaseModel):
    customer_id: int
    product_id: int
    quantity: int = Field(default=1, gt=0)


@app.post("/cart")
def add_to_cart(item: CartItem):
    with get_db_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                "SELECT product_id FROM products WHERE product_id = %s",
                (item.product_id,)
            )

            if cur.fetchone() is None:
                raise HTTPException(
                    status_code=404,
                    detail="Product not found"
                )

            cur.execute("""
                INSERT INTO cart
                (customer_id, product_id, quantity)
                VALUES (%s, %s, %s)
                ON CONFLICT (customer_id, product_id)
                DO UPDATE SET
                quantity = cart.quantity + EXCLUDED.quantity
                RETURNING cart_id, quantity
            """, (
                item.customer_id,
                item.product_id,
                item.quantity
            ))

            row = cur.fetchone()
            conn.commit()

            return {
                "message": "Product added to cart",
                "cart_id": row[0],
                "quantity": row[1]
            }
