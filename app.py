from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    chart_data_1 = {
        'labels': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
        'datasets': [{
            'data': [50, 70, 120, 80, 30],
            'backgroundColor': ['#33b0ff', '#0089DE', '#2E5292', '#7AF7FA', '#B4E2F6']
        }]
    }

    chart_data_2 = {
        'labels': ['Leisure', 'Hobby', 'Work'],
        'datasets': [{
            'data': [25, 5, 70],
            'backgroundColor': ['#ff5733', '#33ff57', '#2E5292']
        }]
    }

    return render_template('index.html', chart_data_1=chart_data_1, chart_data_2=chart_data_2)

if __name__ == '__main__':
    app.run(debug=True)
