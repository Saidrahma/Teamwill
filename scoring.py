from flask import Flask, request, render_template
from random import random
from flask import jsonify

import json
from json import JSONEncoder
from numpy import mean

app = Flask(__name__)

class Customer:
        Id = "1"
        Name ='Customer'
        Values = "value"
        Score = "score"
        Eligibility = "yes"

def trader(taille):
  Traders = []
  for i in range(taille):
    value = random()
    Traders.append(value)
  return Traders

def Eligible(score):
  if score > 0.6 :
    return "yes"
  return "no"


def clients(Customers_number):
  list = []
  for i in range(Customers_number):
    C = Customer() 
    list.append(C)
  return list

class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__    


@app.route('/api/customer/' , methods=['GET','POST'])
def customer():
    c=clients(7)
    for i in range(len(c)):
        setattr(c[i], 'Id', i)
        setattr(c[i], 'Name', c[i].Name+str(i))
        setattr(c[i], 'Values', trader(10))
        setattr(c[i], 'Score', mean(c[i].Values))
        setattr(c[i], 'Eligibility', Eligible(c[i].Score))
        print(c[i].Score)
        print(c[i].Eligibility)   
    return json.dumps(c, indent=4, cls=MyEncoder)



@app.route('/api/test/')
def test():
    customers = {
        'id': '1',
        'Name': 'Customer 1',
        'Values': trader(10),
        'Score': "score(customers[Values])",
        'Eligibility': "yes/no"
    }, {
        'id': 2,
        'Name': 'Customer 2',
        'Values': trader(10),
        'Score': "degrés Celcius",
        'Eligibility': "yes/no"
    }
    return jsonify(customers)

if __name__ == "__main__" :
  app.run(debug=True)
