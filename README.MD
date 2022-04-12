<h1 align="center">porngen - Porn content search module.</h1>

<br>

<h1 align="center"> -How to use?- </h1>

```python
import porngen as pg
from random import choice

categories = pg.getCategories() #get categories
videos = pg.getVideos(choice(categories)) #get videos from random category
videos = pg.getVideos(choice(categories), True) #get all videos from all pages
videos = pg.getVideos(choice(categories), False, 10) #get up to 10 videos

#Get videos with by model name:
videos = pg.getVideos('Peta Jensen', False, 3) #get up to 3 videos with Peta Jensen

#videos variable contains direct lins on video
```