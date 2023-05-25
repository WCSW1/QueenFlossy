from app import app
from flask import render_template, redirect, request, session, url_for
from app.models.post import Post
from app.models.user import User
from app.models.profile import Profile


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/user/login')
    data = {"id": session['user_id']}
    return render_template('dashboard.html', user=User.get_by_id(data), posts=Post.get_all())


@app.route('/contact.html', methods=['GET'])
def contact_page():

    return render_template('contact.html')


@app.route('/about.html', methods=['GET'])
def about_page():

    return render_template('about.html')


@app.route('/posts/new')
def create_post():
    if 'user_id' not in session:
        return redirect('/user/login')
    return render_template('new.html')


@app.route('/posts/new/process', methods=['POST'])
def process_post():
    if 'user_id' not in session:
        return redirect('/user/login')
    if not Post.validate_post(request.form):
        return redirect('/posts/new')
    data = {
        'user_id': session['user_id'],
        'title': request.form['title'],
        'photo': request.form['photo'],
        'posting': request.form['posting'],
    }
    Post.save(data)
    return redirect('/dashboard')


@app.route('/posts/<int:id>')
def view_post(id):
    if 'user_id' not in session:
        return redirect('/user/login')
    return render_template('view.html', post=Post. get_by_id({'id': id}))


@app.route('/posts/edit/<int:id>')
def edit_post(id):
    if 'user_id' not in session:
        return redirect('/user/login')
    data = {'id': id}
    return render_template('edit.html', post=Post.get_by_id({'id': id}))


@app.route('/posts/edit/process/<int:id>', methods=['POST'])
def process_edit_post(id):
    if 'user_id' not in session:
        return redirect('/user/login')
    if not Post.validate_post(request.form):
        return redirect(f'/posts/edit/{id}')

    data = {
        'id': id,
        'title': request.form['title'],
        'posting': request.form['posting'],
        'photo': request.form['photo'],
    }
    Post.update(data)
    return redirect('/dashboard')


@app.route("/posts/delete/<int:id>")
def delete_post(id):
    if 'user_id' not in session:
        return redirect('/user/login')
    data = {"id": id}
    Post.delete(data)
    return redirect("/dashboard")

