from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the home page route
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html', prediction=None, input_data=None)
    elif request.method == 'POST':
        # Get input data from the form
        state = request.form['state']
        season = request.form['season']
        area = float(request.form['area'])
        
        # Perform one-hot encoding for state and season
        input_df = pd.DataFrame(columns=[
            'State_Andaman and Nicobar Islands', 'State_Andhra Pradesh', 'State_Arunachal Pradesh',
            'State_Assam', 'State_Bihar', 'State_Chandigarh', 'State_Chhattisgarh', 'State_Dadra and Nagar Haveli',
            'State_Daman and Diu', 'State_Delhi', 'State_Goa', 'State_Gujarat', 'State_Haryana', 'State_Himachal Pradesh',
            'State_Jammu and Kashmir ', 'State_Jharkhand', 'State_Karnataka', 'State_Kerala', 'State_Madhya Pradesh',
            'State_Maharashtra', 'State_Manipur', 'State_Meghalaya', 'State_Mizoram', 'State_Nagaland', 'State_Odisha',
            'State_Puducherry', 'State_Punjab', 'State_Rajasthan', 'State_Sikkim', 'State_Tamil Nadu', 'State_Telangana ',
            'State_THE DADRA AND NAGAR HAVELI AND DAMAN AND DIU', 'State_Tripura', 'State_Uttar Pradesh', 'State_Uttarakhand',
            'Season_Kharif','Season_Autumn', 'Season_Rabi','Season_Total', 'Season_Summer', 'Season_Winter','Season_WholeYear'
        ])
        
        input_df.loc[0] = 0  # Set all values to 0 initially
        
        # Set the selected state and season to 1
        input_df.loc[0, f'State_{state}'] = 1
        input_df.loc[0, f'Season_{season}'] = 1

        # Concatenate the area value with the one-hot encoded features
        input_data = np.concatenate((input_df.values, np.array([[area]])), axis=1)

        # Make predictions using the loaded model
        prediction = model.predict(input_data)[0]

        # Pass the prediction and input data to the template for rendering
        return f"{prediction}"

if __name__ == '__main__':
    app.run(debug=True)
