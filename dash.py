import streamlit as st
import pandas as pd
import requests
import json
from datetime import date,datetime
import geopandas as gpd
import plotly.express as px

state_index = {'Andaman and Nicobar Islands': 1,
 'Andhra Pradesh': 2,
 'Arunachal Pradesh': 3,
 'Assam': 4,
 'Bihar': 5,
 'Chandigarh': 6,
 'Chhattisgarh': 7,
 'Dadra and Nagar Haveli': 8,
 'Daman and Diu': 37,
 'Delhi': 9,
 'Goa': 10,
 'Gujarat': 11,
 'Haryana': 12,
 'Himachal Pradesh': 13,
 'Jammu and Kashmir': 14,
 'Jharkhand': 15,
 'Karnataka': 16,
 'Kerala': 17,
 'Ladakh': 18,
 'Lakshadweep': 19,
 'Madhya Pradesh': 20,
 'Maharashtra': 21,
 'Manipur': 22,
 'Meghalaya': 23,
 'Mizoram': 24,
 'Nagaland': 25,
 'Odisha': 26,
 'Puducherry': 27,
 'Punjab': 28,
 'Rajasthan': 29,
 'Sikkim': 30,
 'Tamil Nadu': 31,
 'Telangana': 32,
 'Tripura': 33,
 'Uttar Pradesh': 34,
 'Uttarakhand': 35,
 'West Bengal': 36}

st.set_page_config(layout = 'wide')
def VaccineCheck(state):
    today = date.today()
    current_date = today.strftime("%d-%m-%Y")   ##Gets todays Date

    st_id = state_index[state]
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:85.0) Gecko/20100101 Firefox/85.0'}
    district_url = f"https://cdn-api.co-vin.in/api/v2/admin/location/districts/{st_id}"

    
    response = requests.get(district_url,headers = headers)
    a = response.headers.get('Content-Type')
    f'the return for {state} is {a}'
    # dist_data = response.json()
    
    

    # district_index = {}
    # for district in dist_data['districts']:
    #     district_index[district['district_name']] = district['district_id']


    # state_count = {}
    # for district in district_index:
    #     district_count = 0
    #     url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={district_index[district]}&date={current_date}"
    #     response = requests.get(url,headers = headers)
    #     session_data = response.json()
    #     centers = session_data['centers']
        
    #     for center in centers:
    #         for session in center['sessions']:
    #             district_count += session['available_capacity']
    #     state_count[district] = district_count

    # state_df = pd.DataFrame.from_dict(state_count,orient = 'index')
    # state_df.columns = ['Current Availability']



    # file_name = f'{state}.geojson'
    # map = gpd.read_file(file_name)
    # map = map[['distname','geometry']]
    # map.set_index('distname',inplace = True)

    # merged_data = map.merge(state_df,left_index = True,right_index = True)

    # fig = px.choropleth_mapbox(merged_data,geojson = merged_data.geometry,locations = merged_data.index,color = "Current Availability",mapbox_style="carto-positron",center={"lat": 16.784, "lon": 78.113},zoom = 4,
    # color_continuous_scale = 'geyser')

    # st.write('The map is interactive! Scroll and Zoom')

    # fig


st.title('COVID-19 Vaccine Heatmap')
st.header('A district-wise heatmap of current vaccine availability by state')
st.write('Using the CoWIN API. Cached data may be upto 30 minutes old')

usr_state = st.selectbox('Choose State', ['Kerala','Karnataka'])

VaccineCheck(usr_state)