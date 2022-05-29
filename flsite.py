from flask import Flask, render_template, request, flash, url_for, session, redirect, abort

app = Flask(__name__)
app.config["SECRET_KEY"] = "asdasdasdasd9879a87sdas8d97"

menu = [
        {"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"},
]


@app.route("/")
def index():
    return render_template("index.html", menu=menu)


@app.route("/about")
def about():
    return render_template("about.html", title="О Сайте", menu=menu)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template("page404.html", title="Страница не найдена", menu=menu), 404


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        # print(request.form) # отбираем словать формы
        # print(request.form["username"]) # обращаемся по ключу
        if len(request.form["username"]) > 2:
            flash("Сообщение отправлено", category="success")
        else:
            flash("Ошибка отправки", category="error")

    return render_template("contact.html", title="Обратная связь", menu=menu)


@app.route("/login", methods=["GET", "POST"])
def login():
    if "userLogged" in session:
        return redirect(url_for("profile", username=session["userLogged"]))
    elif request.method == "POST" and request.form["username"] == "Black" and request.form["psw"] == "123":
        session["userLogged"] = request.form["username"]
        return redirect(url_for("profile", username=session["userLogged"]))
    return render_template("login.html", title="Авторизация", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    if "userLogged" not in session or session["userLogged"] != username:
        abort(401)
    return f"Профиль пользователя {username}"


if __name__ == "__main__":
    app.run(debug=True)
