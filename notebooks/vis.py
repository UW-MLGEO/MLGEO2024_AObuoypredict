import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import os

def create_simple_plot(pred_data, model_name):
    plt.figure(figsize=(15, 10))
    
    # Randomly select 5 unique buoys
    unique_buoys = pred_data['BuoyID'].unique()
    selected_buoys = np.random.choice(unique_buoys, min(5, len(unique_buoys)), replace=False)
    
    # Color palette for different buoys
    colors = ['blue', 'red', 'green', 'purple', 'orange']
    
    # Plot each selected buoy's trajectory
    for idx, buoy_id in enumerate(selected_buoys):
        buoy_data = pred_data[pred_data['BuoyID'] == buoy_id]
        
        # Calculate sampling rate
        sample_size = max(1, len(buoy_data) // 100)
        data_to_plot = buoy_data.iloc[::sample_size]
        
        # Plot true trajectory
        plt.plot(data_to_plot['True Longitude'], data_to_plot['True Latitude'],
                '-', color=colors[idx], label=f'Buoy {buoy_id} - True',
                linewidth=2)
        
        # Plot predicted trajectory
        plt.plot(data_to_plot['Predicted Longitude'], data_to_plot['Predicted Latitude'],
                '--', color=colors[idx], label=f'Buoy {buoy_id} - Predicted',
                linewidth=2)
        
        # Add start and end points
        plt.plot(buoy_data['True Longitude'].iloc[0], buoy_data['True Latitude'].iloc[0],
                'o', color=colors[idx], markersize=12, label=f'Buoy {buoy_id} - Start')
        plt.plot(buoy_data['True Longitude'].iloc[-1], buoy_data['True Latitude'].iloc[-1],
                's', color=colors[idx], markersize=12, label=f'Buoy {buoy_id} - End')
    
    plt.grid(True, alpha=0.3)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title(f'{model_name} - Trajectory Overview (5 Random Buoys)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Save plot
    output_dir = os.path.join(os.getcwd(), 'MLGEO2024_AObuoypredict', 'data', 'processed', 'prediction_plots')
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, f'{model_name}_simple.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()

def plot_trajectory_comparison(pred_data, model_name):
    create_simple_plot(pred_data, model_name)

def process_predictions():
    prediction_dir = os.path.join(os.getcwd(), 'MLGEO2024_AObuoypredict', 'data', 'processed', 'predictions')
    print(f"Looking for predictions in: {prediction_dir}")
    
    model_types = ['best_dl_model_predictions', 'CNN', 'RNN', 'FCN']
    
    for model_type in model_types:
        pattern = os.path.join(prediction_dir, f'{model_type}*.csv')
        prediction_files = glob.glob(pattern)
        print(f"Found {len(prediction_files)} files for {model_type}")
        
        for pred_file in prediction_files:
            try:
                print(f"Processing: {pred_file}")
                pred_data = pd.read_csv(pred_file)
                # Process data to get only required columns
                required_cols = ['BuoyID', 'True Latitude', 'True Longitude', 'Predicted Latitude', 'Predicted Longitude']
                pred_data = pred_data[required_cols]
                plot_trajectory_comparison(pred_data, model_type)
                print(f"Successfully created plots for {model_type}")
            except Exception as e:
                print(f"Error processing {pred_file}: {str(e)}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    os.chdir(project_root)
    print(f"Working directory: {os.getcwd()}")
    
    # Set random seed for reproducibility
    np.random.seed(42)
    process_predictions()