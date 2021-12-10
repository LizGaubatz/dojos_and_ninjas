from flask import render_template, redirect, request
from flask_app import app
from flask_app.model import ninja, dojo


@app.route('/')
def index():
    # all_ninjas = ninja.Ninja.get_all()
    # print(all_ninjas)
    # new_dojo = dojo.Dojo.save(request.form)
    all_dojos = dojo.Dojo.get_all()
    print(all_dojos)
    return render_template("index.html", all_dojos=all_dojos)

# ______________

@app.post('/new/dojo')
def new_dojo():
    data = {
        'name': request.form['name']
    }
    new_dojo = dojo.Dojo.save(data)
    return redirect('/')

#     @app.post('/user/new')
# def create_user():
#     data = {
#         'first_name': request.form['first_name'],
#         'last_name': request.form['last_name'],
#         'email': request.form['email'],
#     }
#     user_id = usermodel.User.save(data)

#     return redirect(f'/read/{user_id}')

# ______________

# @app.route('/')
# def new():
#     return render_template("new.html")

# @app.post('/ninja/new')
# def create_user():
#     new_ninja = ninja.Ninja.save(request.form)
#     return redirect(f'/read/{new_ninja}')

@app.route('/ninja')
def new():
    all_dojos = dojo.Dojo.get_all()
    print(all_dojos)
    return render_template("new.html",all_dojos=all_dojos)

# @app.post('/ninja/new')
# def create_user():
#     ninja.Ninja.save(request.form)
#     print('Ninja added to dojo!')
#     return redirect('/ninja')

@app.post('/ninja/new')
def create_ninja():
    data = {
        'dojos_id': request.form['dojos'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    new_dojo = ninja.Ninja.save(data)
    print(new_dojo)
    return redirect('/ninja')

# ______________

@app.route('/read/<int:id>')
def read(id):
    data = {
        'id':id
    }
    dojo_info = dojo.Dojo.get_both(data)
    print(dojo_info)
    return render_template("read.html",dojo_info=dojo_info)
