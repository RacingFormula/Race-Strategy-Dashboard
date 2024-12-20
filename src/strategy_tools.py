def calculate_strategy(data):
    avg_speed = data['Speed'].mean()
    projected_lap_time = data['Time'].iloc[-1] / len(data['Lap'].unique())
    return {
        'average_speed': avg_speed,
        'projected_lap_time': projected_lap_time
    }
