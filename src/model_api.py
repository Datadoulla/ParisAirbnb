from flask import Flask, request, render_template
from tools.request_funct import continuous_var, neighbour_dummies, property_dummies, room_dummies, request_data


from tools.predict import model_predict

app = Flask(__name__, template_folder='templates')

@app.route('/', methods = ['GET', 'POST'])
def index():
    meth = request.method
    if meth == 'GET':
        return render_template('hi.html')
    else:
        bathrooms = float(request.form['bathrooms'])
        accommodates = float(request.form['accommodates'])
        bedrooms = float(request.form['bedrooms'] )
        neighbour = request.form['neighbourhood']
        property = request.form['property_type'] 
        room = request.form['room_type']
        
        dt = request_data(bathrooms, accommodates, bedrooms, neighbour, property, room)
        
        lt = {'bathrooms':bathrooms, 'accommodates':accommodates, 'bedrooms':bedrooms, 
              'neighbour':neighbour, 'property':property, 'room':room}
        
        #predict = model_predict(dt)
        
        return  model_predict(dt) 




if __name__ == '__main__':
    app.run(debug=True)