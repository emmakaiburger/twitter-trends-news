#Emma Burger
#US Twitter Trends and Major News Sources
#Final Project
#SI 330: Data Manipulation, Fall 2016

from __future__ import unicode_literals
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import csv
import time
import urllib
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
tls.set_credentials_file(username='ekburger', api_key='aCVTnwZsU5sEDP7nhMvn')

# -*- encoding: utf-8 -*-

import requests
from requests_oauthlib import OAuth1
from urllib.parse import parse_qs

#define the function pretty to make the information more readable
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

#Part I. Web Scraping
#Fetch each news source's URL, and save the html in a variable. Parse the text in each html file
#using BeautifulSoup.

#a. ESPN
with urllib.request.urlopen('http://www.espn.com/') as espn_response:
    espn_doc = espn_response.read()
    espn_html = espn_doc.decode('utf8')

with open('espn.html', 'w') as outfile:
    outfile.write(espn_html)

with open('espn.html', 'r') as infile:
    html_espn = infile.read()

espn_soup = BeautifulSoup(html_espn, "html.parser")
espn_text = espn_soup.text

#b. SB Nation (Sports Blog Nation)
with urllib.request.urlopen('http://www.sbnation.com/') as sb_response:
    sb_doc = sb_response.read()
    sb_html = sb_doc.decode('utf8')

with open('sb.html', 'w') as outfile:
    outfile.write(sb_html)

with open('sb.html', 'r') as infile:
    html_sb = infile.read()

sb_soup = BeautifulSoup(html_sb, "html.parser")
sb_text = sb_soup.text

#c. Bleacher Report
with urllib.request.urlopen('http://bleacherreport.com/') as br_response:
    br_doc = br_response.read()
    br_html = br_doc.decode('utf8')

with open('br.html', 'w') as outfile:
    outfile.write(br_html)

with open('br.html', 'r') as infile:
    html_br = infile.read()

br_soup = BeautifulSoup(html_br, "html.parser")
br_text = br_soup.text

#d. Fox Sports
with urllib.request.urlopen('http://www.foxsports.com/') as foxsports_response:
    foxsports_doc = foxsports_response.read()
    foxsports_html = foxsports_doc.decode('utf8')

with open('foxsports.html', 'w') as outfile:
    outfile.write(foxsports_html)

with open('foxsports.html', 'r') as infile:
    html_foxsports = infile.read()

foxsports_soup = BeautifulSoup(html_foxsports, "html.parser")
foxsports_text = foxsports_soup.text

#e. NBC Sports
with urllib.request.urlopen('http://www.nbcsports.com/') as nbc_response:
    nbc_doc = nbc_response.read()
    nbc_html = nbc_doc.decode('utf8')

with open('nbc.html', 'w') as outfile:
    outfile.write(nbc_html)

with open('nbc.html', 'r') as infile:
    html_nbc = infile.read()

nbc_soup = BeautifulSoup(html_nbc, "html.parser")
nbc_text = nbc_soup.text

#f. CBS Sports
with urllib.request.urlopen('http://www.cbssports.com/') as cbs_response:
    cbs_doc = cbs_response.read()
    cbs_html = cbs_doc.decode('utf8')

with open('cbs.html', 'w') as outfile:
    outfile.write(cbs_html)

with open('cbs.html', 'r') as infile:
    html_cbs = infile.read()

cbs_soup = BeautifulSoup(html_cbs, "html.parser")
cbs_text = cbs_soup.text

#g. Yahoo Sports
with urllib.request.urlopen('http://sports.yahoo.com/') as ys_response:
    ys_doc = ys_response.read()
    ys_html = ys_doc.decode('utf8')

with open('ys.html', 'w') as outfile:
    outfile.write(ys_html)

with open('ys.html', 'r') as infile:
    html_ys = infile.read()

ys_soup = BeautifulSoup(html_ys, "html.parser")
ys_text = ys_soup.text

#h. The Huddle
with urllib.request.urlopen('http://thehuddle.com/') as huddle_response:
    huddle_doc = huddle_response.read()
    huddle_html = huddle_doc.decode('utf8')

with open('huddle.html', 'w') as outfile:
    outfile.write(huddle_html)

with open('huddle.html', 'r') as infile:
    html_huddle = infile.read()

huddle_soup = BeautifulSoup(html_huddle, "html.parser")
huddle_text = huddle_soup.text

#i. Sports Illustrated
with urllib.request.urlopen('http://www.si.com/') as si_response:
    si_doc = si_response.read()
    si_html = si_doc.decode('utf8')

with open('si.html', 'w') as outfile:
    outfile.write(si_html)

