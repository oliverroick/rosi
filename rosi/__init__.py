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

    elif geojson['type'] == 'MultiPoint':
        esri_json['points'] = geojson['coordinates']
        return geometry.MultiPoint(esri_json)

    elif geojson['type'] == 'LineString':
        esri_json['paths'] = [geojson['coordinates']]
        return geometry.Polyline(esri_json)

    else:
        msg = 'Type {} is not supported.'.format(geojson['type'])
        raise UnsupportedGeometryType(msg)
