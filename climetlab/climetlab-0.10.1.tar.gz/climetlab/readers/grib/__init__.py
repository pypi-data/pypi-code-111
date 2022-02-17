# (C) Copyright 2020 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#
from .reader import GRIBReader


def reader(source, path, magic=None, deeper_check=False):
    if magic is None or magic[:4] == b"GRIB":
        return GRIBReader(source, path)
