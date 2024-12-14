# %%
#Import
import pandas as pd
import requests
import discogs_client
import operator
import csv
import pprint
import random


#-------------------------GENRES DISCOGS
# Blues 
# Brass & Military 
# Children's 
# Classical 
# Electronic 
# Folk, World, & Country 
# Funk / Soul 
# Hip Hop 
# Jazz 
# Latin 
# Non-Music
# Pop
# Reggae
# Rock 
# Stage & Screen

#--------------------------STYLES DISCOGS

# Style:
# AOR  (32,196)
# Abstract  (127,203)
# Acid  (51,366)
# Acoustic  (117,939)
# African  (84,033)
# Alternative Rock  (465,193)
# Ambient  (349,906)
# Arena Rock  (31,955)
# Art Rock  (75,516)
# Audiobook  (26,746)
# Avant-garde Jazz  (21,979)
# Avantgarde  (66,880)
# Ballad  (331,107)
# Baroque  (117,756)
# Beat  (67,522)
# Big Band  (107,817)
# Black Metal  (190,962)
# Bluegrass  (37,924)
# Blues Rock  (182,100)
# Bolero  (57,708)
# Bollywood  (23,634)
# Boom Bap  (27,363)
# Bop  (54,873)
# Bossa Nova  (25,117)
# Breakbeat  (82,898)
# Breaks  (70,019)
# Celtic  (38,693)
# Cha-Cha  (26,426)
# Chanson  (267,860)
# Choral  (40,302)
# Classic Rock  (218,424)
# Classical  (170,216)
# Comedy  (63,327)
# Conscious  (51,684)
# Contemporary  (86,080)
# Contemporary Jazz  (100,375)
# Contemporary R&B  (70,897)
# Cool Jazz  (39,094)
# Country  (336,490)
# Country Rock  (102,874)
# Cumbia  (52,260)
# Dance-pop  (74,688)
# Dancehall  (83,290)
# Dark Ambient  (71,938)
# Darkwave  (36,546)
# Death Metal  (167,925)
# Deep House  (146,094)
# Disco  (367,993)
# Dixieland  (31,047)
# Doo Wop  (41,051)
# Doom Metal  (70,285)
# Downtempo  (210,614)
# Drone  (91,160)
# Drum n Bass  (124,904)
# Dub  (94,419)
# Dubstep  (51,489)
# Dungeon Synth  (21,777)
# EBM  (38,036)
# Easy Listening  (200,580)
# Electro  (262,297)
# Electro House  (65,039)
# Emo  (47,704)
# Euro House  (137,713)
# Eurodance  (34,225)
# Europop  (123,589)
# Experimental  (507,638)
# Field Recording  (39,821)
# Flamenco  (33,913)
# Folk  (361,148)
# Folk Rock  (235,278)
# Free Improvisation  (47,637)
# Free Jazz  (39,879)
# Funk  (204,678)
# Fusion  (76,060)
# Future Jazz  (25,425)
# Gangsta  (74,433)
# Garage House  (36,117)
# Garage Rock  (138,963)
# Glam  (56,047)
# Glitch  (24,743)
# Gospel  (137,084)
# Goth Rock  (51,349)
# Grindcore  (58,529)
# Grunge  (34,209)
# Happy Hardcore  (25,963)
# Hard Bop  (43,382)
# Hard House  (38,085)
# Hard Rock  (334,589)
# Hard Trance  (47,315)
# Hardcore  (324,413)
# Hardcore Hip-Hop  (33,622)
# Hardstyle  (29,094)
# Harsh Noise Wall  (30,133)
# Heavy Metal  (263,043)
# Hi NRG  (22,499)
# Hindustani  (30,120)
# Hip Hop  (52,087)
# Holiday  (91,470)
# House  (551,868)
# IDM  (69,492)
# Indie Pop  (101,926)
# Indie Rock  (389,069)
# Industrial  (152,880)
# Instrumental  (63,870)
# Italo-Disco  (41,082)
# Italodance  (28,337)
# J-pop  (47,408)
# Jazz-Funk  (64,564)
# Jazz-Rock  (51,003)
# Jungle  (34,258)
# Kayōkyoku  (27,962)
# Krautrock  (24,319)
# Latin  (27,429)
# Latin Jazz  (46,188)
# Laïkó  (37,470)
# Leftfield  (53,920)
# Lo-Fi  (63,054)
# MPB  (43,351)
# Merengue  (26,430)
# Metalcore  (36,442)
# Minimal  (97,988)
# Modern  (113,717)
# Modern Classical  (50,827)
# Musical  (48,083)
# Neo-Classical  (23,884)
# New Age  (54,724)
# New Wave  (168,977)
# Noise  (208,783)
# Novelty  (34,039)
# Nu Metal  (31,300)
# Oi  (38,555)
# Opera  (90,569)
# Parody  (27,542)
# Poetry  (23,594)
# Polka  (35,551)
# Pop Punk  (40,508)
# Pop Rap  (70,629)
# Pop Rock  (803,530)
# Post Bop  (37,624)
# Post Rock  (55,585)
# Post-Hardcore  (22,214)
# Post-Punk  (71,092)
# Power Metal  (26,651)
# Power Pop  (56,505)
# Prog Rock  (214,995)
# Progressive House  (115,409)
# Progressive Metal  (32,766)
# Progressive Trance  (60,140)
# Psy-Trance  (31,012)
# Psychedelic Rock  (249,217)
# Punk  (496,970)
# Radioplay  (37,201)
# Ranchera  (24,420)
# Reggae  (75,753)
# Reggae-Pop  (22,675)
# Religious  (74,258)
# Renaissance  (21,516)
# Rhythm & Blues  (175,884)
# RnB/Swing  (77,981)
# Rock & Roll  (290,225)
# Rockabilly  (66,914)
# Romantic  (254,984)
# Roots Reggae  (62,816)
# Rumba  (28,784)
# Salsa  (56,250)
# Samba  (39,490)
# Schlager  (211,575)
# Score  (65,317)
# Shoegaze  (41,071)
# Ska  (58,924)
# Smooth Jazz  (35,263)
# Soft Rock  (149,153)
# Soul  (389,848)
# Soul-Jazz  (57,041)
# Soundtrack  (237,979)
# Southern Rock  (30,723)
# Space Rock  (25,153)
# Speed Metal  (24,815)
# Spoken Word  (57,360)
# Stoner Rock  (44,457)
# Story  (40,478)
# Surf  (42,049)
# Swing  (110,127)
# Symphonic Rock  (29,954)
# Synth-pop  (442,943)
# Synthwave  (39,298)
# Tango  (40,213)
# Tech House  (141,012)
# Techno  (340,070)
# Theme  (62,529)
# Thrash  (119,205)
# Thug Rap  (23,915)
# Trance  (179,861)
# Trap  (34,743)
# Tribal  (29,565)
# Trip Hop  (44,267)
# UK Garage  (31,739)
# Vaporwave  (37,253)
# Vocal  (553,767)
# Volksmusik  (45,742)



