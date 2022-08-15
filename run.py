import os
import unittest

from app.main import create_app
#from flask_script import Manager

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.app_context().push()


if __name__ == '__main__':
    app.run(debug=True)

