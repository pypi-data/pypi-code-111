import re
import types
from abc import ABC
from inspect import isfunction, isclass

from numpy import isnan
from pandas import DataFrame, Series
from tqdm.auto import tqdm

from ._type_converter import type2str, is_equal, txt_to_lines
from .section_labels import *
from .section_lists import LINK_SECTIONS, NODE_SECTIONS

SWMM_VERSION = '5.1.015'

SEP_INP = ';;' + "_" * 100


########################################################################################################################
class CustomDict:
    """imitate :class:`collections.UserDict` (:term:`dict-like <mapping>`) but operations only effect self._data"""

    def __init__(self, d=None, **kwargs):
        if d is None:
            self._data = kwargs
        else:
            if isinstance(d, dict):
                self._data = d
            else:
                self._data = dict(d)

    def __len__(self):
        return self._data.__len__()

    def __getitem__(self, key):
        return self._data.__getitem__(key)

    def __setitem__(self, key, item):
        self._data.__setitem__(key, item)

    def __delitem__(self, key):
        self._data.__delitem__(key)

    def __iter__(self):
        return self._data.__iter__()

    def __contains__(self, key):
        return self._data.__contains__(key)

    def __repr__(self):
        return self._data.__repr__()

    def __str__(self):
        return self._data.__str__()

    def get(self, key, default=None):
        if isinstance(key, list):
            return (self.get(k) for k in key)
        return self._data.get(key) if key in self else default

    def copy(self):
        return type(self)(self._data.copy())

    def values(self):
        return self._data.values()

    def keys(self):
        return self._data.keys()

    def items(self):
        return self._data.items()

    def update(self, d=None, **kwargs):
        self._data.update(d, **kwargs)

    def pop(self, key):
        return self._data.pop(key)

    def __bool__(self):
        return bool(self._data)

    # @property
    # def id(self):
    #     return id(self)


class CustomDictWithAttributes(CustomDict):
    def copy(self):
        new = type(self)()
        for key in self:
            if getattr(self[key], 'copy', False):
                new[key] = self[key].copy()
            else:
                new[key] = self[key]
        return new


########################################################################################################################
class InpSectionGeneric(CustomDictWithAttributes):
    """
    abstract class for ``.inp``-file sections without objects

    :term:`dict-like <mapping>`"
    """
    _label = ''
    """str: label of the section"""

    def __init__(self, *args, **kwargs):
        CustomDictWithAttributes.__init__(self, *args, **kwargs)
        self._inp = None

    def __setitem__(self, key, item):
        super().__setitem__(key, item)
        if isinstance(key, str) and ' ' not in key:
            super().__setattr__(key, item)

    def __delitem__(self, key):
        if hasattr(self, key):
            super().__delattr__(key)
        super().__delitem__(key)

    def set_parent_inp(self, inp):
        self._inp = inp

    def get_parent_inp(self):
        return self._inp

    @classmethod
    def from_inp_lines(cls, lines):
        """
        read ``.inp``-file lines and create an section object

        Args:
            lines (str | list[list[str]]): lines in the section of the ``.inp``-file

        Returns:
            InpSectionGeneric: object of the section
        """
        pass

    def to_inp_lines(self, fast=False):
        """
        write ``.inp``-file lines of the section object

        Args:
            fast (bool): speeding up conversion

                - :obj:`True`: if no special formation of the input file is needed
                - :obj:`False`: section is converted into a table to prettify string output (slower)

        Returns:
            str: ``.inp``-file lines of the section object
        """
        f = ''
        max_len = len(max(self.keys(), key=len)) + 2
        for sub in self:
            f += '{key}{value}'.format(key=sub.ljust(max_len),
                                       value=type2str(self[sub]) + '\n')
        return f

    @classmethod
    def create_section(cls):
        return cls()

    # @property
    # def id(self):
    #     return id(self)


