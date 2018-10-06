# rosi

[![TravisCI Build Status](https://api.travis-ci.com/oliverroick/rosi.svg?branch=master)](https://travis-ci.com/oliverroick/rosi) [![Requirements Status](https://requires.io/github/oliverroick/rosi/requirements.svg?branch=master)](https://requires.io/github/oliverroick/rosi/requirements/?branch=master)

ESRI's [ArcGIS API for Python](https://developers.arcgis.com/python/) does not support converting GeoJSON geometries into [ArcGIS geometries](https://esri.github.io/arcgis-python-api/apidoc/html/arcgis.geometry.html). That's what this library does: GeoJSON in – ArcGIS geometries out. 

## Usage

```python
import rosi

geojson = {
    'type': 'Point',
    'coordinates': [12.374811, 51.340652]
}
esri_geom = rosi.convert(geojson)
type(esri_geom)  # <class 'arcgis.geometry._types.Point'>
```

## Why the name _rosi_?

It's my grandmother's name and a pun on [Fiona](https://github.com/Toblerity/Fiona). I think it's funny. 
