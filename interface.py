from flask import Flask,render_template,request,jsonify
import config
from utils import Placement
import traceback

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/prediction",methods=["get","post"])
def prediction():
    if request.method == "post":
        data = request.form.get
        print(data)        
        gender = data("gender")
        print(gender)
        ssc_p = eval(data("ssc_p"))
        ssc_b = data("ssc_b")
        hsc_p = eval(data("hsc_p"))
        hsc_b = data("hsc_b")
        hsc_s = data("hsc_s")
        degree_p = eval(data("degree_p"))
        degree_t = data("degree_t")
        workex = data("workex")
        etest_p = eval(data("etest_p"))
        specialisation = data("specialisation")
        mba_p = eval(data("mba_p"))
        place =Placement()
        pred = place.get_prediction(gender,ssc_p,ssc_b,hsc_p,hsc_b,hsc_s,degree_p,degree_t,workex,etest_p,specialisation,mba_p)
        return render_template("index.html",prediction = pred) 
    else:
        data = request.args.get
        print(data)        
        gender = data("gender")
        print(gender)
        ssc_p = eval(data("ssc_p"))
        ssc_b = data("ssc_b")
        hsc_p = eval(data("hsc_p"))
        hsc_b = data("hsc_b")
        hsc_s = data("hsc_s")
        degree_p = eval(data("degree_p"))
        degree_t = data("degree_t")
        workex = data("workex")
        etest_p = eval(data("etest_p"))
        specialisation = data("specialisation")
        mba_p = eval(data("mba_p"))
        place =Placement()
        pred = place.get_prediction(gender,ssc_p,ssc_b,hsc_p,hsc_b,hsc_s,degree_p,degree_t,workex,etest_p,specialisation,mba_p)
        return render_template("index.html",prediction = pred) 

              
    
        

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5007)
     
