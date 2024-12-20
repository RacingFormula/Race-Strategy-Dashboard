import os
import sys

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_handler import load_telemetry_data
from src.visualisations import plot_live_telemetry
from src.strategy_tools import calculate_strategy
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data_file = os.path.join(base_dir, 'data', 'example_telemetry.csv')
    
    
    telemetry_data = load_telemetry_data(data_file)
    live_plot = plot_live_telemetry(telemetry_data)
    strategy_insights = calculate_strategy(telemetry_data)
    return render_template('dashboard.html', live_plot=live_plot, insights=strategy_insights)

if __name__ == '__main__':
    app.run(debug=True)
