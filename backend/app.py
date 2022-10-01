from flask import Flask, request
import psycopg2
import os

app = Flask(__name__)

conn = psycopg2.connect(
    host=os.environ['DB_HOST'],
    database=os.environ['DB_SCHEMA'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASS'])

@app.route("/welcome", methods = ['GET'])
def welcome():
    return {"msg":"Welcome!"}

@app.route('/products')
def get_products():
    query = "select * from product"
    cursor = conn.cursor()
    cursor.execute(query)
    products_result = cursor.fetchall()
    conn.commit()
    result = list()

    for row in products_result:
       result.append({
            "id": row[0],
            "product_name": row[1],
            "price": row[2]
        })

    return result

@app.route("/order", methods = ['GET'])
def get_orders():
    query = "SELECT a.id, b.product_name, a.total_price, a.amount FROM orders a JOIN product b ON a.product_id::int4 = b.id::int4"

    cursor = conn.cursor()
    cursor.execute(query)
    order_result = cursor.fetchall()
    conn.commit()

    result = list()

    for row in order_result:
        result.append({
            "id": row[0],
            "product_name": row[1],
            "total_price": row[2],
            "quantity": row[3]
        })

    return result

@app.route("/order", methods = ['DELETE'])
def clear_order():
    cursor = conn.cursor()
    query = "DELETE FROM orders"
    cursor.execute(query)
    conn.commit()
    return 'OK'


#expects product_name, quantity
@app.route("/order", methods = ['POST'])
def post_order():
    json = request.get_json()
    cursor = conn.cursor()

    query = "select * from product where product_name = '{}'".format(json["product_name"])
    cursor.execute(query)
    order_result = cursor.fetchone()

    product = {
        "product_id": order_result[0],
        "product_name": order_result[1],
        "price": order_result[2]
    }

    product_id = product["product_id"]
    amount = int(json["quantity"])
    total_price = amount * product["price"]

    postgres_insert_query = """ INSERT INTO orders ( product_id, amount, total_price) VALUES (%s,%s,%s)"""

    record_to_insert = ( product_id, amount, total_price)

    cursor.execute(postgres_insert_query, record_to_insert)

    conn.commit()

    return "OK"


if __name__ == '__main__':
    app.run()
