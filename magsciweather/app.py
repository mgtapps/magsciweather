from flask import Flask, render_template, redirect, url_for, request,send_from_directory, after_this_request,send_file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager,UserMixin, login_user,login_required,logout_user,current_user
import datetime
from datetime import date
from sqlalchemy  import and_
#from sqlalchemy import Numeric
from pws import hash_password, verify_password
import os
import io
import random
import psycopg2
import numpy as np
import down_load as d_l
#from down_selection import mdown_load
from werkzeug.utils import secure_filename
from move_file import move
from psycopg2 import sql
from date_order import bubble_sort
import csv
from flask import Response
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from totals_averages import tots_avgs
from totals_averages_t import tots_avgs_t
from max_temp import max_t


#DATABASE_URL = os.environ['postgres://nybovfojkjifgh:e89820859d0c94d32352df6983a69175693dbb7a8c2f6d8b53919ab15780a816@ec2-54-90-13-87.compute-1.amazonaws.com:5432/d3blce017stk7m']

#conn = psycopg2.connect(DATABASE_URL, sslmode='require')
connection = psycopg2.connect(user="postgres",password="mdms33!",host="127.0.0.1",port="5432",database="magsci_w4")
cur = connection.cursor()

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

    
    
app = Flask(__name__)

app.config['DEBUG']= False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mdms33!@localhost:5432/magsci_w4'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mdms33!@localhost:5432/Magsci_data'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://nybovfojkjifgh:e89820859d0c94d32352df6983a69175693dbb7a8c2f6d8b53919ab15780a816@ec2-54-90-13-87.compute-1.amazonaws.com:5432/d3blce017stk7m'
app.config['SECRET_KEY']='thisisasecret'

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app,db)


#db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.init_app(app)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), unique=True)
    user_password = db.Column(db.String(200),unique=True)
    magsci_datas = db.relationship('Magsci_data', backref='owner')
    
class Magsci_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rain = db.Column(db.Numeric(10,3),nullable=True)
    date_created = db.Column(db.Date, default=date.today())
    month = db.Column(db.String(20),nullable=True)
    temperature = db.Column(db.Numeric(10,3),nullable=True)
    owner_id = db.Column(db.Integer,db.ForeignKey('user.id'))
 

    
    

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        
        name = request.form['nam']
        password = request.form['pw']
        if name =='administrator1':
            user = User.query.filter_by(user_name=name).first()
            s_pw = user.user_password
            if s_pw ==password:
                login_user(user)
                return render_template(('input_search.html'))
        else:
            user =User.query.filter_by(user_name=name).first()
            if user!=None:
                s_pw = user.user_password
                if verify_password(s_pw,password):

                    login_user(user)
                    return render_template(('input_search.html'))
                else:    

                    return render_template(('index.html'))
            else:    

                return render_template(('index.html'))
    else:    

            return render_template(('index.html'))



@app.route('/input_search',methods=['GET','POST'])
@login_required
def input_search():
    d_name = {1 :"january", 2 :"february", 3 :"march", 4 :"april", 5 :"may", 6 :"june", 7 :"july", 8 :"august", 9 :"september", 10 :"october", 11 :"november", 12 :"december"}
    if request.method == 'POST':
        
        rain = request.form['rain']
        
        temperature = request.form['temperature']
        date = request.form.get("date")
        if (rain == "" or temperature == "" )or date == "" :
            return redirect('/input_link')
        else:
            shelf_num = int(date[5]+date[6])
            shelf =d_name[shelf_num] 
            #print(shelf, date)
            new_record = Magsci_data(rain= rain,temperature=temperature,month = shelf, date_created = date, owner_id = current_user.id)
        
            try:
                db.session.add(new_record)
                db.session.commit()

                return redirect('/input_search')

            except:
                return 'There was an issue adding your task'

    elif request.method =='GET':
        s = str(request.args.get('s')).lower()
        c_t = request.args.get('c_t')
        t_mp = request.args.get('t_mp')
        #d_ss = str(request.args.get('d_ss')).lower()
        
        
        if c_t =="":
            shelfs=[]
            if s!="":
                i=int(0)
                for each in current_user.magsci_datas:
                    
                    month = current_user.magsci_datas[i].month
                    if month == s:
                        shelfs.append(each)
                    i=i+1
                    
            elif t_mp!="":
                i=int(0)
                for each in current_user.magsci_datas:
                    
                    temperature = float(current_user.magsci_datas[i].temperature)
                    t_mp = float(t_mp or 0)
                    if temperature == t_mp:
                        shelfs.append(each)
                    i=i+1
            else:
                shelfs = current_user.magsci_datas
                
        else:
            shelfs=[]
            i= int(0)
            for each in current_user.magsci_datas:
                
                    rain = float(current_user.magsci_datas[i].rain)
                    c_t = float(c_t or 0)
                    if rain == c_t:
                        shelfs.append(each)
                    i=i+1
         
        
                    
    return render_template('input_search.html',shelfs = shelfs)


    date = request.form.get("datepicker")


