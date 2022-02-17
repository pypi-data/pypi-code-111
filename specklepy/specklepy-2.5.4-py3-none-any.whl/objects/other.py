from typing import List
from specklepy.objects.geometry import Point, Vector
from .base import Base

OTHER = "Objects.Other."

IDENTITY_TRANSFORM = [
    1.0,
    0.0,
    0.0,
    0.0,
    0.0,
    1.0,
    0.0,
    0.0,
    0.0,
    0.0,
    1.0,
    0.0,
    0.0,
    0.0,
    0.0,
    1.0,
]


class RenderMaterial(Base, speckle_type=OTHER + "RenderMaterial"):
    name: str = None
    opacity: float = 1
    metalness: float = 0
    roughness: float = 1
    diffuse: int = -2894893  # light gray arbg
    emissive: int = -16777216  # black arbg


class Transform(
    Base,
    speckle_type=OTHER + "Transform",
    serialize_ignore={"translation", "scaling", "is_identity"},
):
    """The 4x4 transformation matrix

    The 3x3 sub-matrix determines scaling.
    The 4th column defines translation, where the last value is a divisor (usually equal to 1).
    """

    _value: List[float] = None

    @property
    def value(self) -> List[float]:
        """The transform matrix represented as a flat list of 16 floats"""
        return self._value

    @value.setter
    def value(self, value: List[float]) -> None:
        try:
            value = [float(x) for x in value]
        except (ValueError, TypeError):
            raise ValueError(
                f"Could not create a Transform object with the requested value. Input must be a 16 element list of numbers. Value provided: {value}"
            )
        if len(value) != 16:
            raise ValueError(
                f"Could not create a Transform object: input list should be 16 floats long, but was {len(value)} long"
            )

        self._value = value

    @property
    def translation(self) -> List[float]:
        """The final column of the matrix which defines the translation"""
        return [self._value[i] for i in (3, 7, 11, 15)]

    @property
    def scaling(self) -> List[float]:
        """The 3x3 scaling sub-matrix"""
        return [self._value[i] for i in (0, 1, 2, 4, 5, 6, 8, 9, 10)]

    @property
    def is_identity(self) -> bool:
        return self.value == IDENTITY_TRANSFORM

    def apply_to_point(self, point: Point) -> Point:
        """Transform a single speckle Point

        Arguments:
            point {Point} -- the speckle Point to transform

        Returns:
            Point -- a new transformed point
        """
        coords = self.apply_to_point_value([point.x, point.y, point.z])
        return Point(x=coords[0], y=coords[1], z=coords[2], units=point.units)

    def apply_to_point_value(self, point_value: List[float]) -> List[float]:
        """Transform a list of three floats representing a point

        Arguments:
            point_value {List[float]} -- a list of 3 floats

        Returns:
            List[float] -- the list with the transform applied
        """
        transformed = [
            point_value[0] * self._value[i]
            + point_value[1] * self._value[i + 1]
            + point_value[2] * self._value[i + 2]
            + self._value[i + 3]
            for i in range(0, 15, 4)
        ]

        return [transformed[i] / transformed[3] for i in range(3)]

    def apply_to_points(self, points: List[Point]) -> List[Point]:
        """Transform a list of speckle Points

        Arguments:
            points {List[Point]} -- the list of speckle Points to transform

        Returns:
            List[Point] -- a new list of transformed points
        """
        return [self.apply_to_point(point) for point in points]

    def apply_to_points_values(self, points_value: List[float]) -> List[float]:
        """Transform a list of speckle Points

        Arguments:
            points {List[float]} -- a flat list of floats representing points to transform

        Returns:
            List[float] -- a new transformed list
        """
        if len(points_value) % 3 != 0:
            raise ValueError(
                "Cannot apply transform as the points list is malformed: expected length to be multiple of 3"
            )
        transformed = []
        for i in range(0, len(points_value), 3):
            transformed.extend(self.apply_to_point_value(points_value[i : i + 3]))

        return transformed

    def apply_to_vector(self, vector: Vector) -> Vector:
        """Transform a single speckle Vector

        Arguments:
            point {Vector} -- the speckle Vector to transform

        Returns:
            Vector -- a new transformed point
        """
        coords = self.apply_to_vector_value([vector.x, vector.y, vector.z])
        return Vector(x=coords[0], y=coords[1], z=coords[2], units=vector.units)

    def apply_to_vector_value(self, vector_value: List[float]) -> List[float]:
        """Transform a list of three floats representing a vector

        Arguments:
            vector_value {List[float]} -- a list of 3 floats

        Returns:
            List[float] -- the list with the transform applied
        """
        return [
            vector_value[0] * self._value[i]
            + vector_value[1] * self._value[i + 1]
            + vector_value[2] * self._value[i + 2]
            for i in range(0, 15, 4)
        ][:3]

    @classmethod
    def from_list(cls, value: List[float] = None) -> "Transform":
        """Returns a Transform object from a list of 16 numbers. If no value is provided, an identity transform will be returned.

        Arguments:
            value {List[float]} -- the matrix as a flat list of 16 numbers (defaults to the identity transform)

        Returns:
            Transform -- a complete transform object
        """
        if not value:
            value = IDENTITY_TRANSFORM
        return cls(value=value)


class BlockDefinition(
    Base, speckle_type=OTHER + "BlockDefinition", detachable={"geometry"}
):
    name: str = None
    basePoint: Point = None
    geometry: List[Base] = None


class BlockInstance(
    Base, speckle_type=OTHER + "BlockInstance", detachable={"blockDefinition"}
):
    blockDefinition: BlockDefinition = None
    transform: Transform = None