import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import glob
import os

def plot_trajectory_comparison(pred_data, model_name):
    # create_geographic_map(pred_data, model_name)
    create_simple_plot(pred_data, model_name)

# decided not to use because graphs got chaotic
def create_geographic_map(pred_data, model_name):
    plt.figure(figsize=(20, 5))
    ax = plt.axes(projection=ccrs.PlateCarree())
    
    # Add geographic features
    ax.add_feature(cfeature.LAND, facecolor='#f0f0f0', alpha=0.3)
    ax.add_feature(cfeature.OCEAN, facecolor='#e6f3ff', alpha=0.3)
    ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
    gl = ax.gridlines(draw_labels=True, linestyle='--', alpha=0.3)
    gl.top_labels = False
    gl.right_labels = False
    
    # Take first 100 points
    data_to_plot = pred_data
    
    # Plot trajectories
    ax.plot(data_to_plot['True Longitude'], 
            data_to_plot['True Latitude'],
            'b-', label='True Trajectory', 
            transform=ccrs.PlateCarree(),
            linewidth=2)
    
    ax.plot(data_to_plot['Predicted Longitude'], 
            data_to_plot['Predicted Latitude'],
            'r--', label='Predicted Trajectory', 
            transform=ccrs.PlateCarree(),
            linewidth=2)
    
    # Add markers
    ax.plot(data_to_plot['True Longitude'].iloc[0], 
            data_to_plot['True Latitude'].iloc[0],
            'go', markersize=12, label='Start',
            transform=ccrs.PlateCarree())
    
    ax.plot(data_to_plot['True Longitude'].iloc[-1], 
            data_to_plot['True Latitude'].iloc[-1],
            'ro', markersize=12, label='End',
            transform=ccrs.PlateCarree())
    
    # Set extent
    ax.set_extent([-180, 180, 0, 90], crs=ccrs.PlateCarree())
    
    plt.legend(loc='upper right', fontsize=10)
    plt.title(f'{model_name} - Prediction Results', pad=20, fontsize=12)
    
    # Save geographic map
    output_dir = os.path.join(os.getcwd(), 'MLGEO2024_AObuoypredict', 'data', 'processed', 'prediction_plots')
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, f'{model_name}_geographic.png'), 
                dpi=300, bbox_inches='tight', pad_inches=0.2)
    plt.close()

def create_simple_plot(pred_data, model_name):
    plt.figure(figsize=(15, 10))
    
    # Plot full dataset with sampling for clarity
    sample_size = max(1, len(pred_data) // 100)
    data_to_plot = pred_data.iloc[::sample_size]
    
    plt.plot(data_to_plot['True Longitude'], data_to_plot['True Latitude'],
             'b-', label='True Trajectory', linewidth=2)
    plt.plot(data_to_plot['Predicted Longitude'], data_to_plot['Predicted Latitude'],
             'r--', label='Predicted Trajectory', linewidth=2)
    
    # Add markers
    plt.plot(pred_data['True Longitude'].iloc[0], pred_data['True Latitude'].iloc[0],
             'go', markersize=12, label='Start')
    plt.plot(pred_data['True Longitude'].iloc[-1], pred_data['True Latitude'].iloc[-1],
             'ro', markersize=12, label='End')
    
    plt.grid(True, alpha=0.3)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title(f'{model_name} - Full Trajectory Overview ({len(pred_data)} points)')
    plt.legend()
    
    # Save simple plot
    output_dir = os.path.join(os.getcwd(), 'MLGEO2024_AObuoypredict', 'data', 'processed', 'prediction_plots')
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, f'{model_name}_simple.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()

def process_predictions():
    prediction_dir = os.path.join(os.getcwd(), 'MLGEO2024_AObuoypredict', 'data', 'processed', 'predictions')
    print(f"Looking for predictions in: {prediction_dir}")
    
    model_types = ['GradientBoosting', 'RandomForest', 'XGBoost', 'LightGBM', 'ElasticNet']
    
    for model_type in model_types:
        pattern = os.path.join(prediction_dir, f'{model_type}*.csv')
        prediction_files = glob.glob(pattern)
        print(f"Found {len(prediction_files)} files for {model_type}")
        
        for pred_file in prediction_files:
            try:
                print(f"Processing: {pred_file}")
                pred_data = pd.read_csv(pred_file)
                plot_trajectory_comparison(pred_data, model_type)
                print(f"Successfully created plots for {model_type}")
            except Exception as e:
                print(f"Error processing {pred_file}: {str(e)}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    os.chdir(project_root)
    print(f"Working directory: {os.getcwd()}")
    
    process_predictions()