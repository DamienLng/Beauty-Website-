from sqlalchemy.orm import backref
from main import db

ProductCategory = db.Table('ProductCategory', db.Model.metadata,
                    db.Column('Product_id', db.Integer, db.ForeignKey('Product.id')),
                    db.Column('Category_id', db.Integer, db.ForeignKey('Category.id'))
                    )

ProductSubcategory = db.Table('ProductSubcategory', db.Model.metadata,
                    db.Column('Product_id', db.Integer, db.ForeignKey('Product.id')),
                    db.Column('Subcategory_id', db.Integer, db.ForeignKey('Subcategory.id'))
                   )

# BrandCategory = db.Table('BrandCategory', db.Model.metadata,
#                     db.Column('Brand_id', db.ForeignKey('Brand.id')),
#                     db.Column('Category_id', db.ForeignKey('Category.id'))
#                    )

# BrandSubcategory = db.Table('BrandSubcategory', db.Model.metadata,
#                     db.Column('Brand_id', db.ForeignKey('Brand.id')),
#                     db.Column('Subategory_id', db.ForeignKey('Subcategory.id'))
#                    )

class Category(db.Model):
  __tablename__ = 'Category'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  description = db.Column(db.Text())

  home = db.relationship('Product', secondary=ProductCategory, back_populates='category')
  # brands = db.relationship('Brand', secondary=Brandcategory, back_populates='brandcategory')


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
  home = db.relationship('Product', secondary=ProductSubcategory, back_populates='subcategory')



class Product(db.Model):
  __tablename__ = 'Product'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  description = db.Column(db.Text())
  price = db.Column(db.String())
  image = db.Column(db.String())
  ingredients = db.Column(db.Text())
  # category = db.Column(db.Integer, db.ForeignKey("Category.id"))
  # brand = db.Column(db.Integer, db.ForeignKey("Brand.id"))

  category = db.relationship('Category', secondary=ProductCategory, back_populates='home')
  subcategory = db.relationship('Subcategory', secondary=ProductSubcategory, back_populates='home')




