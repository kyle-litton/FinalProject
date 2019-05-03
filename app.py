from flask import Flask, render_template, request
from search import checkTime


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
      if amOrPm == "am" or hour == "12":
         newHour = int(hour)
      else:
         newHour = int(hour) + 12

      newMinutes = int(minutes)

      roomsAndLinks = checkTime(campus, day, newHour, newMinutes)
      


      return render_template("result.html",campus = campus, day = day, hour = hour, minutes = minutes, amOrPm = amOrPm, list = roomsAndLinks)

if __name__ == '__main__':
   app.run(debug = True)