from flask import Blueprint, render_template

siteblue = Blueprint('siteblue', __name__, template_folder = 'site_templates')

@siteblue.route('/')
def home():
    return render_template('index.html')

@siteblue.route('/profile')
def profile():
    return render_template('profile.html')