from os import name, replace
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy, model
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

import models 

# Homepage route/query for all Products
@app.route('/')
def home():
    products = models.Product.query.all()
    # print(products)
    return render_template('home.html', products = products)

# Subcategory pages for skincare, makeup and hair, hand & body
@app.route('/<string:category>/<string:name>')
def subcat(category, name):
    subcat = models.Subcategory.query.filter_by(name=name).all()
    for Subcategory in subcat:
        print(Subcategory.products)
    return render_template('subcategory.html', subcat = subcat, products = Subcategory.products)

# Subcategory page for different brands of products
@app.route('/<string:table>/<string:name>')
def brands(category, name):
    brands = models.Product.query.filter_by(name=name).all()
    for Product in brands:
        print(Product.products)
    return render_template('brand.html', brands = brands, products = Product.products)

# if table is a brand.name 
# then models.Brand.query.filter_by(name=name).all()

# if table = subcategory 
# then models.Subcategory.query.filter_by(name=name).all()

# this is all under one route @app.route('/<string:table>/<string:name>') with one function name (name has to 
# make sense with both things im trying to query eg, brands and other subcatories), then 
# write render template thing with both html links in there etc think logically to piece the rest together. 
# Furthermore, I may need to fix up models.py to fully make brands query functional. In the end
# I will only have one route querying two different things. So i can delete the subcat query. 



# Individual Product Pages 
@app.route('/product/<int:id>')
def product(id): 
    product = models.Product.query.filter_by(id=id).first_or_404()
    return render_template('product.html', product = product)

# Contact Us Page 
@app.route('/contact_us')
def contact():
    
    return render_template('contact_us.html')


if __name__ == "__main__":
    app.run(debug=True)

