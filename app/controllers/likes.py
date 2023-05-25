from app import app
from flask import render_template, redirect, request, session, url_for, flash
from app.models.like import Like


@app.route("/like/<int:posts_id>")
def like_posts(post_id):
    data = {
        'users_id' : session['id'],
        'posts_id' : post_id
    }
    if Like.has_liked(data) == True:
        flash("Already Liked", "post")
        return redirect(f'/view.html/{post_id}')
    else:
        Like.save(data)
        flash("Liked", "posts")
        return redirect(f'/view.html/{post_id}')
    
@app.route('/unlike/<int:posts_id>')
def unlike_post(post_id):
    data = {
        'users_id' : session['id'],
        'posts_id' : post_id
    }
    Like.unlike(data)
    flash("Unliked", "post")
    return redirect(f'/view.html/{post_id}')
