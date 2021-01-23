import sys
import os

APP_DIR = "/home/ec2-user/flask_proj07/"

sys.path.insert(0, APP_DIR)
os.chdir(APP_DIR)

from flask_app import app as application
