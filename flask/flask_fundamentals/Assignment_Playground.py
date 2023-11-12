from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html') 

@app.route('/boxwithNumber/<num>')
def boxwithNumber(num):
    num  = int(num)
    return render_template('index2.html',num = num ) 

@app.route('/boxwithcolor/<num>/<color>')
def boxwithcolor(num,color):
    num  = int(num)
    return render_template('index3.html',num = num, color = color )  
    
if __name__=="__main__":
    app.run(debug=True) 