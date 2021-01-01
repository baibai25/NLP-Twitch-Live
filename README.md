# NLP-Twitch-Live
Natural language processing for Twitch Live  
(Experimental alpha version)
## Usage
In this alpha version, you need to some programing skills and statistical knowledge. 

1. First you need to register on the Twitch developer site.
https://dev.twitch.tv/docs/authentication#registration

2. Install dependency library (see Installation)

3. Get comment
```
python get_comment.py client-id secret-cliebt video-id
```

4. Analyze chat
```
python detect_lang.py ./data/comment_data.csv
```
- Start `jupyter lab` or `jupyter notebook`
- Open `nlp.ipynb` and run

## Installation
preparing

## Result images
<img src="./result/lang.png" width=100%>
<img src="./result/emotes.png" width=100%>
<img src="./result/freq_en.png" width=100%>
<img src="./result/collocation_network.png" width=100%>

## Previous work
https://github.com/baibai25/NLP-YouTube-Live