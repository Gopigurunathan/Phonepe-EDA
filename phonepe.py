import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import mysql.connector
import plotly.express as px

import requests
import json

#sql connection
#Table Creation
#mysql connection

mydb = mysql.connector.connect(
    username='root',
    host="localhost",
    password="Gopi2708",
    database='phonepe')

cursor = mydb.cursor()

# Define functions to fetch and process data
def fetch_data(query):
    cursor.execute(query)
    result = cursor.fetchall()
    return pd.DataFrame(result, columns=[i[0] for i in cursor.description])

# Fetch data for various tables
aggre_insurance = fetch_data("SELECT * FROM aggregated_insurance")
agg_transaction = fetch_data("SELECT * FROM aggregated_transaction")
aggre_user = fetch_data("SELECT * FROM aggregated_user")
map_insurance = fetch_data("SELECT * FROM map_insurance")
map_transaction = fetch_data("SELECT * FROM map_transaction")
map_user = fetch_data("SELECT * FROM map_user")
top_insurance = fetch_data("SELECT * FROM top_insurance")
top_transaction = fetch_data("SELECT * FROM top_transaction")
top_user = fetch_data("SELECT * FROM top_user")

def transaction_AC_y(df,year):
 
    tacy=df[df['Years']==year]
    tacy.reset_index(drop=True,inplace=True)
    tacy_g=tacy.groupby('States')[['Transaction_count','Transaction_amount']].sum()
    tacy_g.reset_index(inplace=True)

    col1,col2=st.columns(2)

    with col1:

        fig_amount=px.bar(tacy_g,x="States",y='Transaction_amount',title="TRANSACTION AMOUNT",color_discrete_sequence=px.colors.sequential.Redor_r,height=600,width=600)
        st.plotly_chart(fig_amount)

    with col2:

        fig_amount=px.bar(tacy_g,x="States",y='Transaction_count',title="TRANSACTION COUNT",color_discrete_sequence=px.colors.sequential.Bluered_r,height=600,width=600)
        st.plotly_chart(fig_amount)
    

    col1,col2=st.columns(2)
    
    with col1:


        url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response=requests.get(url)

        data1=json.loads(response.content)

        states_name=[]
        for feature in data1["features"]:
            states_name.append((feature["properties"]["ST_NM"]))

        states_name.sort()

        fig_ind_1=px.choropleth(tacy_g, geojson=data1, locations="States", featureidkey="properties.ST_NM",
                                color="Transaction_amount",color_continuous_scale="Viridis",
                                range_color=(tacy_g['Transaction_amount'].min(),tacy_g['Transaction_amount'].max()),
                                hover_name= "States",title= f'{year} TRANSACTION_AMOUNT',
                                fitbounds="locations",height=650,width=600)
        fig_ind_1.update_geos(visible=False)
        st.plotly_chart(fig_ind_1)

    with col2:
        url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response=requests.get(url)

        data1=json.loads(response.content)

        states_name=[]
        for feature in data1["features"]:
            states_name.append((feature["properties"]["ST_NM"]))

        states_name.sort()

        fig_ind_2=px.choropleth(tacy_g, geojson=data1, locations="States", featureidkey="properties.ST_NM",
                                color="Transaction_count",color_continuous_scale="Viridis",
                                range_color=(tacy_g['Transaction_count'].min(),tacy_g['Transaction_count'].max()),
                                hover_name= "States",title= f'{year} TRANSACTION_COUNT',
                                fitbounds="locations",height=650,width=600)
        fig_ind_2.update_geos(visible=False)
        st.plotly_chart(fig_ind_2)

    return tacy


    

def transaction_AC_yQ(df,quarter):
    tacy=df[df['Quarter']==quarter]
    tacy.reset_index(drop=True,inplace=True)
    tacy_g=tacy.groupby('States')[['Transaction_count','Transaction_amount']].sum()
    tacy_g.reset_index(inplace=True)

    col1,col2=st.columns(2)

    with col1:

        fig_amount=px.bar(tacy_g,x="States",y='Transaction_amount',title=f"{tacy['Years'].min()} YEAR {quarter} QUARTER TRANSACTION AMOUNT",color_discrete_sequence=px.colors.sequential.Redor,height=600,width=600)
        st.plotly_chart(fig_amount)
    
    with col2:

        fig_amount=px.bar(tacy_g,x="States",y='Transaction_count',title=f"{tacy['Years'].min()} YEAR {quarter} QUARTER TRANSACTION COUNT",color_discrete_sequence=px.colors.sequential.Bluered_r,height=600,width=600)
        st.plotly_chart(fig_amount)
    
    col1,col2=st.columns(2)

    with col1:

        url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response=requests.get(url)

        data1=json.loads(response.content)

        states_name=[]
        for feature in data1["features"]:
            states_name.append((feature["properties"]["ST_NM"]))

        states_name.sort()

        fig_ind_1=px.choropleth(tacy_g, geojson=data1, locations="States", featureidkey="properties.ST_NM",
                                color="Transaction_amount",color_continuous_scale="Rainbow",
                                range_color=(tacy_g['Transaction_amount'].min(),tacy_g['Transaction_amount'].max()),
                                hover_name= "States",title= f"{tacy['Years'].min()} YEAR {quarter} QUARTER TRANSACTION_AMOUNT",
                                fitbounds="locations",height=650,width=600)
        fig_ind_1.update_geos(visible=False)
        st.plotly_chart(fig_ind_1)

    with col2:

        url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response=requests.get(url)

        data1=json.loads(response.content)

        states_name=[]
        for feature in data1["features"]:
            states_name.append((feature["properties"]["ST_NM"]))

        states_name.sort()

        fig_ind_2=px.choropleth(tacy_g, geojson=data1, locations="States", featureidkey="properties.ST_NM",
                                color="Transaction_count",color_continuous_scale="Rainbow",
                                range_color=(tacy_g['Transaction_count'].min(),tacy_g['Transaction_count'].max()),
                                hover_name= "States",title= f"{tacy['Years'].min()} YEAR {quarter} QUARTER TRANSACTION_COUNT",
                                fitbounds="locations",height=650,width=600)
        fig_ind_2.update_geos(visible=False)
        st.plotly_chart(fig_ind_2)

    return tacy


