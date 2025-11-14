import json
from models import Category, Product, User
from saleapp import app
import hashlib

def load_categories():
    # with open("data/category.json", encoding="utf-8") as f:
    #     cates = json.load(f)


        return Category.query.all()
def auth_user(username, password):

    password = hashlib.md5(password.encode("utf-8")).hexdigest()
    return User.query.filter(User.username.__eq__(username), User.password.__eq__(password)).first()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def load_products(q=None, cate_id=None, page=None):
    # with open("data/product.json", encoding="utf-8") as p:
    #     product = json.load(p)
    #
    #     if q:
    #         product = [p for p in product if p["name"].find(q) >= 0]
    #
    #     if cate_id:
    #         product = [p for p in product if p["cate_id"].__eq__(int(cate_id))]
    #
    #     return product
    query = Product.query

    if q:
        query = query.filter(Product.name.contains((q)))

    if cate_id:
        query = query.filter(Product.cate_id.__eq__(cate_id))

    if page:
        size = app.config["PAGE_SIZE"]
        start = (int(page)-1)*size
        query = query.slice(start, start+size)

    return query.all()

def count_product():
    return Product.query.count()


def get_product_by_id(id):
    # with open("data/product.json", encoding="utf-8") as p:
    #     product = json.load(p)
    #
    #     for p in product:
    #         if p["id"].__eq__(id):
    #             return p
    return Product.query.get(id)


if __name__ == "__main__":
    with app.app_context():
        print(auth_user("nhu", "12345"))
