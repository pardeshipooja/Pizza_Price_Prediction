from flask import Flask, request, jsonify, render_template
from utils import PizzaPrice
import config

app = Flask(__name__)

@app.route('/')
def home1():
    
    return render_template('pizza_price.html')



@app.route('/predictcharges', methods = ['GET', 'POST'])
def predict_charges():

    if request.method == 'GET':
        data = request.args.get
        print("Data :",data)
        
        # company = data("company_labels")
        # diameter = eval(data('diameter'))
        # topping = data('topping_labels')
        # variant = data('variant_labels')
        # size = data('size_labels')
        # extra_sauce = data('extra_sauce_labels')
        # extra_cheese = data ('extra_cheese_labels')

        company = data("company")
        diameter = eval(data('diameter'))
        topping = data('topping')
        variant = data('variant')
        size = data('size')
        extra_sauce = data('extra_sauce')
        extra_cheese = data ('extra_cheese')
       
        Obj = PizzaPrice(company,diameter,topping,variant,size,extra_sauce,extra_cheese)
        pred_price = Obj.get_predicted_price()
        
        return render_template('pizza_price.html', prediction = pred_price)

    elif request.method == 'POST':
        data = request.form
        print("Data :",data)
       
        # company = data["company_labels"]
        # diameter = data['diameter']
        # topping = data['topping_labels']
        # variant = data['variant_labels']
        # size = data['size_labels']
        # extra_sauce = data['extra_sauce_labels']
        # extra_cheese = data ['extra_cheese_labels']


        company = data["company"]
        diameter = eval(data['diameter'])
        topping = data['topping']
        variant = data['variant']
        size = data['size']
        extra_sauce = data['extra_sauce']
        extra_cheese = data ['extra_cheeses']
        
        Obj = PizzaPrice(company,diameter,topping,variant,size,extra_sauce,extra_cheese)
        pred_price = Obj.get_predicted_price()
        
        return render_template('pizza_price.html', prediction = pred_price)

    return jsonify({"Message" : "Unsuccessful"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER)
