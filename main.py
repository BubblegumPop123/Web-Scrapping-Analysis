# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#ALL IMPORTS
import lxml
from bs4 import BeautifulSoup
import urllib.request
import spacy
import matplotlib.pyplot
import numpy
from nltk.tokenize import sent_tokenize
import re
import networkx as nx
import pandas as pd
import csv
import scipy as sp

#FTN FOR SCRAPPING DATA
def webscraping(webpage, soupp):
    for data in soupp:
        all_data = data.text
        file.write(all_data)


# for Fast University
filename = "fast_parsed_data.txt"
file = open(filename, "w")
fast_webpage = urllib.request.urlopen('http://nu.edu.pk/campus/missionvision/Electrical%20Engineering')
soup = BeautifulSoup(fast_webpage, "lxml")
webscraping(fast_webpage, soup)

fast_webpage = urllib.request.urlopen('http://nu.edu.pk/vision-and-mission')
soup = BeautifulSoup(fast_webpage, "lxml")
webscraping(fast_webpage, soup)

fast_webpage = urllib.request.urlopen('http://www.nu.edu.pk/Student/Conduct')
soup = BeautifulSoup(fast_webpage, "lxml")
webscraping(fast_webpage, soup)

fast_webpage = urllib.request.urlopen('http://www.nu.edu.pk/QEC')
soup = BeautifulSoup(fast_webpage, "lxml")
webscraping(fast_webpage, soup)

fast_webpage = urllib.request.urlopen('http://www.nu.edu.pk/University/History')
soup = BeautifulSoup(fast_webpage, "lxml")
webscraping(fast_webpage, soup)
file.close()

# GIKI University
file = open("GK_parsed_data.txt", "w")
GK_webpage = urllib.request.urlopen('https://giki.edu.pk/chancellors-message/')
soup = BeautifulSoup(GK_webpage, "lxml")
webscraping(GK_webpage, soup)

GK_webpage = urllib.request.urlopen('https://giki.edu.pk/quality-enhancement-cell/')
soup = BeautifulSoup(GK_webpage, "lxml")
webscraping(GK_webpage, soup)

GK_webpage = urllib.request.urlopen('https://giki.edu.pk/presidents-message/')
soup = BeautifulSoup(GK_webpage, "lxml")
webscraping(GK_webpage, soup)

GK_webpage = urllib.request.urlopen('https://giki.edu.pk/fee/')
soup = BeautifulSoup(GK_webpage, "lxml")
webscraping(GK_webpage, soup)

GK_webpage = urllib.request.urlopen('https://giki.edu.pk/institute/')
soup = BeautifulSoup(GK_webpage, "lxml")
webscraping(GK_webpage, soup)
file.close()

# For GCU
file = open("GCU_parsed_data.txt", "w")
C_webpage = urllib.request.urlopen('https://www.gcu.edu.pk/vice_chancellor.php')
soup = BeautifulSoup(C_webpage, "lxml")
webscraping(C_webpage, soup)

C_webpage = urllib.request.urlopen('https://www.gcu.edu.pk/intl-students.php')
soup = BeautifulSoup(C_webpage, "lxml")
webscraping(C_webpage, soup)

C_webpage = urllib.request.urlopen('https://www.gcu.edu.pk/gcu-press.php')
soup = BeautifulSoup(C_webpage, "lxml")
webscraping(C_webpage, soup)

C_webpage = urllib.request.urlopen('https://www.gcu.edu.pk/financial-aid.php')
soup = BeautifulSoup(C_webpage, "lxml")
webscraping(C_webpage, soup)

C_webpage = urllib.request.urlopen('https://gcu.edu.pk/about.php')
soup = BeautifulSoup(C_webpage, "lxml")
webscraping(C_webpage, soup)
file.close()

#PART 2; FINDING NOUNS,ADJ AND VERBS
tagger = spacy.load("en_core_web_sm")
file = open("fast_parsed_data.txt", "r")
fast_txt = file.read()

fast_nouns = []
fast_verbs = []
fast_adjectives = []

tag = tagger(fast_txt)
for t in tag:
    if t.pos_ == "NOUN":
        fast_nouns.append(t)
    elif t.pos_ == "ADJ":
        fast_adjectives.append(t)
    elif t.pos_ == "VERB":
        fast_verbs.append(t)
file.close()

file = open("GCU_parsed_data.txt", "r")
gcu_txt = file.read()

gcu_nouns = []
gcu_verbs = []
gcu_adjectives = []

tag = tagger(gcu_txt)
for t in tag:
    if t.pos_ == "NOUN":
        gcu_nouns.append(t)
    elif t.pos_ == "ADJ":
        gcu_adjectives.append(t)
    elif t.pos_ == "VERB":
        gcu_verbs.append(t)

file.close()

file = open("GK_parsed_data.txt", "r")
gk_txt = file.read()

gk_nouns = []
gk_verbs = []
gk_adjectives = []