with open('si.html', 'r') as infile:
    html_si = infile.read()

si_soup = BeautifulSoup(html_si, "html.parser")
si_text = si_soup.text

#j. FiveThirtyEight
with urllib.request.urlopen('http://fivethirtyeight.com/') as fivethirtyeight_response:
    fivethirtyeight_doc = fivethirtyeight_response.read()
    fivethirtyeight_html = fivethirtyeight_doc.decode('utf8')

with open('fivethirtyeight.html', 'w') as outfile:
    outfile.write(fivethirtyeight_html)

with open('fivethirtyeight.html', 'r') as infile:
    html_fivethirtyeight = infile.read()

fivethirtyeight_soup = BeautifulSoup(html_fivethirtyeight, "html.parser")
fivethirtyeight_text = fivethirtyeight_soup.text

#k. CNN
with urllib.request.urlopen('http://www.cnn.com/') as cnn_response:
    cnn_doc = cnn_response.read()
    cnn_html = cnn_doc.decode('utf8')

with open('cnn.html', 'w') as outfile:
    outfile.write(cnn_html)

with open('cnn.html', 'r') as infile:
    html_cnn = infile.read()

cnn_soup = BeautifulSoup(html_cnn, "html.parser")
cnn_text = cnn_soup.text

#l. FOX News
with urllib.request.urlopen('http://www.foxnews.com/') as foxnews_response:
    foxnews_doc = foxnews_response.read()
    foxnews_html = foxnews_doc.decode('utf8')

with open('foxnews.html', 'w') as outfile:
    outfile.write(foxnews_html)

with open('foxnews.html', 'r') as infile:
    html_foxnews = infile.read()

foxnews_soup = BeautifulSoup(html_foxnews, "html.parser")
foxnews_text = foxnews_soup.text

#m. MSNBC
with urllib.request.urlopen('http://www.msnbc.com/') as msnbc_response:
    msnbc_doc = msnbc_response.read()
    msnbc_html = msnbc_doc.decode('utf8')

with open('msnbc.html', 'w') as outfile:
    outfile.write(msnbc_html)

with open('msnbc.html', 'r') as infile:
    html_msnbc = infile.read()

msnbc_soup = BeautifulSoup(html_msnbc, "html.parser")
msnbc_text = msnbc_soup.text

#n. Yahoo News
with urllib.request.urlopen('https://www.yahoo.com/') as yahoo_response:
    yahoo_doc = yahoo_response.read()
    yahoo_html = yahoo_doc.decode('utf8')

with open('yahoo.html', 'w') as outfile:
    outfile.write(yahoo_html)

with open('yahoo.html', 'r') as infile:
    html_yahoo = infile.read()

yahoo_soup = BeautifulSoup(html_yahoo, "html.parser")
yahoo_text = yahoo_soup.text

#o. The Huffington Post
with urllib.request.urlopen('http://www.huffingtonpost.com/') as huffpo_response:
    huffpo_doc = huffpo_response.read()
    huffpo_html = huffpo_doc.decode('utf8')

with open('huffpo.html', 'w') as outfile:
    outfile.write(huffpo_html)

with open('huffpo.html', 'r') as infile:
    html_huffpo = infile.read()

huffpo_soup = BeautifulSoup(html_huffpo, "html.parser")
huffpo_text = huffpo_soup.text

#p. The New York Times
with urllib.request.urlopen('http://www.nytimes.com/?WT.z_jog=1&hF=t&vS=undefined') as nyt_response:
    nyt_doc = nyt_response.read()
    nyt_html = nyt_doc.decode('utf8')

with open('nyt.html', 'w') as outfile:
    outfile.write(nyt_html)

with open('nyt.html', 'r') as infile:
    html_nyt = infile.read()

nyt_soup = BeautifulSoup(html_nyt, "html.parser")
nyt_text= nyt_soup.text

#q. Politico
with urllib.request.urlopen('http://www.politico.com/') as politico_response:
    politico_doc = politico_response.read()
    politico_html = politico_doc.decode('utf8')

with open('politico.html', 'w') as outfile:
    outfile.write(politico_html)

with open('politico.html', 'r') as infile:
    html_politico = infile.read()

politico_soup = BeautifulSoup(html_politico, "html.parser")
politico_text = politico_soup.text

#r. Refinery29
with urllib.request.urlopen('http://www.refinery29.com/') as r29_response:
    r29_doc = r29_response.read()
    r29_html = r29_doc.decode('utf8')

with open('r29.html', 'w') as outfile:
    outfile.write(r29_html)

with open('r29.html', 'r') as infile:
    html_r29 = infile.read()

