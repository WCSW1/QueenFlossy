import os
from flask import render_template, redirect, request, session, url_for
from flask import send_from_directory
from werkzeug.utils import secure_filename
from app import app
from app.models.profile import Profile
from app.models.user import User



app.config['UPLOAD_FOLDER'] = 'app/static/uploads/'

@app.route('/profile.html')
def profile_page():
    if 'user_id' not in session:
        return redirect('/user/login')
    data = {"id": session['user_id']}
    return render_template('profile.html', user=User.get_by_id(data), profile=Profile.get_users_profile('user_id'))


@app.route('/create_profile.html', methods=['GET'])
def create_profile_page():
    if 'user_id' not in session:
        return redirect('/user/login')
    data = {"id": session['user_id']}
    return render_template('create_profile.html', user=User.get_by_id(data), profile=Profile.get_users_profile('user_id'))

@app.route('/edit_profile.html', methods=['GET'])
def edit_profile_page():
    if 'user_id' not in session:
        return redirect('/user/login')
    data = {"id": session['user_id']}
    return render_template('edit_profile.html', user=User.get_by_id(data), profile=Profile.get_users_profile('user_id'))


@app.route('/create_profile', methods=["POST"])
def create_users_profile():
    if not Profile.validations(request.form):
        return redirect('/create_profile')
    if request.files['Pic'].filename == '':
        data = {
            'Pic': None,
            'users_id': session['id'],
            'First_name': request.form['First_name'],
            'Last_name': request.form['Last_name'],
            'email': request.form['email'],
            'phone_number': request.form['phone_number'],
            'Address': request.form['Address'],
            'City': request.form['City'],
            'State': request.form['State'],
            'Country': request.form['Country'],
            'Zip_code': request.form['Zip_code'],
            'Education': request.form['Education'],
        }
        Profile.create_profile(data)
    else:
        if 'Pic' in request.files:
            file = request.files['Pic']
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            data = {
                'Pic': f'uploads/{filename}',
                'users_id': session['id'],
                'First_name': request.form['First_name'],
                'Last_name': request.form['Last_name'],
                'email': request.form['email'],
                'phone_number': request.form['phone_number'],
                'Address': request.form['Address'],
                'City': request.form['City'],
                'State': request.form['State'],
                'Country': request.form['Country'],
                'Zip_code': request.form['Zip_code'],
                'Education': request.form['Education'],
            }
        Profile.create_profile(data)
        print("create_users_profile done!")
        Profile.update_users_profile(data)
    return redirect('/dashboard')


@app.route('/update_profile', methods=["POST"])
def update_users_profile():
    print(request.files['Pic'])
    if not Profile.Profile_validations(request.form):
        return redirect('/update_profile')
    if request.files['Pic'].filename == '':
        data = {
            'Pic': None,
            'First_name': request.form['First_name'],
            'Last_name': request.form['Last_name'],
            'email': request.form['email'],
            'phone_number': request.form['phone_number'],
            'Address': request.form['Address'],
            'City': request.form['City'],
            'State': request.form['State'],
            'Country': request.form['Country'],
            'Zip_code': request.form['Zip_code'],
            'Education': request.form['Education']
        }
        Profile.update_users_profile(data)
    else:
        file = request.files['Pic']
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        data = {
            'users_id': session['id'],
            'Pic': f'uploads/{filename}',
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'phone_number': request.form['phone_number'],
            'Address': request.form['Address'],
            'City': request.form['City'],
            'State': request.form['State'],
            'Country': request.form['Country'],
            'Zip_code': request.form['Zip_code'],
            'Education': request.form['Education'],
            'Experience': request.form['Experience'],
            'Additional_Details': request.form['Additional_Details']
        }
        Profile.update_users_profile(data)
    return redirect('/profile_page')


@app.route('/uploads/<filename>')
def serve_profile_pic(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
