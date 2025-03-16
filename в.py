from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def index1():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index2():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def index3():
    a = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
         "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    return '</br>'.join(a)


@app.route('/promotion_image')
def return_promotion_image():
    return f'''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" 
                        rel="stylesheet" 
                        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" 
                        crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/i.webp')}"> 
                    <br>Вот она какая, красная планета.
                    <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                     Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-danger" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Присоединяйся!
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def image_mars():
    if request.method == 'GET':
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" 
                            rel="stylesheet" 
                            integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" 
                            crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Анкета претендента</h1>
                        <h2>на участие в миссии</h2>
                        <div>
                            <form class="login_form" method="post" enctype="multipart/form-data">
                                <input class="form-control" placeholder="Введите фамилию" name="firstname">
                                <input class="form-control" placeholder="Введите имя" name="lastname">
                                <br>
                                <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                <div class="form-group">
                                    <label for="classSelect">Какое у Вас образование?</label>
                                    <select class="form-control" id="classSelect" name="class">
                                      <option>Начальное</option>
                                      <option>Среднее</option>
                                      <option>Высшее</option>
                                    </select>
                                 </div>
                                 <br>Какие у Вас есть профессии?</br>
                                 <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="prof" name="prof">
                                    <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                    <br><input type="checkbox" class="form-check-input" id="prof" name="prof1">
                                    <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                                    <br><input type="checkbox" class="form-check-input" id="prof" name="prof2">
                                    <label class="form-check-label" for="acceptRules">Пилот</label>
                                    <br><input type="checkbox" class="form-check-input" id="prof" name="prof3">
                                    <label class="form-check-label" for="acceptRules">Метеоролог</label>
                                    <br><input type="checkbox" class="form-check-input" id="prof" name="prof4">
                                    <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label>
                                    <br><input type="checkbox" class="form-check-input" id="prof" name="prof5">
                                    <label class="form-check-label" for="acceptRules">Инженер по радиационной защите</label>
                                    <br><input type="checkbox" class="form-check-input" id="prof" name="prof6">
                                    <label class="form-check-label" for="acceptRules">Врач</label>
                                    <br><input type="checkbox" class="form-check-input" id="prof" name="prof7">
                                    <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                </div>
                                <br>
                                <div class="form-group">
                                    <label for="form-check">Укажите пол</label>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                      <label class="form-check-label" for="male">
                                        Мужской
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                      <label class="form-check-label" for="female">
                                        Женский
                                      </label>
                                    </div>
                                </div>
                                <br>
                                <div class="form-group">
                                    <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                    <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                </div>
                                <div class="form-group">
                                    <label for="photo">Приложите фотографию</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                        </div>
                      </body>
                    </html>'''
    elif request.method == 'POST':
        print(request.form.get('firstname', "Не заполнено"))
        print(request.form.get('lastname', "Не заполнено"))
        print(request.form.get('email', "Не заполнено"))
        print(request.form.get('class', "Не заполнено"))
        print(request.form.get('file', "Не заполнено"))
        print(request.form.get('about', "Не заполнено"))
        print(request.form.get('accept', "Не заполнено"))
        print(request.form.get('sex', "Не заполнено"))
        print(request.form.get('prof', "Не заполнено"))
        print(request.form.get('prof1', "Не заполнено"))
        print(request.form.get('prof2', "Не заполнено"))
        print(request.form.get('prof3', "Не заполнено"))
        print(request.form.get('prof4', "Не заполнено"))
        print(request.form.get('prof5', "Не заполнено"))
        print(request.form.get('prof6', "Не заполнено"))
        print(request.form.get('prof7', "Не заполнено"))
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def image_marss(planet_name):
    return f'''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Варианты выбора</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                </head>
                <body>
                    <h1>Мое предложение:{planet_name}</h1>
                    <br>Эта планета близка к земле;</br>
                    <div class="alert alert-success" role="alert">
                        На ней много необходимых ресурсов;
                    </div>
                    <div class="alert alert-light" role="alert">
                        На ней есть вода и атмосфера;
                    </div>
                    <div class="alert alert-warning" role="alert">
                        На ней есть небольшое магнитное поле;
                    </div>
                    </div><div class="alert alert-danger" role="alert">
                      Наконец, она просто красива!
                    </div>
                </body>
                </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def return_results(nickname, level, rating):
    return f'''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Title</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                </head>
                <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}</h2>
                    <div class="alert alert-success" role="alert">
                      Поздравляем! Ваш рейтинг после {level} отбора
                    </div><div class="alert alert-light" role="alert">
                      составляет {rating}
                    </div><div class="alert alert-warning" role="alert">
                      Желаем удачи!
                    </div>
                </body>
                </html>'''


@app.route('/sample_file_upload', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                             <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                            <h1>Загрузим файл</h1>
                            <form class="file_upload" method="post" enctype="multipart/form-data">
                               <div class="form-group">
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <img src="{url_for('static', filename='img/i1.webp')}"  width='300' height='300'>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f1 = request.files['file']
        map_file = "static/img/map.webp"
        with open(map_file, "wb") as file:
            file.write(f1.read())
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                             <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                            <h1>Загрузим файл</h1>
                            <form class="file_upload" method="post" enctype="multipart/form-data">
                               <div class="form-group">
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <img src="{url_for('static', filename='img/map.webp')}"  width='300' height='300'>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''


@app.route('/landscapes', methods=['POST', 'GET'])
def landscapes():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                          <h1>Пейзажи Марса</h1>
                            <div id="carouselExampleIndicators" class="carousel slide">
                              <div class="carousel-indicators">
                                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
                              </div>
                              <div class="carousel-inner">
                                <div class="carousel-item active">
                                  <img src="{url_for('static', filename='img/5364131058980874098.jpg')}" class="d-block w-100" alt="...">
                                </div>
                                <div class="carousel-item">
                                  <img src="{url_for('static', filename='img/5364131058980874099.jpg')}" class="d-block w-100" alt="...">
                                </div>
                                <div class="carousel-item">
                                  <img src="{url_for('static', filename='img/5364131058980874100.jpg')}" class="d-block w-100" alt="...">
                                </div>
                              </div>
                              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Previous</span>
                              </button>
                              <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Next</span>
                              </button>
                            </div>
                        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
                        </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')