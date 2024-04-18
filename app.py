from flask import Flask
import datetime # import the datetime library

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index(): 
  today = datetime.date.today() # Get today's date
  page = f"""<html><head><link href="static/css/style.css" rel="stylesheet" type="text/css" /></head><body>
  <h1>{today}</h1>
  <p><a href = "/home">Go home</a></p>
  <p><a href = "/portfolio">My portfolio</a></p>
  </body>
  </html>"""
  return page

@app.route('/home') 
def home(): 
  today = datetime.date.today() # Get today's date
  page = f"""<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>ExMateriae LinkTree</title>
  <link href="static/css/home.css" rel="stylesheet" type="text/css" />
</head>

  
<body>
<h3>
   <img src="static/images/arctic.jpeg" width = 50%>
</h3><h1>
EX MATERIAE
  
</h1>
<h2>{today}</h2>
  <p><li><a href="https://www.youtube.com/c/ExMateriae">
  YOUTUBE</a></li>
    <li><a href="https://twitter.com/drtournesol">TWITTER</a></li>
    <li><a href="https://www.senscritique.com/serie/Ex_Materiae/39779333">SENSCRITIQUE</a></li>
    <li><a href="https://www.facebook.com/ExMateriae">FACEBOOK</a></li>
</p>
<p><a href = "/portfolio">See my portfolio</a></p>

  <script src="script.js"></script>
  <script src="https://replit.com/public/js/replit-badge.js" theme="blue" defer></script> 
</body>

</html>
  """

  return page

@app.route('/portfolio')
def portfolio():
  page = f"""<head>
  <title>My Portfolio</title>
  <link href="static/css/portfolio.css" rel="stylesheet" type="text/css" />
</head>


<body>
<h1>Ex Materiae's Portfolio</h1>
<h2>Day 24 - RollDice</h2>

<p>Roll a random dice! It showed how a bit of code could do quite a lot and was used in impressive manners the days after.</p>

 <img src="static/images/dragon water portal.jpeg" width = 20%>
  <p><a href = "https://replit.com/@sefirosuyanou/RollDice">How many sides does your dice have?</a></p>

<h2>Day 53 - Video Game Inventory</h2>
<p>A basic working video game inventory.</p>

  <a href = "https://replit.com/@sefirosuyanou/TO-DO-List-with-priorities"><img src="static/images/ExMateriae_monocolor_4k_background_ambient_gradient_paper_look__ebd95671-cbda-4881-8562-0cff31525513.png" width = 20%></a>
  <img src="static/images/ExMateriae_monocolor_4k_background_ambient_gradient_cardboard_l_52fcdbee-d70d-493f-82df-c2a111f27fca.png" width = 20%></a>
  <p><a href = "https://replit.com/@sefirosuyanou/Day53100Days">Behold the infamous Dark saber.</a></p>
  
<h2>Day 55 - To Do List</h2>

<p>Add, edit, remove or view to do elements. It asked us to consider a large code with several subroutines.</p>

  <img src="static/images/day 55.png" width = 20%>
  <img src="static/images/ExMateriae_a_meteorite_hitting_earth_seen_from_outer_space_big__6de5342f-4008-4656-b083-4d3c4dc98e0f.png" width = 20%></a>
  <p><a href = "https://replit.com/@sefirosuyanou/TO-DO-List-with-priorities">Here's another joke.</a></p>

<h2>Day 64 - Jobs Classes Creator</h2>
<p>Use of the classes to create differents instances of characters. I knew pygame but this was a clear way of using OOP.</p>

<img src="static/images/Prince_pork_crispy_with_honey_Ukiyo-e_5d5802c5-2827-4f90-9d1b-7570a6b40f40.png" width = 20%></a>
<img src="static/images/day 64.png" width = 20%>
<p><a href = "https://replit.com/@sefirosuyanou/Classes-jobs"> Create your own experience in this new revolutionary MMORPG.(only if you want to be a generic hero, a vampire or an orc)</a></p>

<h2>Day 70 - Passwords handling</h2>

<p>This project allows users to create logins, store them and then login. It showed a very real world application.</p>

  <img src="static/images/wkqcks_korea_load_4k_highquality_b7d5fd36-1275-4cdc-b27f-89f9f3d94b2a.png" width = 20%>


<p><a href = "/home">Go back home</a></p>

</body>"""
  return page

app.run(host='0.0.0.0', port=81)