from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html', page_title="HOME")

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/category/<int:id>')
def category(id):

    return render_template('category.html', category = category)

@app.route('/subcategory/<int:id>')
def subcategory(id):

    return render_template('subcategory.html', subcategory = subcategory)

@app.route('/product/<int:id>')
def product(id):

    return render_template('product.html', product = product)

@app.route('/wishlist/<int:id>')
def wishlist(id):

    return render_template('wishlist.html', wishlist = wishlist)
