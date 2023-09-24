from flask import Flask, jsonify, render_template
import requests
from numerize.numerize import numerize

CHANNELS = {
  'qazi': 'UCqrILQNl5Ed9Dz6CGMyvMTQ',
  'mrbeast': 'UCX6OQ3DkcsbYNE6H8uQQuVA',
  'mkbhd': 'UCBJycsmduvYEL83R_U4JriQ',
  'pm': 'UC3DkFux8Iv-aYnTRWzwaiBA'
}

ACTIVE_CHANNEL = CHANNELS['mkbhd']

app = Flask(__name__)


@app.route('/')
def index():
	url = "https://youtube138.p.rapidapi.com/channel/videos/"

	querystring = {"id": ACTIVE_CHANNEL, "hl": "en", "gl": "US"}

	headers = {
		"X-RapidAPI-Key": "6f87b5df1amshb0001c9166f4723p1f72dbjsn7d37107147b3",
		"X-RapidAPI-Host": "youtube138.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	data = response.json()
	contents = data['contents']
	videos = [video['video'] for video in contents if video['video']['publishedTimeText']]
	return render_template('index.html', **locals())


@app.template_filter()
def numberize(views):
	return numerize(views, 1)


@app.template_filter()
def highest_quality_image(thumbnails):
	return thumbnails[3]['url'] if len(thumbnails) >= 4 else thumbnails[0]['url']