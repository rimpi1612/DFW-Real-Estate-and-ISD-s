#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import all packages and libraries
import panel as pn
pn.extension('plotly')
import plotly.express as px
import requests
import pandas as pd
import hvplot.pandas
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
from dotenv import load_dotenv
import warnings
warnings.filterwarnings('ignore')
import statistics


# In[2]:


#MAPBOX_TOKEN 
load_dotenv()
mapbox_token = os.getenv("MAPBOX_TOKEN")


# In[3]:


#load csv and check data
isd_data = pd.read_csv("dfw_real_estate_isd.csv")
#isd_data.dropna(inplace = True) # dropna is dropping all rows
isd_data.shape


# In[4]:


#checking for null value
isd_data.isnull().any()


# In[5]:


# Count nulls 
isd_data.isnull().sum()


# In[6]:


#drop columns with all empty values
isd_data.drop(columns="grad_rate",inplace=True)
isd_data.drop(columns="dropout_rate",inplace=True)
#isd_data.head()


# In[8]:


#fill null column value with number.. 
isd_data["2016_median_property_value"]=isd_data["2016_median_property_value"].fillna(0)


# In[9]:


# check the shape
isd_data.shape


# In[10]:


isd_data.head()


# In[11]:


#isd_data.dtypes


# In[12]:


# Mean Income of the DFW Households
statistics.mean(isd_data['median_income_isd'])


# In[13]:


# Standard Deviation of Income in DFW Households
statistics.stdev(isd_data['median_income_isd'])


# In[14]:


# rating data frame 
isd_ranking_df =  isd_data[['district_name','county_name','district_rating_2019']]


# In[15]:


# rename the rating dataframe
isd_ranking_df = isd_ranking_df.rename(columns = {
    "district_rating_2019": "district_rating"
})


# In[16]:


# change the ranking with numeric value
isd_ranking_df.district_rating[isd_ranking_df.district_rating =='A'] =4
isd_ranking_df.district_rating[isd_ranking_df.district_rating =='B'] =3
isd_ranking_df.district_rating[isd_ranking_df.district_rating =='C'] =2
isd_ranking_df.district_rating[isd_ranking_df.district_rating =='D'] =1


# In[17]:


isd_ranking_df.head()


# In[18]:


# change rating datatype to numeric
isd_ranking_df['district_rating'] = pd.to_numeric(isd_ranking_df['district_rating']) 
isd_ranking_df.dtypes


# In[19]:


# DFW ISD Rating Percentage
group_count_isd = isd_ranking_df.groupby(['district_rating'])['district_name'].count().reset_index()
group_count_isd['Percentage'] = 100 * group_count_isd['district_name']  / group_count_isd['district_name'].sum()
group_count_isd


# In[20]:


# DFW ISD County Base Rating Percentage
group_count_isd = isd_ranking_df.groupby(['county_name','district_rating'])['district_name'].count().reset_index()
group_count_isd['Percentage'] = 100 * group_count_isd['district_name']  / group_count_isd['district_name'].sum()
group_count_isd


# In[75]:


# Sunburst of Rating of Each County


# In[76]:


fig_rate_collin =px.sunburst(
    isd_ranking_df[isd_ranking_df["county_name"] == "collin"],
    names='district_name',
    parents='county_name',
    values='district_rating',
    color='district_name',
    title = "School Rating By School District - Collin"
    
)
#fig_rate_collin.show()


# In[77]:


fig_rate_dallas =px.sunburst(
    isd_ranking_df[isd_ranking_df["county_name"] == "dallas"],
    names='district_name',
    parents='county_name',
    values='district_rating',
    color='district_name',
    title = "School Rating By School District - Dallas"
    
)


# In[78]:


fig_rate_denton =px.sunburst(
    isd_ranking_df[isd_ranking_df["county_name"] == "denton"],
    names='district_name',
    parents='county_name',
    values='district_rating',
    color='district_name',
    title = "School Rating By School District - Denton"
    
)


# In[79]:


fig_rate_tarrant =px.sunburst(
    isd_ranking_df[isd_ranking_df["county_name"] == "tarrant"],
    names='district_name',
    parents='county_name',
    values='district_rating',
    color='district_name',
    title = "School Rating By School District - Tarrant"
    
)


# In[83]:


fig_rate = pn.Row(fig_rate_collin,fig_rate_dallas,fig_rate_denton,fig_rate_tarrant)
#fig_rate


