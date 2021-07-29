from os import name
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy, model
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

import models 

# Homepage route/query
@app.route('/')
def home():
    return render_template('home.html', page_title="HOME")

# Cleanser page route/query 
@app.route("/<string:category>/<string:name>")
def cleanser(category, name):
    cleanser = models.Subcategory.query.filter_by(name='Cleanser').all()
    return render_template('cleanser.html', cleanser = cleanser)

# Base page route/query 
@app.route("/<string:category>/<string:name>")
def base(category, name):
    base = models.Subcategory.query.filter_by(name='Base').all()
    return render_template('base.html', base = base)

# Description of Cleanser 
# @app.route("/<string:subcat>/<string:name>")
# def subcat(subcat, name):
#     result = models.Subcategory.query.filter_by(name='Cleanser').all()
#     return render_template('cleanser.html', result = result)


# This is Mr Dunford's Query/Explanation, and this is also connected to the variable name of products in models.py
# @app.route("/skincare/all_skincare/<string:name>")
# def all_skincare(name):
#     cat = models.Category.query.filter_by(name=name).first_or_404()
#     print(cat)
#     print(cat.products) 
#     return render_template('all_skincare.html', cat = cat)

# Trying to get all skincare products to show up on all skincare subcat page. This code shows unexpected '%' syntax error and highlights {% endfor %}
# @app.route("/skincare/all_skincare")
# def all_skincare():
#     cat = models.Category.query.all()
#     return render_template('all_skincare.html', cat = cat)


# Prints it works etc on each subcat page 
# @app.route("/<string:subcat>/<string:name>")
# def subcat(subcat, name):
#     result = models.Subcategory.query.filter_by(name=subcat).all()
#     return "works! {} {} {}".format(subcat, name, result)



# @app.route('/skincare/<int:id>')
# def subcategory(id):
#     subcategory = models.Subcategory.query.all()
#     return render_template('subcategory.html', subcategory = subcategory)

# @app.route('/wishlist/<int:id>')
# def wishlist(id):
#     return render_template('wishlist.html', wishlist = wishlist)

# @app.route('/product/<int:id>')
# def product(id):
#     product = models.Product.query.all()
#     return render_template('product.html', product = product)

# @app.route('/best_sellers/<int:id>')
# def best_sellers(id):
#     return render_template('best_sellers.html', best_sellers = best_sellers)

if __name__ == "__main__":
    app.run(debug=True)