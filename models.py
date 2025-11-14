import json
from sqlalchemy.orm import relationship
from saleapp import db, app
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DateTime, Enum
from datetime import datetime
from enum import Enum as RoleEnum
from flask_login import UserMixin


class UserRole(RoleEnum):
    USER = 1
    ADMIN = 2


class Base(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False, unique=True)
    active = Column(Boolean, default=True)
    create_date = Column(DateTime, default=datetime.now())

    def __str__(self):
        return self.name


class User(Base, UserMixin):
    username = Column(String(150), unique=True, nullable=False)
    password = Column(String(150), nullable=False)
    avatar = Column(String(500),default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fpngtree.com%2Fso%2Fuser-avatar&psig=AOvVaw0Z6_2JBbGpTCGGfI1sA1ua&ust=1763189938740000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCLixk-KQ8ZADFQAAAAAdAAAAABAE')
    role = Column(Enum(UserRole), default=UserRole.USER)


class Category(Base):
    products = relationship('Product', backref="category", lazy=True)


class Product(Base):
    price = Column(Float, default=0.0)
    image = Column(String(300), default="https://shopdunk.com/images/thumbs/0049405_iphone-17-256gb.png")
    cate_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == "__main__":
    with app.app_context():
        # db.create_all()
        # c1 = Category(name="Laptop")
        # c2 = Category(name="Mobile")
        # c3 = Category(name="Tablet")
        #
        # db.session.add_all([c1, c2, c3])
        #
        # with open("saleapp/data/product.json", encoding="utf-8") as f:
        #     product = json.load(f)
        #
        #     for p in product:
        #         db.session.add(Product(**p))
        #

        import hashlib
        password = hashlib.md5("12345".encode("utf-8")).hexdigest()
        u1 = User(name="QuynhNhuu", username="nhuu", avatar = "https://e7.pngegg.com/pngimages/340/946/png-clipart-avatar-user-computer-icons-software-developer-avatar-child-face-thumbnail.png",password=password)


        db.session.add(u1)
        db.session.commit()