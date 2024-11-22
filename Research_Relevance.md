# Research Relevance

This document outlines the relevance of the research conducted for the MLGEO2024 AObuoy prediction project.

## Abstract

The Arctic Ocean's dynamic environment makes predicting the movement of drifting buoys challenging, yet these buoys are essential for collecting oceanographic and meteorological data. This research aims to develop a machine learning model to accurately forecast buoy positions based on wind and ice conditions. Improved predictions will allow for accurate tasking of high-resolution satellite imagery, which requires advance targeting. By leveraging machine learning, this project seeks to optimize buoy tracking, reduce imaging costs, and contribute to a deeper understanding of Arctic environmental dynamics.


## Methods

- This problem is connected to **regression** because the goal is to develop a model that can continuously predict the buoy’s future position as a function of various environmental inputs (such as wind speed). Regression techniques will enable estimation the continuous trajectories of the buoys over time, thus providing precise location forecasts based on the training of available past buoy track data. By utilizing regression, the model can learn from the trajectories of past buoys and wind speed/direction leading to more accurate training predictions for buoy paths in dynamic Arctic conditions.

- The expected outcomes of applying machine learning to our buoy dataset include developing a model that predicts the buoy’s path based on wind surface wind conditions. Given the limited availability of labeled data, the project will likely benefit from a **semi-supervised or self-supervised** approach, where the model can leverage both labeled and unlabeled data to improve accuracy. This method allows for effective learning from smaller datasets while progressively enhancing performance as more data becomes available

## Expected Outcome & Impact

Applying **machine learning** techniques to our buoy dataset is anticipated to result in a predictive model capable of forecasting the buoy's trajectory based on varying wind and ice movement conditions. The model's successful development could enhance our understanding of environmental dynamics, leading to improved location predictions, monitoring, and more efficient satellite image capturing. This approach not only optimizes precise satellite image capturing but also holds potential for broader applications in marine research and operational forecasting, including management of risk derived from ice hazards, forecasting the location of certain ice features for in-situ investigation, and the overall understanding of how machine learning algorithms can be trained using drifting buoy data.