tag = tagger(gk_txt)
for t in tag:
    if t.pos_ == "NOUN":
        gk_nouns.append(t)
    elif t.pos_ == "ADJ":
        gk_adjectives.append(t)
    elif t.pos_ == "VERB":
        gk_verbs.append(t)

file.close()

#REMOVING DUPLICATES
fast_nouns_cleaned = []
gcu_nouns_cleaned = []
gk_nouns_cleaned = []

for t in fast_nouns:
    c = True
    for n in fast_nouns_cleaned:
        if str(t) == str(n):
            c = False

    if c:
        fast_nouns_cleaned.append(t)

for t in gcu_nouns:
    c = True
    for n in gcu_nouns_cleaned:
        if str(t) == str(n):
            c = False

    if c:
        gcu_nouns_cleaned.append(t)

for t in gk_nouns:
    c = True
    for n in gk_nouns_cleaned:
        if str(t) == str(n):
            c = False

    if c:
        gk_nouns_cleaned.append(t)


data = [[len(fast_nouns_cleaned), len(gcu_nouns_cleaned), len(gk_nouns_cleaned)],
             [len(fast_adjectives), len(gcu_adjectives), len(gk_adjectives)],
             [len(fast_verbs), len(gcu_verbs), len(gk_verbs)]]

#PLOTTING BAR CHART
names = ["FAST", "GCU", "GIKI"]
uni_plot_difference = [0.25, 1.25, 2.25]
X = numpy.arange(3)
fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(111)
ax.bar(X+0.00, data[0], color='r', width=0.25)
ax.bar(X+0.25, data[1], color='g', width=0.25)
ax.bar(X+0.50, data[2], color='b', width=0.25)
ax.legend(labels=["Nouns", "Adjectives", "Verbs"])
matplotlib.pyplot.xticks(uni_plot_difference, names)
matplotlib.pyplot.show()

#PART3
# removing unwanted corpus such as telephone number and emails
fast_sentences = sent_tokenize(fast_txt)
fast_sentences.pop(0)
fast_sentences.pop(0)
fast_sentences.pop(3)
fast_sentences.pop(15)
fast_sentences.pop(15)
fast_sentences.pop(15)
fast_sentences.pop(15)
fast_sentences.pop(15)
fast_sentences.pop(17)
fast_sentences.pop(17)
fast_sentences.pop(17)
fast_sentences.pop(17)
fast_sentences.pop(-1)
fast_sentences.pop(-1)
fast_sentences.pop(-4)
fast_sentences.pop(-4)
fast_sentences.pop(-4)
fast_sentences.pop(-4)


gk_sentences = sent_tokenize(gk_txt)
gk_sentences.pop(0)
gk_sentences.pop(15)
gk_sentences.pop(26)
gk_sentences.pop(26)
gk_sentences.pop(26)
gk_sentences.pop(40)
gk_sentences.pop(40)
gk_sentences.pop(-1)
gk_sentences.pop(-1)
gk_sentences.pop(-1)
gk_sentences.pop(13)
gk_sentences.pop(13)
gk_sentences.pop(22)
gk_sentences.pop(22)
gk_sentences.pop(55)

gcu_sentences = sent_tokenize(gcu_txt)
gcu_sentences.pop(0)
gcu_sentences.pop(0)
gcu_sentences.pop(13)
gcu_sentences.pop(13)
gcu_sentences.pop(13)
gcu_sentences.pop(13)
gcu_sentences.pop(13)
gcu_sentences.pop(13)
gcu_sentences.pop(18)
gcu_sentences.pop(18)
gcu_sentences.pop(18)
gcu_sentences.pop(30)
gcu_sentences.pop(30)
gcu_sentences.pop(30)
gcu_sentences.pop(30)
gcu_sentences.pop(0)
gcu_sentences.pop(-1)
gcu_sentences.pop(-1)
gcu_sentences.pop(-1)
gcu_sentences.pop(-1)
gcu_sentences.pop(-1)
gcu_sentences.pop(-6)
gcu_sentences.pop(-7)
gcu_sentences.pop(-7)
gcu_sentences.pop(44)
gcu_sentences.pop(44)
gcu_sentences.pop(44)
gcu_sentences.pop(44)
gcu_sentences.pop(44)
gcu_sentences.pop(44)
gcu_sentences.pop(44)
gcu_sentences.pop(63)
gcu_sentences.pop(63)
gcu_sentences.pop(63)
gcu_sentences.pop(63)
gcu_sentences.pop(63)
gcu_sentences.pop(63)
gcu_sentences.pop(63)
gcu_sentences.pop(63)
gcu_sentences.pop(63)
gcu_sentences.pop(63)
gcu_sentences.pop(63)
gcu_sentences.pop(63)
gcu_sentences.pop(63)
gcu_sentences.pop(63)
gcu_sentences.pop(63)
gcu_sentences.pop(63)
gcu_sentences.pop(63)
gcu_sentences.pop(63)
gcu_sentences.pop(63)
gcu_sentences.pop(63)
gcu_sentences.pop(63)

