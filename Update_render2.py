# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 18:32:26 2022

@author: maggi
"""
#timezone
#every 30 min
#prit interval

#colors
#not luftfeucht in ticker
#what if api bad response??

#hovermenu dont say variabel sondern Messwert
#kei = zeichen
#und mit ziit 
#minor ticks sölled länger si jetzt sind igendwie major ticks grösser


#get table data 
#get graph data

#google fonts roboto bold condensed h1
#roboto light oder reg für normaler text
#dropdown direkt unter graph
#h bold
#dropdown hover color  bg setze und anderi für hover 
#tabelle zeilenabstand etwas kleiner
#datum dort unter 12.00 striche

from dash import dash, dcc, html,dash_table, Output, Input, ctx
import os
import plotly.graph_objs as go
import pandas as pd
import numpy as np

from dash_table.Format import Format, Group, Scheme
import dash_table.FormatTemplate as FormatTemplate
from datetime import datetime as dt
#from app import app
import plotly.express as px


import requests
import json
#import pandas as pd

from datetime import datetime, timezone, timedelta
import pytz
import plotly.io as pio
#pio.templates  #tells you which themes are available
pio.templates.default = "plotly_white"
plotly_template = pio.templates["plotly_white"]
plotly_template.layout

# Layout({
#     'annotationdefaults': {'arrowcolor': '#2a3f5f', 'arrowhead': 0, 'arrowwidth': 1},
#     'autotypenumbers': 'strict',
#     'coloraxis': {'colorbar': {'outlinewidth': 0, 'ticks': ''}},
#     'colorscale': {'diverging': [[0, '#8e0152'], [0.1, '#c51b7d'], [0.2,
#                                  '#de77ae'], [0.3, '#f1b6da'], [0.4, '#fde0ef'],
#                                  [0.5, '#f7f7f7'], [0.6, '#e6f5d0'], [0.7,
#                                  '#b8e186'], [0.8, '#7fbc41'], [0.9, '#4d9221'],
#                                  [1, '#276419']],
#                    'sequential': [[0.0, '#0d0887'], [0.1111111111111111,
#                                   '#46039f'], [0.2222222222222222, '#7201a8'],
#                                   [0.3333333333333333, '#9c179e'],
#                                   [0.4444444444444444, '#bd3786'],
#                                   [0.5555555555555556, '#d8576b'],
#                                   [0.6666666666666666, '#ed7953'],
#                                   [0.7777777777777778, '#fb9f3a'],
#                                   [0.8888888888888888, '#fdca26'], [1.0,
#                                   '#f0f921']],
#                    'sequentialminus': [[0.0, '#0d0887'], [0.1111111111111111,
#                                        '#46039f'], [0.2222222222222222, '#7201a8'],
#                                        [0.3333333333333333, '#9c179e'],
#                                        [0.4444444444444444, '#bd3786'],
#                                        [0.5555555555555556, '#d8576b'],
#                                        [0.6666666666666666, '#ed7953'],
#                                        [0.7777777777777778, '#fb9f3a'],
#                                        [0.8888888888888888, '#fdca26'], [1.0,
#                                        '#f0f921']]},
#     'colorway': [#636efa, #EF553B, #00cc96, #ab63fa, #FFA15A, #19d3f3, #FF6692,
#                  #B6E880, #FF97FF, #FECB52],
#     'font': {'color': '#2a3f5f'},
#     'geo': {'bgcolor': 'white',
#             'lakecolor': 'white',
#             'landcolor': 'white',
#             'showlakes': True,
#             'showland': True,
#             'subunitcolor': '#C8D4E3'},
#     'hoverlabel': {'align': 'left'},
#     'hovermode': 'closest',
#     'mapbox': {'style': 'light'},
#     'paper_bgcolor': 'white',
#     'plot_bgcolor': 'white',
#     'polar': {'angularaxis': {'gridcolor': '#EBF0F8', 'linecolor': '#EBF0F8', 'ticks': ''},
#               'bgcolor': 'white',
#               'radialaxis': {'gridcolor': '#EBF0F8', 'linecolor': '#EBF0F8', 'ticks': ''}},
#     'scene': {'xaxis': {'backgroundcolor': 'white',
#                         'gridcolor': '#DFE8F3',
#                         'gridwidth': 2,
#                         'linecolor': '#EBF0F8',
#                         'showbackground': True,
#                         'ticks': '',
#                         'zerolinecolor': '#EBF0F8'},
#               'yaxis': {'backgroundcolor': 'white',
#                         'gridcolor': '#DFE8F3',
#                         'gridwidth': 2,
#                         'linecolor': '#EBF0F8',
#                         'showbackground': True,
#                         'ticks': '',
#                         'zerolinecolor': '#EBF0F8'},
#               'zaxis': {'backgroundcolor': 'white',
#                         'gridcolor': '#DFE8F3',
#                         'gridwidth': 2,
#                         'linecolor': '#EBF0F8',
#                         'showbackground': True,
#                         'ticks': '',
#                         'zerolinecolor': '#EBF0F8'}},
#     'shapedefaults': {'line': {'color': '#2a3f5f'}},
#     'ternary': {'aaxis': {'gridcolor': '#DFE8F3', 'linecolor': '#A2B1C6', 'ticks': ''},
#                 'baxis': {'gridcolor': '#DFE8F3', 'linecolor': '#A2B1C6', 'ticks': ''},
#                 'bgcolor': 'white',
#                 'caxis': {'gridcolor': '#DFE8F3', 'linecolor': '#A2B1C6', 'ticks': ''}},
#     'title': {'x': 0.05},
#     'xaxis': {'automargin': True,
#               'gridcolor': '#EBF0F8',
#               'linecolor': '#EBF0F8',
#               'ticks': '',
#               'title': {'standoff': 15},
#               'zerolinecolor': '#EBF0F8',
#               'zerolinewidth': 2},
#     'yaxis': {'automargin': True,
#               'gridcolor': '#EBF0F8',
#               'linecolor': '#EBF0F8',
#               'ticks': '',
#               'title': {'standoff': 15},
#               'zerolinecolor': '#EBF0F8',
#               'zerolinewidth': 2}
# })


# =============================================================================
# # import os
# # SECRET_KEY = os.getenv("SECRET_KEY")
# 
# =============================================================================

#from app import app
#from app import server
#import layouts  #, page2, page3
#import callbacks
#from layouts import corporate_colors

app = dash.Dash(__name__)  #, suppress_callback_exceptions=True)
#app = dash(__name__)
#########################################################3
server = app.server

########################################

####################################################################################################
# 000 - FORMATTING INFO
####################################################################################################


colormap={
                "AtmosphericPressure": "#F9C74F",  #yellow #FF97FF",
                
                "T": "#B22222",           ##EF553B",  #rot
                "RH": "#1874CD",                 #"#19D3F3", #türkis
                "PM2p5": "#8B5A2B",         #636EFA", #dunkelviolet
                "PM1p0": "#F9844A",             #AB63FA", #rosaviolet
                "AirQualityIndex": "#79CDCD",   #00CC96", #mint
                "DewPoint": "#6E8B3D"
                }
table_col=["#B22222","#79CDCD", "#1874CD", "#8B5A2B", "#F9844A", "#6E8B3D", "#F9C74F" ]
table_colOP=["#B2222298","#79CDCD98", "#1874CD98", "#8B5A2B98", "#F9844A98", "#6E8B3D98", "#F9C74F98" ]

palette={'red': '#F94144',
         'lightorange': '#F8961E',
         'muddygreen': '#90BE6D',
         'blue': '#277DA1',
         'yellow': '#F9C74F',
         'samon': '#F9844A',
         'turquoise': '#43AA8B'
         
         }

palette2={'red': '#AE2012',
         'lightorange': '#CA6702',
         'lightblue': '#94D2BD',
         'blue': '#005F73',
         'yellow': '#EE9B00',
         'lighteryellow': '#F9C74F',
         'samon': '#F9844A',
         'turquoise': '#0A9396',
         'darkorange': '#BB3E03',
         'purple': '#9e0059',
         'green':'#3fa34d',
         'mint':'#7ae582'
         }


#dodgerblue3	#1874CD	RGB(24,116,205)
#darkslategray1	#79CDCD	RGB(151,255,255)
#darksalmon	#E9967A	RGB(233,150,122)
#darkolivegreen4	#6E8B3D	RGB(110,139,61)
#tan4	#8B5A2B	RGB(139,90,43)
#steelblue3	#4F94CD	RGB(79,148,205)

#turquoise3	#00C5CD	RGB(0,197,205)
#navy	#000080	RGB(0,0,128)
#mediumseagreen	#3CB371	RGB(60,179,113)
#firebrick	#B22222	RGB(178,34,34)
#banana	#E3CF57	RGB(227,207,87)
#aquamarine3	#66CDAA	RGB(102,205,170)
#red1	#FF0000	RGB(255,0,0)
#purple	#800080	RGB(128,0,128)	 
#purple1	#9B30FF	RGB(155,48,255)
#springgreen	#00FF7F	RGB(0,255,127)
#lawngreen	#7CFC00	RGB(124,252,0)
#aqua	#00FFFF	RGB(0,255,255)
#'blue' : 'rgb(0,0,255)'
#violetred4	#8B2252	RGB(139,34,82)
#yellow1	#FFFF00	RGB(255,255,0)
#gold1	#FFD700	RGB(255,215,0)

corporate_colors = {
    'dark-blue-grey' : 'rgb(62, 64, 76)',
    'sgigray12' : 'rgb(71,70,70)', #474646 schriftfarbe von susanne  called charcoal
    'darkorange' : 'rgb(255,140,0)',#FF8C00
    'carrot' : 'rgb(237,145,33)',
    #07889B teal passt zu orange
    'chocolate1' : 'rgb(255,127,36)',
    'orange1' : 'rgb(255,165,0)',
    'papayawhip' : 'rgb(255,239,213)', #creme für background
    'seashell1' : 'rgb(255,245,238)',
    'wheat' : 'rgb(245,222,179)', #dunkler creme für dropdown
    'ivory1' : 'rgb(255,255,240)',
    'medium-blue-grey' : 'rgb(77, 79, 91)',
    'superdark-green' : 'rgb(41, 56, 55)',
    'dark-green' : 'rgb(57, 81, 85)',
    'medium-green' : 'rgb(93, 113, 120)',
    'light-green' : 'rgb(186, 218, 212)',
    'pink-red' : 'rgb(255, 101, 131)',
    'dark-pink-red' : 'rgb(247, 80, 99)',
    'white' : 'rgb(255,255,255)', #not anymore  ##FBFBF
    'light-grey' : 'rgb(208, 206, 206)',
    'bg': 'rgb(246, 242, 237)'   ##F6F2ED besser #background color #FBF9F7  	251, 249, 247
}

#ext row mit graph and tabelle
externalgraph_rowstyling = {
    'margin-left' : '15px',
    'margin-right' : '15px'
}

#ext, col-10 mit graph und tabelle

externalgraph_colstyling = {
    'border-radius' : '10px',
    'border-style' : 'solid',
    'border-width' : '1px',
    'border-color' : corporate_colors['white'],
    'background-color' : corporate_colors['bg'],
    #'box-shadow' : '0px 0px 17px 0px rgba(186, 218, 212, .5)',
    'padding-top' : '0.4%' ,#vorher'5px' jeztz 5.1px #war 10 px 
    'padding-left' : '0.6%',
    'padding-right' : '0.3%',
}

boxcol_styling = {
    #'border-radius' : '10px',
    'border-style' : 'solid',
    'border-width' : '1px',
    'border-color' : corporate_colors['white'],
    'background-color' : corporate_colors['white'],
    #'box-shadow' : '0px 0px 17px 0px rgba(186, 218, 212, .5)',
    'padding' : '5% 5%'#vorher'5px' jeztz 5.1px #war 10 px 
    
    }
# filterdiv_borderstyling = {
#     'border-radius' : '0px 0px 10px 10px',
#     'border-style' : 'solid',
#     'border-width' : '1px',
#     'border-color' : corporate_colors['wheat'],
#     'background-color' : corporate_colors['wheat']
#     #,
#     #'box-shadow' : '2px 5px 5px 1px rgba(255, 101, 131, .5)'
#     }



#internal row mit graph und tabelle
recapdiv = {
    'border-radius' : '10px',
    'border-style' : 'solid',
    'border-width' : '1px',
    'border-color' : corporate_colors['bg'],
    'margin-left' : '1%',
    'margin-right' : '1%',
    'margin-top' : '0.8%',
    'margin-bottom' : '2%', #should be 12 px
    'padding-top' : '0.4%',
    'padding-bottom' : '0.4%',
    'background-color' : corporate_colors['bg']
    }

recapdiv_text = {
    'text-align' : 'left',
    'font-weight' : '350',
    'color' : corporate_colors['sgigray12'],
    'font-size' : '1rem',
    'letter-spacing' : '0.04em'
    }

####################### Corporate chart formatting

corporate_title = {
    'font' : {
        'size' : 18,
        
        'color' : corporate_colors['sgigray12']}
}

# corporate_xaxis = {
#     "ticklabelmode" :"period",
#     #'showgrid' : True,
#     # 'linecolor' : corporate_colors['light-grey'],
#     #  'gridcolor' : corporate_colors['dark-green'],
#     # 'color' : corporate_colors['light-grey'],
#     # 'tickangle' : 315,
#     # #tickangle Default: "auto" Sets the angle of the tick labels with respect to the horizontal. For example, a `tickangle` of -90 draws the tick labels vertically.
#     # 'titlefont' : {
#     #     'size' : 12,
#     #     'color' : corporate_colors['light-grey']},
#     # 'tickfont' : { #punkte vom Graph
#     #     'size' : 11,
#     #     'color' : corporate_colors['light-grey']},
#     # 'zeroline': False #Determines whether or not a line is drawn at along the 0 value of this axis. If "True", the zero line is drawn on top of the grid lines.
# }

# corporate_yaxis = {
#     'showgrid' : True,
#     # 'color' : corporate_colors['light-grey'],
#     # 'gridwidth' : 0.5,
#      'gridcolor' : corporate_colors['dark-green'],
#     # 'linecolor' : corporate_colors['light-grey'],
#     # 'titlefont' : {
#     #     'size' : 12,
#     #     'color' : corporate_colors['light-grey']},
#     # 'tickfont' : {
#     #     'size' : 11,
#     #     'color' : corporate_colors['light-grey']},
#     # 'zeroline': False #Determines whether or not a line is drawn at along the 0 value of this axis. If "True", the zero line is drawn on top of the grid lines.
# }

corporate_font_family = ['RobotoLight','RobotoCondensed' ]

#legend bgcolor default  paper_bgcolor

corporate_legend = {
    "borderwidth" : 1, 
    "bordercolor" :corporate_colors['sgigray12'], 
     'orientation' : 'h',  #horizontal vs "v" vertikal
     "title" : {"text" : ""},
    # "itemwidth" : "10",#makes color line smaller but default is 30 and cant go smaller
    'yanchor' : 'bottom',
    'y' : 1.01,
    #'y' : -0.1,
    # 'xanchor' : 'left',
    'xanchor' : 'right',

    'x' : 1.05,
    #'x' : 0,
 	'font' : {'size' : 9, 'color' : corporate_colors['sgigray12']}
     }

#legend position 
#x= number between or equal to -2 and 3
#Sets the x position (in normalized coordinates) of the legend. Defaults to "1.02" for vertical legends and defaults to "0" for horizontal legends.
#y
#Defaults to "1" for vertical legends, defaults to "-0.1" for horizontal legends on graphs w/o range sliders and defaults to "1.1" for horizontal legends on graph with one or multiple range sliders.



corporate_margins = {'l' : 5, 'r' : 5, 't' : 45, 'b' : 5}  # Set top margin to in case there is a legend
#corporate_margins = {'l' : 5, 'r' : 5, 't' : 10, 'b' : 60} 
# "pad" makes space btw axis and plot inside so bad


AQI=" Air Quality Index "

Markdown_Text='''   
## Infobox   

Der 
**Air Quality Index**
 ist eine Messgrösse für Luftqualität auf einer Skala von 0-500, Werte unter 50 entsprechen einer guten Luftqualität.
 
 Der zulässige Jahresmittelwert für PM10 ( **Feinstaubpartikel** unter 10 µm Durchmesser) beträgt 20 µg/m³. Für PM2.5 ist in der Schweiz kein Immissionsgrenzwert festgelegt (WHO-Empfehlung: 10 µg/m³). Unsere Messstation verzeichnete einen Jahresmittelwert von 13.4 µg/m³ PM2,5 zwischen Aug 2021 und 2022).
  
 Der **Taupunkt** ist die Temperatur bei der die rel. Luftfeuchtigkeit 100% beträgt, sinkt die Temperatur unter den Taupunkt entsteht Tau oder Nebel. 
 '''



#print("This is bold text looks like:",'\033[1m' + 'Python' + '\033[0m')
#pm2.5 pm10 artikel
#Der zulässige Jahresmittelwert für Staubpartikel mit einem Durchmesser von weniger 
#als 10 Tausendstelmillimeter (PM10) beträgt 20 µg/m³
#Als kurzfristiger Grenzwert, 
#der jedoch nur einmal pro Jahr überschritten werden darf, gilt der 24-Stunden-Mittelwert von 50 µg/m³. Für PM2.5 ist in der Schweiz kein Immissionsgrenzwert festgelegt (WHO-Empfehlung: 10 µg/m³, US-Grenzwert: 12 µg/m³).

#https://de.wikipedia.org/wiki/Feinstaub#cite_note-44
#Der Grenzwert für PM10 als 24-h-Mittelwert von 50 µg/m³ darf höchstens dreimal im Jahr überschritten werden
#In der Schweiz beträgt der Grenzwert für PM10 für den Jahresmittelwert 20 µg/m³
# Ultrafeine Partikel mit einer Größe <0,1 µm durchdringen die Wand der Lungenbläschen und sind im Blutstrom zu finden
####################################################################################################
# 000 - IMPORT DATA
####################################################################################################
#sales_filepath = 'data/df.pkl'
###DATEN EINLESEN








api_key = os.getenv('api_key')
organizationId = os.getenv('organizationId')

deviceId = os.getenv('deviceId')
# #How to authenticate to a rest API 
headers = {'Accept': 'application/json', "Api-Key" : api_key}


def get_data():
    #how to get date of yesterday with utc as timezone
    #yesterday = datetime.now(timezone.utc) - timedelta(days=5)
    # yesterday=datetime.now(pytz.timezone('Europe/Zurich')) - timedelta(days=5)
    # print(yesterday)
    # #get yesterdays date iso with time zone info and no microsecs
    # print(yesterday.replace(microsecond=0, second=0).astimezone().isoformat())
    # yesterday=yesterday.replace(microsecond=0).replace(second=0).astimezone().isoformat()
    # print(yesterday)
    today=datetime.now(pytz.timezone('Europe/Zurich'))
    print(today)

    yesterday=today - timedelta(days=5)
    print(yesterday)
    #get yesterdays date iso with time zone info and no microsecs
    #print(yesterday.replace(microsecond=0, second=0).astimezone().isoformat())
    yesterday=yesterday.replace(microsecond=0).replace(second=0).astimezone(pytz.timezone('Europe/Zurich')).isoformat()
    print(yesterday)
    today=today.replace(microsecond=0).replace(second=0).astimezone(pytz.timezone('Europe/Zurich')).isoformat()
    #today=datetime.now(timezone.utc).replace(microsecond=0, second=0).astimezone().isoformat()
    print(today)
    
    #format so url is readable
    yesterday=yesterday.replace(":", "%3A")
    print(yesterday)
    yesterday=yesterday.replace("+", "%2B")
    print(yesterday)
    #From ="2022-07-01T10:00+02:00"
    From =yesterday
    #fix with astimetone pytz.timezone('Europe/Zurich')
#     Sep 15 03:31:00 PM  2022-09-15 15:30:52.845427+02:00
# Sep 15 03:31:00 PM  2022-09-10 15:30:52.845427+02:00
# Sep 15 03:31:00 PM  2022-09-10T13:30:00+00:00
# Sep 15 03:31:00 PM  2022-09-15T13:30:00+00:00
# Sep 15 03:31:00 PM  2022-09-10T13%3A30%3A00+00%3A00
# Sep 15 03:31:00 PM  2022-09-10T13%3A30%3A00%2B00%3A00
# Sep 15 03:31:00 PM  2022-09-15T13%3A30%3A00+00%3A00
# Sep 15 03:31:00 PM  2022-09-15T13%3A30%3A00%2B00%3A00
    #string($date-time)
    # DateTime which defines the start of the selected time range 
    # (see aggregationTimeRange for more details about valid values). 
    # This value cannot be earlier than to. It must be formatted 
    # according to ISO 8601 (2007-08-31T16:47+00:00). 
    # The timezone information specified here, 
    # is used in the result as timezone. 
    # If no timezone is provided, all times are considered UTC.
    #to="2022-07-01T11:00+02:00"
    
    #format so url is readable
    today=today.replace(":", "%3A")
    print(today)
    today=today.replace("+", "%2B")
    print(today)
    
    to=today
    aggregationTimeRange="FiveMinutes"
    # The number of minutes which is used to determine the size of the time windows to use the mean operator on it. Example: If this value is "SixtyMinutes" it will repeatedly mean all data within 60 minutes over the selected date range (see from and to). Valid values are: "None", "FiveMinutes", "ThirtyMinutes", "SixtyMinutes", "TwentyFourHours". This value limits the date range which can be processed. These limitations are:
    
    # "FiveMinutes" minutes has a maximum date range of 31 days
    # "FifteenMinutes" minutes has a maximum date range of 62 days
    # "ThirtyMinutes" minutes has a maximum date range of 183 days
    # "SixtyMinutes" minutes has a maximum date range of 366 days
    # "TwentyFourHours" minutes (one day) has a maximum date range of 366 days
    # "None" provides the raw data at the exact time of measurement and has a maximum date range of 7 days
    # Available values : None, FiveMinutes, FifteenMinutes, ThirtyMinutes, SixtyMinutes, TwentyFourHours
    
    returnMissing="false"
    
    m_url="https://cloud.nubo-air.com/api/"+organizationId+"/devices/"+deviceId+"/measurements/v2?from="+From+"&to="+to+"&aggregationTimeRange="+aggregationTimeRange+"&returnMissing="+returnMissing


    
    response = requests.get(
        m_url,
        headers = headers
    )
    # print(response)
    # print(response.json())
    # #store the data
    json_dd=response.json()
    # print(json_dd)
    
    
    df = pd.read_json(json.dumps(json_dd))
    dff = df.copy()
    dff.AtmosphericPressure=dff.AtmosphericPressure/100
    return dff


# =============================================================================
#     
#     df.to_pickle("data/df3.pkl")
# =============================================================================



# =============================================================================
# 
# df= pd.read_pickle("data/df3.pkl")
# #df= pd.read_pickle("/home/vnewoivnevoimcew/Deploy/data/df2.pkl")
# #/home/yourusername/project-folder/myfile.txt
# =============================================================================

# =============================================================================
# #FORMATIEREN DER DATEN
# #einheit von luftdruck umrechnen in Bar
# #1 hPa =0.001  Bar
# dff = df.copy()
# dff.AtmosphericPressure=dff.AtmosphericPressure/100
# =============================================================================


#LABELS IN DICT
legend={}
legend['AtmosphericPressure'] = "Luftdruck (MPascal = 0.1 Bar)"
legend['AirQualityIndex'] = "Air Quality Index"
legend['T'] = "Temperature (°C)"
legend["RH"] = "relative Luftfeuchtigkeit (%)"
legend["PM2p5"] = "Feinstaubpartikel <2,5 µm Durchmesser [µg/m³]"
legend["PM1p0"] = "Feinstaubpartikel <10 µm Durchmesser [µg/m³]"
legend["DewPoint"] = "Taupunkt (°C)"
legend['timeWindowStart'] = "Datum"
legend["Datum"] = "Datum"
legend["value"] = "Messwert"
legend["Luftdruck (MPascal =0.1 Bar)"] = "Luftdruck (MPascal =0.1 Bar)"
legend["Air Quality Index"] = "Air Quality Index"
legend["Temperature (°C)"] = "Temperature (°C)"

legend2={}
legend2["value"] = "Messwert"
# legend2["variable"]= "Messwert"
# legend2['timeWindowStart'] = "Datum"
legend2['timeWindowStart'] = ""




# Python
## Extract the third row
#df.iloc[2]

def get_table_dd(dff):
    #####TABELLE DATEN ERSTELLLEN
    #returns panda series df
    dd_table=dff.iloc[-1,]
    print(dd_table)
    
    #series attributes
    #dd_table.columns  #not for series
    dd_table.dtypes  #Out[58]: dtype('O')
    dd_table.axes
    dd_table.dtypes #Out[61]: dtype('O')
    dd_table=pd.DataFrame(dd_table)
    dd_table.index
    #jetzt index als Zahl nicht namen der Variabeln
    #nachher index numerisch und alte index als colaber wemmer nöd deshalb
    #dd_table=dd_table.reset_index()
    dd_table=dd_table.reset_index(drop=True)
    print(dd_table)
    
    #make an index
    idx = pd.Index(["Datum", "rel. Luftfeuchtigkeit (%)","Temperatur (°C)",  "Feinstaubpartikel <2,5 µm [µg/m³]", "Feinstaubpartikel <10 µm [µg/m³]",'Luftdruck (MPascal = 0.1 Bar)', 'Taupunkt (°C)',"Air Quality Index"], name='')
    #idx.rename('Messwerte') kann Namen überschreiben
    dd_table=dd_table.set_index(idx)
    #assign the index we made to the series
    dd_table.reindex(idx)
    
    print(dd_table)
    #change name of the column, can make a longer list if there were more than 1 column
    dd_table.set_axis(["Aktuelle Messwerte"], axis=1, inplace=True)
    dd_table=dd_table.reset_index()
    
    #data.iloc[0] # first row of data frame 
    #data.iloc[:,0] # first column of data frame (first_name)
    print(dd_table.iloc[0])
    Datum=dd_table.iloc[0,1]
    #iso to date
    #datetime.datetime.fromisoformat('2019-01-04T16:41:24+0200')
    Datum=dt.fromisoformat(Datum)
    print(Datum)
    
    # Name: 0, dtype: object
    # 2022-08-22 14:40:00+02:00
    
    #remove Datum from tabelle
    # dd_table2=dd_table.iloc[1:,:]
    
    #datetime object to str
    # date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    # print("date and time:",date_time)
    #Datum= Datum.strftime("%d/%m/%Y, %H:%M")  #22/08/2022, 14:40
    
    Datum= Datum.strftime("%d. %b, %R")
    #print(Datum)   #22. Aug, 14:40
    
    
    #dd_table.set_axis([Datum, ""], axis=1, inplace=True)
    dd_table.set_axis(['Aktuelle Messungen vom '+ Datum+'',''], axis=1, inplace=True)
    #Zahlen runden
    #2 col alles ausser 1. reihe weil datum
    rounded=dd_table.iloc[1:,1]
    print(rounded)
    for i in range(1, len(rounded)+1):
        rounded[i]=round(rounded[i],1)
    print(rounded)
    print(dd_table)
    
    #variabeln sortieren
    
    ##### reindex or change the order of rows
     
    #df.reindex([8,11,9,2, 1, 0,7,5,6,4,10,3])
    #[0,2,7,1,3,4,6,5]
    #dd_table=dd_table.reindex([0,6,3,1,4,5,2,7])
    dd_table=dd_table.reindex([0,2,7,1,3,4,6,5])
    print(dd_table)

    return dd_table.iloc[1:,:].to_dict('records')#dd_table


def get_header():

    header = html.Div([

        # html.Div([
        #     html.Img(
        #             src = app.get_asset_url('Sensirion1.png'),
        #             height = '35 px',
        #             width = 'auto')
            
        #     ],
        #     className = 'col-2',
        #     style = {'align-items': 'center',
        #             'padding-top' : '0.6%',
        #             'height' : 'auto'}
                    

           # ), #Same as img width, allowing to have the title centrally aligned

        html.Div([
            html.H1(children='Umweltdaten bei Noser Engineering Winterthur',
                    style = {'textAlign' : 'left'
                             }
            )],
            className='col-8',
            style = {'padding-top' : '1%',
                     'padding-left' : '5%'}
        ),

        html.Div([
            html.Img(
                    src = app.get_asset_url('NoserEng_Logo_RGB.webp'),
                    height = '30 px',
                    width = 'auto',
                    style={ 'width': '60%',
                              'height': 'auto',
                              'aspect-ratio': '1200/374',
                            }
                    )
            ],
            className = 'col-2',
            style = {
                    #'align-items': 'right',
                    'text-align': 'right',
                    'padding-top' : '1.8%',
                    'height' : '3%'})
        ,
        html.Div([
            html.Img(
                    src = app.get_asset_url('Sensirion1.png'),
                    height = '35 px',
                    width = 'auto',
                    style={ 'width': '80%',
                              'height': 'auto',
                              'aspect-ratio': '280/95',
                            }
                    )
            
            ],
            className = 'col-2',
            style = {#'align-items': 'left',
                     'text-align': 'left',
                    'padding' : '1% ',
                    'height' : '3%'}
            )

        ],
        className = 'row',
        style = {'height' : '3%',
                'background-color' : corporate_colors['white']}
        )

    return header

def get_emptyrow(h='10px'):
  #  """This returns an empty row of a defined height"""

    emptyrow = html.Div([
        html.Div([
            html.Br()
        ], className = 'col-12')
    ],
    className = 'row',
    style = {'height' : h})

    return emptyrow



app.layout = html.Div(children=[
    #####################
    #Row 1 : Header
    get_header(),

    #Row 3 : Filters
    html.Div([ # External row
              
         html.Div([ # External 10-column
                  # html.H2(children = 'Verlauf der letzen 5 Tage', #"Titel",
                  #   style = {'color' : corporate_colors['sgigray12'], 'text-align' : 'left'}),

            html.Div([ # Internal row - RECAPS
                     
                          dcc.Interval(
                id='my_interval',
                disabled=False,     #if True, the counter will no longer update
                #interval=900000*2,    #every 30 min  #increment the counter n_intervals every interval milliseconds
                interval=900000*2,
                n_intervals=0,      #number of times the interval has passed
                # max_intervals=1,    #number of times the interval will be fired.
                                    #if -1, then the interval has no limit (the default)
                                    #and if 0 then the interval stops running.
    ),
        html.Div([ # Internal col-9
            
                    dcc.Graph(
                        id="time-series-chart", animate=False, 
                        style={'height': '80%'},
                        )
                    ,
 
                   
              
                          html.Div([ # Internal row

                # Chart Column
           #######anfang Kopie vom drop
                    html.Div([#"Wählen Sie Messwerte für die Graphik:" ,
                            dcc.Checklist(id="ticker",
                    
                        # #{ "label": html.Div(['Air Quality Index'], style={'color': 'Gold','border-radius' : '2px', 'border' : '1px solid #ccc', 'font-size': 20}),
                        # "value": "AirQualityIndex",
                        # },
                      options=[
                        # {"label": "Air Quality Index", "value":'AirQualityIndex' },
                           { "label": html.Div(['Temperatur (°C)'], style={'border-radius' : '0.5rem', 'border' : '0.3rem solid #B22222',
                                                                   'padding':'0rem 0.2rem', 'background-color':'#B2222298 '  #, 'opacity':'.4'
                                                                   # 'display':'block'
                                                                   #'width':'25%'
                                                                   }),
                        "value": "T",
                        },
                        { "label": html.Div(['Air Quality Index'], style={'border-radius' : '0.5rem', 'border' : '0.3rem solid #79CDCD', 
                                                                           # 'display':'block'
                                                                           #'width':'50%'
                                                                           'padding':'0rem 0.2rem' , 'background-color':'#79CDCD98 '
                                                                           }),
                        "value": "AirQualityIndex",
                        },
                        
                         { "label": html.Div(['relative Luftfeuchtigkeit (%)'], style={'border-radius' : '0.5rem', 'border' : '0.3rem solid #1874CD',
                                                                                  # 'display':'block'
                                                                                  #'width':'25%'
                                                                                  'padding':'0rem 0.2rem', 'background-color':'#1874CD98 '
                                                                                  }),
                        "value": "RH",
                        },
                        { "label": html.Div(['Feinstaubpartikel <2,5 µm Durchm.'], style={'border-radius' : '0.5rem', 'border' : '0.3rem solid #8B5A2B',
                                                                                  #'display':'block'
                                                                                 # 'width':'25%'
                                                                                 'padding':'0rem 0.2rem',  'background-color':'#8B5A2B98 '
                                                                                  }),
                        "value": "PM2p5",
                        },
                        { "label": html.Div(['Feinstaubpartikel <10 µm Durchm.'], style={'border-radius' : '0.5rem', 'border' : '0.3rem solid #F9844A',
                                                                                 # 'display':'block'
                                                                                 #'width':'25%'
                                                                                 'padding':'0rem 0.2rem',  'background-color':'#F9844A98 '
                                                                                 }),
                        "value": "PM1p0",
                        },
                        { "label": html.Div(['Taupunkt (°C)'], style={'border-radius' : '0.5rem', 'border' : '0.3rem solid #3fa34d',
                                                                 'padding':'0rem 0.2rem', 'background-color':'#3fa34d98 '
                                                                 # 'display':'block'
                                                                 #'width':'25%'
                                                                 }),
                        "value": "DewPoint", 
                        },
                         { "label": html.Div(['Luftdruck (MPascal =0.1 Bar)'], style={'border-radius' : '0.5rem', 'border' : '0.3rem solid #F9C74F', 
                                                                             # 'display':'block'
                                                                            # 'width':'25%'
                                                                            'padding':'0rem 0.2rem', 'background-color':'#F9C74F98 '
                                                                             }),
                        "value": "AtmosphericPressure",
                        },
                        # { "label": html.Div(['relative Luftfeuchtigkeit (%)'], style={'border-radius' : '0.5rem', 'border' : '0.2rem solid #4F94CD',
                        #                                                           # 'display':'block'
                        #                                                           #'width':'25%'
                        #                                                           'padding':'0rem 0.2rem', 'background-color':'#4F94CD98 '
                        #                                                           }),
                        # "value": "RH",
                        # },

                        
                     
                        # {"label": 'Luftdruck (MPascal)', "value": "AtmosphericPressure"},
                        # {"label": "relative Luftfeuchtigkeit", "value": 'RH'},
                      #   {"label": "Feinstaubpartikel <2,5 µm", "value": 'PM2p5'},
                      #   {"label": "Feinstaubpartikel <10 µm", "value": 'PM1p0'},
                      #   {"label": "Taupunkt", "value": 'DewPoint'},
                      # {"label": "Temperatur", "value": 'T'}
                       ]
                      ,
                 #use label so that what user sees can be different word than what is in the df
                #multi=True,  #allows the user to select more than 1
                value=["T",'PM2p5', "PM1p0",'RH', 'AirQualityIndex' ], #initial value the user can change that
                
                #class names refer to css properties we define in seperate css file
                className='my_box_container',           # class of the container (div)
                  style={'display':'inline-block'
                         ,'text-align':'left'
                         #, 'width': "30em"
                         #,"margin-left": "3px"
                         },             # style of the container (div)

                inputClassName='my_box_input',          # class of the <input> checkbox element, checkbox itself
                 inputStyle={'cursor':'pointer'
                             ,'margin-right': '0.4rem'
                             #, 'column-count': '2'
                             },      # style of the <input> checkbox element

                labelClassName='my_box_label',          # class of the <label> that wraps the checkbox input and the option's label
                # labelStyle={'background':'#A5D6A7',   # style of the <label> that wraps the checkbox input and the option's label
                #             'padding':'0.5rem 1rem',
                #             'border-radius':'0.5rem'},
                labelStyle = {'color' : corporate_colors['sgigray12'], 'font-size': "1.7rem"
                              , 'white-space': 'nowrap'
                              #,'padding':'0.5rem 1rem',
                              ,'padding-top':'0.5rem '
                              ,'padding-bottom':'0.5rem '
                              ,'padding-left':'1rem '
                              ,'padding-right':'1rem '
                              ,'display':'inline-flex'
                              , "margin-right": "1rem"
                              , 'font-weight':'600'
                               # ,'font-family':'Roboto'
                              #,  'column-count': '2'
                              },


                )
                            ],
               
                className = 'col-12',
                style= {'padding': '3% 0%'}
                ),

                

            ],
            className = 'row'), # Internal row
                    ],
                 
                    
                    className = 'col-9'), # Empty column
                
               # html.Div([],className = 'col-4'), # Empty column

                html.Div([  #internal col 3
                    #titel für tabelle
                       # html.H5(
                       #       children="Aktuelle Messungen :", #('+ Datum+"):",
                       #       style = {'text-align' : 'left', 'color' : corporate_colors['sgigray12']}
                       #   ),
                    html.Div([     #internal row
                              html.Div([ #internal col
                    dash_table.DataTable(
                        
                              id='tabelle',
                  # data=dd_table.iloc[1:,:].to_dict('records'),  # the contents of the table
                        # =============================================================================
#                             neu
# =============================================================================
                                # style_data={
                                #          'whiteSpace': 'normal', #first 2 should allow for text in cells to be in multiple lines
                                #          #'height': 'auto',
                                #         'lineHeight': '3px' #is in my css file
                                #     },  #style data all cells but not the header
                      ###to wrap onto multiple lines but only data not header          
# =============================================================================
#                      style_data={
#                                         'whiteSpace': 'normal',
#                                         'height': 'auto',
#                                     },
# =============================================================================
                    #for cells not header
                        style_table = {
                                        "borderRadius": "10px"
                                        , "overflow": "hidden"
                                      #  ,
                                      # 'border-collapse': 'separate !important'
                                        },
# ================works border radius for entire thing but also in header will wiss grusig=============================================================
#                         style_table = {"borderRadius": "10px"
#                                         , "overflow": "hidden"
#                                       #  ,
#                                       # 'border-collapse': 'separate !important'
#                                         },
# =============================================================================
                        style_header = {
                            # 'backgroundColor': 'transparent',
                            'background-color': corporate_colors['bg'],
                            'fontFamily' : corporate_font_family[1],
                            'font-size' : '1.5rem',
                            "font-weight" : "600",
                            'color' : corporate_colors['sgigray12'],
                            'border': '0',
                            'textAlign' : 'left',
                             'whiteSpace': 'normal',
                             'height': 'auto',
                             },
                        style_cell = {
                            #'backgroundColor': 'transparent',
                           # 'background-color': corporate_colors['white'],
                            'fontFamily' : corporate_font_family[0],
                            'font-size' : '1.2rem',
                            "font-weight" : "600",
                            'color' : corporate_colors['white'],
                            #"border": "1px solid ",
                            # 'border': '1px solid white',
                            # 'border-radius': '.5rem',
                            'textAlign' : 'left',
                            # "borderRadius": "10px",
                            # "overflow": "hidden"
                            },
                        cell_selectable = False,
                        column_selectable = False
                        ,
                        style_data_conditional=
                            # [
                                  
                            #                     {
                            #                     'if': {
                            #                         'row_index': 0} ,                                               
                            #                     'border-top-radius':'15px'}]+
                            [ 
                                                {'if': {'row_index': i}, 'background-color': table_col[i]
                                                  ,
                                                 
                                                  'border': '1px solid'+table_col[i]
                                                
                                                 } 

                            for i in range(7)],
####fix width % of 1. col
                        style_cell_conditional=[
                                                {'if': {'column_id': '' },
                                                  'width': '20%'},
                                              ]
#style_data_conditional=[{'if': {'row_index': i, 'column_id': 'COLOR'}, 'background-color': df['COLOR'][i], 'color': df['COLOR'][i]} for i in range(df.shape[0])]
#https://stackoverflow.com/questions/62175730/plotly-dash-data-table-background-color-for-individual-cell
                    )
                    ] , className = 'col-12',
                                   style=boxcol_styling),
                              ] ,           className = 'row'
                             ,
            style = recapdiv
            )
                    ,
                     html.Div([     #internal row
                          html.Div([ #internal col
                    dcc.Markdown(id="markdown", children=Markdown_Text  #block element 
                                 ,
                                 style={ "border": "1px solid black",
                                        'border-radius' : '0.5rem',
                                        'margin-top' : '1rem', #abstand von border und tabelle
                                        #margin ist zwischen border und aussen
                                        #"margin-left": "10px",
                                        "padding-bottom": ".3rem",
                                        "padding-left": ".5rem", #abstand zwischen text und border
                                        "padding-right": ".5rem",
                                        'background-color': corporate_colors['white']
                                        }  
                                 )
                    ] , className = 'col-12',
                                   style=boxcol_styling),
                              ],
                                          className = 'row',
            style = recapdiv
            ),

                ],
                       className = 'col-3'),
                 # dcc.Interval(
                 #                id='interval-component',
                 #                interval=1*1000*60*5, # every 5 Minutes in milliseconds
                 #                n_intervals=0
                 #            ),

                #html.Div([],className = 'col-4') # Empty column

            ],
            className = 'row',
            style = recapdiv
            ),
            
           #  html.Div([ # Internal row

           #      # Chart Column
           # #######anfang Kopie vom drop
           #          html.Div([#"Wählen Sie Messwerte für die Graphik:" ,
           #                  dcc.Checklist(id="ticker",
                    
           #              # #{ "label": html.Div(['Air Quality Index'], style={'color': 'Gold','border-radius' : '2px', 'border' : '1px solid #ccc', 'font-size': 20}),
           #              # "value": "AirQualityIndex",
           #              # },
           #            options=[
           #              # {"label": "Air Quality Index", "value":'AirQualityIndex' },
           #                 { "label": html.Div(['Temperatur (°C)'], style={'border-radius' : '0.5rem', 'border' : '0.2rem solid #B22222',
           #                                                         'padding':'0rem 0.2rem', 'background-color':'#B2222298 '  #, 'opacity':'.4'
           #                                                         # 'display':'block'
           #                                                         #'width':'25%'
           #                                                         }),
           #              "value": "T",
           #              },
           #              { "label": html.Div(['Air Quality Index'], style={'border-radius' : '0.5rem', 'border' : '0.2rem solid #79CDCD', 
           #                                                                 # 'display':'block'
           #                                                                 #'width':'50%'
           #                                                                 'padding':'0rem 0.2rem' , 'background-color':'#79CDCD98 '
           #                                                                 }),
           #              "value": "AirQualityIndex",
           #              },
                        
           #               { "label": html.Div(['relative Luftfeuchtigkeit (%)'], style={'border-radius' : '0.5rem', 'border' : '0.2rem solid #1874CD',
           #                                                                        # 'display':'block'
           #                                                                        #'width':'25%'
           #                                                                        'padding':'0rem 0.2rem', 'background-color':'#1874CD98 '
           #                                                                        }),
           #              "value": "RH",
           #              },
           #              { "label": html.Div(['Feinstaubpartikel <2,5 µm Durchm.'], style={'border-radius' : '0.5rem', 'border' : '0.2rem solid #8B5A2B',
           #                                                                        #'display':'block'
           #                                                                       # 'width':'25%'
           #                                                                       'padding':'0rem 0.2rem',  'background-color':'#8B5A2B98 '
           #                                                                        }),
           #              "value": "PM2p5",
           #              },
           #              { "label": html.Div(['Feinstaubpartikel <10 µm Durchm.'], style={'border-radius' : '0.5rem', 'border' : '0.2rem solid #F9844A',
           #                                                                       # 'display':'block'
           #                                                                       #'width':'25%'
           #                                                                       'padding':'0rem 0.2rem',  'background-color':'#F9844A98 '
           #                                                                       }),
           #              "value": "PM1p0",
           #              },
           #              { "label": html.Div(['Taupunkt (°C)'], style={'border-radius' : '0.5rem', 'border' : '0.2rem solid #3fa34d',
           #                                                       'padding':'0rem 0.2rem', 'background-color':'#3fa34d98 '
           #                                                       # 'display':'block'
           #                                                       #'width':'25%'
           #                                                       }),
           #              "value": "DewPoint", 
           #              },
           #               { "label": html.Div(['Luftdruck (MPascal =0.1 Bar)'], style={'border-radius' : '0.5rem', 'border' : '0.2rem solid #F9C74F', 
           #                                                                   # 'display':'block'
           #                                                                  # 'width':'25%'
           #                                                                  'padding':'0rem 0.2rem', 'background-color':'#F9C74F98 '
           #                                                                   }),
           #              "value": "AtmosphericPressure",
           #              },
           #              # { "label": html.Div(['relative Luftfeuchtigkeit (%)'], style={'border-radius' : '0.5rem', 'border' : '0.2rem solid #4F94CD',
           #              #                                                           # 'display':'block'
           #              #                                                           #'width':'25%'
           #              #                                                           'padding':'0rem 0.2rem', 'background-color':'#4F94CD98 '
           #              #                                                           }),
           #              # "value": "RH",
           #              # },

                        
                     
           #              # {"label": 'Luftdruck (MPascal)', "value": "AtmosphericPressure"},
           #              # {"label": "relative Luftfeuchtigkeit", "value": 'RH'},
           #            #   {"label": "Feinstaubpartikel <2,5 µm", "value": 'PM2p5'},
           #            #   {"label": "Feinstaubpartikel <10 µm", "value": 'PM1p0'},
           #            #   {"label": "Taupunkt", "value": 'DewPoint'},
           #            # {"label": "Temperatur", "value": 'T'}
           #             ]
           #            ,
           #       #use label so that what user sees can be different word than what is in the df
           #      #multi=True,  #allows the user to select more than 1
           #      value=["T",'PM2p5', "PM1p0",'RH', 'AirQualityIndex' ], #initial value the user can change that
                
           #      #class names refer to css properties we define in seperate css file
           #      className='my_box_container',           # class of the container (div)
           #        style={'display':'inline-block'
           #               #, 'width': "30em"
           #               #,"margin-left": "3px"
           #               },             # style of the container (div)

           #      inputClassName='my_box_input',          # class of the <input> checkbox element, checkbox itself
           #       inputStyle={'cursor':'pointer'
           #                   ,'margin-right': '0.2rem'
           #                   #, 'column-count': '2'
           #                   },      # style of the <input> checkbox element

           #      labelClassName='my_box_label',          # class of the <label> that wraps the checkbox input and the option's label
           #      # labelStyle={'background':'#A5D6A7',   # style of the <label> that wraps the checkbox input and the option's label
           #      #             'padding':'0.5rem 1rem',
           #      #             'border-radius':'0.5rem'},
           #      labelStyle = {'color' : corporate_colors['sgigray12'], 'font-size': "1.7rem"
           #                    , 'white-space': 'nowrap'
           #                    #,'padding':'0.5rem 1rem',
           #                    ,'padding-top':'0.5rem '
           #                    ,'padding-bottom':'0.5rem '
           #                    ,'padding-left':'1rem '
           #                    ,'display':'inline-flex'
           #                   # , "margin-right": "7px"
           #                    , 'font-weight':'500'
           #                     # ,'font-family':'Roboto'
           #                    #,  'column-count': '2'
           #                    },


           #      )
           #                  ],
               
           #      className = 'col-12'),

                

           #  ],
           #  className = 'row'), # Internal row
            
        ],
        className = 'col-12',
       # ),
        style = externalgraph_colstyling), # External 10-column


       

    ],
    className = 'row'), # External row

]
    ,
    # style= {'display':'flex',
    #         'flex-direction': 'column',
    #         'flex' : '1'
    #     }
    )

# @app.callback(Output(component_id="tabelle", component_property="data"),
#               Input('interval-component', 'n_intervals'))


    
@app.callback(
    [Output(component_id="tabelle", component_property="data"),
     Output(component_id="time-series-chart", component_property="figure")  ]
     ,
    [Input('my_interval', 'n_intervals'),
     Input(component_id="ticker", component_property="value")]
    #,prevent_initial_call=True
)

def get_dataupdate(n, ticker):
    if n==0:
        #dff=pd.DataFrame()
        #declare dfff empty so dont use global
        global dff
        dff=get_data()
        return get_table_dd(dff),display_time_series(ticker, dff)
    else:
        triggered_id = ctx.triggered_id
        print(triggered_id)
        if triggered_id == 'my_interval':
             #return reset_graph()
             # global dff
             dff=get_data()
            # get_table_dd(dff)
             print("interval activated")
             return get_table_dd(dff), display_time_series(ticker, dff)
            # return figure 
         #(data, figure) 
             #return     get_data(), get_table_dd(dff), display_time_series(ticker, dff)
        elif triggered_id == "ticker":
             return display_time_series(ticker, dff)
    # get_data()
    # get_table_dd(dff)
    # display_time_series(ticker, dff)
    #return data, figure
    
# #num is the n intervals so how many times 
# def update_graph(num):
#     """update every 3 seconds"""
#     if num==0:  #if interval 0 then dont update anything
#         raise PreventUpdate
#     else:
#         y_data=num
#         fig=go.Figure(data=[go.Bar(x=[1, 2, 3, 4, 5, 6, 7, 8, 9], y=[y_data]*9)],
#                       layout=go.Layout(yaxis=dict(tickfont=dict(size=22)))
#         )

#     return (y_data,fig)


# @app.callback(
#      Output(component_id="time-series-chart", component_property="figure"),
    
#     Input(component_id="ticker", component_property="value"))


def display_time_series(ticker, dff):
    #b = [a] if type(a) is str else a
    #make a str a list if it isnt already
    ticker = [ticker] if type(ticker) is str else ticker
    print(ticker)
    print(type(ticker))
    #container = "The year chosen by user was: {}".format(ticker)
    
  #container = "The year chosen by user was: {}".format(ticker)
    #1. make copy of df bc dont want to change it in the function
    #dff = df.copy()
    #say the option the user selected is going to filter the df
    #so we only pick rows with the year the user selected
    #year is a collum in hos df
    #so now only have rows with 2016 in it
    #dff = dff[dff["Year"] == option_slctd]
    #her say no matter what the user chooses we only want rows with 
    #where bees were affected by these mites that is a type pf disease
    #i only want those rows only with this disease dont want the other diseases
    #dff = dff[dff["Affected by"] == "Varroa_mites"]
    #with multi=True returns a list so this may solve the problem select only cols from df that are in that list
    #https://community.plotly.com/t/callbacks-with-a-drop-down-with-multi-select/11235/16
    dd=pd.DataFrame()
    for i in range(0,len(ticker)):
         #create df with the selected variables
        dd[ticker[i]]=dff[ticker[i]]
    dd['timeWindowStart']=dff['timeWindowStart']
    #dd['Datum']=dff['timeWindowStart']  so wäre der Name schon richtig 
    #df = px.data.stocks() # replace with your own data source
    fig = px.line(dd, x='timeWindowStart', y=ticker, labels=legend2, color_discrete_map= colormap)
    # fig.update_layout(title_text='Verlauf der letzen 5 Tage',
    #               title_font_size=30, showlegend=True, #legend_title_text="Legende", 
    
    fig.update_layout( title_text='Verlauf der letzen 5 Tage',
                 # title_font_size=30, 
                  showlegend=False, #legend_title_text="Legende",     font = {'family' : corporate_font_family},
    title = corporate_title, 

    
    font = {'family' : corporate_font_family[1]},
#     title = corporate_title,
    #title_x = 0.5, # Align chart title to center
    # paper_bgcolor =corporate_colors['bg'] , #macht box idem de graph isch farbig
    # plot_bgcolor = corporate_colors['white'],  #macht plot bg farbig aber laht grid linie wiss
    # xaxis = corporate_xaxis,
    # yaxis = corporate_yaxis,
    # height = 270,
    legend = corporate_legend,
    margin = corporate_margins
    )
    #time series doc:https://plotly.com/python/time-series/#configuring-tick-labels
# =============================================================================
#     fig.update_xaxes(
#     dtick="M1",  #so kann nur Monat anzeigen 
#     tickformat="%b\n%Y",
#     ticklabelmode="period")
# =============================================================================

    fig.for_each_trace(lambda t: t.update(#marker_color=colormap[t.name]
                                          #,
                                            name = legend[t.name],
                                            legendgroup = legend[t.name],
                                            xhoverformat="%d. %b %H:%M",
                                            # hoverlabel=legend[t.name],
                                            hovertemplate=
        # "<b>%{t.name}<br>" +
        "Messwert: %{y}<br>" +
        "Zeitpunkt: %{x}<br>"
                                            #hovertemplate = t.hovertemplate.replace(t.name, legend[t.name])
                                            #, marker_color=colormap[t.name]
                                            )
                                          )  
    # hovertemplate=
    #     "<b>%{name}<br>" +
    #     "Messwert: %{y}<br>" +
    #     "Zeitpunkt: %{x}<br>" +
    #     "Population: %{marker.size:,}" +
    #     "<extra></extra>",
    # fig.update_xaxes(    
    #     #mit nur dem beuchum ich genau de default plot scho mal guet
    # #dtick=86400000/2,  #86400000 set to 1 day so durch 2 sollte alle 12 h
    # dtick=86400000/2,  #1 pro tag angeschrieb um 12.00  sweil period
    # #tickformat="%H \n %d %b",   
    # ##%b - abbreviated month name.*
    # ##%H - hour (24-hour clock) as a decimal number [00,23].
    # #xaxis_tickformat = '%d %B (%a)<br>%Y'  #gibt Datum Mon. (Wochentag) year
    # #important /n und <br>
    # ##Date axis tick labels have the special property that any portion after the first instance of '\n' in tickformat will appear on a second line only once per unique value, as with the year numbers in the example below. To have the year number appear on every tick label, '<br>' should be used instead of '\n'.
    # ticklabelmode="period"
    # ,
    # ticks= "outside",
    # tickcolor= "black", 
    # #showticklabels = True,
    # # minor=dict(ticks="outside", 
    # #            ticklen=4, #sets lenght of line
    # #            #tickformat="%H", 
    # #             dtick=86400000/2,   #so sind 12 und 24.00 uhr eingezeichnet   # nr of milisecs in a week 7*24*60*60*1000 ,
    # #             showgrid=True)
    # )
    
# =============minor für 12 und 00 nur dat mon================================================================
    fig.update_xaxes(
    showline=True, 
    # #linewidth=2, 
    # linecolor=corporate_colors['sgigray12'],
    linecolor= '#474646',
    # gridcolor= corporate_colors['sgigray12'],
        
        #mit nur dem beuchum ich genau de default plot scho mal guet
    #dtick=86400000/2,  #86400000 set to 1 day so durch 2 sollte alle 12 h
    dtick=86400000,  #1 pro tag angeschrieb um 12.00  sweil period
    #tickformat="%R \n %d %b",  
    tickformat="%d. %b",   #mit uhr %H:%M, %d. %b",
    ##%b - abbreviated month name.*
    ##%H - hour (24-hour clock) as a decimal number [00,23].
    #xaxis_tickformat = '%d %B (%a)<br>%Y'  #gibt Datum Mon. (Wochentag) year
    #important /n und <br>
    ##Date axis tick labels have the special property that any portion after the first instance of '\n' in tickformat will appear on a second line only once per unique value, as with the year numbers in the example below. To have the year number appear on every tick label, '<br>' should be used instead of '\n'.
    ticklabelmode="period"
    ,
    ticks= "inside",
    tickcolor= corporate_colors['sgigray12'], 
    ticklen=8,
    
    #showticklabels = True,
    minor=dict(ticks="outside", 
                ticklen=2, #sets lenght of line  #was 4
                #tickformat="%H", 
                dtick=86400000/2,   #so sind 12 und 24.00 uhr eingezeichnet   # nr of milisecs in a week 7*24*60*60*1000 ,
                showgrid=True,
                # gridcolor= corporate_colors['sgigray12']
                )
    )
    fig.update_yaxes(
    showline=True, 
    #     #linewidth=2, 
    linecolor=corporate_colors['sgigray12'],
    #     #showgrid=True, gridwidth=1, 
    #     gridcolor=corporate_colors['sgigray12']
    )
    
# =============================================================================
    
    
# ===============Monthly Period Labels With Weekly Minor Ticks==============================================================
#     fig.update_xaxes(ticks= "outside",
#                  ticklabelmode= "period", 
#                  tickcolor= "black", 
#                  ticklen=10, 
#                  minor=dict(
#                      ticklen=4,  
#                      dtick=7*24*60*60*1000,  
#                      tick0="2016-07-03", 
#                      griddash='dot', 
#                      gridcolor='white')
#                 )
# =============================================================================
    
    return fig






if __name__ == '__main__':
    app.run_server()
     #app.run_server(debug=False)
     
