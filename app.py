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

      # cast hour and minutes to ints for the search method
      # convert to military time
      if amOrPm == "pm":
         newHour = int(hour) + 12
      else:
         newHour = int(hour)

      newMinutes = int(minutes)

      # rooms = search(campus, day, newHour, newMinutes)
      rooms = ["AB1", "AB2", "AB3", "AB4", "AB5", "AB6", "AB7", "AB8"]


      return render_template("result.html",campus = campus, day = day, hour = hour, minutes = minutes, amOrPm = amOrPm, rooms = rooms)

if __name__ == '__main__':
   app.run(debug = True)