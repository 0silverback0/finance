from flask import Flask, render_template,request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from forms import UserForm
import numpy as np
import matplotlib.pyplot as plt
from getAdjustedClose import getAdjustedClose

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Deja1218@localhost:5432/start'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config["SECRET_KEY"] = "shh"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

### routes

@app.route('/', methods=['GET', 'POST'])
def home():
    
    form = UserForm()
    
    if form.validate_on_submit():
        stock1 = form.stock1.data
        stock2 = form.stock2.data
        stock3 = form.stock3.data
        stock4 = form.stock4.data

        stocks = [stock1, stock2, stock3, stock4]
        
        data = getAdjustedClose(stocks)
    
        return render_template('index.html', form=form, tables=[data.to_html(classes='data')], titles=data.columns.values)
    return render_template('index.html', form=form, data='')