def agg_tra_type(df,state):
    tacy=df[df['States']==state]
    tacy.reset_index(drop=True,inplace=True)
     # Aggregate transaction_type data
    tacy_g=tacy.groupby('Transaction_type')[['Transaction_count','Transaction_amount']].sum()
    tacy_g.reset_index(inplace=True)
    # Define custom color sequence
    custom_colors = ['#FF5733', '#33FF57', '#3357FF']

    col1,col2=st.columns(2)
    
    with col1:

        fig_pie_1=px.pie(data_frame= tacy_g , names="Transaction_type" , values="Transaction_count",
                            width=600,title=f"{state.upper()} TRANSACTION AMOUNT", hole= 0.5,color_discrete_sequence=custom_colors)

        st.plotly_chart(fig_pie_1)

    with col2:

        fig_pie_2=px.pie(data_frame= tacy_g , names="Transaction_type" , values="Transaction_count",
                            width=600,title=f"{state.upper()} TRANSACTION COUNT", hole= 0.5,color_discrete_sequence=custom_colors)

        st.plotly_chart(fig_pie_2)    


def aggre_userb_y(df,year):
    auy=df[df['Years']==year]
    auy.reset_index(drop=True,inplace=True)
    
    auyg=pd.DataFrame(auy.groupby('Brands')['Transaction_count'].sum())
    auyg.reset_index(inplace=True)

    fig_bar_1=px.bar(auyg,x="Brands" , y ='Transaction_count',title=f"BRANDS AND TRANSACTION COUNT {year}", width=850,color='Brands',
                    color_discrete_sequence=px.colors.sequential.Viridis,hover_name="Brands"
                    )
    fig_bar_1.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig_bar_1.update_layout(uniformtext_minsize=8, uniformtext_mode='hide',plot_bgcolor='white',margin=dict(l=50, r=50, t=50, b=50))
    st.plotly_chart(fig_bar_1)

    return auy

def aggre_userb_q(df,quarter):
    auyq=df[df['Quarter']==quarter]
    auyq.reset_index(drop=True,inplace=True)
    
    auygq=pd.DataFrame(auyq.groupby('Brands')['Transaction_count'].sum())
    auygq.reset_index(inplace=True)

    fig_bar_1=px.bar(auygq,x="Brands" , y ='Transaction_count',title=f"BRANDS AND TRANSACTION COUNT ( {quarter} QUARTER and {auyq['Years'].min()} YEAR )", width=850,color='Brands',
                    color_discrete_sequence=px.colors.sequential.Cividis_r,hover_name='Brands'
                    )
    fig_bar_1.update_layout(uniformtext_minsize=8, uniformtext_mode='hide',plot_bgcolor='white',margin=dict(l=50, r=50, t=50, b=50))
    st.plotly_chart(fig_bar_1)

    return auyq


#aggre_user_analysis3

def agg_userb_S(df,state):
    aggus=df[df['States']== state]
    aggus.reset_index(drop=True,inplace=True)

    fig_line_1=px.line(aggus,x='Brands',y='Transaction_count',hover_data="Percentage",
                    title=f"BRANDS TRANSACTION COUNT PERCENTAGE ANALYSIS FOR {state.upper()}",width=1000, markers=True)
    st.plotly_chart(fig_line_1)

#Map_insurance_district
def Map_insur_District(df, state):

    tacy= df[df["States"] == state]
    tacy.reset_index(drop = True, inplace= True)

    tacyg= tacy.groupby("District")[["Transaction_count","Transaction_amount"]].sum()
    tacyg.reset_index(inplace= True)

    col1,col2= st.columns(2)

    with col1:
        fig_bar_1= px.bar(tacyg, x= "Transaction_amount", y= "District", orientation= "h", height= 600,
                        title= f"{state.upper()} DISTRICT AND TRANSACTION AMOUNT", color_discrete_sequence= px.colors.sequential.Mint_r)
        fig_bar_1.update_layout(uniformtext_minsize=8, uniformtext_mode='hide',plot_bgcolor='white',margin=dict(l=50, r=50, t=50, b=50))
        st.plotly_chart(fig_bar_1)

    with col2:

        fig_bar_2= px.bar(tacyg, x= "Transaction_count", y= "District", orientation= "h", height= 600,
                        title= f"{state.upper()} DISTRICT AND TRANSACTION COUNT", color_discrete_sequence= px.colors.sequential.Bluered_r)
        fig_bar_2.update_layout(uniformtext_minsize=8, uniformtext_mode='hide',plot_bgcolor='white',margin=dict(l=50, r=50, t=50, b=50))
        st.plotly_chart(fig_bar_2)

    return tacy

