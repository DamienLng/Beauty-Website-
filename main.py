from os import name, replace
from flask import Flask, render_template, url_for, abort
from flask_sqlalchemy import SQLAlchemy, model
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

import models 


# Reroute when a 404 error is found
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# Homepage route/query for all Products
@app.route('/')
def home():
    products = models.Product.query.all()
    # print(products)
    return render_template('home.html', products = products)


# Subcategory pages for skincare, makeup and hair, hand & body
@app.route('/<string:category>/<string:name>')
def subcat(category, name):
    try:
        subcat = models.Subcategory.query.filter_by(name=name).all()
        for Subcategory in subcat:
            print(Subcategory.products)
        return render_template('subcategory.html', subcat = subcat, products = Subcategory.products)
    except:
        abort(404)


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

