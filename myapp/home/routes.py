from flask import render_template
from . import home_bp


@home_bp.route('/', methods=['GET'])
def home():
    return render_template('index.html', menu=0)
