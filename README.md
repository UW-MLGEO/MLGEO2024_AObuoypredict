# MLGEO2024_AObuoypredict
Autumn 2024 project to predict buoy positions in the Arctic Ocean

**Contributors**: Ben Cohen, Rudra Singh, Jinsu Jang, Erin Davis

Contact: bencohen@uw.edu, rsingh34@uw.edu, davise12@uw.edu, jjs9904@uw.edu

## Motivation
The dynamics of the Arctic Ocean environment are complex and variable. [The International Arctic Buoy Programme (IABP)](https://iabp.apl.uw.edu/) is a collaborative effort to deploy and maintain a network of drifting buoys in the Arctic Ocean to collect oceanographic and meteorological data that support research for a variety of applications. While the buoys can provide real-time and historical information on their location and in-situ environment, predicting the motion of these drifting buoys is challenging. 

Accurate forecasts of buoy positions would be useful for a number of reasons: Imaging the features buoys are deployed on is of great interest to researchers of various disciplines. Recent developments in satellite imaging technology and the industry surrounding the practice have allowed researchers unprecedented access to high-resolution, on-demand imagery products. However, these satellite imaging frameworks necessarily operate under the restrictions inherent to orbital intstrumentation - namely the need for advance (>24hrs) determination of areas of interest for instruments to target. Without an accurate prediction of where features of interest coincident with buoy deployments will be, accurate satellite imaging regresses to guesswork. Failed captures are not only monetarily expensive, but also temporally expensive as icebergs are inherently transient, impermanent features. Furthermore, as climate change continues to affect the distribution and longevity of sea ice in the Arctic, ship traffic has increased dramatically. Forecasts of iceberg positions would provide ship operators with information that could serve to avoid collisions or other hazardous situations. Finally, predictions of buoy positions would contribute to the understanding of the force-balance dynamics that affect icebergs of various sizes and origins, especially as this project evolves and more climate metrics are added to the data ecosystem.

## Data used in this project
### Buoy data
The IABP oeprates a network of ~100 buoys in the Arctic Ocean. To use as training data, buoys that reported in 2024 were selected and their datastreams interpolated with MERRA-2 weather reanalysis data. This project also queries the IABP API to collect real-time buoy positions for use as initial conditions for prediction.

### Reanalyses
NCEP ftp://ftp.cdc.noaa.gov/Datasets/ncep/


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

### Collecting and manipulating project data
Scripts shoud be used in the following order:
1. download_data.ipynb

   -This notebook handles downloading data of various types for this project, including: past buoy data, weather reanalyses, weather forecasts, and current buoy positions.

   -Data will be stored in the data/raw folder.
2. data_cleaning.ipynb

   -This notebook cleans the buoy data for use in later steps.

   -The script removes rows with missing values, transmissions outside of the study area of interest, standardizes the latitude and longitude fields, and removes buoy tracks with less than 50 rows (these are assumed to have failed or been destroyed)

   -The resulting files will be stored in the data/cleaned directory.
3. prepare_ai_ready_data.ipynb

   -This notebook manipulates the buoy and weather data for use in model training and prediction.

   -The weather reanalyses are converted into numpy/pandas arrays and encoded with the proper values for day of year, etc.
4. eda.ipynb

   -This notebook performs some exploratory data analysis on the buoy and weather data to provide insights into trends, correlations, and potential data issues.

### Data access
API key file (should go in top level folder): 
https://drive.google.com/file/d/1o8u7ZBOuwydCDieQRjXQM6VDswB3ngR-/view?usp=drive_link

The API key file should be stored in highest level of your local folder for this repo

Wind data (these should go in data/raw/reanalyses/ERA5):
https://drive.google.com/file/d/1fzJLpbSXRI0Nn2Sq5brIHj0zCpMdTEpX/view?usp=drive_link

https://drive.google.com/file/d/1Y1I-BWPc10n0EIydsoINcT7uwTwWNFZd/view?usp=drive_link

Buoy data (should go in top level folder):
https://drive.google.com/file/d/1oHp-1rz8KltO6OpzMyp2Syq5Wy6DIhmM/view?usp=sharing
