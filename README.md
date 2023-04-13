# Linked Data Website

The purpose of this Django project is to serve as a starting point for creating a linked data-based site. I tend to like RDF but I'm not a massive fan of triple stores, so this is the 'static site' version of a linked data site.

Firstly, I recommend using [Hedgehog](https://github.com/ads04r/Hedgehog/tree/v2). It does a good job of crunching RDF into datasets, and v2 will output the flat file RDF format required. Once you've done this, put the files in the `media/rdf` directory. Then configure your Django variables (allowed hosts, etc) and run the server. Calling URIs with .rdf, .json, .ttl or .nt extensions should now return the appropriately formatted RDF data.

To build a website on top, create a second app. The ldwebsite app is designed to be a bolt-on.