@app.route("/reverse_list", methods=['GET','POST'])
@login_required
def reverse_list():
    shelfs = current_user.magsci_datas
    def reverse_list(mylist):
        return [ele for ele in reversed(mylist)]
    my_shelfs = reverse_list(shelfs)
    shelfs = my_shelfs[:3]


    return render_template('input_search.html',shelfs = shelfs)

@app.route("/list_all", methods=['GET','POST'])
@login_required
def list_all():
    #shelfs = current_user.magsci_datas
    cur.execute("""SELECT * FROM magsci_data WHERE owner_id=%s;""",[current_user.id])
    data_s = cur.fetchall()
    #connection.commit()
    
    data_s = bubble_sort(data_s)
    connection.commit() 
    
    return render_template('input_search.html',data_s = data_s)

@app.route('/modify',methods=['GET','POST'])
@login_required
def modify():
    if request.method =='GET':
        s = str(request.args.get('s')).lower()
        c_t = request.args.get('c_t')
        t_mp = request.args.get('t_mp')
        d_t = request.args.get('d_t')
        if d_t != "":
            yyyy =int(d_t[0]+d_t[1]+d_t[2]+d_t[3])
            mm = int(d_t[5]+d_t[6])
            dd = int(d_t[8]+d_t[9])
            d_t =datetime.date(yyyy,mm,dd)
        
        
        
        if c_t =="":
            dshelfs=[]
            if s!="":
                i=int(0)
                for each in current_user.magsci_datas:
                    
                    month = current_user.magsci_datas[i].month
                    if month == s:
                        dshelfs.append(each)
                    i=i+1
                    
            elif t_mp!="":
                i=int(0)
                for each in current_user.magsci_datas:
                    
                    temperature = float(current_user.magsci_datas[i].temperature)
                    t_mp = float(t_mp or 0)
                    if temperature == t_mp:
                        dshelfs.append(each)
                    i=i+1
                    
            elif d_t!="":
                #print("d_t ",d_t,"d_t data type:",type(d_t))
                i=int(0)
                for each in current_user.magsci_datas:
                    
                    date_created = (current_user.magsci_datas[i].date_created)
                    #t_mp = float(t_mp or 0)
                    if date_created == d_t:
                        dshelfs.append(each)
                    i=i+1
                    
            
            
            else:
                dshelfs = current_user.magsci_datas
                
        else:
            dshelfs=[]
            i= int(0)
            for each in current_user.magsci_datas:
                
                    rain = float(current_user.magsci_datas[i].rain)
                    c_t = float(c_t or 0)
                    if rain == c_t:
                        dshelfs.append(each)
                    i=i+1
            
                    
    return render_template('input_search.html',dshelfs = dshelfs)



@app.route('/delete/<int:id>')
@login_required
def delete(id):
    task_to_delete = Magsci_data.query.get_or_404(id)
    
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/input_search')
    except:
        return 'There was a problem deleting that task'



@app.route('/delete_all')
def delete_all():
    cur.execute("""DELETE FROM magsci_data WHERE owner_id=%s;""",[current_user.id])
    connection.commit()
    return render_template('input_search.html')





@app.route('/down_load', methods=['GET','POST'])
@login_required
def down_load():
    
    
    shelfs = current_user.magsci_datas
    num =len(shelfs)
    data = [[]]
    i=0
    for i in range(num):
        row =[]
        rain=shelfs[i].rain
        row.append(float(rain))
        temp=shelfs[i].temperature
        row.append(float(temp))
        month=shelfs[i].month
        row.append(month)
        date_created = shelfs[i].date_created
        row.append(date_created)
        data.append(row)
        i= i+1
    #print("data",data)
    m_dir = os.getcwd()
    my_dir = str(m_dir + '\data_files')
    file_name_o= str("weather_data.csv")
    fname = os.path.join(my_dir, file_name_o)
    file_o = open(fname,'w',encoding='UTF8')
    writer = csv.writer(file_o)
    writer.writerows(data)

    #file_d.close()
    file_o.close()
    if request.method =='GET':
        d_ll = str(request.args.get('d_ll')).lower()
        if d_ll =="down":
            response= send_file(fname, as_attachment=True)
            
            return response

    return render_template('download.html', file= fname)
    #return send_from_directory(my_dir,fname)


@app.route('/re_load')
def re_load():

    #print("resetting")
    shelfs = current_user.magsci_datas
    num =len(shelfs)
    data = [[]]
    i=0
    for i in range(num):
        row =[]
        rain=0.0
        row.append(float(rain))
        temp=0.0
        row.append(float(temp))
        month=''
        row.append(month)
        date_created = '00/00/0000'
        row.append(date_created)
        data.append(row)
        i= i+1
    #print("data",data)
    m_dir = os.getcwd()
    my_dir = str(m_dir + '\data_files')
    file_name_d= str("weather_data.csv")
    fname_d = os.path.join(my_dir, file_name_d)
    file_d = open(fname_d,'w',encoding='UTF8')
    writer = csv.writer(file_d)
    writer.writerows(data)

    #file_d.close()
    file_d.close()

    return render_template('input_search.html',file=fname_d)
    

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    dshelf = Magsci_data.query.get_or_404(id)
    if request.method == 'POST':
        dshelf.rain = request.form['rain']
        dshelf.date_created = request.form['date']
        dshelf.temperature = request.form['temperature']
        dshelf.month = request.form['month']
        
        try:
            db.session.commit()
            return redirect('/input_search')
        except:
            return 'there was an issue updating your shelf'
    else:
        return render_template('update.html', dshelf=dshelf)
    
@app.route('/search_delete',methods=['GET','POST'])
@login_required
def search_delete():
    start_date = ""
    end_date =""
    data = []
    #print("start_date before get",start_date, type(start_date))
    
    if request.method =='GET':
        start_date = request.args.get('start_date')
        #option = request.args.get('question')

        if start_date != "":
            yyyy =int(start_date[0]+start_date[1]+start_date[2]+start_date[3])
            mm = int(start_date[5]+start_date[6])
            dd = int(start_date[8]+start_date[9])
            start_date =datetime.date(yyyy,mm,dd)

            end_date = request.args.get('end_date')    

            if end_date != "":
                yyyy =int(end_date[0]+end_date[1]+end_date[2]+end_date[3])
                mm = int(end_date[5]+end_date[6])
                dd = int(end_date[8]+end_date[9])
                end_date =datetime.date(yyyy,mm,dd)
        
                cur.execute("""SELECT * FROM magsci_data WHERE owner_id=%s AND date_created >= %s AND date_created <= %s;""",(current_user.id, start_date, end_date))
                data= cur.fetchall()
                data = bubble_sort(data) 


                connection.commit()
        #num =len(data)
        #print("data   :",data)

    return render_template('search_delete.html', data=data,start_date = start_date, end_date = end_date)
    

    
    
@app.route("/analysis")
def analysis():
    cur.execute("""SELECT * FROM magsci_data WHERE owner_id=%s;""",[current_user.id])
    data= cur.fetchall()
    connection.commit()
    
    num =len(data)
    result, year = tots_avgs(data)
    result_t, year_t, max_temp_data = tots_avgs_t(data)
    #print("result_t ",result_t)
    
           
    
        
    return render_template('stats.html', result = result, year = year, result_t = result_t, year_t = year_t, max_temp_data=max_temp_data)

@app.route("/stats_d")
def stats_d():
    cur.execute("""SELECT * FROM magsci_data WHERE owner_id=%s;""",[current_user.id])
    data= cur.fetchall()
    connection.commit()
    year = datetime.date.today().year
    this_month= datetime.date.today().month
    date_now= datetime.date.today()
    
    
    return render_template('stats_d.html',data = data, year = year)