########################################################################################################################
class InpSection(CustomDict):
    """
    class for ``.inp``-file sections with objects (i.e. nodes, links, subcatchments, raingages, ...)
    """

    def __init__(self, section_object):
        """
        create an object for ``.inp``-file sections with objects (i.e. nodes, links, subcatchments, raingages, ...)

        Args:
            section_object (BaseSectionObject-like): object class which is stored in this section.
                This information is used to set the index of the section and
                to decide if the section can be exported (converted to a string) as a table.
        """
        CustomDict.__init__(self)
        self._section_object = section_object
        self._inp = None

    def set_parent_inp(self, inp):
        self._inp = inp

    def get_parent_inp(self):
        return self._inp

    # def __repr__(self):
    #     # return CustomDict.__repr__(self)
    #     return str(self)

    # def __str__(self):
    #     return f'[{self._section_object._section_label}] '  # + ' | '.join((str(s) for s in self.keys()))

    def __setitem__(self, key, value):
        if isinstance(self._identifier, str):
            if not isinstance(key, str):
                raise UserWarning('Wrong key type')
        else:
            if len(self._identifier) != len(key):
                raise UserWarning('Wrong number of keys')

        if not isinstance(value, self._section_object):
            raise UserWarning('Wrong section-object type')

        super().__setitem__(key, value)

    @property
    def objects(self):
        """
        all swmm objects in this section

        Returns:
            dict[str, BaseSectionObject]: dictionary of objects with label as key and the object os value
        """
        return self._data

    @property
    def _identifier(self):
        """
        to set the index of the section (key to select an object an index for the dataframe export)
        Returns:
            str | tuple: key of the objects label (can be a single or multiple keys)
        """
        return self._section_object._identifier

    @property
    def _label(self):
        """
        get the label of the section

        Returns:
            str: label of the section
        """
        return self._section_object._section_label

    @property
    def _table_inp_export(self):
        # if the section can be exported (converted to a string) as a table.
        return self._section_object._table_inp_export

    def add_multiple(self, *items):
        """
        add objects to section

        Args:
            *items (BaseSectionObject): new objects
        """
        if (len(items) == 1) and isinstance(items[0], types.GeneratorType):
            items = items[0]
        for obj in items:
            self.add_obj(obj)

    def add_obj(self, obj):
        """
        add object to section

        Args:
            obj (BaseSectionObject): new object
        """
        self[obj.get(self._identifier)] = obj

    def add_inp_lines(self, multi_line_args):
        """
        creates and adds objects for each line

        Args:
            multi_line_args (list[list[str]]): lines in the input file section
        """
        self.add_multiple(*self._section_object._convert_lines(multi_line_args))

    @classmethod
    def from_inp_lines(cls, lines, section_class):
        """
        convert the lines of a section to this class and each line to a object

        This function is used for the ``.inp``-file reading

        Args:
            lines (str | list[list[str]]): lines of a section in a ``.inp``-file
            section_class (BaseSectionObject): object class which is stored in this section.

        Returns:
            InpSection: section of the ``.inp``-file
        """
        return section_class.create_section(lines)

    def get_objects(self, sort_alphabetical=False):
        keys = self.keys()
        if sort_alphabetical:
            keys = sorted(keys, key=natural_keys)

        for k in keys:
            yield self[k]

    def to_inp_lines(self, fast=False, sort_objects_alphabetical=False):
        """
        convert the section to a multi-line ``.inp``-file conform string

        This function is used for the ``.inp``-file writing

        Args:
            fast (bool): speeding up conversion

                - :obj:`True`: if no special formation of the input file is needed
                - :obj:`False`: section is converted into a table to prettify string output (slower)

            sort_objects_alphabetical (bool): if objects in a section should be sorted alphabetical |
                default: use order of the read inp-file and append new objects

        Returns:
             str: lines of the ``.inp``-file section
        """
        if not self:  # if empty
            return ';; No Data'

        if fast or not self._table_inp_export:

            # only show write progress for big files
            n_objects = len(self.keys())
            values = self.get_objects(sort_objects_alphabetical)
            if n_objects > 50_000:
                _iterable = tqdm(values,
                                 desc=self._section_object.__name__,
                                 postfix='Write',
                                 total=n_objects)
            else:
                _iterable = values

            return '\n'.join(o.to_inp_line() for o in _iterable)
        else:
            return dataframe_to_inp_string(self.get_dataframe(set_index=True,
                                                              sort_objects_alphabetical=sort_objects_alphabetical))

    @property
    def frame(self):
        """convert section to a pandas data-frame

        This property is used for debugging purposes and data analysis of the input data of the swmm model.

        Returns:
            pandas.DataFrame: section as table
        """
        return self.get_dataframe(set_index=True, sort_objects_alphabetical=True)

    def get_dataframe(self, set_index=True, sort_objects_alphabetical=False):
        """convert section to a pandas data-frame

        Args:
            set_index (bool): set object keys as index
            sort_objects_alphabetical (bool): if objects in a section should be sorted alphabetical |
                default: use order of the read inp-file and append new objects

        Returns:
            pandas.DataFrame: section as table
        """
        if not self:  # if empty
            return DataFrame()
        df = DataFrame([i.to_dict_() for i in self.get_objects(sort_objects_alphabetical)])
        if set_index:
            df = df.set_index(self._identifier)
        return df

    def create_new_empty(self):
        """
        create a new empty section of this kind of section

        Returns:
            InpSection: new empty section
        """
        return type(self)(self._section_object)

    def copy(self):
        """
        get a copy of the section

        Returns:
            InpSection: copy of the section
        """
        new = self.create_new_empty()
        # ΔTime: 18.678 s
        # new._data = deepcopy(self._data)
        # ΔTime: 2.943 s
        new._data = {k: self[k].copy() for k in self}
        return new

    def filter_keys(self, keys, by=None):
        """
        filter parts of the section with keys (identifier strings or attribute string)

        Args:
            keys (list | set): list of names to filter by (ether the identifier or the attribute of "by")
            by (str | list[str] | tuple[str]): attribute name of the section object to filter by

        Returns:
            tuple[BaseSectionObject] | list[BaseSectionObject]: filtered objects
        """

        # working with pandas makes it x10 faster
        if by is None:
            filtered_keys = set(self.keys()).intersection(set(keys))
        else:
            f = self.get_dataframe(set_index=False)
            if f.empty:
                return tuple()

            if isinstance(by, (list, set, tuple)):
                filtered_keys = f[f[by].isin(keys).all(axis=1)].set_index(self._identifier).index
                # filtered_keys = (k for k in self if any(map(lambda b: self[k][b] in keys, by)))

            else:
                # filtered_keys = filter(lambda k: self[k][by] in keys, self)
                # filtered_keys = (k for k in self if self[k][by] in keys)
                filtered_keys = f[f[by].isin(keys)].set_index(self._identifier).index

        return (self[k] for k in filtered_keys)

    def slice_section(self, keys, by=None):
        """
        filter parts of the section with keys (identifier strings or attribute string)

        Args:
            keys (list | set): list of names to filter by (ether the identifier or the attribute of "by")
            by (str | list[str] | tuple[str]): attribute name of the section object to filter by

        Returns:
            InpSection: new filtered section
        """
        new = self.create_new_empty()
        new.add_multiple(*self.filter_keys(keys, by=by))
        return new


