<p align="center">
    <img src = "https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190710102234/download3.png">
	<h1 align="center">Unofficial GFG API</h1>
	<h3 align="center">An unofficial API for GeeksForGeeks for developers to make cool stuff using GFG profile data.</h3>
</p>

<p align="center">
Forked from <a href="https://github.com/arnoob16/GeeksForGeeksAPI">arnoob16/GeeksForGeeksAPI</a>
</p>

---

## Functionalities
  -  [x]  Has all the relevant data from the GFG profile page.
  -  [x]  Has the count of all the problems solved based on difficulties.
  -  [x]  Has the links & names of all the problems solved by the user segregated based on difficulties.
  -  [x]  Methods supported - `GET`

---

## Endpoints

To access the API, there is 2 endpoints, 

1. *https://geeks-for-geeks-stats.vercel.app/userdata/yourGeeksForGeeksUsername* - This endpoint will give you all the data of the user.

`Sample URL` - https://geeks-for-geeks-stats.vercel.app/userdata/sandiplowsnuf

2. *https://geeks-for-geeks-stats.vercel.app/stats/yourGeeksForGeeksUsername* - This endpoint will give you an svg image of the user's profile stats.

`Sample URL` - https://geeks-for-geeks-stats.vercel.app/stats/sandiplowsnuf

## How was it built:
The API was built using Web Scraping the profile page and a server deployed on web.

<p align=center>
    <img src = "https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>
    <img src = "https://img.shields.io/badge/Flask-FF9800?style=for-the-badge&logo=flask"/>
    <img src = "https://img.shields.io/badge/Vercel-008080?style=for-the-badge&logo=vercel"/>
</p>

---

## Instructions to run on your local system

* Pre-requisites:
	- Python 3.x
    - Install all the required libraries using the *requirements.txt* file. 
    
    ``` pip install requirements.txt ```

* Directions to execute
    - ``` python app.py``` or ``` py app.py```
    - Open the browser of your choice and visit your localhost, either *http://127.0.0.1:5000/yourGeeksForGeeksUsername* or *http://localhost:5000/yourGeeksForGeeksUsername*
    - See the API Response, understand it and build something with it.

---

### Sample API Responses


#### Sample stats Image
https://geeks-for-geeks-stats.vercel.app/stats/aganswiar

<img src="https://geeks-for-geeks-stats.vercel.app/stats/aganswiar" alt="sample image" >

--- 

#### Userdata: Success Response
https://geeks-for-geeks-stats.vercel.app/userdata/aganswiar
```
{
    "info": {
        "userName": "aganswiar",
        "profilePicture": "https://media.geeksforgeeks.org/img-practice/user_web-1598433228.svg",
        "instituteRank": "527",
        "currentStreak": "03",
        "maxStreak": "1170",
        "institution": "National Institute of Technology, Durgapur (NIT Durgapur) ",
        "languagesUsed": "C++, Java, Python",
        "campusAmbassador": "algo_artisan_sandip",
        "codingScore": "357",
        "totalProblemsSolved": "144",
        "monthlyCodingScore": "28"
    },
    "solvedStats": {
        "school": {
            "count": 0,
            "questions": []
        },
        "basic": {
            "count": 19,
            "questions": [
                {
                    "question": "Set the rightmost unset bit",
                    "questionUrl": "https://practice.geeksforgeeks.org/problems/set-the-rightmost-unset-bit4436/0"
                },
                {
                    "question": "Odd or Even",
                    "questionUrl": "https://practice.geeksforgeeks.org/problems/odd-or-even3618/0"
                },
                ...
            ]
        },
        "easy": {
            "count": 71,
            "questions": [
                {
                    "question": "Array Leaders",
                    "questionUrl": "https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/0"
                },
                {
                    "question": "Disjoint set (Union-Find)",
                    "questionUrl": "https://practice.geeksforgeeks.org/problems/disjoint-set-union-find/0"
                },
                ...
            ]
        },
        "hard": {
            "count": 1,
            "questions": [
                {
                    "question": "Alien Dictionary",
                    "questionUrl": "https://practice.geeksforgeeks.org/problems/alien-dictionary/0"
                }
            ]
        }
    }
}
``` 

#### Failure Response
```
{
    "error": "Profile Not Found"
}
```
---

#### Notes

- If you are using this, do mention about this repository in your readme, I'll also mention your project here in this repository.
- A star to the repository would be massive boost to a NOOB like me.


<p align=center>
<img src="https://forthebadge.com/images/badges/built-with-love.svg"/>
</p>
