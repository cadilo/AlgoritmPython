from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

app = Flask(__name__)

@app.route('/')
def home():
    file_path = ('C:/Users/volod/PycharmProjects/Lab4_Yar/.venv/weatherHistory.csv')
    data = pd.read_csv(file_path)

    x = data[['Temperature (C)', 'Humidity', 'Wind Speed (km/h)']]
    y = data['Apparent Temperature (C)']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    model = linear_model.LinearRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    mse = mean_squared_error(y_test, y_pred)

    data_visual = x_test.copy()
    data_visual['Predicted Apparent Temperature (C)'] = y_pred

    plt.switch_backend('agg')
    sns.pairplot(data_visual, x_vars=['Temperature (C)', 'Humidity', 'Wind Speed (km/h)'],
                 y_vars=['Predicted Apparent Temperature (C)'], kind='reg', plot_kws={'line_kws': {'color': 'black'}})
    plt.savefig('static/output.png')

    return render_template('index.html', mse=mse)


@app.route('/predict', methods=['POST'])
def predict():
    file_path = "C:/Users/volod/PycharmProjects/Lab4_Yar/.venv/weatherHistory.csv"
    data = pd.read_csv(file_path)

    x = data[['Temperature (C)', 'Humidity', 'Wind Speed (km/h)']]
    y = data['Apparent Temperature (C)']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    model = linear_model.LinearRegression()
    model.fit(x_train, y_train)

    temperature = float(request.form.get('temperature'))
    humidity = float(request.form.get('humidity'))
    windspeed = float(request.form.get('windspeed'))

    prediction = model.predict([[temperature, humidity, windspeed]])

    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
