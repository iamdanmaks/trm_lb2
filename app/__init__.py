from flask import Flask

app = Flask(__name__)

from app.views import index
from app.endpoints import handle_file
from app.endpoints import handle_analysis
