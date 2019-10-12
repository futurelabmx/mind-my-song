from flask import Flask
from flask import request
from flask import render_template

from forms import UserForm
from db import MONGO_URI
from db import db_connect
from db import db_fetch_one
from db import db_insert_document


application = Flask(__name__)
users = None
# users = db_connect(MONGO_URI, 'mind-my-song', 'users')


@application.route('/', methods=['GET', 'POST'])
def test():
    return """<h1>Hello world!</h1>"""

def index():
    form = UserForm(request.form)

    if len(form.errors):
        print(form.errors)
    if request.method == 'POST':
        if form.email.data and form.password.data:
            if 'signup' in request.form:
                query = db_fetch_one(users, {'email' : form.email.data})
                if query is not None:
                    return render_template('index.html', flag='user')
                new_user = {
                    'email': form.email.data,
                    'password' : form.password.data
                }
                db_insert_document(users, new_user)
                return render_template('index.html', flag='registration')
            if 'login' in request.form:
                query = db_fetch_one(users,
                                    {
                                        'email' : form.email.data,
                                        'password' : form.password.data
                                    })
                if query is not None:
                    return render_template('dashboard.html')
                else:
                    return render_template('index.html', flag='password')
    return render_template('index.html', flag=None)


@application.errorhandler(404)
def not_found(error=None):
    return render_template('404.html')


if __name__ == '__main__':
    application.run()