r29_soup = BeautifulSoup(html_r29, "html.parser")
r29_text = r29_soup.text

#s. Buzzfeed
with urllib.request.urlopen('https://www.buzzfeed.com/') as bf_response:
    bf_doc = bf_response.read()
    bf_html = bf_doc.decode('utf8')

with open('bf.html', 'w') as outfile:
    outfile.write(bf_html)

with open('bf.html', 'r') as infile:
    html_bf = infile.read()

bf_soup = BeautifulSoup(html_bf, "html.parser")
bf_text = bf_soup.text

#t. People Magazine
with urllib.request.urlopen('http://people.com/') as people_response:
    people_doc = people_response.read()
    people_html = people_doc.decode('utf8')

with open('people.html', 'w') as outfile:
    outfile.write(people_html)

with open('people.html', 'r') as infile:
    html_people = infile.read()

people_soup = BeautifulSoup(html_people, "html.parser")
people_text = people_soup.text

#Part II. Twitter API

#Used some code below from Thomas Sileo at https://thomassileo.name/blog/2013/01/25/using-twitter-rest-api-v1-dot-1-with-python/
#Provide authorization information from Twitter's API

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "gytQSUKbP8va9XOPW6PUSXlNq"
CONSUMER_SECRET = "VwYLVQXhV08eb7sovWTownfSyZoEodXMRAiOr8cY5LmSdmXCwi"

OAUTH_TOKEN = "868387074-CJjDPafisj5xJMIW3kj8WFLrztTSVCDEtCI7AtaM"
OAUTH_TOKEN_SECRET = "d8ex3vE3WDPsdGTQ6ed8Tqv6hfrGGYIEdBj0H1Vgh4POT"

#Authorize my application via identifier
def setup_oauth():
    # Provide and parse request token
    oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)

    resource_owner_key = credentials.get('oauth_token')[0]
    resource_owner_secret = credentials.get('oauth_token_secret')[0]

    #Authorize API user
    authorize_url = AUTHORIZE_URL + resource_owner_key
    print('Please go here and authorize: ' + authorize_url)

    verifier = raw_input('Please input the verifier: ')
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

    #Obtain the access token
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    token = credentials.get('oauth_token')[0]
    secret = credentials.get('oauth_token_secret')[0]

    return token, secret

#Define and call the function get_oauth
def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

#Run code contained in main function, retrieving top nationwide Twitter trends, excluding hashtags
if __name__ == "__main__":
    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print("OAUTH_TOKEN: " + token)
        print("OAUTH_TOKEN_SECRET: " + secret)
    else:
        oauth = get_oauth()
        USA = requests.get(url="https://api.twitter.com/1.1/trends/place.json?exclude=hashtags&id=23424977", auth=oauth)

        #Iterate through the list of top nationwide Twitter trends and append them to the trend_list
        json_data = json.loads(USA.text)
        trend_list = []
        for item in json_data:
            trends = item.get("trends")
            for x in trends:
                trend = x.get("name")
                if "#" in trend:
                    trend = trend[1:]
                trend_list.append(trend)

        print(trend_list)
        #print(len(trend_list))

        time.sleep(30)