#Map_insurance_district
def Map_insur_District(df, state):

    tacy= df[df["States"] == state]
    tacy.reset_index(drop = True, inplace= True)

    tacyg= tacy.groupby("District")[["Transaction_count","Transaction_amount"]].sum()
    tacyg.reset_index(inplace= True)

    col1,col2= st.columns(2)
    with col1:
        fig_bar_1= px.bar(tacyg, x= "Transaction_amount", y= "District", orientation= "h", height= 600,
                        title= f"{state.upper()} DISTRICT AND TRANSACTION AMOUNT", color_discrete_sequence= px.colors.sequential.Mint_r)
        st.plotly_chart(fig_bar_1)

    with col2:

        fig_bar_2= px.bar(tacyg, x= "Transaction_count", y= "District", orientation= "h", height= 600,
                        title= f"{state.upper()} DISTRICT AND TRANSACTION COUNT", color_discrete_sequence= px.colors.sequential.Bluered_r)
        st.plotly_chart(fig_bar_2)


# map_user_plot_1
def map_user_plot_1(df, year):
    muy= df[df["Years"]== year]
    muy.reset_index(drop= True, inplace= True)

    muyg= muy.groupby("States")[["RegisteredUser", "AppOpens"]].sum()
    muyg.reset_index(inplace= True)

    fig_line_1= px.line(muyg, x= "States", y= ["RegisteredUser", "AppOpens"],
                        title= f"{year} REGISTERED USER, APPOPENS",width= 1000, height= 800, markers= True)
    st.plotly_chart(fig_line_1)

    return muy

# map_user_plot_2
def map_user_plot_2(df, quarter):
    muyq= df[df["Quarter"]== quarter]
    muyq.reset_index(drop= True, inplace= True)

    muyqg= muyq.groupby("States")[["RegisteredUser", "AppOpens"]].sum()
    muyqg.reset_index(inplace= True)

    fig_line_1= px.line(muyqg, x= "States", y= ["RegisteredUser", "AppOpens"],
                        title= f"{df['Years'].min()} YEARS {quarter} QUARTER REGISTERED USER, APPOPENS",width= 1000, height= 800, markers= True,
                        color_discrete_sequence= px.colors.sequential.Rainbow_r)
    st.plotly_chart(fig_line_1)

    return muyq

#map_user_plot_3
def map_user_plot_3(df, states):
    muyqs= df[df["States"]== states]
    muyqs.reset_index(drop= True, inplace= True)

    col1,col2= st.columns(2)
    with col1:
        fig_map_user_bar_1= px.bar(muyqs, x= "RegisteredUser", y= "Districts", orientation= "h",
                                title= f"{states.upper()} REGISTERED USER", height= 800, color_discrete_sequence= px.colors.sequential.Rainbow_r)
        fig_map_user_bar_1.update_layout(uniformtext_minsize=8, uniformtext_mode='hide',plot_bgcolor='white',margin=dict(l=50, r=50, t=50, b=50))
        st.plotly_chart(fig_map_user_bar_1)

    with col2:

        fig_map_user_bar_2= px.bar(muyqs, x= "AppOpens", y= "Districts", orientation= "h",
                                title= f"{states.upper()} APPOPENS", height= 800, color_discrete_sequence= px.colors.sequential.Rainbow)
        fig_map_user_bar_2.update_layout(uniformtext_minsize=8, uniformtext_mode='hide',plot_bgcolor='white',margin=dict(l=50, r=50, t=50, b=50))
        st.plotly_chart(fig_map_user_bar_2)


# top_insurance_plot_1
def Top_insurance_plot_1(df, state):
    tiy= df[df["States"]== state]
    tiy.reset_index(drop= True, inplace= True)

    col1,col2= st.columns(2)
    with col1:
        fig_top_insur_bar_1= px.bar(tiy, x= "Quarter", y= "Transaction_amount", hover_data= "pincodes",
                                title= "TRANSACTION AMOUNT", height= 650,width= 600, color_discrete_sequence= px.colors.sequential.GnBu_r)
        st.plotly_chart(fig_top_insur_bar_1)

    with col2:

        fig_top_insur_bar_2= px.bar(tiy, x= "Quarter", y= "Transaction_count", hover_data= "pincodes",
                                title= "TRANSACTION COUNT", height= 650,width= 600, color_discrete_sequence= px.colors.sequential.Agsunset_r)
        st.plotly_chart(fig_top_insur_bar_2)

def top_user_plot_1(df, year):
    tuy= df[df["Years"]== year]
    tuy.reset_index(drop= True, inplace= True)

    tuyg= pd.DataFrame(tuy.groupby(["States", "Quarter"])["RegisteredUser"].sum())
    tuyg.reset_index(inplace= True)

    fig_top_plot_1= px.bar(tuyg, x= "States", y= "RegisteredUser", color= "Quarter", width= 1000, height= 800,
                        color_discrete_sequence= px.colors.sequential.Burgyl, hover_name= "States",
                        title= f"{year} REGISTERED USERS")
    st.plotly_chart(fig_top_plot_1)

    return tuy


