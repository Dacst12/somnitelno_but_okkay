from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    user_type = db.Column(db.String(20), nullable=False)  # 'user' or 'employer'

    # Fields specific to regular users
    name = db.Column(db.String(120), nullable=True)
    profession = db.Column(db.String(120), nullable=True)
    experience_level = db.Column(db.String(120), nullable=True)
    work_experience = db.Column(db.Text, nullable=True)
    about_me = db.Column(db.Text, nullable=True)
    github_link = db.Column(db.String(120), nullable=True)
    leetcode_link = db.Column(db.String(120), nullable=True)
    figma_link = db.Column(db.String(120), nullable=True)
    telegram_link = db.Column(db.String(120), nullable=True)
    is_verified = db.Column(db.Boolean, nullable=False, default=False)

    # Fields specific to employers
    about_us = db.Column(db.Text, nullable=True)
    company_link = db.Column(db.String(120), nullable=True)
    vk_link = db.Column(db.String(120), nullable=True)
    employer_telegram_link = db.Column(db.String(120), nullable=True)

class VerifiedAccountRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/portfolio')
@app.route('/')
@app.route('/index')
def index():
    employers = User.query.filter_by(user_type='employer').all()
    performers = User.query.filter_by(user_type='user').all()
    return render_template('portfolio.html', employers=employers, performers=performers, user=current_user)

@app.route('/profile')
@login_required
def profile():
    if current_user.user_type == 'employer':
        return redirect(url_for('profile_employer'))
    return render_template('profile.html', user=current_user)

@app.route('/profile-employer')
@login_required
def profile_employer():
    if current_user.user_type == 'user':
        return redirect(url_for('profile'))
    return render_template('profile-employer.html', user=current_user)

@app.route('/editing', methods=['GET', 'POST'])
@login_required
def editing():
    if current_user.user_type == 'employer':
        return redirect(url_for('editing_employer'))

    if request.method == 'POST':
        if 'name' in request.form:
            current_user.name = request.form['name']
            current_user.profession = request.form['profession']
            current_user.github_link = request.form['github']
            current_user.leetcode_link = request.form['leetcode']
            current_user.telegram_link = request.form['telegram']
            current_user.figma_link = request.form['figma']
            flash('Profile updated successfully')
        elif 'description' in request.form:
            current_user.about_me = request.form['description']
            flash('Description updated successfully')
        db.session.commit()
        return redirect(url_for('editing'))

    return render_template('editing.html', user=current_user)

@app.route('/editing-employer', methods=['GET', 'POST'])
@login_required
def editing_employer():
    if current_user.user_type == 'user':
        return redirect(url_for('editing'))

    if request.method == 'POST':
        if 'name' in request.form:
            current_user.name = request.form['name']
            current_user.profession = request.form['profession']
            current_user.company_link = request.form['site']
            current_user.vk_link = request.form['vk']
            current_user.employer_telegram_link = request.form['telegram']
            flash('Profile updated successfully')
        elif 'description' in request.form:
            current_user.about_us = request.form['description']
            flash('Company description updated successfully')
        db.session.commit()
        return redirect(url_for('editing_employer'))

    return render_template('editing-employer.html', user=current_user)

@app.route('/login', methods=['POST'])
def login():
    login = request.form['login']
    password = request.form['password']
    user = User.query.filter_by(login=login).first()
    if user and check_password_hash(user.password, password):
        login_user(user, remember=True)
        return redirect(url_for('index'))
    else:
        flash('Invalid login or password')
    return redirect(url_for('index'))

@app.route('/register', methods=['POST'])
def register():
    login = request.form['login']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm-password']
    user_type = 'employer' if 'employer' in request.form else 'user'

    if password != confirm_password:
        flash('Passwords do not match')
        return redirect(url_for('index'))

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = User(login=login, email=email, password=hashed_password, user_type=user_type)
    db.session.add(new_user)
    db.session.commit()
    flash('Registration successful')
    return redirect(url_for('index'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/change-password', methods=['POST'])
@login_required
def change_password():
    old_password = request.form['old-password']
    new_password = request.form['new-password']
    repeat_password = request.form['repeat-password']

    if not check_password_hash(current_user.password, old_password):
        flash('Старый пароль неверен')
        return redirect(request.referrer)

    if new_password != repeat_password:
        flash('Новые пароли не совпадают')
        return redirect(request.referrer)

    current_user.password = generate_password_hash(new_password, method='pbkdf2:sha256')
    db.session.commit()
    flash('Пароль успешно изменен')
    return redirect(request.referrer)

@app.route('/change-email', methods=['POST'])
@login_required
def change_email():
    new_email = request.form['new-email']
    password = request.form['password']

    if not check_password_hash(current_user.password, password):
        flash('Пароль неверен')
        return redirect(request.referrer)

    current_user.email = new_email
    db.session.commit()
    flash('E-mail успешно изменен')
    return redirect(request.referrer)

@app.route('/submit-verified-account', methods=['POST'])
def submit_verified_account():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']

    new_request = VerifiedAccountRequest(name=name, phone=phone, email=email)
    db.session.add(new_request)
    db.session.commit()

    flash('Ваша заявка отправлена. Наши специалисты свяжутся с вами.')
    return redirect(url_for('index'))

@app.route('/profile/<int:user_id>')
@login_required
def view_profile(user_id):
    user = User.query.get_or_404(user_id)
    if user.user_type == 'employer':
        return redirect(url_for('view_profile_employer', user_id=user_id))
    return render_template('profile.html', user=user, editable=(user.id == current_user.id))

@app.route('/profile-employer/<int:user_id>')
@login_required
def view_profile_employer(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('profile-employer.html', user=user, editable=(user.id == current_user.id))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5002, debug=True)