#Discogs Client & User token
# %%
d = discogs_client.Client("ExampleApplication/0.1", user_token= "aPYjQukkBxJNCzDiALSJxttKmPMfuLmJDAVOOuKS")


# %%
def random_title1(genre, year):
    list = []
    results = d.search(genre=genre,year=year)
    for el in results:
        list.append(el)
    return pd.DataFrame(list)
   
# %%
random_title1("Hip Hop",1983)
# %%

# %%
def random_title2(genre, year):
    results = d.search(genre=genre,year=year)
    test = len(results)
    if test != 0:
        page_random = random.randint(1,results.pages)
        nb_results = len(results.page(page_random))
        k_random = random.randint(0,nb_results-1)
        return results.page(page_random)[k_random]
    else:
        return "todo"

# %%
random_title2("Reggae",1970)



#-------------------------------------------Random SELECTA

# %%
def random_genre_album(genre, year):
    results = d.search(genre=genre, year=year)
    test = len(results)
    if test != 0:
        page_random = random.randint(1,results.pages)
        nb_results = len(results.page(page_random))
        k_random = random.randint(0,nb_results-1)
        album = results.page(page_random)[k_random]
        title = album.title
        str = title.lower()
        str2 = str.replace(" ","+")
        return title, f'https://www.youtube.com/results?search_query={str2}' 
    else:
        return "todo"
    
# [0].title


# %%
random_genre_album("Hip Hop", 1982)
# %%


# %%
def random_style_album(genre,style, year):
    results = d.search(genre=genre,style=style, year=year)
    test = len(results)
    if test != 0:
        page_random = random.randint(1,results.pages)
        nb_results = len(results.page(page_random))
        k_random = random.randint(0,nb_results-1)
        album = results.page(page_random)[k_random]
        title = album.title
        image = album.images[0]["uri"]
        str = title.lower()
        str2 = str.replace(" ","+")
        return title, image, f'https://www.youtube.com/results?search_query={str2}' 
    else:
        return "todo"
    
# [0].title


# %%
random_style_album("Hip Hop","", 2005)
# %%

