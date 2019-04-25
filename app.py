from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def getForm():
   return render_template('my-form.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      campus = request.form['campus']
      
      time = request.form['time']
      
      amOrPm = request.form['amOrPm']
      
      # send these three variables into the search method which returns an array
      # then send the array of building-room numbers into render_template
      return render_template("result.html",campus = campus, time = time, amOrPm = amOrPm)

if __name__ == '__main__':
   app.run(debug = True)