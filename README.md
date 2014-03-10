SpotOn.it SEC
======================
This is my version of the SpotOn.it SEC, based on https://docs.google.com/document/d/1sMMRtG_tIKnp4NsVpnUZFFK7scaMazfGP3n-adMFXvo/edit

This is a python package, which I wrote to be fairly modular. It has two major components: a "selecter" which chooses links from the original given URL towards event/calendar pages, and a "lister" which generates a list of event URLs from that event/calendar page.

The python package is a very basic MVP state. It's not perfect- it will return links that aren't events, and it's not the fastest program in the world, or have a good testing framework. 
That being said, it is kinda decent at finding the event links (50% to 100% depending on the source), and generally won't crash.

To use the program, load the package in python. Alternatively, run 
```
python sec_lister.py
```
in the package folder to test it on the original 4 websites given.
