from flask import Flask,render_template,request

app=Flask(__name__)
@app.route("/")
def welcome():
    return "<html><H1>welcome to the flasj course</H1></html>"
@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')
@app.route("/about")
def about():
    return render_template('about.html')
@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')
@app.route("/success/<int:score>")
def success(score):
    res=""
    if score>=50:
        res="pass"
    else:
        res="fail"
    return render_template('results.html',results=res)
@app.route("/successress/<int:score>")
def successress(score):
    res = ""
    if score >= 50:
        res = "pass"
    else:
        res = "fail"
    exp = {'score': score, "res": res}
    return render_template('result1.html', results=exp)


if __name__=="__main__":
    app.run(debug=True)
