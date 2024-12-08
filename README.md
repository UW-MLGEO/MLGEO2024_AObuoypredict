# MLGEO2024_AObuoypredict
Autumn 2024 project to predict buoy positions in the Arctic Ocean.

**Contributors**: Ben Cohen, Rudra Prakash Singh, Jinsu Jang, Erin Davis

Contact: bencohen@uw.edu, rsingh34@uw.edu, davise12@uw.edu, jjs9904@uw.edu

## Motivation  

The Arctic Ocean's dynamic environment presents unique challenges. The [International Arctic Buoy Programme (IABP)](https://iabp.apl.uw.edu/) deploys and maintains a network of drifting buoys to collect critical oceanographic and meteorological data. However, predicting buoy motion remains a key challenge.  

### Why Accurate Forecasts Matter:  
- **Satellite Imaging**:  
  - High-resolution satellite imagery requires advance targeting (>24 hours).  
  - Accurate buoy forecasts prevent wasted resources on missed captures of transient features like icebergs.  

- **Arctic Navigation**:  
  - Increased ship traffic due to climate change heightens collision risks.  
  - Forecasting buoy and iceberg positions improves safety for vessels.  

- **Climate Research**:  
  - Tracking buoy movement aids in studying iceberg dynamics and the forces affecting them.  
  - Contributes to understanding climate-driven changes in sea ice distribution and longevity.  

## High-Level Overview of Machine Learning Aspect
**ML Model Selection Methodology**
![Machine Learning Model Selection Methodology](https://github.com/UW-MLGEO/MLGEO2024_AObuoypredict/blob/main/visualizations/ml_process_vis.png)

**Hyperparameter Tuning Process**
![Tuning Process](https://github.com/UW-MLGEO/MLGEO2024_AObuoypredict/blob/main/visualizations/tuning%20process_vis.png)

## Data used in this project
### Buoy data
This project used the complete set of drifting buoy data collected and provided by the IABP.

**Data Cleaning Pipeline**
![Data Visualization](https://github.com/UW-MLGEO/MLGEO2024_AObuoypredict/blob/main/visualizations/data_cleaning.png)

### Reanalyses
This project used the ERA5 surface winds reanalysis products as environmental forcing variables.


## Using this repository
The contents of this repository can be used to collect, clean, and process geospatial data for use in training ML algorithms to predict buoy motion. Please refer to the license file for information on distribution and reproduction of this work. 
Use of resources in the following order is suggested:
### Cloning the repository and activating the environment
1. Clone the repository
```bash
git clone https://github.com/UW-MLGEO/MLGEO2024_AObuoypredict
```

2. Navigate to the repository locally
```bash
cd MLGEO2024_AObuoypredict
```

3. Create a conda environment
```bash
conda env create -n mlggeo2024_aobuoypredict -f environment.yml
```

4. Activate the conda environment
```bash
conda activate mlggeo2024_aobuoypredict
```

Your environment is now ready and activated!

### Notebook/script information
Scripts shoud be used in the following order:
1. download_data.ipynb

   -This notebook handles downloading data of various types for this project.

   -Data will be stored in the data/raw folder.
2. data_cleaning.ipynb

   -This notebook cleans the buoy data for use in later steps.

   -The script removes rows with missing values, transmissions outside of the study area of interest, standardizes the latitude and longitude fields, and removes buoy tracks with less than 50 rows (these are assumed to have failed or been destroyed)

   -The resulting files will be stored in the data/cleaned directory.
3. prepare_ai_ready_data.ipynb

   -This notebook manipulates the buoy and weather data for use in model training and prediction.
4. eda.ipynb

   -This notebook performs some exploratory data analysis on the buoy and weather data to provide insights into trends, correlations, and potential data issues.
5. modeltraining_hyperparameter.ipynb

  -This notebook implements a five-fold cross-validation model selection pipeline for classic machine learning architectures. 

  -Once the best model is selected, its hyperparameters are tuned using Optuna.

  -Once the best hyperparameters for the best performing model are selected, the tuned model is trained on the entire dataset with 5 buoys withheld for validation and evaluation of accuracy.
6. deep_learning.ipynb

  -This notebook implements a five-fold cross-validation model selection pipeline for deep learning architectures.

  -Due to computational contraints, hyperparameter tuning was not implemented in this context.

  -Once the best deep learning model is selected, the model is trainined on the entire dataset with 5 buoys withheld for validation and evaluation of accuracy.
7. vis.py

   -This script processes buoy trajectory prediction data, generating plots that compare the true and predicted positions for randomly selected buoys. It reads CSV files, extracts relevant columns, and creates visual comparisons for up to five buoys. The plots are saved in a specified directory.
8. prepare_ppt.ipynb
  
  -This notebook is/was used to prepare certain visualizations for use in presentations, summary documents, etc.

## Summary and Future Improvements

#### Summary
- **Objective**: The goal was to predict drifting buoy motion for Arctic research using classic ML and deep learning models, trained on IABP drifting buoy data and ERA5 wind reanalyses.
- **Results**:
  - Predictions showed acceptable accuracy for short trajectories.
  - For longer buoy paths, the accuracy decreased due to cumulative errors and environmental factors. Error propagation was a major issue.
  - The model's predictions were generally of poor quality for satellite imaging applications, but they form a solid foundation for future improvement.

#### Key Insights
- **Trajectory Length Impact**: 
  - Shorter trajectories had more accurate predictions.
  - Longer trajectories showed a drop in accuracy, especially for distances with complex environmental conditions.
- **Environmental Influences**: 
  - Predictions were probably affected by environmental factors like sea ice concentration, ocean currents, wind speed, and temperature gradients.
  - Seasonal changes, climate shifts, and fluctuating ocean currents also posed challenges to maintaining consistent accuracy.
- **Data Gaps**: 
  - The model's performance could be improved with more frequent measurements and better data processing techniques.
  
#### Future Directions for Improvement
- **Model Selection**: 
  - Test and implement additional classic ML and deep learning models for better accuracy.
- **Data Expansion**: 
  - Include data from other sources like IABP and ERA5 for a broader dataset.
- **Training Duration**: 
  - Extend training times for better model refinement.
- **Data Source Expansion**: 
  - Incorporate data from more buoy-deploying agencies and weather reanalyses.
- **Physical Laws**: 
  - Improve the PINN by incorporating more detailed physical laws to enhance model accuracy.
- **Forecasting**: 
  - Transition from using solely reanalysis data to including forecast data for improved prediction.