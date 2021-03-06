from sqlalchemy.orm import backref
from main import db

# ProductCategory = db.Table('ProductCategory', db.Model.metadata,
#                     db.Column('pid', db.Integer, db.ForeignKey('Product.id')),
#                     db.Column('cid', db.Integer, db.ForeignKey('Category.id'))
#                     )

ProductSubcategory = db.Table('ProductSubcategory', db.Model.metadata,
                    db.Column('pid', db.Integer, db.ForeignKey('Product.id')),
                    db.Column('sid', db.Integer, db.ForeignKey('Subcategory.id'))
                   )

# BrandCategory = db.Table('BrandCategory', db.Model.metadata,
#                     db.Column('bid', db.ForeignKey('Brand.id')),
#                     db.Column('cid', db.ForeignKey('Category.id'))
#                    )

# BrandSubcategory = db.Table('BrandSubcategory', db.Model.metadata,
#                     db.Column('bid', db.ForeignKey('Brand.id')),
#                     db.Column('sid', db.ForeignKey('Subcategory.id'))
#                    )

class Category(db.Model):
  __tablename__ = 'Category'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  description = db.Column(db.Text())

  # products = db.relationship('Product', secondary=ProductCategory, back_populates='category')


# class Brand(db.Model):
#   __tablename__ = 'Brand'
#   id = db.Column(db.Integer, primary_key=True)
#   name = db.Column(db.String())
  
#   subcategory = db.relationship('Subcategory', secondary=BrandSubcategory, back_populates='brands')
#   category = db.relationship('Category', secondary=BrandCategory, back_populates='brands')


class Subcategory(db.Model):
  __tablename__ = 'Subcategory'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  description = db.Column(db.Text())
  category = db.Column(db.Integer, db.ForeignKey("Category.id"))


  # brands = db.relationship('Brand', secondary=BrandSubcategory, back_populates='subcategory')
  products = db.relationship('Product', secondary=ProductSubcategory, back_populates='subcategory')



class Product(db.Model):
  __tablename__ = 'Product'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  description = db.Column(db.Text())
  price = db.Column(db.String())
  image = db.Column(db.String())
  ingredients = db.Column(db.Text())

  # category = db.relationship('Category', secondary=ProductCategory, back_populates='products')
  subcategory = db.relationship('Subcategory', secondary=ProductSubcategory, back_populates='products')




