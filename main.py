from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

import models 

@app.route('/')
def home():
    return render_template('home.html', page_title="HOME")

@app.route('/categories/<int:id>')
def category(id):
    print(id)
    category = models.Category.query.all()
    return render_template('category.html', category = category)

@app.route('/subcategory/<int:id>')
def subcategory(id):
    subcategory = models.Subcategory.query.all()
    return render_template('subcategory.html', subcategory = subcategory)

@app.route('/product/<int:id>')
def product(id):
    product = models.Product.query.all()
    return render_template('product.html', product = product)

@app.route('/wishlist/<int:id>')
def wishlist(id):
    return render_template('wishlist.html', wishlist = wishlist)


if __name__ == "__main__":
    app.run(debug=True)