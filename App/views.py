from flask import Blueprint, request, render_template, g, current_app
from flask.json import jsonify
from flask_cache import Cache

from App.models import  Collect, db, Movie

blue = Blueprint('blue',__name__)
#当运行服务器的时候 会报错from flask.ext.cache import make_template_fragment_key
#ImportError: No module named 'flask.ext'
#解决方法  修改 flask-cache  jinja2ext.py中的flaks.ext.cache为flask_cache

cache = Cache(config={'CACHE_TYPE':'simple'})

@blue.route('/')
@cache.cached(timeout=30)
def hello():
    print('大家不是很兴奋')
    return '没想到 今天都是周四了'

#在浏览器的地址栏上输入一个请求 携带2个参数  分别是userid 和 movie_id 去查询有没有collect对象
@blue.route('/get/')
def get():
    user_id = request.args.get('user_id')
    movie_id = request.args.get('movie_id')

    print(user_id)
    print(movie_id)
    collect = Collect.query.filter_by(c_user = user_id).filter_by(c_movie = movie_id)

    if collect.count() > 0:
        return '您已经添加了 自己去修改数量吧  好不好'

    collect = Collect()
    collect.c_user = user_id
    collect.c_movie = movie_id

    db.session.add(collect)
    db.session.commit()
    return '真的添加成了'

'''
从数据库中查找每一页的数据 然后显示

视图函数   要获取数据  然后传送给页面
页面负责遍历

'''

@blue.route('/index/')
def index():
    #page是要查询的页码  问题？page从哪里获得
    page = int(request.args.get('page',1))
    #思考该方法的返回值类型 然后观察该类有什么方法
    pagination = Movie.query.paginate(page,5,False)

    return render_template('index.html',pagination=pagination)

@blue.route('/getcache/')
def getcache():
    #获取请求的主机 也就是ip
    key = request.remote_addr + 'user'
    #查看缓存中有没有ip
    value = cache.get(key)
    if value:
        return '先别访问了 我大哥来了'

    cache.set(key,'呵呵大',timeout=20)
    return '欢迎再来'


@blue.route('/dage/')
def dage():
    print(g.ip)
    print('大哥大哥你好吗')
    return '123'

# @blue.before_request
# def dasao():
#     #下面这个ip如何传到dage这个方法中  g.xxx代表全局变量
#     g.ip = request.remote_addr
#     # print('大嫂大嫂你好吗')
@blue.route('/getconfig/')
def getconfig():

    #config在页面中可以直接获取  但是在python文件中 需要使用current_app.config来获取
    print(current_app.config)
    return render_template('index1.html')

@blue.route('/getjson/')
def getjson():
    data={
        'msg':'ok',
        'status':'200',
        'scorelist':[100,90,99,101]

    }
    #return是不可以直接返回json的 必须使用jsonify方法  然后才可以相应
    return jsonify(data)


@blue.route('/a/')
def a():
    return render_template('scoreList.html')





