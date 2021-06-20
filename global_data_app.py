import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns; sns.set(style="dark")

df_world = pd.read_csv("Great_data.csv", encoding = "latin1")
indicator_list = ['Life Expectancy', 'Income', 'Population', 'Economic Freedom Index',
                  'Property Rights', 'Government Integrity', 'Judicial Effectiveness', 'Tax Burden',
                  'Government Spending', 'Fiscal Health', 'Business Freedom',
                  'Labor Freedom', 'Monetary Freedom', 'Trade Freedom',
                  'Investment Freedom', 'Financial Freedom', 'Income Index',
                  'Expected years of Schooling', 'Education Index',
                  'Human Development Index']
def run():
    st.set_page_config(layout="wide")
    st.title("Global Prosperity Projects")
    st.write("Humanity has experienced tremendous growth over the past two centuries due to the power of innovation in different areas such as medicine, business and engineering. This immense growth has led us to live in a very prosperous era. Different organizations have sought to collect data in order to examine prosperity.")
    st.write("Gapminder has collected 200 years' worth of data on human progress. The Heritage Foundation has focused more on collecting data centered around economic progress. Finally, the United Nations has also developed data related to human development. Datasets from these sources were combined to form a new dataset. This novel dataset has mulitple features that describe countries' attributes and performance. These features can be called indicators.")
    st.write("Some countries were ommitted from the dataset during data collection because there was not enough data on them. These countries are Hong Kong, Swaziland, The Bahamas, Democratic Republic of Congo, Republic of Congo, Laos, Kyrgyz Republic, The Gambia, Macau, Eswatini, Taiwan and Liechtenstein.")
   
    from PIL import Image
    image = Image.open("worldmap-countries-hd.jpg")
    st.image(image, use_column_width=True,
             caption="Photo credit: https://www.freeworldmaps.net/printable/")
    st.header("Global Analysis Charts")
    st.write("Below are different charts showcasing how the indicators fare against each other and how countries/continents perform according to the indicators")
    st.write("Note: Data on some indicators are missing for some years. Hence, the charts will be blank for those years.")
    
    st.subheader("Indicators' Comparison")
    st.write("This is a chart showcasing how different indicators fare against one another in a specific year.")
    st.write("Use the drop-down menus and the slider below to interact with the chart.")
    indicator1 = st.selectbox("Indicator 1", indicator_list, 3)
    indicator2 = st.selectbox("Indicator 2", indicator_list, 19)
    year1 = st.slider("Year", 1995, 2019, 2010, 1)
    df = df_world[df_world["Year"] == year1]
    fig, ax = plt.subplots(figsize=(16,8))
    sns.scatterplot(x=indicator1, y=indicator2, data=df, hue="Continent", palette='deep')
    ax.set_title("%s vs %s in %d" % (indicator2,indicator1, year1), fontsize=15)
    ax.set_xlabel(indicator1)
    ax.set_ylabel(indicator2)
    st.pyplot(fig)

    st.subheader("Continents' Comparison")
    st.write("This chart highlights the disparities between continents based on different indicators in a specific year.")
    st.write("Use the drop-down menu and the slider below to interact with the chart.")
    indicator3 = st.selectbox("Indicator", indicator_list, 3)
    year2 = st.slider("Year", 1995, 2019, 2008, 1)
    df2 = df_world[df_world["Year"] == year2]
    fig2, ax2 = plt.subplots(figsize=(16, 8))
    sns.boxplot(x="Continent", y=indicator3, data=df2, hue="Continent", palette="deep")
    ax2.set_title("How Continents differ in terms of %s in %d" %(indicator3, year2), fontsize=15)
    ax2.set_xlabel("Continent")
    ax2.set_ylabel(indicator3)
    st.pyplot(fig2)

    st.subheader("Countries' Progress")
    st.write("This chart provides a proper insight into how a country has changed over a given period of time according to an indicator.")
    st.write("Use the drop-down menus below to interact with the chart.")
    indicator4 = st.selectbox("Indicator", indicator_list, 16)
    country1 = st.selectbox("Country", list(df_world["Country"].unique()))
    df3 = df_world[df_world["Country"] == country1]
    fig3, ax3 = plt.subplots(figsize=(16, 8))
    sns.lineplot(x="Year", y=indicator4, style="Country", markers="o", hue = "Continent", palette = "deep", data=df3)
    ax3.set_title("%s changes over time in %s" % (indicator4, country1), fontsize=15)
    ax3.set_xlabel("Year")
    ax3.set_ylabel(indicator4)
    ax3.legend().set_visible(False)
    st.pyplot(fig3)

    st.subheader("Relevant Sources")
    st.write("\'2021 Index of Economic Freedom,\' The Heritage Foundation. [Online]. Available: https://www.heritage.org/index/")
    st.write("\'Download the Data,\' Gapminder Foundation. [Online]. Available: https://www.gapminder.org/data/")
    st.write("\'Human Development Reports,\' United Nations Development Programme. [Online]. Available: http://hdr.undp.org/en/data")
if __name__ == "__main__":
    run()

