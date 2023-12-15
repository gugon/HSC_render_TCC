from flask import Flask

from flask_bootstrap import Bootstrap

from .home import home_bp
from .nav import nav
from .proveedores import proveedores
from .productos import productos

app = Flask(__name__)
Bootstrap(app)
nav.init_app(app)
app.config.from_pyfile('config/config.cfg')
app.register_blueprint(home_bp)
app.register_blueprint(proveedores)
app.register_blueprint(productos)
