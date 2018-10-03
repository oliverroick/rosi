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


def test_multiline_is_converted():
    geojson = {
        "type": "MultiLineString",
        "coordinates": [
            [
                [12.381377, 51.34338],
                [12.382857, 51.34303],
                [12.382729, 51.34255]
            ], [
                [12.381205, 51.34271],
                [12.380840, 51.34196],
                [12.382557, 51.34179]
            ]
        ]
    }
    esri_geom = rosi.convert(geojson)
    assert esri_geom.type == 'Polyline'
    assert esri_geom.is_valid is True
    assert depth(esri_geom.paths) == 3
    assert len(esri_geom.paths) == 2
    assert len(esri_geom.paths[0]) == 3
    assert len(esri_geom.paths[1]) == 3
    assert esri_geom.paths[0] == geojson['coordinates'][0]
    assert esri_geom.paths[1] == geojson['coordinates'][1]


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


def test_multipolygon_is_converted():
    geojson = {
        "type": "MultiPolygon",
        "coordinates": [
            [
                [
                    [12.378566, 51.343494],
                    [12.378501, 51.342864],
                    [12.379617, 51.342850],
                    [12.379617, 51.343521],
                    [12.378566, 51.343494]
                ]
            ], [
                [
                    [12.379703, 51.342770],
                    [12.379703, 51.342127],
                    [12.380883, 51.342167],
                    [12.380840, 51.342770],
                    [12.379703, 51.342770]
                ]
            ]
        ]
    }
    esri_geom = rosi.convert(geojson)
    assert esri_geom.type == 'Polygon'
    assert esri_geom.is_valid is True
    assert depth(esri_geom.rings) == 3
    assert len(esri_geom.rings) == 2
    assert len(esri_geom.rings[0]) == 5
    assert len(esri_geom.rings[1]) == 5
    assert esri_geom.rings[0] == geojson['coordinates'][0][0]
    assert esri_geom.rings[1] == geojson['coordinates'][1][0]


def test_unsupported_geometry_type_throws_exception():
    geojson = {
        'type': 'Marker',
        'coordinates': [12.374811, 51.340652]
    }
    with pytest.raises(rosi.UnsupportedGeometryType) as e:
        rosi.convert(geojson, wkid=129)
        assert e.message == 'Type Marker is not supported.'