# top_user_plot_2
def top_user_plot_2(df, state):
    tuys= df[df["States"]== state]
    tuys.reset_index(drop= True, inplace= True)

    fig_top_pot_2= px.bar(tuys, x= "Quarter", y= "RegisteredUser", title= "REGISTEREDUSERS, PINCODES, QUARTER",
                        width= 1000, height= 800, color= "RegisteredUser", hover_data= "pincodes",
                        color_continuous_scale= px.colors.sequential.Magenta)
    st.plotly_chart(fig_top_pot_2)


#top_chart_transactioncount func

def top_chat_TC(table_name):
    mydb = mysql.connector.connect(
    username='root',
    host="localhost",
    password="Gopi2708",
    database='phonepe')
    cursor = mydb.cursor()

    # Define SQL query1
    query1 = f'''
        SELECT states, SUM(transaction_count) AS Transaction_count
        FROM {table_name}
        GROUP BY states
        ORDER BY Transaction_count DESC
        LIMIT 10
    '''

    # Execute the query
    cursor.execute(query1)

    # Fetch all rows from the result set
    result_set = cursor.fetchall()

    # Create a DataFrame from the fetched rows
    table1 = pd.DataFrame(result_set, columns=['states', 'Transaction_count'])

    col1,col2=st.columns(2)

    with col1:
        
        fig_amount= px.bar(table1, x="states", y="Transaction_count", title="TOP 10 OF TRANSACTION COUNT", hover_name= "states",
                                    color_discrete_sequence=px.colors.sequential.Aggrnyl, height= 650,width= 600)
        st.plotly_chart(fig_amount)


    # Define SQL query2
    query2 =f'''
        SELECT states, SUM(transaction_count) AS Transaction_count
        FROM {table_name}
        GROUP BY states
        ORDER BY Transaction_count 
        LIMIT 10
    '''

    # Execute the query
    cursor.execute(query2)

    # Fetch all rows from the result set
    result_set = cursor.fetchall()

    # Create a DataFrame from the fetched rows
    table2 = pd.DataFrame(result_set, columns=['states', 'Transaction_count'])


    with col2:
        
        fig_amount1= px.bar(table2, x="states", y="Transaction_count", title="LOWEST 10 OF TRANSACTION COUNT", hover_name= "states",
                                    color_discrete_sequence=px.colors.sequential.Aggrnyl_r, height= 650,width= 600)
        st.plotly_chart(fig_amount1)


    # Define SQL query3
    query3 =f'''
        SELECT states, AVG(transaction_count) AS Transaction_count
        FROM {table_name}
        GROUP BY states
        ORDER BY Transaction_count 
        LIMIT 10
    '''

    # Execute the query
    cursor.execute(query3)

    # Fetch all rows from the result set
    result_set = cursor.fetchall()

    # Create a DataFrame from the fetched rows
    table3 = pd.DataFrame(result_set, columns=['states', 'Transaction_count'])

    fig_amount2= px.bar(table3, x="states", y="Transaction_count", title="TOP 10 OF TRANSACTION COUNT", hover_name= "states",orientation='h',
                                    color_discrete_sequence=px.colors.sequential.Viridis_r, height= 800,width= 1000)
    st.plotly_chart(fig_amount2)

#top_chart_transactionamount func

def top_chat_TA(table_name):
    mydb = mysql.connector.connect(
    username='root',
    host="localhost",
    password="Gopi2708",
    database='phonepe')
    cursor = mydb.cursor()

    # Define SQL query1
    query1 = '''
        SELECT states, SUM(transaction_amount) AS Transaction_amount
        FROM aggregated_insurance
        GROUP BY states
        ORDER BY Transaction_amount DESC
        LIMIT 10
    '''

    # Execute the query
    cursor.execute(query1)

    # Fetch all rows from the result set
    result_set = cursor.fetchall()

    # Create a DataFrame from the fetched rows
    table1 = pd.DataFrame(result_set, columns=['states', 'Transaction_amount'])

    col1,col2=st.columns(2)

    with col1:
        
        fig_amount= px.bar(table1, x="states", y="Transaction_amount", title="TOP 10 OF TRANSACTION AMOUNT", hover_name= "states",
                                    color_discrete_sequence=px.colors.sequential.Aggrnyl, height= 650,width= 600)
        st.plotly_chart(fig_amount)


    # Define SQL query2
    query2 = '''
        SELECT states, SUM(transaction_amount) AS Transaction_amount
        FROM aggregated_insurance
        GROUP BY states
        ORDER BY Transaction_amount 
        LIMIT 10
    '''

    # Execute the query
    cursor.execute(query2)

    # Fetch all rows from the result set
    result_set = cursor.fetchall()

    # Create a DataFrame from the fetched rows
    table2 = pd.DataFrame(result_set, columns=['states', 'Transaction_amount'])


    with col2:
        
        fig_amount1= px.bar(table2, x="states", y="Transaction_amount", title="LOWEST 10 OF TRANSACTION AMOUNT", hover_name= "states",
                                    color_discrete_sequence=px.colors.sequential.Aggrnyl_r, height= 650,width= 600)
        st.plotly_chart(fig_amount1)


    # Define SQL query3
    query3 = '''
        SELECT states, AVG(transaction_amount) AS Transaction_amount
        FROM aggregated_insurance
        GROUP BY states
        ORDER BY Transaction_amount 
        LIMIT 10
    '''

    # Execute the query
    cursor.execute(query3)

    # Fetch all rows from the result set
    result_set = cursor.fetchall()

    # Create a DataFrame from the fetched rows
    table3 = pd.DataFrame(result_set, columns=['states', 'Transaction_amount'])

    fig_amount2= px.bar(table3, x="states", y="Transaction_amount", title="TOP 10(AVG) OF TRANSACTION AMOUNT", hover_name= "states",orientation='h',
                                    color_discrete_sequence=px.colors.sequential.Viridis, height= 800,width= 1000)
    st.plotly_chart(fig_amount2)



