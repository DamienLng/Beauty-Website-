from os import name
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy, model
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

import models 

@app.route('/')
def home():
    return render_template('home.html', page_title="HOME")

# @app.route('/categories/<int:id>')
# def category(id):
#     print(id)
#     category = models.Category.query.all()
#     return render_template('category.html', category = category)


'''TODO: Make relationship table between Product and Category Table to see 
if this fixes the .products relationship problem'''
# This is Mr Dunford's Query/Explanation, and this is also connected to the variable name of products in models.py
@app.route("/skincare/subcategory/all_skincare/<string:name>")
def all_skincare(name):
    cat = models.Category.query.filter_by(name=name).first_or_404()
    print(cat)
    print(cat.products) 
    return render_template('all_skincare.html', cat = cat)



@app.route('/skincare/<int:id>')
def subcategory(id):
    subcategory = models.Subcategory.query.all()
    return render_template('subcategory.html', subcategory = subcategory)

@app.route('/wishlist/<int:id>')
def wishlist(id):
    return render_template('wishlist.html', wishlist = wishlist)

# @app.route('/product/<int:id>')
# def product(id):
#     product = models.Product.query.all()
#     return render_template('product.html', product = product)

@app.route('/best_sellers/<int:id>')
def best_sellers(id):
    return render_template('best_sellers.html', best_sellers = best_sellers)

if __name__ == "__main__":
    app.run(debug=True)