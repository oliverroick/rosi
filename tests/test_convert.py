import pytest
import rosi


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


def test_unsupported_geometry_type_throws_exception():
    geojson = {
        'type': 'Marker',
        'coordinates': [12.374811, 51.340652]
    }
    with pytest.raises(rosi.UnsupportedGeometryType) as e:
        rosi.convert(geojson, wkid=129)
        assert e.message == 'Type Marker is not supported.'
