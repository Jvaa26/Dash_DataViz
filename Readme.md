# Geolocalization Dashboard
# This is a Python project that generates a web-based dashboard for exploring geolocalization data in Brazil. It uses the Dash framework for building the dashboard and Plotly for generating the visualizations.

# Project Structure
The project consists of the following files:

* app.py: The main script for running the Dash app.
* df_dados.csv: The dataset used for generating the visualizations.
* df_geo_api.csv: A dataset with geolocation data obtained from APIs.
* df_geo_estados.csv: A dataset with geographical data for Brazilian states.
* dataMaps.json: A GeoJSON file with geographical data for Brazilian states and municipalities.

# Installation
To run the project, you need to have Python 3.x installed on your machine, as well as the following Python packages:

* dash
* dash_bootstrap_components
* pandas
* plotly

You can install these packages by running the following command:
pip install dash dash_bootstrap_components pandas plotly

# Usage
To run the app, simply run the app.py script in a Python environment with the required packages installed. The app will start running on a local web server, and you can access it by navigating to the URL provided by the console output.

The dashboard allows you to select the Brazilian states you want to explore and shows you visualizations of the geolocation data for those states. You can also click on a state in the map to see more detailed information about that state.

# Contributing
This is an open-source project, and contributions are welcome. If you find a bug or have an idea for a new feature, please open an issue on the GitHub repository. If you want to contribute code, please fork the repository and submit a pull request with your changes.
