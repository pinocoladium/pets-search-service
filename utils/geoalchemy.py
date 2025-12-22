from geoalchemy2 import Geometry, WKBElement
from geoalchemy2.shape import to_shape
from shapely import Point

from utils.constants import DEFAULT_SRID


class BaseGeometry(Geometry):
    geometry_type: str
    srid: int = DEFAULT_SRID
    as_binary = 'ST_AsEWKB'

    def __init__(self, *args, **kwargs) -> None:
        kwargs['geometry_type'] = self.geometry_type
        kwargs['srid'] = self.srid
        super().__init__(*args, **kwargs)


class PointField(BaseGeometry):
    geometry_type = 'POINT'

    def result_processor(self, dialect, coltype):
        def process(value) -> Point:
            if value is not None:
                return to_shape(WKBElement(value, self.srid, self.extended))

        return process

    def bind_processor(self, dialect):
        def process(value) -> str:
            if value is not None:
                return f"SRID={self.srid};POINT({value.x} {value.y})"

        return process
