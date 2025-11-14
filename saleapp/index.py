import math

from flask import Flask, render_template, request, redirect
import dao
from saleapp import app, login, admin
from flask_login import login_user, current_user, logout_user

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

@app.route("/login", methods=['get', 'post'])
def login_old():
    err_msg = None
    if current_user.is_authenticated:
        return redirect('/')
    if request.method.__eq__('POST'):
        username = request.form.get("username")
        password = request.form.get("pwd")

        user = dao.auth_user(username, password)

        if user:
            login_user(user)
            return redirect('/')
        else:
            err_msg = "Tai khoan hoac mat khau khong dung!"

    cates = dao.load_categories()
    return render_template("login.html", cates=cates, err_msg=err_msg)
@app.route("/logout")
def logout_myuser():
    logout_user()
    return redirect("/login")
@login.user_loader
def get_user(id):
    return dao.get_user_by_id(id)

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)