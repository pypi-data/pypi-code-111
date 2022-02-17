__author__ = "Markus Pichler"
__credits__ = ["Markus Pichler"]
__maintainer__ = "Markus Pichler"
__email__ = "markus.pichler@tugraz.at"
__version__ = "0.1"
__license__ = "MIT"

import pandas as pd
from pandas import to_datetime
from pandas._libs.tslibs.timedeltas import Timedelta

from .helpers import _get_title_of_part, _remove_lines, _part_to_frame, _continuity_part_to_dict, UNIT, \
    _routing_part_to_dict

"""
not ready to use
experimental

reading generated report (*.rpt) files
"""


class SwmmReport:
    def __init__(self, filename):
        """
        create Report instance to read an .rpt-file

        Args:
            filename (str): path to .rpt file
        """
        self._filename = filename
        # ________________
        self._raw_parts = dict()
        self._converted_parts = dict()
        # ________________
        self._report_to_dict()

        # ________________
        self._version_title = None
        self._note = None

        self._routing_time_step_summary = None

        # input summarys
        self._element_count = None
        self._rainfall_file_summary = None

        # ________________
        self._raingage_summary = None
        self._subcatchment_summary = None
        self._node_summary = None
        self._link_summary = None
        self._crosssection_summary = None
        self._transect_summary = None

        self._runoff_quantity_continuity = None
        self._flow_routing_continuity = None
        self._groundwater_continuity = None
        self._quality_routing_continuity = None
        self._runoff_quality_continuity = None

        self._highest_continuity_errors = None
        self._time_step_critical_elements = None
        self._highest_flow_instability_indexes = None

        self._analysis_options = None

        self._node_depth_summary = None
        self._node_inflow_summary = None
        self._node_surcharge_summary = None
        self._node_flooding_summary = None
        self._storage_volume_summary = None
        self._outfall_loading_summary = None

        self._link_flow_summary = None
        self._flow_classification_summary = None
        self._conduit_surcharge_summary = None

        self._subcatchment_runoff_summary = None

        self._groundwater_summary = None

        self._pollutant_summary = None
        self._landuse_summary = None
        self._link_pollutant_load_summary = None
        self._subcatchment_washoff_summary = None

        self._pumping_summary = None

        self._lid_control_summary = None
        self._lid_performance_summary = None

        self._control_actions_taken = None

    def __repr__(self):
        return f'SwmmReport(file="{self._filename}")'

    @property
    def flow_unit(self):
        return self.analysis_options['Flow Units']

    @property
    def UNIT(self):
        return UNIT(self.flow_unit)

    def _report_to_dict(self):
        """
        convert the report file into a dictionary depending of the different parts

        Args:
            fn (str): path to the report file

        Returns:
            dict: dictionary of parts of the report file
        """
        with open(self._filename, 'r') as file:
            lines = file.readlines()

        self._raw_parts['Simulation Infos'] = ''.join(lines[-3:])
        lines = lines[:-3]
        parts0 = ''.join(lines).replace('\n\n  ****', '\n  \n  ****').split('\n  \n  ****')

        for i, part in enumerate(parts0):
            if part.startswith('*'):
                part = '  ****' + part

            self._raw_parts[_get_title_of_part(part, i)] = _remove_lines(part, title=False, empty=True, sep=False)

    def converted(self, key):
        if key not in self._converted_parts:
            if key not in self._raw_parts:
                return ''
            self._converted_parts[key] = _remove_lines(self._raw_parts[key], title=True, empty=False)

        return self._converted_parts[key]

    @property
    def analysis_options(self):
        """
        get the Analysis Options

        Returns:
            dict: Analysis Options
        """
        if self._analysis_options is None:
            p = self.converted('Analysis Options')

            res = dict()
            last_key = None
            last_initial_spaces = 0

            for line in p.split('\n'):
                initial_spaces = len(line) - len(line.lstrip())

                if '..' in line:
                    key = line[:line.find('..')].strip()
                    value = line[line.rfind('..') + 2:].strip()

                    if last_initial_spaces > initial_spaces:
                        last_key = None

                    if last_key is not None:
                        res[last_key].update({key: value})
                    else:
                        res[key] = value

                    last_initial_spaces = initial_spaces

                else:
                    last_key = line.replace(':', '').strip()
                    res[last_key] = dict()

            self._analysis_options = res
        return self._analysis_options

    @property
    def element_count(self):
        if self._element_count is None:
            p = self.converted('Element Count')

            res = dict()
            last_key = None
            last_initial_spaces = 0

            for line in p.split('\n'):
                initial_spaces = len(line) - len(line.lstrip())

                if '..' in line:
                    key = line[:line.find('..')].strip()
                    value = line[line.rfind('..') + 2:].strip()

                    if last_initial_spaces > initial_spaces:
                        last_key = None

                    if last_key is not None:
                        res[last_key].update({key: value})
                    else:
                        res[key] = value

                    last_initial_spaces = initial_spaces

                else:
                    last_key = line.replace(':', '').strip()
                    res[last_key] = dict()

            self._element_count = res
        return self._element_count


    @property
    def flow_routing_continuity(self):
        """
        get the Flow Routing Continuity

        Returns:
            dict: Flow Routing Continuity
        """
        if self._flow_routing_continuity is None:
            raw = self._raw_parts.get('Flow Routing Continuity', None)
            self._flow_routing_continuity = _continuity_part_to_dict(raw)
        return self._flow_routing_continuity

    @property
    def runoff_quantity_continuity(self):
        """
        get the Runoff Quantity Continuity

        Returns:
            dict: Runoff Quantity Continuity
        """
        if self._runoff_quantity_continuity is None:
            raw = self._raw_parts.get('Runoff Quantity Continuity', None)
            self._runoff_quantity_continuity = _continuity_part_to_dict(raw)
        return self._runoff_quantity_continuity

    @property
    def groundwater_continuity(self):
        if self._groundwater_continuity is None:
            p = self._raw_parts.get('Groundwater Continuity', None)
            self._groundwater_continuity = _continuity_part_to_dict(p)
        return self._groundwater_continuity

    @property
    def quality_routing_continuity(self):
        if self._quality_routing_continuity is None:
            p = self._raw_parts.get('Quality Routing Continuity', None)
            self._quality_routing_continuity = _continuity_part_to_dict(p)
        return self._quality_routing_continuity

    @property
    def runoff_quality_continuity(self):
        if self._runoff_quality_continuity is None:
            p = self._raw_parts.get('Runoff Quality Continuity', None)
            self._runoff_quality_continuity = _continuity_part_to_dict(p)
        return self._runoff_quality_continuity

    @property
    def highest_continuity_errors(self):
        """
        get the Highest Continuity Errors

        Returns:
            dict: Highest Continuity Errors
        """
        if self._highest_continuity_errors is None:
            p = self.converted('Highest Continuity Errors')
            self._highest_continuity_errors = _routing_part_to_dict(p)
        return self._highest_continuity_errors

    @property
    def time_step_critical_elements(self):
        """
        get the Time-Step Critical Elements

        Returns:
            dict: Time-Step Critical Elements
        """
        if self._time_step_critical_elements is None:
            p = self.converted('Time-Step Critical Elements')
            self._time_step_critical_elements = _routing_part_to_dict(p)
        return self._time_step_critical_elements

    @property
    def highest_flow_instability_indexes(self):
        """
        get the Highest Flow Instability Indexes

        Returns:
            dict: Highest Flow Instability Indexes
        """
        if self._highest_flow_instability_indexes is None:
            p = self.converted('Highest Flow Instability Indexes')
            self._highest_flow_instability_indexes = _routing_part_to_dict(p)
        return self._highest_flow_instability_indexes

    @property
    def node_summary(self):
        """
        get the Node Depth Summary

        Returns:
            pandas.DataFrame: Node Depth Summary
        """
        if self._node_summary is None:
            p = self.converted('Node Summary')
            # p = '-'*10 + '\n' + p
            self._node_summary = _part_to_frame(p)
        return self._node_summary

    @property
    def link_summary(self):
        """
        get the Node Depth Summary

        Returns:
            pandas.DataFrame: Node Depth Summary
        """
        if self._link_summary is None:
            p = self.converted('Link Summary')
            # p = '-'*10 + '\n' + p
            p = p.replace('From Node', 'FromNode')
            p = p.replace('To Node', 'ToNode')
            self._link_summary = _part_to_frame(p)
        return self._link_summary

    @property
    def rainfall_file_summary(self):
        """
        get the Node Depth Summary

        Returns:
            pandas.DataFrame: Node Depth Summary
        """
        if self._rainfall_file_summary is None:
            p = self.converted('Rainfall File Summary')
            # p = '-'*10 + '\n' + p
            # p = p.replace('Data Source', 'DataSource')
            self._rainfall_file_summary = _part_to_frame(p)
        return self._rainfall_file_summary

    @property
    def raingage_summary(self):
        """
        get the Node Depth Summary

        Returns:
            pandas.DataFrame: Node Depth Summary
        """
        if self._raingage_summary is None:
            p = self.converted('Raingage Summary')
            # p = '-'*10 + '\n' + p
            p = p.replace('Data Source', 'DataSource')
            self._raingage_summary = _part_to_frame(p)
        return self._raingage_summary

    @property
    def subcatchment_summary(self):
        """
        get the Node Depth Summary

        Returns:
            pandas.DataFrame: Node Depth Summary
        """
        if self._subcatchment_summary is None:
            p = self.converted('Subcatchment Summary')
            # p = '-'*10 + '\n' + p
            p = p.replace('Rain Gage', 'RainGage')
            self._subcatchment_summary = _part_to_frame(p)
        return self._subcatchment_summary

    @property
    def crosssection_summary(self):
        """
        get the Node Depth Summary

        Returns:
            pandas.DataFrame: Node Depth Summary
        """
        if self._crosssection_summary is None:
            p = self.converted('Cross Section Summary')
            # p = '-'*10 + '\n' + p
            self._crosssection_summary = _part_to_frame(p)
        return self._crosssection_summary

    @property
    def subcatchment_runoff_summary(self):
        """
        get the Subcatchment Runoff Summary

        Returns:
            pandas.DataFrame: Subcatchment Runoff Summary
        """
        if self._subcatchment_runoff_summary is None:
            p = self.converted('Subcatchment Runoff Summary')
            self._subcatchment_runoff_summary = _part_to_frame(p)
        return self._subcatchment_runoff_summary

    @property
    def node_depth_summary(self):
        """
        get the Node Depth Summary

        Returns:
            pandas.DataFrame: Node Depth Summary
        """
        if self._node_depth_summary is None:
            p = self.converted('Node Depth Summary')
            self._node_depth_summary = _part_to_frame(p)
        return self._node_depth_summary

    @property
    def node_inflow_summary(self):
        """
        get the Node Inflow Summary

        Returns:
            pandas.DataFrame: Node Inflow Summary
        """
        if self._node_inflow_summary is None:
            p = self.converted('Node Inflow Summary')
            self._node_inflow_summary = _part_to_frame(p)
        return self._node_inflow_summary

    @property
    def node_surcharge_summary(self):
        """
        get the Node Surcharge Summary

        Returns:
            pandas.DataFrame: Node Surcharge Summary
        """
        if self._node_surcharge_summary is None:
            p = self.converted('Node Surcharge Summary')
            # if 'No nodes were surcharged.' in p:
            #     self._node_surcharge_summary = pd.DataFrame()
            # else:
            self._node_surcharge_summary = _part_to_frame(p)
        return self._node_surcharge_summary

    @property
    def node_flooding_summary(self):
        """
        get the Node Flooding Summary

        Returns:
            pandas.DataFrame: Node Flooding Summary
        """
        if self._node_flooding_summary is None:
            p = self.converted('Node Flooding Summary')
            # if 'No nodes were flooded.' in p:
            #     self._node_flooding_summary = pd.DataFrame()
            # else:
            self._node_flooding_summary = _part_to_frame(p)
        return self._node_flooding_summary

    @property
    def storage_volume_summary(self):
        """
        get the Storage Volume Summary

        Returns:
            pandas.DataFrame: Storage Volume Summary
        """
        if self._storage_volume_summary is None:
            p = self.converted('Storage Volume Summary')

            # for reading the table and accepting names shorten than 8 characters
            p = p.replace('Storage Unit', 'Storage_Unit')

            self._storage_volume_summary = _part_to_frame(p)
        return self._storage_volume_summary

    @property
    def outfall_loading_summary(self):
        """
        get the Outfall Loading Summary

        Returns:
            pandas.DataFrame: Outfall Loading Summary
        """
        if self._outfall_loading_summary is None:
            p = self.converted('Outfall Loading Summary')
            self._outfall_loading_summary = _part_to_frame(p.replace('Outfall Node', 'Outfall_Node '))
        return self._outfall_loading_summary

    @property
    def link_flow_summary(self):
        """
        get the Link Flow Summary

        Returns:
            pandas.DataFrame: Link Flow Summary
        """
        if self._link_flow_summary is None:
            p = self.converted('Link Flow Summary')
            self._link_flow_summary = _part_to_frame(p)
        return self._link_flow_summary

    @property
    def flow_classification_summary(self):
        """
        get the Flow Classification Summary

        Returns:
            pandas.DataFrame: Flow Classification Summary
        """
        if self._flow_classification_summary is None:
            p = self.converted('Flow Classification Summary')
            t = '---------- Fraction of Time in Flow Class ----------'
            p = p.replace(t, ' ' * len(t))
            self._flow_classification_summary = _part_to_frame(p)
        return self._flow_classification_summary

    @property
    def conduit_surcharge_summary(self):
        """
        get the Conduit Surcharge Summary

        Returns:
            pandas.DataFrame: Conduit Surcharge Summary
        """
        if self._conduit_surcharge_summary is None:
            p = self.converted('Conduit Surcharge Summary')

            # --------------------------------------------
            # if 'No conduits were surcharged.' in p:
            #     self._conduit_surcharge_summary = pd.DataFrame()
            #
            # else:
            p = p.replace('--------- Hours Full -------- ', 'HoursFull Hours Full HoursFull')
            p = p.replace('Both Ends', 'Both_Ends')
            self._conduit_surcharge_summary = _part_to_frame(p)
        return self._conduit_surcharge_summary

    @property
    def control_actions_taken(self):
        if self._control_actions_taken is None:
            p = self.converted('Control Actions Taken')
            if p:
                self._control_actions_taken = p.split('\n')
        return self._control_actions_taken

    @property
    def groundwater_summary(self):
        if self._groundwater_summary is None:
            p = self.converted('Groundwater Summary')
            self._groundwater_summary = _part_to_frame(p)
        return self._groundwater_summary

    @property
    def landuse_summary(self):
        if self._landuse_summary is None:
            p = self.converted('Landuse Summary')
            self._landuse_summary = _part_to_frame(p)
        return self._landuse_summary

    @property
    def lid_control_summary(self):
        if self._lid_control_summary is None:
            p = self.converted('LID Control Summary')
            self._lid_control_summary = _part_to_frame(p)
        return self._lid_control_summary

    @property
    def lid_performance_summary(self):
        if self._lid_performance_summary is None:
            p = self.converted('LID Performance Summary')
            self._lid_performance_summary = _part_to_frame(p)
        return self._lid_performance_summary

    @property
    def link_pollutant_load_summary(self):
        if self._link_pollutant_load_summary is None:
            p = self.converted('Link Pollutant Load Summary')
            self._link_pollutant_load_summary = _part_to_frame(p)
        return self._link_pollutant_load_summary

    @property
    def note(self):
        if self._note is None:
            self._note = ' '.join(self.converted('Note').strip(' *').split())
        return self._note

    @property
    def pollutant_summary(self):
        if self._pollutant_summary is None:
            p = self.converted('Pollutant Summary')
            self._pollutant_summary = _part_to_frame(p)
        return self._pollutant_summary

    @property
    def pumping_summary(self):
        if self._pumping_summary is None:
            p = self.converted('Pumping Summary')
            self._pumping_summary = _part_to_frame(p)
        return self._pumping_summary

    @property
    def routing_time_step_summary(self):
        if self._routing_time_step_summary is None:
            p = self.converted('Routing Time Step Summary')
            if p:
                self._routing_time_step_summary = dict()
                for line in self.converted('Routing Time Step Summary').split('\n'):
                    if 'Time Step Frequencies' in line:
                        continue
                    key, value = ' '.join(line.split()).split(' : ')
                    if 'sec' in value:
                        value = pd.Timedelta(value)
                    elif '%' in value:
                        value = value
                    else:
                        value = float(value)
                    self._routing_time_step_summary[key] = value

        return self._routing_time_step_summary

    @property
    def subcatchment_washoff_summary(self):
        if self._subcatchment_washoff_summary is None:
            p = self.converted('Subcatchment Washoff Summary')
            self._subcatchment_washoff_summary = _part_to_frame(p)
        return self._subcatchment_washoff_summary

    @property
    def transect_summary(self):
        if self._transect_summary is None:
            p = self.converted('Transect Summary')
            self._transect_summary = dict()
            for transect in p.split('Transect')[1:]:
                label, *data = transect.split()
                self._transect_summary[label] = dict()
                sub = data[0][:-1]
                d = []
                for i in data[1:]:
                    if i.endswith(':'):
                        self._transect_summary[label][sub] = d
                        sub = i[:-1]
                    else:
                        d.append(float(i))
                self._transect_summary[label][sub] = d

                self._transect_summary[label] = pd.DataFrame.from_dict(self._transect_summary[label])
        return self._transect_summary

    def get_simulation_info(self):
        t = self._raw_parts.get('Simulation Infos', None)
        if t:
            return dict(line.strip().split(':', 1) for line in t.split('\n'))

    @property
    def analyse_start(self):
        v = self.get_simulation_info()['Analysis begun on']
        if v:
            return to_datetime(v)

    @property
    def analyse_end(self):
        v = self.get_simulation_info()['Analysis ended on']
        if v:
            return to_datetime(v)

    @property
    def analyse_duration(self):
        v = self.get_simulation_info()['Total elapsed time']
        if v:
            if '< 1 sec' in v:
                return Timedelta(seconds=1)

            return Timedelta(v)

    @staticmethod
    def _pprint(di):
        if not di:
            print('{}')
            return
        f = ''
        max_len = len(max(di.keys(), key=len)) + 5
        for key, value in di.items():
            if isinstance(value, (list, tuple, set)):
                key += f' ({len(value)})'
            key += ':'
            if isinstance(value, list) and len(value) > 20:
                start = 0
                for end in range(20, len(value), 20):
                    f += f'{key:<{max_len}}{", ".join(value[start:end])}\",\n'
                    key = ''
                    start = end
            else:
                f += f'{key:<{max_len}}{value}\n'
        print(f)

    def get_errors(self):
        t = self._raw_parts.get('Version+Title', None)
        di = dict()
        if t:
            for line in t.split('\n'):
                line = line.strip()
                if line.startswith('ERROR'):
                    label, txt = line.split(':', 1)
                    if label in di:
                        di[label].append(txt)
                    else:
                        di[label] = [txt]
        return di

    def print_errors(self):
        self._pprint(self.get_errors())

    def get_version_title(self):
        if self._version_title is None:
            t = self._raw_parts.get('Version+Title', None)
            self._version_title = t.split('\n')[0].strip()
        return self._version_title

    def get_warnings(self):
        """
        WARNING 01: wet weather time step reduced to recording interval for Rain Gage xxx.
            The wet weather time step was automatically reduced so that no period with rainfall would be skipped
            during a simulation.
        WARNING 02: maximum depth increased for Node xxx.
            The maximum depth for the node was automatically increased to match the top of the highest connecting
            conduit.
        WARNING 03: negative offset ignored for Link xxx.
            The link’s stipulated offset was below the connecting node's invert so its actual offset was set to 0.
        WARNING 04: minimum elevation drop used for Conduit xxx.
            The elevation drop between the end nodes of the conduit was below 0.001 ft (0.00035 m) so the latter
            value was used instead to calculate its slope.
        WARNING 05: minimum slope used for Conduit xxx.
            The conduit's computed slope was below the user-specified Minimum Conduit Slope so the latter value was
            used instead.
        WARNING 06: dry weather time step increased to wet weather time step.
            The user-specified time step for computing runoff during dry weather periods was lower than that set for
            wet weather periods and was automatically increased to the wet weather value.
        WARNING 07: routing time step reduced to wet weather time step.
            The user-specified time step for flow routing was larger than the wet weather runoff time step and was
            automatically reduced to the runoff time step to prevent loss of accuracy.
        WARNING 08: elevation drop exceeds length for Conduit xxx.
            The elevation drop across the ends of a conduit exceeds its length. The program computes the conduit's
            slope as the elevation drop divided by the length instead of using the more accurate right triangle
            method. The user should check for errors in the length and in both the invert elevations and offsets at
            the conduit's upstream and downstream nodes.
        WARNING 09: time series interval greater than recording interval for Rain Gage xxx.
            The smallest time interval between entries in the precipitation time series used by the rain gage is
            greater than the recording time interval specified for the gage. If this was not actually intended then
            what appear to be continuous periods of rainfall in the time series will instead be read with time gaps
            in between them.
        WARNING 10: crest elevation is below downstream invert for regulator Link xxx.
            The height of the opening on an orifice, weir, or outlet is below the invert elevation of its downstream
            node. Users should check to see if the regulator's offset height or the downstream node's invert
            elevation is in error.
        WARNING 11: non-matching attributes in Control Rule xxx.
            The premise of a control is comparing two different types of attributes to one another (for example,
            conduit flow and junction water depth).
        """
        t = self._raw_parts.get('Version+Title', None)
        di = dict()
        if t:
            for line in t.split('\n'):
                line = line.strip()
                if line.startswith('WARNING'):

                    if ('WARNING 06' in line) or ('WARNING 07' in line):
                        di[line] = True
                    else:
                        *message, object_label = line.split()
                        message = ' '.join(message)
                        if message in di:
                            di[message].append(object_label)
                        else:
                            di[message] = [object_label]
        return di

    def print_warnings(self):
        self._pprint(self.get_warnings())


def read_rpt_file(report_filename):
    return SwmmReport(report_filename)
