from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

def checkerBoard():
    return render_template ('index4.html',  rows = 8, columns = 8) 

@app.route('/<int:rows>')
def checkerBoardRows(rows):
    return render_template ('index4.html', rows = int(rows), columns = 8)

@app.route('/<int:rows>/<int:columns>')
def checkerBoardRowsandColumns(rows,columns):
    return render_template ('index4.html', rows = int(rows), columns = int(columns))

if __name__=="__main__":
    app.run(debug=True)



