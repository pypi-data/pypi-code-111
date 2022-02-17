#
# Copyright (c) 2009-2022 CERN. All rights nots expressly granted are
# reserved.
#
# This file is part of iLCDirac
# (see ilcdirac.cern.ch, contact: ilcdirac-support@cern.ch).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# In applying this licence, CERN does not waive the privileges and
# immunities granted to it by virtue of its status as an
# Intergovernmental Organization or submit itself to any jurisdiction.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
"""Contains the list of models and their properties.

:author: S. Poss
:since: Jul 07, 2011
"""
from __future__ import absolute_import
__RCSID__ = "$Id$"

from DIRAC import S_OK, S_ERROR
from DIRAC.ConfigurationSystem.Client.Helpers.Operations import Operations


class GeneratorModels(object):
  """Contains the list of known models."""

  def __init__(self):
    self.ops = Operations()
    self.models = {}
    res = self.ops.getOptionsDict("/Models")
    if res['OK']:
      self.models = res['Value']

  def hasModel(self, model):
    """Check that specified model exists."""
    if model in self.models:
      return S_OK()
    else:
      return S_ERROR("Model %s is not defined, use any of %s" % (model, list(self.models.keys())))

  def getFile(self, model):
    """Return the proper model file (usually LesHouches)"""
    res = self.hasModel(model)
    if not res['OK']:
      return res
    if not self.models[model]:
      return S_ERROR("No file attached to model %s" % model)
    return S_OK(self.models[model])

  def getParamsForWhizard(self, model):
    """When creating the final file, this is needed to get the parameters for the SM."""
    params = ''
    if model == 'sm':
      params = """<GF type="float" value="1.16639E-5">
<!-- Fermi constant -->
</GF>
<mZ type="float" value="91.1882">
<!-- Z-boson mass -->
</mZ>
<mW type="float" value="80.419">
<!-- W-boson mass -->
</mW>
<mH type="float" value="120">
<!-- Higgs mass -->
</mH>
<alphas type="float" value="0.1178">
<!-- Strong coupling constant alpha_s(MZ) -->
</alphas>
<me type="float" value="0.">
<!-- electron mass -->
</me>
<mmu type="float" value="0.1066">
<!-- muon mass -->
</mmu>
<mtau type="float" value="1.777">
<!-- tau-lepton mass -->
</mtau>
<ms type="float" value="0.">
<!-- s-quark mass -->
</ms>
<mc type="float" value="0.54">
<!-- c-quark mass -->
</mc>
<mb type="float" value="2.9">
<!-- b-quark mass -->
</mb>
<mtop type="float" value="174">
<!-- t-quark mass -->
</mtop>
<wtop type="float" value="1.523">
<!-- t-quark width -->
</wtop>
<wZ type="float" value="2.443">
<!-- Z-boson width -->
</wZ>
<wW type="float" value="2.049">
<!-- W-boson width -->
</wW>
<wH type="float" value="0.3605E-02">
<!-- Higgs width -->
</wH>
<vckm11 type="float" value="0.97383">
<!-- Vud -->
</vckm11>
<vckm12 type="float" value="0.2272">
<!-- Vus -->
</vckm12>
<vckm13 type="float" value="0.00396">
<!-- Vub -->
</vckm13>
<vckm21 type="float" value="-0.2271">
<!-- Vcd -->
</vckm21>
<vckm22 type="float" value="0.97296">
<!-- Vcs -->
</vckm22>
<vckm23 type="float" value="0.04221">
<!-- Vcb -->
</vckm23>
<vckm31 type="float" value="0.00814">
<!-- Vtd -->
</vckm31>
<vckm32 type="float" value="-0.04161">
<!-- Vts -->
</vckm32>
<vckm33 type="float" value="0.99910">
<!-- Vtb -->
</vckm33>
<khgaz type="float" value="1.000">
<!-- anomaly Higgs coupling K factors -->
</khgaz>
<khgaga type="float" value="1.000">
<!-- anomaly Higgs coupling K factors -->
</khgaga>
<khgg type="float" value="1.000">
<!-- anomaly Higgs coupling K factors -->
</khgg>
"""
    else:
      params = """
      """
    return S_OK(params)
