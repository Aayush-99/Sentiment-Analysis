import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
import requests

filename = "review.csv"
f = open(filename, "w")

headers = "contributions,title,review\n"

f.write(headers)
k=0

for i in range(5,4505,5):
	myurl = f"https://www.tripadvisor.in/Hotel_Review-g60763-d99762-Reviews-or{i}-Hotel_Giraffe_by_Library_Hotel_Collection-New_York_City_New_York.html#REVIEWS"
	uClient = uReq(myurl)
	page_html = uClient.read()
	uClient.close()

	page_soup = soup(page_html,"html.parser")

	containers = page_soup.findAll("div",{"class":"hotels-community-tab-common-Card__card--ihfZB hotels-community-tab-common-Card__section--4r93H"})



	for container in containers:
		reviewer_contri = container.findAll("span",{"class":"social-member-MemberHeaderStats__bold--3z3qh"})
		contributions = (reviewer_contri[0].text)
		#helpful = (reviewer_contri[1].text)

		review_title = container.findAll("a",{"class":"location-review-review-list-parts-ReviewTitle__reviewTitleText--2tFRT"})
		title = review_title[0].text

		rev = container.findAll("div",{"class":"cPQsENeY"})
		review = rev[0].text

		#print("contributions: " + contributions)
		#print("helpful: " + helpful)
		#print("title: " + title)
		#print("review: " + review)

		f.write(contributions + "," + title.replace(",","|") + "," + review.replace(",","|") + "\n")
		print(k+1)
		k = k+1




