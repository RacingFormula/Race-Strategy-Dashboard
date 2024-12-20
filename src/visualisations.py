import matplotlib.pyplot as plt
import io
import base64

def plot_live_telemetry(data):
    plt.figure()
    plt.plot(data['Time'], data['Speed'], label='Speed')
    plt.xlabel('Time (s)')
    plt.ylabel('Speed (km/h)')
    plt.legend()
    plt.grid()

    # Convert the plot to a base64 string
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()
