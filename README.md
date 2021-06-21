# Global Prosperity Projects

Humanity has experienced tremendous growth over the past two centuries due to the power of innovation in different areas such as medicine, business and engineering. This immense growth has led us to live in a very prosperous era. Different organizations have sought to collect data in order to examine prosperity. Gapminder has collected 200 years' worth of data on human progress. The Heritage Foundation has focused more on collecting data centered around economic progress. Finally, the United Nations has also developed data related to human development. Datasets from these sources were combined to form a new dataset. This novel dataset has mulitple features that describe countries' attributes and performance. These features can be called indicators.

This is a repository for analyzing the indicators that lead to prosperity in nations. Different indicators shall be examined in terms of how they relate to one another, and how different nations/continents perform with respect to these variables.

### Coding Platforms/Technologies
Here are some platforms that will be used to analyze and explore the datasets to extract crucial insights. 
* Tableau
* R
* Python
* pandas
* seaborn
* streamlit

## Data Collection & Wrangling

Data was collected from The Heritage Foundation, Gapminder Foundation and the United Nations. Then, the datasets were wrangled to have a better understanding of them using Python and R. The reasoning behind utilizing both R and Python was to get the experience of using both platforms for Data Wrangling. Using R, it was possible to create a new dataset called New_world.csv. This dataset was created by combining both the economic freedom data from Heritage Foundation and the progress data from the Gapminder Foundation. Then, python was used to wrangle the datasets to create a new dataset called World_data.csv. The main difference between New_world.csv and World_data.csv is that World_data.csv includes the United Nations' indicators' datasets. World_data.csv was thoroughly wrangled to ensure that all the important information was captured. This ensured that we had a comprehensive dataset. While building the World_data.csv dataset, certain countries were removed because they were not found in other datasets. Some of these countries are Hong Kong, Swaziland, The Bahamas, Democratic Republic of Congo, Republic of Congo, Laos, Kyrgyz Republic, The Gambia, Macau, Eswatini, Taiwan and Liechtenstein.

## Exploratory Data Analysis

Graphs were created by using both ggplot2 on R and seaborn on Python. The usage of both systems proved that Python was a more flexible approach for creating charts because it was possible to easily create versatile functions for generating graphs on Jupyter Notebooks. The graphs created on both platforms can be viewed in the Exploratory Data Analysis files in the repository. Building charts were not enough to display the relationships. Hence, Tableau was leveraged to create dashboards that made it easy to interact with the charts. Some of these dashboards reflected different countries' progress over the past 24 years while others focused more on continental comparison. You can check out these dashboards on Tableu public via this link.

## Web development

The final phase of the project involved the creation of a website use of python packages such as pandas, streamlit, seaborn and matplotlib. With the use of heroku, it was possible to complete the web application. The web application makes it possible for visitors to use drop-down menus and sliders to interact with the charts. One of its major feature is how different indicators vary with one other during a specific year. It also allows visitors to see how continents differ in terms of different indicators. Finally, it provides visitors with the ability to see how a certain country has performed over time according to an indicator. The website can be accessed  [here](https://global-prosperity.herokuapp.com/).

### Contact Info
* Mubarak Ganiyu
  - Incoming Graduate Student, Vanderbilt University Data Science Institute 
  - mubarak.a.ganiyu@vanderbilt.edu
* Kenneth Konam
  - Chemical Engineering Student, Vanderbilt University
  - kenneth.g.konam@vanderbilt.edu

#### Relevant Sources
- '2021 Index of Economic Freedom,' The Heritage Foundation. [Online]. Available: https://www.heritage.org/index/
- 'Download the Data,' Gapminder Foundation. [Online]. Available: https://www.gapminder.org/data/
- 'Human Development Reports,' United Nations Development Programme. [Online]. Available: http://hdr.undp.org/en/data
