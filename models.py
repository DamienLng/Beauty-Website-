from main import db

Productsubcategory = db.Table('Productsubcategory', db.Model.metadata,
                    db.Column('Product_id', db.ForeignKey('Product.id')),
                    db.Column('Subcategory_id', db.ForeignKey('Subcategory.id'))
                   )


Brandcategory = db.Table('Brandcategory', db.Model.metadata,
                    db.Column('Brand_id', db.ForeignKey('Brand.id')),
                    db.Column('Category_id', db.ForeignKey('Category.id'))
                   )


Brandsubcategory = db.Table('Brandsubcategory', db.Model.metadata,
                    db.Column('Brand_id', db.ForeignKey('Brand.id')),
                    db.Column('Subategory_id', db.ForeignKey('Subcategory.id'))
                   )


class Category(db.Model):
  __tablename__ = 'Category'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  description = db.Column(db.Text())
  brands = db.relationship('Brand', secondary=Brandcategory, back_populates='category')


class Brand(db.Model):
  __tablename__ = 'Brand'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  subcategory = db.relationship('Subcategory', secondary=Brandsubcategory, back_populates='brands')
  category = db.relationship('Category', secondary=Brandcategory, back_populates='brands')


class Subcategory(db.Model):
  __tablename__ = 'Subcategory'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  description = db.Column(db.Text())
  brands = db.relationship('Brand', secondary=Brandsubcategory, back_populates='subcategory')
  products = db.relationship('Product', secondary=Productsubcategory, back_populates='subcategory')


class Product(db.Model):
  __tablename__ = 'Product'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  description = db.Column(db.Text())
  price = db.Column(db.String())
  image = db.Column(db.String())
  ingredients = db.Column(db.Text())
  category = db.Column(db.Integer, foreign_key=True)
  brand = db.Column(db.Integer, foreign_key=True)
  subcategory = db.relationship('Subcategory', secondary=Productsubcategory, back_populates='products')

  