for x in zip(gk_sentences):
    print (x)

G = nx.Graph()
edges_fast=0

#GRAPH OF FAST
length_fast=len(fast_sentences)
while(length_fast):
    samp = fast_sentences[length_fast-1]
    #print(str(samp.split()))
    adjnouns=[]
    for t in (samp.split()):
        for n in fast_nouns_cleaned:
            if str(t) == str(n):
                adjnouns.append(t)
    for e in adjnouns:
        for e2 in adjnouns:
            if e!=e2:
                G.add_edge(e,e2)
                edges_fast=edges_fast+1
    #print(adjnouns)
    length_fast=length_fast-1

#FOR DEGREES OF FAST
nx.degree(G)
degrees_OFFAST = dict(nx.degree(G))
nx.set_node_attributes(G, name='degree', values=degrees_OFFAST)
degree_indataframe = pd.DataFrame(G.nodes(data='degree'), columns=['node', 'degree'])
degree_indataframe = degree_indataframe.sort_values(by='degree', ascending=False)
degree_indataframe
maxnodestoshow = 10
degree_indataframe[:maxnodestoshow].plot(x='node', y='degree', kind='barh').invert_yaxis()
matplotlib.pyplot.title("10 MAX DEGREE NOUNS WITH HIGHEST DEGREE FOR FAST")
matplotlib.pyplot.show()

matplotlib.pyplot.figure(figsize=(8,8))
nx.draw(G, with_labels=True, node_color='skyblue', width=.3, font_size=8)
matplotlib.pyplot.title("FAST")
matplotlib.pyplot.show()


edges_gcu=0
#GRAPH OF GCU
length_gcu=len(gcu_sentences)
while(length_gcu):
    samp = gcu_sentences[length_gcu-1]
    #print(str(samp.split()))
    adjnouns=[]
    for t in (samp.split()):
        for n in gcu_nouns_cleaned:
            if str(t) == str(n):
                adjnouns.append(t)
    for e in adjnouns:
        for e2 in adjnouns:
            if e!=e2:
                G.add_edge(e,e2)
                edges_gcu=edges_gcu+1
    #print(adjnouns)
    length_gcu=length_gcu-1

#FOR DEGREES OF GCU
nx.degree(G)
degrees_OFGCU = dict(nx.degree(G))
nx.set_node_attributes(G, name='degree', values=degrees_OFGCU)
degree_indataframe = pd.DataFrame(G.nodes(data='degree'), columns=['node', 'degree'])
degree_indataframe = degree_indataframe.sort_values(by='degree', ascending=False)
degree_indataframe
maxnodestoshow = 10
degree_indataframe[:maxnodestoshow].plot(x='node', y='degree', kind='barh').invert_yaxis()
matplotlib.pyplot.title("10 MAX DEGREE NOUNS WITH HIGHEST DEGREE FOR GCU")
matplotlib.pyplot.show()

matplotlib.pyplot.figure(figsize=(8,8))
nx.draw(G, with_labels=True, node_color='skyblue', width=.3, font_size=8)
matplotlib.pyplot.title("GCU")
matplotlib.pyplot.show()

edges_giki=0
#GRAPH OF GIKI
length_gk=len(gk_sentences)
while(length_gk):
    samp = gk_sentences[length_gk-1]
    #print(str(samp.split()))
    adjnouns=[]
    for t in (samp.split()):
        for n in gcu_nouns_cleaned:
            if str(t) == str(n):
                adjnouns.append(t)
    for e in adjnouns:
        for e2 in adjnouns:
            if e!=e2:
                G.add_edge(e,e2)
                edges_giki=edges_giki+1
    #print(adjnouns)
    length_gk=length_gk-1

#FOR DEGREES OF GIKI
nx.degree(G)
degrees_OFGIKI = dict(nx.degree(G))
nx.set_node_attributes(G, name='degree', values=degrees_OFGIKI)
degree_indataframe = pd.DataFrame(G.nodes(data='degree'), columns=['node', 'degree'])
degree_indataframe = degree_indataframe.sort_values(by='degree', ascending=False)
degree_indataframe
maxnodestoshow = 10
degree_indataframe[:maxnodestoshow].plot(x='node', y='degree', kind='barh').invert_yaxis()
matplotlib.pyplot.title("10 MAX DEGREE NOUNS WITH HIGHEST DEGREE FOR GIKI")
matplotlib.pyplot.show()

matplotlib.pyplot.figure(figsize=(8,8))
nx.draw(G,with_labels=True, node_color='skyblue', width=.3, font_size=8)
matplotlib.pyplot.title("GIKI")
matplotlib.pyplot.show()


#FOR CALCULATING TOTAL NUMBER OF CONNECTED COMPONENTS
print("Total Edges of Graph for FAST: ",edges_fast)   #total number of edges for fast
print("Total Edges of Graph for GCU: ",edges_gcu)    #total number of edges for GCU
print("Total Edges of Graph for GIKI: ",edges_giki)   #total number of edges for GIKI