#sql connection
def top_chart_registered_user(table_name, state):
    mydb = mysql.connector.connect(
    username='root',
    host="localhost",
    password="Gopi2708",
    database='phonepe')
    cursor = mydb.cursor()
    #plot_1
    query1= f'''SELECT districts, SUM(registereduser) AS registereduser
                FROM {table_name}
                WHERE states= '{state}'
                GROUP BY districts
                ORDER BY registereduser DESC
                LIMIT 10;'''

    cursor.execute(query1)
    table_1= cursor.fetchall()
    mydb.commit()

    df_1= pd.DataFrame(table_1, columns=("districts", "registereduser"))

    col1,col2= st.columns(2)
    with col1:
        fig_amount= px.bar(df_1, x="districts", y="registereduser", title="TOP 10 OF REGISTERED USER", hover_name= "districts",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl, height= 650,width= 600)
        st.plotly_chart(fig_amount)

    #plot_2
    query2= f'''SELECT districts, SUM(registereduser) AS registereduser
                FROM {table_name}
                WHERE states= '{state}'
                GROUP BY districts
                ORDER BY registereduser
                LIMIT 10;'''

    cursor.execute(query2)
    table_2= cursor.fetchall()
    mydb.commit()

    df_2= pd.DataFrame(table_2, columns=("districts", "registereduser"))

    with col2:
        fig_amount_2= px.bar(df_2, x="districts", y="registereduser", title="LAST 10 REGISTERED USER", hover_name= "districts",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl_r, height= 650,width= 600)
        st.plotly_chart(fig_amount_2)

    #plot_3
    query3= f'''SELECT districts, AVG(registereduser) AS registereduser
                FROM {table_name}
                WHERE states= '{state}'
                GROUP BY districts
                ORDER BY registereduser;'''

    cursor.execute(query3)
    table_3= cursor.fetchall()
    mydb.commit()

    df_3= pd.DataFrame(table_3, columns=("districts", "registereduser"))

    fig_amount_3= px.bar(df_3, y="districts", x="registereduser", title="AVERAGE OF REGISTERED USER", hover_name= "districts", orientation= "h",
                        color_discrete_sequence=px.colors.sequential.Bluered_r, height= 800,width= 1000)
    st.plotly_chart(fig_amount_3)

#sql connection
def top_chart_appopens(table_name, state):
    mydb = mysql.connector.connect(
    username='root',
    host="localhost",
    password="Gopi2708",
    database='phonepe')
    cursor = mydb.cursor()
    query1= f'''SELECT districts, SUM(appopens) AS appopens
                FROM {table_name}
                WHERE states= '{state}'
                GROUP BY districts
                ORDER BY appopens DESC
                LIMIT 10;'''

    cursor.execute(query1)
    table_1= cursor.fetchall()
    mydb.commit()

    df_1= pd.DataFrame(table_1, columns=("districts", "appopens"))


    col1,col2= st.columns(2)
    with col1:

        fig_amount= px.bar(df_1, x="districts", y="appopens", title="TOP 10 OF APPOPENS", hover_name= "districts",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl, height= 650,width= 600)
        st.plotly_chart(fig_amount)

    #plot_2
    query2= f'''SELECT districts, SUM(appopens) AS appopens
                FROM {table_name}
                WHERE states= '{state}'
                GROUP BY districts
                ORDER BY appopens
                LIMIT 10;'''

    cursor.execute(query2)
    table_2= cursor.fetchall()
    mydb.commit()

    df_2= pd.DataFrame(table_2, columns=("districts", "appopens"))

    with col2:

        fig_amount_2= px.bar(df_2, x="districts", y="appopens", title="LAST 10 APPOPENS", hover_name= "districts",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl_r, height= 650,width= 600)
        st.plotly_chart(fig_amount_2)

    #plot_3
    query3= f'''SELECT districts, AVG(appopens) AS appopens
                FROM {table_name}
                WHERE states= '{state}'
                GROUP BY districts
                ORDER BY appopens;'''

    cursor.execute(query3)
    table_3= cursor.fetchall()
    mydb.commit()

    df_3= pd.DataFrame(table_3, columns=("districts", "appopens"))

    fig_amount_3= px.bar(df_3, y="districts", x="appopens", title="AVERAGE OF APPOPENS", hover_name= "districts", orientation= "h",
                        color_discrete_sequence=px.colors.sequential.Bluered_r, height= 800,width= 1000)
    st.plotly_chart(fig_amount_3)

