#!/usr/bin/python

from flask import Flask, render_template, request, redirect, url_for
from sense_hat import SenseHat

app = Flask(__name__)
sense = SenseHat()


@app.route('/')
def main():
    ftemp = round((sense.get_temperature()*9)/5+32)
    humid = round(sense.get_humidity())

    return render_template('index.html', temp=ftemp, humid=humid)

@app.route('/scroll',methods=['POST'])
def scroll():
    scroll_text=request.form['text']
    if len(scroll_text) > 0:
        sense.show_message(scroll_text, text_colour=[255, 0, 0])
    return redirect(url_for("main"))

@app.route('/clear')
def clear():
    sense.clear()
    return redirect(url_for("main"))

if __name__ == '__main__':
      app.run(debug=True,host='0.0.0.0', port=80)
