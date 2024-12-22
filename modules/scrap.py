from bs4 import BeautifulSoup as bs
import requests
import re

class scrap():
    def __init__(self, username):
        self.username = username
    
    def fetchResponse(self):
        BASE_URL = 'https://www.geeksforgeeks.org/user/{}/'.format(self.username)

        def extract_details(soup):
            response = {}
            conding_scores = soup.find_all("div", class_ = "scoreCard_head__nxXR8")
            
            for score in conding_scores:

                title= score.find("div", class_ = "scoreCard_head_left--text__KZ2S1").text
                value = score.find("div", class_ = "scoreCard_head_left--score__oSi_x").text

                if value == "__":
                    continue
                
                title = title.replace(" ", "")
                title = ''.join(title[0].lower() + title[1:])

                response[title] = value

            return response 

        def extract_questions(soup):
            result = {}
            
            difficulties = list(filter(lambda x: x.text.split(' ')[1] != "(0)", soup.find_all("div", class_="problemNavbar_head_nav__a4K6P")))
            questions = soup.find_all("div", class_ = "problemList_head__FfRAd")

            for difficulty, question in zip(difficulties, questions):
                q_list = question.find_all("a")
                qs = list(map(lambda x: { "question": x.text, "questionUrl": x["href"] }, q_list))

                title = difficulty.text.lower().split(' ')[0]
                cnt = len(qs)

                result[title] = {
                    "count": cnt,
                    "questions": qs
                }


            return result

        profilePage = requests.get(BASE_URL)

        if profilePage.status_code == 200:
            response = {}
            solvedStats = {}
            generalInfo = {}
            soup = bs(profilePage.content, 'html.parser')

            generalInfo["userName"] = self.username
            
            profile_pic = soup.select_one("div.profilePicSection_head_img__1GLm0 img")
            instituton = soup.find("div", class_ = "educationDetails_head_left--text__tgi9I")
            institute_rank = soup.find("span", class_ = "educationDetails_head_left_userRankContainer--text__wt81s")
            languagesUsed = soup.find("div", class_ = "educationDetails_head_right--text__lLOHI")
            streak_count = soup.find("div", class_ = "circularProgressBar_head_mid_streakCnt__MFOF1 tooltipped")

            try:
                generalInfo["profilePicture"] = profile_pic.get("src")
            except:
                generalInfo["profilePicture"] = ""

            try: 
                generalInfo["institute"] = instituton.text
            except:
                generalInfo["institute"] = ""

            try:
                generalInfo["instituteRank"] = institute_rank.text
            except:
                generalInfo["instituteRank"] = ""

            try:
                generalInfo["languagesUsed"] = languagesUsed.text
            except:
                generalInfo["languagesUsed"] = ""

            try:
                streak_details = streak_count.text.replace(" ", "").split("/")
                generalInfo["currentStreak"] = streak_details[0]
                generalInfo["maxStreak"] = streak_details[1]
            except:
                generalInfo["currentStreak"] = "00"
                generalInfo["maxStreak"] = "00"


            additional_details = extract_details(soup)
            question_count_details = extract_questions(soup)
            
            for _key , _value in additional_details.items():
                generalInfo[_key] = _value

            for _key, value in question_count_details.items():
                solvedStats[_key] = value

            response["info"] = generalInfo
            response["solvedStats"] = solvedStats
            return response
        else:
            return {"error" : "Profile Not Found"}