# In[84]:


# Sunburst of Avg. Tax Due of Each County


# In[85]:


fig_tax_collin =px.sunburst(
    isd_data[isd_data["county_name"] == "collin"],
    names='district_name',
    parents='county_name',
    values='2019_avg_annual_taxdue',
    color='district_name',
    title='Average Annual Tax Due - Collin County'
)
#fig_tax_collin


# In[86]:


fig_tax_denton =px.sunburst(
    isd_data[isd_data["county_name"] == "denton"],
    names='district_name',
    parents='county_name',
    values='2019_avg_annual_taxdue',
    color='district_name',
    title='Average Annual Tax Due - Denton County'
)


# In[87]:


fig_tax_dallas =px.sunburst(
    isd_data[isd_data["county_name"] == "dallas"],
    names='district_name',
    parents='county_name',
    values='2019_avg_annual_taxdue',
    color='district_name',
    title='Average Annual Tax Due - Dallas County'
)


# In[88]:


fig_tax_tarrant =px.sunburst(
    isd_data[isd_data["county_name"] == "tarrant"],
    names='district_name',
    parents='county_name',
    values='2019_avg_annual_taxdue',
    color='district_name',
    title='Average Annual Tax Due - Tarrant County'
)


# In[89]:


fig_tax = pn.Row(fig_tax_collin,fig_tax_dallas,fig_tax_denton,fig_tax_tarrant)
#fig_tax


# In[90]:


fig_sunburst = pn.Column(fig_rate,fig_tax)
#fig_sunburst


# In[91]:


# Top 20 City of highest median income isd 
top20_city = isd_data.groupby(['primary_city']).mean()
top20_city.sort_values(['median_income_isd'], ascending=False, inplace=True)
top20_city = top20_city.reset_index().head(20)
#top20_city


# In[96]:


# Top 20 District Rating with Median Houholds Income and Avg. Tax Due in Category Plot representation 
plot_category = px.parallel_categories(
    top20_city,
    dimensions=['primary_city', 'total_households_isd', 'district_rating_2019_num', 'median_income_isd','2019_avg_annual_taxdue'],
    color='median_income_isd',
    color_continuous_scale=px.colors.sequential.Inferno,
    labels={
        'primary_city': 'City',
        'median_income_isd': 'Median Income - ISD',
        'total_households_isd': 'Total House',
        'district_rating_2019_num': 'District Rating',
        '2019_avg_annual_taxdue':'Avg Annual Tax Due'
        },
    width=1000,
    title = 'Top 20 District Rating with Median Houholds Income and Avg. Tax Due'
)
#plot_category.show()


# In[97]:


# District Rating by City with Median Houholds Income and Avg. Tax Due in Tree representation 
fig_tree = px.treemap(isd_data, path=['primary_city', 'total_households_isd','2019_avg_annual_taxdue'], 
                    values='median_income_isd',
                      color='district_rating_2019_num', hover_data=['2019_avg_annual_taxdue'],
                      color_continuous_scale='RdBu',
                      color_continuous_midpoint=np.average(isd_data['district_rating_2019_num'], 
                      weights=isd_data['median_income_isd']),
                     title = "District Rating by City",
                     width=1000)
#fig_tree.show()


# In[102]:


# District Rating by City with Median Houholds Income and Avg. Tax Due in 3D Scatter representation 
scatter_3d=px.scatter_3d(isd_data,
             x="district_rating_2019_num",
             y="total_households_isd",
             z = "2019_avg_annual_taxdue",
             color= "primary_city",
             size = "median_income_isd"
            )
#scatter_3d


# In[99]:


#isd_2016_df =  isd_data[['district_name','county_name','2016_property_value_total', '2016_median_property_value','2016_isd_taxrate', '2016_avg_annual_taxdue']]


# In[100]:


#isd_2016_df["avg_annual_taxdue"]= isd_2016_df["avg_annual_taxdue"].str.replace(",", "")
#isd_2016_df["avg_annual_taxdue"]= isd_2016_df["avg_annual_taxdue"].str.replace("-", "")
#isd_2016_df["avg_annual_taxdue"]= isd_2016_df["avg_annual_taxdue"].str.replace("    ", "")
#isd_2016_df["avg_annual_taxdue"] = pd.to_numeric(isd_2016_df["avg_annual_taxdue"])
#isd_2016_df.dtypes


