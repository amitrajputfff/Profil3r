<p align=center>
  <span> Find the profiles of a person on social networks, as well as their email addresses</span>
  <br>
 
  <a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"></a>
  <a target="_blank" href="LICENSE" title="License: MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
  <a target="_blank" href="https://twitter.com/AmitRaj51760706" title="Python version"><img src="https://img.shields.io/badge/-@Amitrajput-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/AmitRaj51760706"></a>
</p>

<p align="center">
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#features">Features</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#report">Report</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#contact">Contact</a>
</p>


Profil3r is an [OSINT](https://en.wikipedia.org/wiki/Open-source_intelligence) tool that allows you to find potential profiles of a person on social networks, as well as their email addresses. This program also alerts you to the presence of a data leak for the found emails.

![](https://i.imgur.com/73ZyfKE.gif)
## 💡 Prerequisite
[Python 3](https://www.python.org/)

## Installation

Install PyInquirer, jinja2 and bs4 :

```bash
pip3 install PyInquirer jinja2 bs4
``` 

Install Profil3r :

```bash
git clone https://github.com/amitrajputfff/Profil3r.git
cd Profil3r/
sudo python3 setup.py install
```
## Features

#### 📙 Domain
- [x] TLD (.com, .org, .net, etc...)

#### ✉️ Emails 
- [x] Data leaks
- [x] Emails

#### 🌐 Social

|Service      | Profile Scraping |
|-------------|------------------|
| Instagram   | Yes ✔️            |
| Facebook    | No               |
| Twitter     | Yes ✔️            |
| Tiktok      | No               |
| Pinterest   | No               |
| Linktr.ee   | Yes ✔️            |
| MySpace     | Yes ✔️            |
| Flickr      | Yes ✔️            |
| DeviantArt  | No               |
| GoodReads   | No               |

#### 🎵 Music

|Service      | Profile Scraping |
|-------------|------------------|
| Soundcloud  | No               |
| Spotify     | No               |
| Smule       | No               |

#### ‍💻 Programming

|Service      | Profile Scraping |
|-------------|------------------|
| Github      | Yes ✔️            |
| Pastebin    | Yes ✔️            |
| LessWrong   | Yes ✔️            |
| Repl.it     | No               |
| Cracked.to  | No               |

#### 💬 Forum

|Service        | Profile Scraping |
|---------------|------------------|
| 0x00sec.org   | No               |
| Hackernews    | Yes ✔️            |
| Jeuxvideo.com | Yes ✔            |

#### 🗣️ Tchat

|Service        | Profile Scraping |
|---------------|------------------|
| Skype         | No               |

#### 📺 Entertainment

|Service        | Profile Scraping |
|---------------|------------------|
| Dailymotion   | No               |
| Vimeo         | No               |

#### 🚫 Porn

|Service        | Profile Scraping |
|---------------|------------------|
| PornHub       | Yes ✔            |
| RedTube       | No               |
| XVideos       | No               |

#### 💸 Money

|Service        | Profile Scraping |
|---------------|------------------|
| BuyMeACoffee  | No               |
| Patreon       | No               |

#### 🕸️ Web Hosting

|Service        | Profile Scraping |
|---------------|------------------|
| AboutMe       | Yes ✔            |
| SlideShare    | Yes ✔            |
| WordPress     | No               |

#### 🎮 Gaming 

|Service        | Profile Scraping |
|---------------|------------------|
| Gaming        | No               |

#### 📰 Medias

|Service        | Profile Scraping |
|---------------|------------------|
| Medium        | No               |


## Report

#### JSON

A report in JSON format is automatically generated in the `reports/json` folder

#### CSV

A report in CSV format is automatically generated in the `reports/csv` folder

#### HTML

A report in HTML format is automatically generated in the `reports/html` folder, you can access it in your webbrowser

![](https://i.imgur.com/6Ts0eL4.gif)

## ⚙️ The config.json file 

You can modify the paths of the reports, the separators and the services Profil3r will search by default in the `config.json` file

| Field | Type | Default | Description |
|-----------------|--------|------------------------------------|-----------------------------------------------------------------------------------------------------|
| report_elements | Array | `["email", "facebook", "twitter"]` | List of the services for which profil3r will search |
| json_report_path | String | `"./reports/json/{}.json"` | The path of the report's JSON file, this path must include a {} which corresponds to the file name |
| html_report_path | String | `"./reports/html/{}.html"` | The path of the report's HTML file, this path must include a {} which corresponds to the file name |
| csv_report_path | String | `"./reports/csv/{}.csv"` | The path of the report's CSV file, this path must include a {} which corresponds to the file name |
separators |Object|`{"Dot": ".", "Dash": "-", "Underscore": "_"}`| List of separators to separate items, for example: `john.doe`, `john-doe`, `john_doe`|

## 📚 Example

```bash
python3 profil3r.py -p john doe
```

## 📝 License

This project is under the MIT license.

## Contact 

for any remark, suggestion or job offer, you can contact me at AmitR3245@gmail.com or on twitter [@AmitRaj51760706](https://twitter.com/AmitRaj51760706)