#For each news source, count the occurences of Twitter trends from the trend_list that appear on
# their homepage

        #a. ESPN
        espn_count = 0
        for word in trend_list:
            if word in espn_text:
                espn_count += 1
        espn_count = str(espn_count)
        espn_count = int(espn_count)
        espn_overlap = int((espn_count / len(trend_list)) * 100)
        print(("ESPN overlap with Twitter Trends: ") + str(espn_overlap) + "%")

        #b. SB Nation
        sb_count = 0
        for word in trend_list:
            if word in sb_text:
                sb_count += 1
        sb_count = str(sb_count)
        sb_count = int(sb_count)
        sb_overlap = int((sb_count / len(trend_list)) * 100)
        print(("SB Nation overlap with Twitter Trends: ") + str(sb_overlap) + "%")

        #c. Bleacher Report
        br_count = 0
        for word in trend_list:
            if word in br_text:
                br_count += 1
        br_count = str(br_count)
        br_count = int(br_count)
        br_overlap = int((br_count / len(trend_list)) * 100)
        print(("Bleacher Report overlap with Twitter Trends: ") + str(br_overlap) + "%")

        #d. FOX Sports
        foxsports_count = 0
        for word in trend_list:
            if word in foxsports_text:
                foxsports_count += 1
        foxsports_count = str(foxsports_count)
        foxsports_count = int(foxsports_count)
        foxsports_overlap = int((foxsports_count / len(trend_list)) * 100)
        print(("FOX Sports overlap with Twitter Trends: ") + str(foxsports_overlap) + "%")

        #e. NBC Sports
        nbc_count = 0
        for word in trend_list:
            if word in nbc_text:
                nbc_count += 1
        nbc_count = str(nbc_count)
        nbc_count = int(nbc_count)
        nbc_overlap = int((nbc_count / len(trend_list)) * 100)
        print(("NBC Sports overlap with Twitter Trends: ") + str(nbc_overlap) + "%")

        #f. CBS Sports
        cbs_count = 0
        for word in trend_list:
            if word in cbs_text:
                cbs_count += 1
        cbs_count = str(cbs_count)
        cbs_count = int(cbs_count)
        cbs_overlap = int((cbs_count / len(trend_list)) * 100)
        print(("CBS Sports overlap with Twitter Trends: ") + str(cbs_overlap) + "%")

        #g. Yahoo Sports
        ys_count = 0
        for word in trend_list:
            if word in ys_text:
                ys_count += 1
        ys_count = str(ys_count)
        ys_count = int(ys_count)
        ys_overlap = int((ys_count / len(trend_list)) * 100)
        print(("Yahoo Sports overlap with Twitter Trends: ") + str(ys_overlap) + "%")

        #h. The Huddle
        huddle_count = 0
        for word in trend_list:
            if word in huddle_text:
                huddle_count += 1
        huddle_count = str(huddle_count)
        huddle_count = int(huddle_count)
        huddle_overlap = int((huddle_count / len(trend_list)) * 100)
        print(("The Huddle overlap with Twitter Trends: ") + str(huddle_overlap) + "%")

        #i. Sports Illustrated
        si_count = 0
        for word in trend_list:
            if word in si_text:
                si_count += 1
        si_count = str(si_count)
        si_count = int(si_count)
        si_overlap = int((si_count / len(trend_list)) * 100)
        print(("Sports Illustrated overlap with Twitter Trends: ") + str(si_overlap) + "%")

        #j. FiveThirtyEight
        fivethirtyeight_count = 0
        for word in trend_list:
            if word in fivethirtyeight_text:
                fivethirtyeight_count += 1
        fivethirtyeight_count = str(fivethirtyeight_count)
        fivethirtyeight_count = int(fivethirtyeight_count)
        fivethirtyeight_overlap = int((fivethirtyeight_count / len(trend_list)) * 100)
        print(("FiveThirtyEight overlap with Twitter Trends: ") + str(fivethirtyeight_overlap) + "%")

        #k. CNN
        cnn_count = 0
        for word in trend_list:
            if word in cnn_text:
                cnn_count += 1
        cnn_count = str(cnn_count)
        cnn_count = int(cnn_count)
        cnn_overlap = int((cnn_count / len(trend_list)) * 100)
        print(("CNN overlap with Twitter Trends: ") + str(cnn_overlap) + "%")

        #l. FOX News
        foxnews_count = 0
        for word in trend_list:
            if word in foxnews_text:
                foxnews_count += 1
        foxnews_count = str(foxnews_count)
        foxnews_count = int(foxnews_count)
        foxnews_overlap = int((foxnews_count / len(trend_list)) * 100)
        print(("FOX News overlap with Twitter Trends: ") + str(foxnews_overlap) + "%")

        #m. MSNBC News
        msnbc_count = 0
        for word in trend_list:
            if word in msnbc_text:
                msnbc_count += 1
        msnbc_count = str(msnbc_count)
        msnbc_count = int(msnbc_count)
        msnbc_overlap = int((msnbc_count / len(trend_list)) * 100)
        print(("MSNBC overlap with Twitter Trends: ") + str(msnbc_overlap) + "%")

        #n. Yahoo News
        yahoo_count = 0
        for word in trend_list:
            if word in yahoo_text:
                yahoo_count += 1
        yahoo_count = str(yahoo_count)
        yahoo_count = int(yahoo_count)
        yahoo_overlap = int((yahoo_count / len(trend_list)) * 100)
        print(("Yahoo News overlap with Twitter Trends: ") + str(yahoo_overlap) + "%")

        #o. Huffington Post
        huffpo_count = 0
        for word in trend_list:
            if word in huffpo_text:
                huffpo_count += 1
        huffpo_count = str(huffpo_count)
        huffpo_count = int(huffpo_count)
        huffpo_overlap = int((huffpo_count / len(trend_list)) * 100)
        print(("Huffington Post overlap with Twitter Trends: ") + str(huffpo_overlap) + "%")

        #p. The New York Times
        nyt_count = 0
        for word in trend_list:
            if word in nyt_text:
                nyt_count += 1
        nyt_count = str(nyt_count)
        nyt_count = int(nyt_count)
        nyt_overlap = int((nyt_count/len(trend_list))*100)
        print(("New York Times overlap with Twitter Trends: ") + str(nyt_overlap) + "%")

        #q. Politico
        politico_count = 0
        for word in trend_list:
            if word in politico_text:
                politico_count += 1
        politico_count = str(politico_count)
        politico_count = int(politico_count)
        politico_overlap = int((politico_count / len(trend_list)) * 100)
        print(("Politico overlap with Twitter Trends: ") + str(politico_overlap) + "%")

        #r. Refinery29
        r29_count = 0
        for word in trend_list:
            if word in r29_text:
                r29_count += 1
        r29_count = str(r29_count)
        r29_count = int(r29_count)
        r29_overlap = int((r29_count / len(trend_list)) * 100)
        print(("Refinery29 overlap with Twitter Trends: ") + str(r29_overlap) + "%")

        #s. Buzzfeed
        bf_count = 0
        for word in trend_list:
            if word in bf_text:
                bf_count += 1
        bf_count = str(bf_count)
        bf_count = int(bf_count)
        bf_overlap = int((bf_count / len(trend_list)) * 100)
        print(("Buzzfeed overlap with Twitter Trends: ") + str(bf_overlap) + "%")

        #t. People Magazine
        people_count = 0
        for word in trend_list:
            if word in people_text:
                people_count += 1
        people_count = str(people_count)
        people_count = int(people_count)
        people_overlap = int((people_count / len(trend_list)) * 100)
        print(("People Magazine overlap with Twitter Trends: ") + str(people_overlap) + "%")