#sql connection
def top_chart_registered_users(table_name):
    mydb = mysql.connector.connect(
    username='root',
    host="localhost",
    password="Gopi2708",
    database='phonepe')
    cursor = mydb.cursor()
    #plot_1
    query1= f'''SELECT states, SUM(registereduser) AS registeredusers
                FROM {table_name}
                GROUP BY states
                ORDER BY registeredusers DESC
                LIMIT 10'''

    cursor.execute(query1)
    table_1= cursor.fetchall()
    mydb.commit()

    df_1= pd.DataFrame(table_1, columns=("states", "registereduser"))
    
    col1,col2= st.columns(2)
    with col1:

        fig_amount= px.bar(df_1, x="states", y="registereduser", title="TOP 10 OF REGISTERED USERS", hover_name= "states",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl, height= 650,width= 600)
        st.plotly_chart(fig_amount)

    #plot_2
    query2= f'''SELECT states, SUM(registereduser) AS registeredusers
                FROM {table_name}
                GROUP BY states
                ORDER BY registeredusers
                LIMIT 10;'''

    cursor.execute(query2)
    table_2= cursor.fetchall()
    mydb.commit()

    df_2= pd.DataFrame(table_2, columns=("states", "registereduser"))

    with col2:

        fig_amount_2= px.bar(df_2, x="states", y="registereduser", title="LAST 10 REGISTERED USERS", hover_name= "states",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl_r, height= 650,width= 600)
        st.plotly_chart(fig_amount_2)

    #plot_3
    query3= f'''SELECT states, AVG(registereduser) AS registeredusers
                FROM {table_name}
                GROUP BY states
                ORDER BY registeredusers;'''

    cursor.execute(query3)
    table_3= cursor.fetchall()
    mydb.commit()

    df_3= pd.DataFrame(table_3, columns=("states", "registereduser"))

    fig_amount_3= px.bar(df_3, y="states", x="registereduser", title="AVERAGE OF REGISTERED USERS", hover_name= "states", orientation= "h",
                        color_discrete_sequence=px.colors.sequential.Bluered_r, height= 800,width= 1000)
    st.plotly_chart(fig_amount_3)







#streamlit part

st.set_page_config(layout='wide')
st.title("Phonepe Data Visualization And Exploration")


with st.sidebar:

    select=option_menu('Main Menu',["HOME","DATA EXPLORATION","TOP CHARTS"])

if select=='HOME':
      
    col1,col2= st.columns(2)

    with col1:
        st.header("PHONEPE")
        st.subheader("INDIA'S BEST TRANSACTION APP")
        st.markdown("PhonePe  is an Indian digital payments and financial technology company")
        st.write("****FEATURES****")
        st.write("****Credit & Debit card linking****")
        st.write("****Bank Balance check****")
        st.write("****Money Storage****")
        st.write("****PIN Authorization****")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
    with col2:
        pass

    col3,col4= st.columns(2)
    
    with col3:
        pass

    with col4:
        st.write("****Easy Transactions****")
        st.write("****One App For All Your Payments****")
        st.write("****Your Bank Account Is All You Need****")
        st.write("****Multiple Payment Modes****")
        st.write("****PhonePe Merchants****")
        st.write("****Multiple Ways To Pay****")
        st.write("****1.Direct Transfer & More****")
        st.write("****2.QR Code****")
        st.write("****Earn Great Rewards****")

    col5,col6= st.columns(2)

    with col5:
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.write("****No Wallet Top-Up Required****")
        st.write("****Pay Directly From Any Bank To Any Bank A/C****")
        st.write("****Instantly & Free****")

    with col6:
        pass




