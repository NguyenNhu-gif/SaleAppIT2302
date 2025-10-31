import math

from flask import Flask, render_template, request
import dao
from saleapp import app

@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    print(q)
    pages = request.args.get("page")
    cates = dao.load_categories()
    pros = dao.load_products(q=q, cate_id=cate_id, page = pages)
    pages = math.ceil(dao.count_product()/app.config["PAGE_SIZE"])
    return render_template("index.html", cates=cates, pros=pros, pages=pages)

@app.route("/products/<int:id>")
def details(id):
    return render_template("products-details.html", pros = dao.get_product_by_id(id))

@app.route("/login")
def login():
    cates = dao.load_categories()
    return render_template("login.html", cates=cates)

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)