db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        print(user.check_password(form.password.data), form.password.data)
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            cookie_saver(user.email, user.hashed_password)
            return redirect("/snow/main")


def main():
    db_session.global_init("db/users.db")
    app.run(port=8080, host='127.0.0.1')


def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Snow',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Snow',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User()
        user.email = form.email.data
        user.hashed_password = generate_password_hash(form.password.data)
        user.rank = "client"
        db_sess.add(user)
        db_sess.commit()
        cookie_saver(user.email, user.hashed_password)
        return redirect('/snow/login')
    return render_template('register.html', title='Snow', form=form)