def split_line_with_quotes(line):
    if isinstance(line, (list, tuple)):
        line = ' '.join(line)
    if '"' not in line:
        return line.split()
    return re.findall(r'("[^"]*"|[^" ]+)', line)


########################################################################################################################
class BaseSectionObject(ABC):
    """
    base class for all section objects to unify operations

    sections objects only have __init__ with object parameters

    acts :term:`like a dict <mapping>` (getter and setter)"""
    _identifier = ''
    """str: attribute of an object which will be used as identifiers"""
    _table_inp_export = True
    """bool: if an section is writeable as table. Default ist True"""
    _section_class = InpSection
    """class: section class to identify functionality"""
    _section_label = ''
    """str: label of the section"""

    # @property
    # def section_label(self):
    #     return self._section_label

    __name__ = 'BaseSectionObject'

    def get(self, key):
        if isinstance(key, list):
            return tuple([self.get(k) for k in key])
        return self.to_dict_().get(key)

    def set(self, key, value):
        assert key in self.to_dict_(), f'{key} not a Object attribute | {self}'
        vars(self)[key] = value

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, item):
        self.set(key, item)

    def to_dict_(self):
        """
        get all object parameters as dictionary

        Returns:
            dict:
        """
        return vars(self).copy()

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self._to_debug_string()

    def __eq__(self, other):
        # TODO: testing!!!
        return isinstance(self, type(other)) and all([is_equal(self[k], other[k]) for k in self.to_dict_().keys()])

    def __hash__(self):
        di = self.to_dict_()
        return tuple([(k, v) for k, v in di.items()]).__hash__()

    # @property
    # def id(self):
    #     return id(self)

    def _to_debug_string(self):
        """for debugging purposes

        string is almost equal to python syntax
        so you could copy it and past it into your code

        Returns:
            str: debug string of the object
        """
        args = list()
        for k, d in self.to_dict_().items():
            if isinstance(d, float) and isnan(d):
                args.append(f'{k}=NaN')
            elif isinstance(d, str):
                args.append(f'{k}="{d}"')
            else:
                args.append(f'{k}={d}')
        return '{}({})'.format(self.__class__.__name__, ', '.join(args))

    def to_inp_line(self):
        """
        convert object to one line of the ``.inp``-file

        for ``.inp``-file writing

        Returns:
            str: SWMM .inp file compatible string
        """
        di = self.to_dict_()
        # s = ''
        # if isinstance(self._identifier, list):
        #     s += ' '.join([str(di.pop(i)) for i in self._identifier])
        # else:
        #     s += str(di.pop(self._identifier))

        # s += ' ' + ' '.join([type2str(i) for i in di.values()])
        # return s
        return ' '.join([type2str(i) for i in di.values()])

    @classmethod
    def from_inp_line(cls, *line_args):
        """
        convert line in the ``.inp``-file to the object

        needed if multiple sub-classes of an object are available (i.e. Infiltration)

        Args:
            *line_args (list[str]): arguments in the line

        Returns:
            BaseSectionObject: object of the ``.inp``-file section
        """
        return cls(*line_args)

    def copy(self):
        """
        copy object

        Returns:
            BaseSectionObject or Child: copy of the object
        """
        return type(self)(**vars(self).copy())

    @classmethod
    def create_section(cls, lines=None) -> InpSection:
        """
        creates a new section for the ``.inp``-file of this object and ads objects described in `lines`

        Args:
            lines:

        Returns:
            InpSection: new section of this object
        """
        sec = cls._section_class(cls)
        # import sys
        if lines is not None:
            # print(f'BYTES: {len(lines):>9_d}', )
            if isinstance(lines, str):
                if len(lines) > 10_000_000:
                    n_lines = lines.strip().count('\n') + 1
                    # to create a progressbar in the reading process
                    # only needed with big (> 200 MB) files
                    lines_iter = tqdm(txt_to_lines(lines), desc=cls.__name__, total=n_lines, postfix='Read')
                else:
                    lines_iter = txt_to_lines(lines)
            else:
                lines_iter = lines

            sec.add_inp_lines(lines_iter)

            if isinstance(lines_iter, tqdm):
                lines_iter.close()

        return sec

    @classmethod
    def from_inp_lines(cls, lines):
        return cls.create_section(lines)

    @classmethod
    def _convert_lines(cls, multi_line_args):
        """
        convert the ``.inp``-file section

        creates and yields an object for each line

        Args:
            multi_line_args (list[list[str]]): lines in the input file section

        Yields:
            BaseSectionObject: object of the ``.inp``-file section
        """
        # overwrite if each object has multiple lines
        for line_args in multi_line_args:
            yield cls.from_inp_line(*line_args)