# In[101]:


#Median Household Income of Isd by County
scatter_plot = px.scatter(
    isd_data,
    x="median_income_isd",
    y="district_name", 
    size = "median_income_isd", 
    color = "county_name",
    hover_name = 'district_name',
    title= "Median Household Income of Isd by County"
)


# In[43]:


#scatter_plot


# In[103]:


isd_data_by_county = isd_data.groupby(['district_name','county_name']).mean().reset_index()
isd_data_by_county.head(10)


# In[104]:


#isd_data_by_county.hvplot.line(
#    "district_name",
#    "median_income_isd",
#    xlabel= "County Name",
#    ylabel="Income Value",
#    groupby="county_name",
#    rot=90,
#    width=1000,
#    height=800
#)


# In[52]:


# 5 years Property Value in Bar for each County
county_bar = isd_data_by_county.hvplot.bar(
    x='district_name', 
    y=['2016_median_property_value', '2017_median_property_value','2018_median_property_value','2019_median_property_value','2020_median_property_value'], 
    xlabel='District Name', 
    ylabel='Median Property Value', 
    groupby='county_name', 
    rot=90, 
    width=1500, 
    height=800
).opts(yformatter="%.0f")
#county_bar


# In[105]:


# TEA API Data 
#tea_url = "https://services2.arcgis.com/5MVN2jsqIrNZD4tP/arcgis/rest/services/School2020to2021/FeatureServer/0/query?where=1%3D1&outFields=Score,City,Postal,Country,DisplayX,DisplayY,Rank,Zip4,Phone,County_Nam,County_Num,Web_Addres,Performanc,Region&returnGeometry=false&outSR=4326&f=json"
#tea_url = "https://services2.arcgis.com/5MVN2jsqIrNZD4tP/arcgis/rest/services/School2020to2021/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
tea_url ="https://opendata.arcgis.com/datasets/059432fd0dcb4a208974c235e837c94f_0.geojson"


# In[106]:


def get_tea_data(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    response = requests.get(url,headers=headers)
    return response.json()['features']


# In[110]:


tea_data = get_tea_data(tea_url)

tea_list = []
for data in tea_data:
    tea_list.append(data['properties'])
df_tea = pd.DataFrame.from_dict(tea_list)
df_tea_filtered = df_tea.loc[(df_tea['County_Nam'] == 'COLLIN COUNTY') | (df_tea['County_Nam'] == 'DALLAS COUNTY') | (df_tea['County_Nam'] == 'DENTON COUNTY') | (df_tea['County_Nam'] == 'TARRANT COUNTY')]
df_tea_filtered = df_tea_filtered[["County_Nam","City","Score","District_1","X","Y","Zipcode5"]]
df_tea_filtered = df_tea_filtered.sort_values('County_Nam')
df_tea_filtered.dropna()
#df_tea_filtered.columns
df_tea_filtered.head()
#tea_data


# In[111]:


px.set_mapbox_access_token(mapbox_token)


# In[112]:


map_plot = px.scatter_mapbox(
    df_tea_filtered,
    lat="Y",
    lon="X",
    size="Score",
    color="Score",
    color_continuous_scale=px.colors.cyclical.Phase,
    hover_name="District_1",
    title="School Score of City",
    zoom=11
)
#map_plot.show()


# In[114]:


#map_plot


# In[143]:


# A representation of Citywise number of schools in DFW
import plotly.graph_objects as go
from plotly.subplots import make_subplots

freq = df_tea_filtered.City.value_counts().reset_index().rename(columns={"index": "x"})

# Initialize figure with subplots
fig = make_subplots(
    rows=2, cols=2,
    column_widths=[0.6, 0.4],
    row_heights=[0.4, 0.6],
    specs=[[{"type": "scattergeo", "rowspan": 2}, {"type": "bar"}],
           [            None                    , {"type": "surface"}]])

fig.add_trace(
    go.Scattergeo(lat=df_tea_filtered["Y"],
                  lon=df_tea_filtered["X"],
                  mode="markers",
                  hoverinfo="text",
                  showlegend=False,
                  marker=dict(color="crimson", size=4, opacity=0.8)),
    row=1, col=1
)

# Add City bar chart
fig.add_trace(
    go.Bar(x=freq["x"][0:10],y=freq["City"][0:10], marker=dict(color="crimson"), showlegend=False),
    row=1, col=2
)

# Add 3d surface  
fig.add_trace(
    go.Surface(z=df_tea_filtered["District_1"].values.tolist(), showscale=False),
    row=2, col=2
)

# Update geo subplot properties

fig.update_geos(
    visible=False, resolution=110, scope="usa",
    showcountries=True, countrycolor="WHITE",
    showsubunits=True, subunitcolor="Blue"
)


# Set theme, margin, and annotation in layout
fig.update_layout(
    template="plotly_dark",
    margin=dict(r=10, t=25, b=40, l=60),
    annotations=[
        dict(
            text="Source: TEA",
            showarrow=False,
            xref="paper",
            yref="paper",
            x=0,
            y=0)
    ]
)

#fig.show()


# In[161]:


# Import Library for SQL 
from sqlalchemy import create_engine
import psycopg2


# In[169]:


# Connect to Database rental_db 
engine = create_engine("postgresql+psycopg2://postgres:Fintech2021!@localhost:5432/rental_db")
query = "select * from isd_capita;"
capita_df = pd.read_sql(query,engine)


# In[170]:


# Texas School Districts Per Capita Rates 
capita_df.head()


# In[172]:


# Texas School Districts Per Capita Rates 1949-2021
## We could not use this data as it gives the entire state per capita for ASF funding . 
tx_capita_plot = capita_df.plot(x="year",y="rate",rot=90, title="Texas School Districts Per Capita Rates 1949-2021")


# In[44]:


#isd_2016_df.columns


# In[125]:


isd_income=isd_data_by_county.loc[:,["district_name","median_income_isd"]]
isd_income.head()


# In[126]:


isd_income.set_index("district_name", inplace = True)


# In[129]:


# top 25 Income data by school district
income_large= isd_income.nlargest(25,"median_income_isd")
income_large=income_large.hvplot.bar(
    width=800,
    height= 600,
    rot=90,
    yformatter="%.2f",
    title="Households Income"
) # top largest data
#income_large


# In[130]:


scatter_test_income = px.scatter(
    isd_data,
    x="median_income_isd",
    y="district_rating_2019",
    size ="median_income_isd",
    color = "district_name",
    hover_name = "district_name",
    title= "Median Household Income of Isd by District"
)
#scatter_test_income


# In[131]:


scatter_test_value = px.scatter(
    isd_data,
    x="2019_median_property_value",
    y="district_rating_2019",
    size = "2019_median_property_value",
    color = "district_name",
    hover_name = "district_name",
    title= "Median Property Value within ISD by District"
)
#scatter_test_value


# In[132]:


scatter_test_taxdue = px.scatter(
    isd_data,
    x="2019_median_property_value",
    y="district_rating_2019",
    size = "2019_median_property_value",
    color = "district_name",
    hover_name = "district_name",
    title= "Median Property Tax Owed within ISD by District"
)
#scatter_test_taxdue


# In[133]:


scatter_test_taxrate2 = px.scatter(
    isd_data,
    x="district_rating_2019",
    y="2019_isd_taxrate",
    size = "2019_isd_taxrate",
    color = "district_name",
    hover_name = "district_name",
    title= "Property Tax Rate of ISD by District"
)
#scatter_test_taxrate2


# In[134]:


welcome_plot_1 = pn.Row(scatter_test_income,scatter_test_value) 


# In[135]:


welcome_plot_2 = pn.Row(scatter_test_taxdue,scatter_test_taxrate2) 


# In[136]:


welcome_plot = pn.Column(welcome_plot_1,welcome_plot_2)


# In[137]:


welcome_column = pn.Column("#### This Dashboard presents the DFW Housing and Schooling.", welcome_plot)


# In[144]:


# Dashboard
dashboard = pn.Tabs(
    (
        "Welcome",
        welcome_column
    ),
    (
        "Households Income ",
        scatter_3d
    ),
    (
        "School Score",
        map_plot
    ),
    (
        "Households Income",
        income_large
    ),
    ( 
        'Top 20 District Rating',
         plot_category
    ),
    (
        'District Rating',
         fig_tree
    ),
    (
        "Bar Analysis",
        county_bar
    ),
    (
        "Sunburst Plot Analysis",
        fig_sunburst
    ),
    (
        'Ratio',
        fig
    )
)


# In[141]:


dashboard.servable()


# In[ ]:




