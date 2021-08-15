from os import name, replace
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy, model
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

import models 



# import jinja2
# test = jinja2.Template('{{ test1 | replace("Facial_Treatments", "Facial Treatments") }}')
# print(test)



# Homepage route/query
# @app.route('/')
# def home():
#     return render_template('home.html', page_title="HOME")

# Homepage route/query for all Products
@app.route('/')
def home():
    products = models.Product.query.all()
    print(products)
    return render_template('home.html', products = products)

# Replace Underscores test code
# underscore = "Facial_Treatments"
# alter = underscore.replace("_", " ")
# print(alter)

# General page route/query for all Subcategory pages     
@app.route("/<string:category>/<string:name>")
def subcat(category, name):
    subcat = models.Subcategory.query.filter_by(name=name).all()
    return render_template('subcategory.html', subcat = subcat)




if __name__ == "__main__":
    app.run(debug=True)