########################################################################################################################
def dataframe_to_inp_string(df):
    """convert a data-frame into a multi-line string

    used to make a better readable .inp file and for debugging

    Args:
        df (pandas.DataFrame): section table

    Returns:
        str: .inp file conform string for one section
    """
    comment_sign = ';;'
    if df.empty:
        return ';; NO data'

    c = df.copy()
    if c.columns.name is None:
        c.columns.name = comment_sign
    else:
        if not c.columns.name.startswith(comment_sign):
            c.columns.name = comment_sign + c.columns.name

    if c.index.name is not None:
        if not c.index.name.startswith(comment_sign):
            c.index.name = comment_sign + c.index.name

    if c.index._typ == 'multiindex':
        if c.index.names is not None:
            if not c.index.levels[0].name.startswith(comment_sign):
                c.index.set_names(';' + c.index.names[0], level=0, inplace=True)
                # because pandas 1.0
                # c.index.levels[0].name = ';' + c.index.levels[0].name

    return c.applymap(type2str).to_string(sparsify=False,
                                          line_width=999999,
                                          max_rows=999999,
                                          max_cols=999999,
                                          max_colwidth=999999)


########################################################################################################################
def convert_section(head, lines, converter):
    """
    convert section string to a section object

    Args:
        head (str): header of the section
        lines (str): lines in the section
        converter (dict): dict of converters assigned to header {header: converter]

    Returns:
        str | InpSection | InpSectionGeneric: converted section
    """
    if head in converter:
        section_ = converter[head]

        if isfunction(section_):  # section_ ... converter function
            return section_(lines)

        elif isclass(section_):  # section_ ... type/class
            return section_.from_inp_lines(lines)

        else:
            raise NotImplemented()
    else:
        return lines.replace(SEP_INP, '').strip()


