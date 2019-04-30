from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def getForm():
   return render_template('my-form.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      campus = request.form['campus']

      day = request.form['day']
      
      hour = request.form['hour']

      minutes = request.form['minutes']
      
      amOrPm = request.form['amOrPm']

      rooms = ["AB1", "AB2", "AB3", "AB4", "AB5", "AB6", "AB7", "AB8"]

      # send these three variables into the search method which returns an array
      # then send the array of building-room numbers into render_template
      return render_template("result.html",campus = campus, day = day, hour = hour, minutes = minutes, amOrPm = amOrPm, rooms = rooms)

if __name__ == '__main__':
   app.run(debug = True)