#Create a CSV file which stores the name of each news source and its corresponding percentage representing
#the news source homepage's overlap with US Twitter trends
with open('outputfile.csv', 'w', newline='') as csvfile:
    fieldnames=['ESPN', 'SB Nation', 'Bleacher Report', 'FOX Sports', 'NBC Sports', 'CBS Sports', 'Yahoo Sports',
                'The Huddle', 'Sports Illustrated', 'FiveThirtyEight', 'CNN', 'FOX News', 'MSNBC', 'Yahoo News',
                'The Huffington Post', 'The New York Times', 'Politico', 'Refinery29', 'BuzzFeed', 'People Magazine']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'ESPN': espn_overlap, 'SB Nation': sb_overlap, 'Bleacher Report': br_overlap,
                     'FOX Sports': foxsports_overlap, 'NBC Sports': nbc_overlap, 'CBS Sports': cbs_overlap,
                     'Yahoo Sports': ys_overlap, 'The Huddle': huddle_overlap, 'Sports Illustrated': si_overlap,
                     'FiveThirtyEight': fivethirtyeight_overlap, 'CNN': cnn_overlap, 'FOX News': foxnews_overlap,
                     'MSNBC': msnbc_overlap, 'Yahoo News': yahoo_overlap, 'The Huffington Post': huffpo_overlap,
                     'The New York Times': nyt_overlap, 'Politico': politico_overlap, 'Refinery29': r29_overlap,
                     'BuzzFeed': bf_overlap, 'People Magazine': people_overlap})

#Send the data to plotly to input into the graph
data = [go.Bar(x = ['ESPN', 'SB Nation', 'Bleacher Report', 'FOX Sports', 'NBC Sports', 'CBS Sports', 'Yahoo Sports',
                    'The Huddle', 'Sports Illustrated', 'FiveThirtyEight', 'CNN', 'FOX News', 'MSNBC', 'Yahoo News',
                    'The Huffington Post', 'The New York Times', 'Politico', 'Refinery29', 'BuzzFeed', 'People Magazine'],
               y = [espn_overlap, sb_overlap, br_overlap, foxsports_overlap, nbc_overlap, cbs_overlap, ys_overlap,
                    huddle_overlap, si_overlap, fivethirtyeight_overlap, cnn_overlap, foxnews_overlap, msnbc_overlap,
                    yahoo_overlap, huffpo_overlap, nyt_overlap, politico_overlap, r29_overlap, bf_overlap, people_overlap])]

#Send the desired layout information to plotly to format the graph
layout = go.Layout(yaxis=dict(
        title='Percentage Overlap with Twitter Trends',
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,
        tickangle=45,
        tickfont=dict(
            family='Old Standard TT, serif',
            size=14,
            color='black'
        ),
        exponentformat='e',
        showexponent='All'
    )
)

#Render the graph in plotly and print a url that directs users to said graph
fig = go.Figure(data = data , layout = layout)
py.iplot(fig, filename='basic-bar')
