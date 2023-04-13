from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS, XSD, FOAF
from hashlib import md5

import os, re

def dumpdata(request, uri_fragment, format):
	uri = settings.BASE_URI + uri_fragment
	url = request.build_absolute_uri('?')
	hash = md5(uri.encode('utf8')).hexdigest()
	ttl_file = os.path.join(settings.RDF_ROOT, hash[0], hash + '.ttl')
	if not(os.path.exists(ttl_file)):
		raise Http404
	g = Graph()
	data = ''
	with open(ttl_file, 'r') as fp:
		for l in fp.readlines():
			data = data + re.sub(r'\\+$', '', l)
	g.parse(data=data, format='ttl')
	g.add((URIRef(url), FOAF.primaryTopic, URIRef(uri)))
	if format == 'ttl':
		return HttpResponse(g.serialize(format='turtle'), content_type='application/rdf+turtle')
	if format == 'rdf':
		return HttpResponse(g.serialize(format='pretty-xml'), content_type='application/rdf+xml')
	if format == 'json':
		return HttpResponse(g.serialize(format='json-ld'), content_type='application/json')
	if format == 'nt':
		return HttpResponse(g.serialize(format='nt'), content_type='application/ntriples')
	raise Http404
