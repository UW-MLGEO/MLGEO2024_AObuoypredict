# MLGEO2024_AObuoypredict
Autumn 2024 project to predict buoy positions in the Arctic Ocean

## Motivation
The dynamics of the Arctic Ocean environment are complex and variable. [The International Arctic Buoy Programme (IABP)](https://iabp.apl.uw.edu/) is a collaborative effort to deploy and maintain a network of drifting buoys in the Arctic Ocean to collect oceanographic and meteorological data that support research for a variety of applications. While the buoys can provide real-time and historical information on their location and in-situ environment, predicting the motion of these drifting buoys is challenging. 

Accurate forecasts of buoy positions would be useful for a number of reasons. Imaging the features buoys are deployed on is of great interest to researchers of various disciplines. Recent developments in satellite imaging technology and the industry surrounding the practice have allowed researchers unprecedented access to high-resolution, on-demand imagery products. However, these satellite imaging frameworks necessarily operate under the restrictions inherent to orbital intstrumentation - namely the need for advance (>24hrs) determination of areas of interest for instruments to target. Without an accurate prediction of where features of interest coincident with buoy deployments will be, accurate satellite imaging regresses to guesswork. Failed captures are not only monetarily expensive, but also temporally expensive as icebergs are inherently transient, impermanent features. Furthermore, as climate change continues to affect the distribution and longevity of sea ice in the Arctic, ship traffic has increased dramatically. Forecasts of iceberg positions would provide ship operators with information that could serve to avoid collisions or other hazardous situations. Finally, predictions of buoy positions would contribute to the understanding of the force-balance dynamics that affect icebergs of various sizes and origins.

## Data used in this project
### Buoy data
The IABP oeprates a network of ~100 buoys in the Arctic Ocean. To use as training data, buoys that reported in 2024 were selected and their datastreams interpolated with MERRA-2 weather reanalysis data. This project also queries the IABP API to collect real-time buoy positions for use as initial conditions for prediction.

### Reanalyses

## Using this repository
The contents of this repository can be used to collect, clean, and process geospatial data for use in training ML algorithms to predict buoy motion. 
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
