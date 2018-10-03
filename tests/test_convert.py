import pytest
import rosi

from .util import depth


def test_wkid_is_set():
    geojson = {
        'type': 'Point',
        'coordinates': [12.374811, 51.340652]
    }
    esri_geom = rosi.convert(geojson, wkid=129)
    assert esri_geom.spatialReference['wkid'] == 129


def test_point_is_converted():
    x = 12.374811
    y = 51.340652
    geojson = {
        'type': 'Point',
        'coordinates': [x, y]
    }
    esri_geom = rosi.convert(geojson)
    assert esri_geom.type == 'Point'
    assert esri_geom.x == x
    assert esri_geom.y == y


def test_multipoint_is_converted():
    geojson = {
       'type': 'MultiPoint',
       'coordinates': [
           [12.374811, 51.340652], [12.375476, 51.338521]
       ]
    }
    esri_geom = rosi.convert(geojson)
    assert esri_geom.type == 'Multipoint'
    assert esri_geom.points == geojson['coordinates']


def test_line_is_converted():
    geojson = {
        "type": "LineString",
        "coordinates": [
            [12.381463, 51.343346],
            [12.382900, 51.342984],
            [12.382535, 51.341993],
            [12.382578, 51.341510]
        ]
    }
    esri_geom = rosi.convert(geojson)
    assert esri_geom.type == 'Polyline'
    assert esri_geom.is_valid is True
    assert depth(esri_geom.paths) == 3
    assert len(esri_geom.paths) == 1
    assert len(esri_geom.paths[0]) == 4
    assert esri_geom.paths[0] == geojson['coordinates']


def test_polygon_is_converted():
    geojson = {
        "type": "Polygon",
        "coordinates": [
            [
                [12.3788022, 51.343521],
                [12.3782229, 51.342810],
                [12.3796176, 51.342341],
                [12.3802185, 51.343011],
                [12.3788022, 51.343521]
            ]
        ]
    }
    esri_geom = rosi.convert(geojson)
    assert esri_geom.type == 'Polygon'
    assert esri_geom.is_valid is True
    assert depth(esri_geom.rings) == 3
    assert len(esri_geom.rings) == 1
    assert len(esri_geom.rings[0]) == 5
    assert esri_geom.rings[0] == geojson['coordinates'][0]


def test_unsupported_geometry_type_throws_exception():
    geojson = {
        'type': 'Marker',
        'coordinates': [12.374811, 51.340652]
    }
    with pytest.raises(rosi.UnsupportedGeometryType) as e:
        rosi.convert(geojson, wkid=129)
        assert e.message == 'Type Marker is not supported.'
