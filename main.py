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
    print(products)
    return render_template('home.html', products = products)

# Each Subcategory Page 
@app.route("/<string:category>/<string:name>")
def subcat(category, name):
    subcat = models.Subcategory.query.filter_by(name=name).all()
    return render_template('subcategory.html', subcat = subcat)

# Contact Us Page 
@app.route('/contact_us')
def contact():
    
    return render_template('contact_us.html')

if __name__ == "__main__":
    app.run(debug=True)





# Replace Underscores test code
# underscore = "Facial_Treatments"
# alter = underscore.replace("_", " ")
# print(alter)
# OR
# import jinja2
# test = jinja2.Template('{{ test1 | replace("Facial_Treatments", "Facial Treatments") }}')
# print(test)
# General page route/query for all Subcategory pages     