elif select=="DATA EXPLORATION":
    # Tabs for data exploration
    tab1,tab2,tab3=st.tabs(['Aggregrated','Map','Top'])

   
    with tab1:
        st.write("Content of Aggregated Analysis tab")
        method = st.radio("Select the Method", ['Insurance Analysis', 'Transaction Analysis', 'User Analysis'])

        if method == 'Insurance Analysis':
            col1,col2= st.columns(2)

            with col1:
                years= st.slider("Select The Year",aggre_insurance["Years"].min(),aggre_insurance["Years"].max(),aggre_insurance["Years"].min())
            agg_ins_Y= transaction_AC_y(aggre_insurance, years)

            col1,col2= st.columns(2)

            with col1:

                quarters= st.slider("Select The Quarter",agg_ins_Y["Quarter"].min(), agg_ins_Y["Quarter"].max(),agg_ins_Y["Quarter"].min())
            transaction_AC_yQ(agg_ins_Y, quarters)


            
        elif method == 'Transaction Analysis':
            years=st.slider("Select the Year",agg_transaction['Years'].min(),agg_transaction['Years'].max(),agg_transaction['Years'].min())
            agg_tran_Y=transaction_AC_y(agg_transaction,years)

            col1,col2=st.columns(2)

            with col1:
                states=st.selectbox("Select the State",agg_tran_Y['States'].unique())
                
            agg_tra_type(agg_tran_Y,states)

            col1,col2= st.columns(2)

            with col1:

                quarters= st.slider("Select The Quarter",agg_tran_Y["Quarter"].min(), agg_tran_Y["Quarter"].max(),agg_tran_Y["Quarter"].min())
            Aggre_tran_tac_Y_Q= transaction_AC_yQ(agg_tran_Y, quarters)

            col1,col2= st.columns(2)

            with col1:
            
                states= st.selectbox("Select The State_Ty", Aggre_tran_tac_Y_Q["States"].unique())

            agg_tra_type(Aggre_tran_tac_Y_Q, states)  
            
        elif method == 'User Analysis':
            col1,col2= st.columns(2)

            with col1:
                years= st.slider("Select The Year",aggre_user["Years"].min(),aggre_user["Years"].max(),aggre_user["Years"].min())
            agg_user_by= aggre_userb_y(aggre_user, years)

            col1,col2= st.columns(2)

            with col1:
                min_quarter = agg_user_by["Quarter"].min()
                max_quarter = agg_user_by["Quarter"].max()

                # Check if min_quarter equals max_quarter
                if min_quarter == max_quarter:
                    st.write("There is only one quarter value available.")
                    selected_quarter = min_quarter  # Set a default value or handle the case
                else:
                    # Display the slider if there's a range of values
                    selected_quarter = st.slider("Select The Quarter", min_value=min_quarter, max_value=max_quarter)


            agg_user_bq=aggre_userb_q(agg_user_by,selected_quarter)
            
            col1,col2=st.columns(2)

            with col1:
                states=st.selectbox("Select the State",agg_user_bq['States'].unique())
                
            agg_userb_S(agg_user_bq,states)




    with tab2:
        st.write("Content of Map Analysis tab")
        method2= st.radio("Select the Method", ['Map Insurance Analysis', 'Map Transaction Analysis', 'Map User Analysis'])

        if method2 == 'Map Insurance Analysis':
            min_year = map_insurance['Years'].min()
            max_year = map_insurance['Years'].max()
            year_slider_insurance = st.slider("Select the Year_MY", min_value=int(min_year), max_value=int(max_year), value=int(min_year))
            map_ins_y = transaction_AC_y(map_insurance, year_slider_insurance)

            col1,col2=st.columns(2)

            with col1:
                state_select_insurance= st.selectbox("Select The State_MYD", map_ins_y["States"].unique())
            map_ins_D=Map_insur_District(map_ins_y,state_select_insurance)

            col1,col2= st.columns(2)

            col1,col2= st.columns(2)
            with col1:

                quarter_slider_insurance= st.slider("Select The Quarter_MQ",map_ins_y["Quarter"].min(), map_ins_y["Quarter"].max(),map_ins_y["Quarter"].min())
            map_insur_tac_Y_Q= transaction_AC_yQ(map_ins_y, quarter_slider_insurance)

            col1,col2= st.columns(2)
            with col1:
                quarter_select_insurance= st.selectbox("Select The State_MQD", map_insur_tac_Y_Q["States"].unique())

            Map_insur_District(map_insur_tac_Y_Q, quarter_select_insurance)
 

        elif method2== 'Map Transaction Analysis':
            col1,col2= st.columns(2)
            with col1:
                min_year_T = map_transaction['Years'].min()
                max_year_T = map_transaction['Years'].max()
                year_slider_transaction = st.slider("Select the Year_MY", min_value=int(min_year_T), max_value=int(max_year_T), value=int(min_year_T))

                
            map_tran_tac_Y= transaction_AC_y(map_transaction,year_slider_transaction)

            col1,col2= st.columns(2)
            with col1:
                state_select= st.selectbox("Select The State_MD", map_tran_tac_Y["States"].unique())

            Map_insur_District(map_tran_tac_Y, state_select)

            col1,col2= st.columns(2)
            with col1:

                quarter_slider= st.slider("Select The Quarter_MQ",map_tran_tac_Y["Quarter"].min(), map_tran_tac_Y["Quarter"].max(),map_tran_tac_Y["Quarter"].min())
            map_tran_tac_Y_Q= transaction_AC_yQ(map_tran_tac_Y, quarter_slider)

            col1,col2= st.columns(2)
            with col1:
                state_select_q= st.selectbox("Select The State_MDQ", map_tran_tac_Y_Q["States"].unique())

            Map_insur_District(map_tran_tac_Y_Q, state_select_q)


        elif method2 == 'Map User Analysis':

            col1,col2= st.columns(2)
            with col1:

                slider_year_MU= st.slider("Select The Year_mu",map_user["Years"].min(), map_user["Years"].max(),map_user["Years"].min())
            map_user_Y= map_user_plot_1(map_user, slider_year_MU)

            col1,col2= st.columns(2)
            with col1:

                slider_quarter_mapuser= st.slider("Select The Quarter_mu",map_user_Y["Quarter"].min(), map_user_Y["Quarter"].max(),map_user_Y["Quarter"].min())
            map_user_Y_Q= map_user_plot_2(map_user_Y, slider_quarter_mapuser)

            col1,col2= st.columns(2)
            with col1:
                select_state_mapuser= st.selectbox("Select The State_mu", map_user_Y_Q["States"].unique())

            map_user_plot_3(map_user_Y_Q, select_state_mapuser)




    with tab3:
        st.write("Content of Top Analysis tab")
        method3= st.radio("Select the Method", ['Top Insurance Analysis', 'Top Transaction Analysis', 'Top User Analysis'])

        if method3 == 'Top Insurance Analysis':
            
            col1,col2= st.columns(2)
            with col1:

                years= st.slider("Select The Year_ti",top_insurance["Years"].min(), top_insurance["Years"].max(),top_insurance["Years"].min())
            top_insur_tac_Y= transaction_AC_y(top_insurance, years)

            col1,col2= st.columns(2)
            with col1:
                states= st.selectbox("Select The State_ti", top_insur_tac_Y["States"].unique())

            Top_insurance_plot_1(top_insur_tac_Y, states)

            col1,col2= st.columns(2)
            with col1:

                quarters= st.slider("Select The Quarter_mu",top_insur_tac_Y["Quarter"].min(), top_insur_tac_Y["Quarter"].max(),top_insur_tac_Y["Quarter"].min())
            top_insur_tac_Y_Q= transaction_AC_yQ(top_insur_tac_Y, quarters)

      
        elif method3== 'Top Transaction Analysis':
            
            col1,col2= st.columns(2)
            with col1:

                years= st.slider("Select The Year_tt",top_transaction["Years"].min(), top_transaction["Years"].max(),top_transaction["Years"].min())
            top_tran_tac_Y= transaction_AC_y(top_transaction, years)

            col1,col2= st.columns(2)
            with col1:
                states= st.selectbox("Select The State_tt", top_tran_tac_Y["States"].unique())

            Top_insurance_plot_1(top_tran_tac_Y, states)

            col1,col2= st.columns(2)
            with col1:

                quarters= st.slider("Select The Quarter_tt",top_tran_tac_Y["Quarter"].min(), top_tran_tac_Y["Quarter"].max(),top_tran_tac_Y["Quarter"].min())
            top_tran_tac_Y_Q= transaction_AC_yQ(top_tran_tac_Y, quarters)

        elif method3 == 'Top User Analysis':
            col1,col2= st.columns(2)
            with col1:

                years= st.slider("Select The Year_tu",top_user["Years"].min(), top_user["Years"].max(),top_user["Years"].min())
            top_user_Y= top_user_plot_1(top_user, years)

            col1,col2= st.columns(2)
            with col1:
                states= st.selectbox("Select The State_tu", top_user_Y["States"].unique())

            top_user_plot_2(top_user_Y, states)