@app.route('/delete_some/<start_date>/<end_date>')
def delete_some(start_date, end_date):
    
    
    cur.execute("""DELETE FROM magsci_data WHERE owner_id=%s AND date_created >= %s AND date_created <= %s;""",(current_user.id, start_date, end_date))
    connection.commit()
    return render_template('search_delete.html')



@app.route("/plot.png")
def plot_png():
    cur.execute("""SELECT * FROM magsci_data WHERE owner_id=%s;""",[current_user.id])
    data= cur.fetchall()
    connection.commit()
    result, year = tots_avgs(data)
    
    xs = []
    ys = []
    
    for row in result:
        xs.append(row[0])
        ys.append(row[1]) # total
        #y2s.append(row[2]) # average
    title = 'Monthly totals' 
    x_ax = 'Month'
    y_ax = 'Rainfall/mm'
    fig = create_figure(xs,ys,title,x_ax,y_ax)
    #fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route("/plot1.png")
def plot1_png():
    cur.execute("""SELECT * FROM magsci_data WHERE owner_id=%s;""",[current_user.id])
    data= cur.fetchall()
    connection.commit()
    result, year = tots_avgs(data)
    
    xs = []
    ys = []
    
    for row in result:
        xs.append(row[0])
        #ys.append(row[1]) # total
        ys.append(row[2]) # average
    title = 'Monthly averages' 
    x_ax = 'Month'
    y_ax = 'Rainfall/mm'
    fig = create_figure(xs,ys,title,x_ax,y_ax)
    #fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure(xs,ys,title,x_ax,y_ax):
    fig = Figure()
    axis = fig.add_subplot(111)
    axis.bar(xs, ys)
    
    axis.set_title(title)
    axis.set_xlabel(x_ax)
    axis.set_ylabel(y_ax)
    
    axis.set_xticklabels(xs,rotation = 90)
    return fig

  

@app.route("/input_link")
def input_link():
    return render_template('input_data.html') 

@app.route("/search_link")
def search_link():
    return render_template('search_data.html')

@app.route("/modify_link")
def modify_link():
    return render_template('modify_data.html')
    
@app.route("/test_link")
def test_link():
    return render_template('index.html')

@app.route("/statsd_link")
def statsd_link():
    return render_template('stats_d.html')

@app.route("/stats_link")
def stats_link():
    return render_template('stats.html')

@app.route("/sd_link")
def ss_link():
    return render_template('search_delete.html')


    
    
@app.route("/admin", methods=['GET','POST'])
@login_required
def admin():
    
    if current_user.user_name == 'new_admin':
        users = User.query.all()
        return render_template(('admin.html'),users = users)
        
    
    
    return render_template(('admin.html'),users = users)

    
    
    
@app.route('/update_user/<int:id>',methods=['GET','POST'])
@login_required
def update_user(id):
    this_user = User.query.get_or_404(id)
    if request.method == 'POST':
       
        new_password =request.form['password']
        new_password = hash_password(new_password)
        this_user.user_password = new_password
        
        try:
            db.session.commit()
            return redirect('/admin')
        except:
            return 'there was an issue updating this user'
    else:
        return render_template('update_user.html',this_user=this_user)
    
@app.route('/delete_user/<int:id>')
@login_required
def delete_user(id):
    user_to_delete =User.query.get_or_404(id)
    
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        return redirect('/admin')
    except:
        return 'There was a problem deleting that user'
    
    

    
@app.route("/profile", methods=['GET','POST'])
@login_required
def profile():
    users=[]
    user = current_user
    users.append(user)
        
    
    
    return render_template(('profile.html'),users = users)

@app.route('/change_password',methods=['GET','POST'])
def change_password():
    user = current_user
    if request.method == 'POST':
        new_password =request.form['password']
        new_password = hash_password(new_password)
        user.user_password = new_password
        
        try:
            db.session.commit()
            return render_template('profile.html',user=user)
        except:
            return 'there was an issue updating your password'
    else:
        return render_template('change_password.html')
    



@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name =request.form['user_name']
        password = request.form['user_password']
        password = hash_password(password)
        new_record = User(user_name = name,user_password = password)
        if new_record!= None:
            try:

                db.session.add(new_record)
                db.session.commit()
                return redirect('/register')
                
                

            except:
                return 'There was a problem adding your details'
    else:
        return render_template(('register.html'))
    



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template(('index.html'))

#connection.close()
   
if __name__ == '__main__':
    
    
    
    app.run()
    