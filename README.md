Flickrgy
========

Present a flickr slide show based on your current energy consumption. The more energy you are producing, the happier the pictures get. The more you are consuming, the more depressing and sad they get.

The page uses a [volkszaehler](http://www.volkszaehler.org/) API to get the energy readings.

To set it up, just serve the content of the ```page/``` folder with a webserver of your choice and adapt the volkszaehler API url in ```index.html```. On some volkszaehler deployments you might have to proxy volkszahler through the webserver serving the website to work around ajax request origin policies of the volkszaehler host like I had to.

Also, you will have to add your own API key in a file called ```apikey.js```
```javascript
var APIKEY = 'YOUR_API_KEY_HERE';
```

Future work
===========

* The present wordlist is not exactly well-suited for the task. I suspect a hand-curated wordlist would seriously improve results.
* The HTML is *very* prototype-y. Perhaps somebody actually knowing HTML should re-do this.
* The current selection of search criteria is still pretty basic. The google image search API could be interesting to improve this. Possible improvements include excluding uninteresting pictures like those of faces, lego figures etc.
* When you are serving this to teh internetz, you will want to proxy flickr API requests so the (secret) API key does not leave your server.

Credits
=======
The labMIT dataset is from Dodds PS, Harris KD, Kloumann IM, Bliss CA, Danforth CM (2011): Temporal Patterns of Happiness and Information in a Global Social Network: Hedonometrics and Twitter. PLoS ONE 6(12): e26752. doi:10.1371/journal.pone.0026752 ([http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0026752])