elif select=="TOP CHARTS":
        
    question= st.selectbox("Select the Question",["1. Transaction Amount and Count of Aggregated Insurance",
                                                    "2. Transaction Amount and Count of Map Insurance",
                                                    "3. Transaction Amount and Count of Top Insurance",
                                                    "4. Transaction Amount and Count of Aggregated Transaction",
                                                    "5. Transaction Amount and Count of Map Transaction",
                                                    "6. Transaction Amount and Count of Top Transaction",
                                                    "7. Transaction Count of Aggregated User",
                                                    "8. Registered users of Map User",
                                                    "9. App opens of Map User",
                                                    "10. Registered users of Top User",
                                                    ])
    
 

        
    if question == "1. Transaction Amount and Count of Aggregated Insurance":
        
        st.subheader("TRANSACTION AMOUNT")
        top_chat_TA("aggregated_insurance")

        st.subheader("TRANSACTION COUNT")
        top_chat_TC("aggregated_insurance")

    elif question == "2. Transaction Amount and Count of Map Insurance":
        
        st.subheader("TRANSACTION AMOUNT")
        top_chat_TA("map_insurance")

        st.subheader("TRANSACTION COUNT")
        top_chat_TC("map_insurance")

    elif question == "3. Transaction Amount and Count of Top Insurance":
        
        st.subheader("TRANSACTION AMOUNT")
        top_chat_TA("top_insurance")

        st.subheader("TRANSACTION COUNT")
        top_chat_TC("top_insurance")

    elif question == "4. Transaction Amount and Count of Aggregated Transaction":
        
        st.subheader("TRANSACTION AMOUNT")
        top_chat_TA("aggregated_transaction")

        st.subheader("TRANSACTION COUNT")
        top_chat_TC("aggregated_transaction")

    elif question == "5. Transaction Amount and Count of Map Transaction":
        
        st.subheader("TRANSACTION AMOUNT")
        top_chat_TA("map_transaction")

        st.subheader("TRANSACTION COUNT")
        top_chat_TC("map_transaction")

    elif question == "6. Transaction Amount and Count of Top Transaction":
        
        st.subheader("TRANSACTION AMOUNT")
        top_chat_TA("top_transaction")

        st.subheader("TRANSACTION COUNT")
        top_chat_TC("top_transaction")

    elif question == "7. Transaction Count of Aggregated User":

        st.subheader("TRANSACTION COUNT")
        top_chat_TC("aggregated_user")

    elif question == "8. Registered users of Map User":
        
        states= st.selectbox("Select the State", map_user["States"].unique())   
        st.subheader("REGISTERED USERS")
        top_chart_registered_user("map_user", states)

    elif question == "9. App opens of Map User":
        
        states= st.selectbox("Select the State", map_user["States"].unique())   
        st.subheader("APPOPENS")
        top_chart_appopens("map_user", states)

    elif question == "10. Registered users of Top User":
          
        st.subheader("REGISTERED USERS")
        top_chart_registered_users("top_user")