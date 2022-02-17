from swmm_api.input_file.macros import calc_slope, get_link_tags, nodes_dict
from swmm_api.input_file.sections import CrossSection, Loss, Vertices
from swmm_api.input_file.sections.link import _Link, Conduit, Orifice, Outlet, Pump, Weir
from swmm_api import SwmmInput
import shape_generator


class SuperConduit(Conduit, CrossSection, Loss, Vertices):
    def __init__(self, inp, conduit, cross_section, loss=None, vertices=None, tag=None):
        self.inp = inp
        Conduit.__init__(self, **conduit.to_dict_())
        CrossSection.__init__(self, **cross_section.to_dict_())
        if loss is not None:
            Loss.__init__(self, **loss.to_dict_())
        if vertices is not None:
            Vertices.__init__(self, **vertices.to_dict_())
        self.tag = tag

        self._nodes = nodes_dict(self.inp)

    @classmethod
    def from_inp(cls, inp, label):
        """

        Args:
            inp (swmm_api.SwmmInput):
            label:

        Returns:

        """
        if label in inp.CONDUITS:
            loss = None
            if label in inp.LOSSES:
                loss = inp.LOSSES[label]

            vertices = None
            if label in inp.VERTICES:
                vertices = inp.VERTICES[label]
            tag = None
            tags = get_link_tags(inp)
            if label in tags:
                tag = tags[label]
            return cls(inp, inp.CONDUITS[label], inp.XSECTIONS[label], loss, vertices, tag)

    @property
    def curve_obj(self):
        if self.Shape == CrossSection.SHAPES.CUSTOM:
            return self.inp.CURVES[self.Curve]

    @property
    def shape_generator(self):
        if self.Shape == CrossSection.SHAPES.CUSTOM:
            return shape_generator.CrossSection.from_curve(self.curve_obj, height=self.Geom1)
        elif self.Shape == CrossSection.SHAPES.IRREGULAR:
            return  # Todo: I don't know how
        elif self.Shape in [CrossSection.SHAPES.RECT_OPEN, CrossSection.SHAPES.RECT_CLOSED]:
            return  # Todo: Rect
        else:
            return shape_generator.swmm_std_cross_sections(self.Shape, height=self.Geom1)

    @property
    def profil_area(self):
        if self.Shape == CrossSection.SHAPES.CUSTOM:
            return self.shape_generator.area_v
        elif self.Shape == CrossSection.SHAPES.IRREGULAR:
            return  # Todo: I don't know how
        elif self.Shape in [CrossSection.SHAPES.RECT_OPEN, CrossSection.SHAPES.RECT_CLOSED]:
            return self.Geom1 * self.Geom2
        else:
            return self.shape_generator.area_v

    @property
    def from_node(self):
        return self._nodes[self.FromNode]

    @property
    def to_node(self):
        return self._nodes[self.ToNode]

    @property
    def slope(self):
        return (self.from_node.Elevation + self.InOffset - (
                self.to_node.Elevation + self.OutOffset)) / self.Length
