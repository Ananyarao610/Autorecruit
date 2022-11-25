import res
from turtle import heading
#from pure_eval import group_expressions
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, jsonify
import json
#from flask import Flask, flash, redirect, render_template, request, session, jsonify, request
from werkzeug.utils import secure_filename
import os
#global p
app = Flask(__name__)  


#app.config['UPLOADS'] = 'C:/Users/Ananya/OneDrive/Desktop/se/static/uploads'
#app.config['UPLOADS'] = 'D:/checkse/Autorecruit/static/uploads'
app.config['UPLOADS'] = 'C:\\Users\\Ananya\\OneDrive\\Desktop\\se_se_new\\Autorecruit\\static\\uploads'
#app.config['UPLOADS'] = '/home/ananya/Ananya/SE Project/Autorecruit/static/uploads'
@app.route("/coun")
def coun():
  return render_template("coun.html")

@app.route("/home")
def home1():
      return render_template("home.html")

@app.route("/")
def home():
  return render_template("home.html")  

@app.route("/about")
def about():
      return render_template("about.html")
  
@app.route("/resu")
def resu():
  #score=res.main[0]()
  #missing = res.main[1]()
  r = res.main()
  print("this is the tuple",r)
  score = r[0]
  missing = r[1]
  print("this is missing",missing)
  print("this is scoreeeeeeeeeee",score)
  return render_template("display.html", objs = score , miss=missing)  


@app.route("/upload", methods=['POST', 'GET'])
def upload():
  if request.method == "POST":
        pdf = request.files['file']
        if pdf.filename == '':
          print('Invalid')
          return redirect(request.url)
        filename = secure_filename(pdf.filename)
        
        print("this is file",filename)
        print("/static/uploads/"+filename)
        #t=f(filename)
        """
        if(filename != 'NULL'):
          print("i am in the if loop")
          return("/static/uploads/"+filename)    """
        global p 
        
        #p = "D:/checkse/Autorecruit/static/uploads/"+ filename
        #p = "/home/ananya/Ananya/SE Project/Autorecruit/static/uploads/"+ filename
        p = "C:\\Users\\Ananya\\OneDrive\\Desktop\\se_se_new\\Autorecruit\\static\\uploads\\" +filename

        basedir = os.path.abspath(os.path.dirname(__file__))
        pdf.save(os.path.join(basedir, app.config["UPLOADS"], filename))
        #return("/static/uploads/"+filename)
        print("before 2nd return")
        return render_template("display.html",new_p = p)
  #return("/static/uploads/"+filename)
  print("before 3rd return")
  return render_template("display.html")




def f():
   #p="/static/uploads/"+l
   #global p
   print("i am in func f",p)
   return p       


if __name__=='__main__':
  app.run(debug=True,port=5000)