########################################################################################################################
SECTIONS_ORDER_MP = ([
                         TITLE,
                         OPTIONS,
                         REPORT,
                         EVAPORATION,
                         TEMPERATURE

                     ] + NODE_SECTIONS +
                     [
                         DWF,
                         INFLOWS

                     ] + LINK_SECTIONS +
                     [

                         LOSSES,
                         XSECTIONS,
                         TRANSECTS,

                         CURVES,
                         TIMESERIES,
                         RAINGAGES,
                         PATTERNS,

                         SUBCATCHMENTS,
                         SUBAREAS,
                         INFILTRATION,

                         POLLUTANTS,
                         LOADINGS,
                     ])

SECTION_ORDER_DEFAULT = [TITLE,
                         OPTIONS,
                         FILES,
                         EVAPORATION,
                         TEMPERATURE,
                         RAINGAGES,
                         SUBCATCHMENTS,
                         SUBAREAS,
                         INFILTRATION,
                         LID_CONTROLS,
                         LID_USAGE,
                         AQUIFERS,
                         GROUNDWATER,
                         GWF,
                         SNOWPACKS,
                         JUNCTIONS,
                         OUTFALLS,
                         STORAGE,
                         CONDUITS,
                         PUMPS,
                         ORIFICES,
                         WEIRS,
                         OUTLETS,
                         XSECTIONS,
                         TRANSECTS,
                         LOSSES,
                         CONTROLS,
                         POLLUTANTS,
                         LANDUSES,
                         COVERAGES,
                         LOADINGS,
                         BUILDUP,
                         WASHOFF,
                         TREATMENT,
                         INFLOWS,
                         DWF,
                         HYDROGRAPHS,
                         RDII,
                         CURVES,
                         TIMESERIES,
                         PATTERNS,
                         REPORT,
                         ADJUSTMENTS,
                         TAGS,
                         MAP,
                         COORDINATES,
                         VERTICES,
                         POLYGONS,
                         SYMBOLS,
                         LABELS,
                         BACKDROP,
                         PROFILES]


def check_order(inp, order_list=None):
    if order_list is None:
        order_list = SECTION_ORDER_DEFAULT
    order = [order_list.index(o) if o in order_list else len(order_list) for o in inp]
    return all((order[i+1] - order[i]) > 0 for i in range(len(order)-1))


def _sort_by(key, sections_order):
    if key in sections_order:
        return sections_order.index(key)
    else:
        return len(sections_order)


re_int = re.compile('(\d+)')


def natural_keys(text):
    return [int(text) if text.isdigit() else text for text in re_int.split(text)]


def section_to_string(section, fast=True, sort_objects_alphabetical=False):
    """
    create a string of a section in an ``.inp``-file

    Args:
        section (InpSection | InpSectionGeneric):
            section of an ``.inp``-file
        fast (bool): don't use any formatting else format as table
        sort_objects_alphabetical (bool): if objects in a section should be sorted alphabetical |
            default: use order of the read inp-file and append new objects

    Returns:
        str: string of the ``.inp``-file section
    """
    f = ''

    # ----------------------
    if isinstance(section, str):  # Title
        f += section.replace(SEP_INP, '').strip()

    # ----------------------
    elif isinstance(section, list):  # V0.1
        for line in section:
            f += type2str(line) + '\n'
    #
    # # ----------------------
    elif isinstance(section, dict):  # V0.2
        max_len = len(max(section.keys(), key=len)) + 2
        for sub in section:
            f += '{key}{value}'.format(key=sub.ljust(max_len),
                                       value=type2str(section[sub]) + '\n')
    #
    # ----------------------
    elif isinstance(section, (DataFrame, Series)):  # V0.3
        if section.empty:
            f += ';; NO data'

        if isinstance(section, DataFrame):
            f += dataframe_to_inp_string(section)

        elif isinstance(section, Series):
            f += section.apply(type2str).to_string()

    # ----------------------
    elif isinstance(section, (InpSection, InpSectionGeneric)):  # V0.4
        f += section.to_inp_lines(fast=fast, sort_objects_alphabetical=sort_objects_alphabetical)

    # ----------------------
    f += '\n'
    return f
