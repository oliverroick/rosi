from arcgis import geometry


class UnsupportedGeometryType(Exception):
    pass


def convert(geojson, wkid=4326):
    esri_json = {
         'spatialReference': {'wkid': wkid}
    }
    if geojson['type'] == 'Point':
        esri_json['x'] = geojson['coordinates'][0]
        esri_json['y'] = geojson['coordinates'][1]
        return geometry.Point(esri_json)

    else:
        msg = 'Type {} is not supported.'.format(geojson['type'])
        raise UnsupportedGeometryType(msg)
