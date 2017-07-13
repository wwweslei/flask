from flask import render_template, flash, url_for, request
from app import app, db
from forms import FormPassword
from models import Password

model = Password


@app.route('/', methods=('GET', 'POST'))
def home():
    form = FormPassword()
    if form.validate_on_submit():
        db.session.add(model(form.site.data, form.username.data,
                             form.email.data, form.password.data))
        try:
            db.session.commit()
            flash("Seus dados foram salvos")
        except:
            flash("Site já registrado")
    return render_template('index.html', form=form)


@app.route('/select', methods=('GET', 'POST'))
def select():
    if request.method == "POST":
        search = (request.form.get("search"))
        views = model.query.filter(model.site.endswith(search)).all()
    return render_template('select.html', views=views)


@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    form = FormPassword()
    query = model.query.filter_by(id=id).first()
    if form.validate_on_submit():
        query.site = form.site.data
        query.username = form.username.data
        query.email = form.email.data
        query.password = form.password.data
        try:
            db.session.commit()
            flash("Seus dados foram atualizados")
        except:
            flash("Site já registrado")
    return render_template('update.html', query=query, form=form)
