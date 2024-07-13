import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from Pandas_project_end import modifc
data=modifc()
def intro():
    st.title("Superstore Analysis")
    st.write("""This project aims to leverage the capabilities of Pandas for data manipulation
             and analysis, combined with Streamlit for creating interactive and visually 
             appealing data-driven applications.\n
             Key Features:\n
             1.Data Loading and Cleaning: Importing data into Pandas, cleaning and 
             preprocessing as necessary.\n
             2.Visualization: Creating insightful plots and charts using Matplotlib or Plotly
             and seaborn to visualize data distributions, trends, and correlations.\n
             3.Hypothesis Testing: Formulating and testing hypotheses using statistical 
             methods available in Pandas.\n
             4.Interactive Web Interface: Building a multi-page Streamlit app with navigation
             to explore different aspects of the analysis, providing a user-friendly interface
             for exploring data insights.\n
             5.Documentation: Documenting data sources, analysis methodology, and findings to
             ensure transparency and reproducibility of results.
             """)
def hypo1():
    st.title("Hypothesis 1:Average profit by different segment customers ")
    st.write("Corporate segment customers identified by prefixes like DV generate higher average profits per order compared to other segments.")
    segm_grouped=data.groupby('Segment')['Profit'].mean().sort_values()
    fig, ax = plt.subplots()
    segm_grouped.plot(kind='bar',color=['blue','green','orange'])
    plt.title('Average profit by different segment customers')
    plt.xlabel('Segment')
    plt.ylabel('Profit')
    st.pyplot(fig)
    st.write("I grouped segment and mean of profit gained,sorted the values and plotted a bar graph to understand different segment customers profits gained.The conlusion was that home office have more profits, so the hypothesis was wrong.")
def hypo2():
    st.title("Hypothesis 2:Average duration by different shipping modes")
    st.write("Orders shipped via Standard Class have shorter shipping durations compared to Second Class, impacting customer satisfaction")
    shipmode_grp=data.groupby('Ship Mode')['Shipping Duration'].mean()
    fig, ax = plt.subplots()
    shipmode_grp.plot(kind='bar',color=['blue','green','orange','purple'])
    plt.title('Average duration by different shipping modes')
    plt.xlabel('ship mode')
    plt.ylabel('shipping duration')
    st.pyplot(fig)
    st.write("This time, I made a separate column shipping duration,grouped ship mode withit and plotted a bar graph. The conclusion was that standard class has shorter duration than second class.")
    

def hypo3():
    st.title("Hypothesis 3:Total sales and profit margin by different categories")
    st.write("Furniture products contribute significantly to total sales revenue but have lower profit margins compared to Office Supplies.")
    prsales_cate = data.groupby('Category').agg({'Sales': 'sum', 'Profit': 'mean'})
    fig, ax1 = plt.subplots()
    prsales_cate['Profit'].plot(kind='bar', ax=ax1, color='green', position=0, width=0.4)
    ax1.set_ylabel('Profit')
    ax1.set_xlabel('Category')
    ax1.set_title('Total Sales and Profit Margin by Different Categories')
    ax2 = ax1.twinx()
    prsales_cate['Sales'].plot(kind='bar', ax=ax2, color='blue', position=1, width=0.4)
    ax2.set_ylabel('Sales')
    st.pyplot(fig)
    st.write("with the visualisation we can conclude that furniture products contribute significantly to total sales revenue but have lower profit margins compared to Office Supplies.")

def hypo4():
    st.title("Hypothesis 4:Top 5 cities with highest average sales revenue")
    st.write("Jamestown has the highest amount of sales where as independence is 4th highest in terms of sales as compared to other cities.")
    citysal_grp=data.groupby('City')['Sales'].mean().nlargest(5)
    fig, ax = plt.subplots()
    citysal_grp.plot(kind='bar',color=['red','green','purple','orange','blue'])
    plt.title('Top 5 cities with highest average sales revenue ')
    plt.xlabel('City')
    plt.ylabel('Sales')
    st.pyplot(fig)
    st.write("we can conclude that Jamestown has the highest amount of sales where as independence is 4th highest in terms of sales as compared to other cities.")

def hypo5():
    st.title("Hypothesis 5:Profit margin recorded in different seasons")
    st.write("Moonsoon has the lowest recorded profit margin and the margin always declines in the start of year ")
    seaspr_grp=data.groupby('Seasons')['Profit'].mean()
    fig, ax = plt.subplots()
    seaspr_grp.plot(kind='bar',color=['red','green','purple','orange','blue'])
    plt.title('Profit margin recorded in different seasons')
    plt.xlabel('Seasons')
    plt.ylabel('Profit')
    st.pyplot(fig)
    data['Month'] = data['Order Date'].dt.to_period('M')
    sales_by_month = data.groupby('Month')['Profit'].sum()
    fig1, ax1 = plt.subplots()
    sales_by_month.plot(marker='o')
    plt.title('Total Profit by Month')
    plt.xlabel('Month')
    plt.ylabel('Total Profit')
    plt.grid(True)
    st.pyplot(fig1)
    st.write("we can conclude that Moonsoon has the lowest recorded profit margin and the margin always declines in the start of year")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Description", "Hypothesis 1", "Hypothesis 2", "Hypothesis 3", "Hypothesis 4", "Hypothesis 5"])

# Display the selected page
if page == "Description":
    intro()
elif page == "Hypothesis 1":
    hypo1()
elif page == "Hypothesis 2":
    hypo2()
elif page == "Hypothesis 3":
    hypo3()
elif page == "Hypothesis 4":
    hypo4()
elif page == "Hypothesis 5":
    hypo5()
             
             
             
             
             
             
             
             
             
             


