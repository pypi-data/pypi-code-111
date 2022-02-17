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
"""User Job class. Used to define user jobs!

Example usage:

>>> from ILCDIRAC.Interfaces.API.NewInterface.UserJob import UserJob
>>> from ILCDIRAC.Interfaces.API.DiracILC import DiracILC
>>> myDiracInstance = DiracILC( withRepo=False )
>>> myJob = UserJob()
>>> ...
>>> myJob.append( myMarlinApp )
>>> myJob.submit(myDiracInstance)

:author: Stephane Poss
:author: Remi Ete
:author: Ching Bon Lam
"""

from __future__ import absolute_import
from DIRAC import S_OK, gLogger
from DIRAC.Core.Security.ProxyInfo import getProxyInfo

from ILCDIRAC.Interfaces.API.NewInterface.Job import Job
from ILCDIRAC.Interfaces.API.DiracILC import DiracILC
from ILCDIRAC.Interfaces.Utilities.SplitMixin import SplitMixin
import six


__RCSID__ = "$Id$"
LOG = gLogger.getSubLogger(__name__)


class UserJob(SplitMixin, Job):
  """User job class.

  To be used by users, not for production.
  """

  def __init__(self, script=None):
    """Initialize UserJob, including proxy and splitmixin."""
    super(UserJob, self).__init__(script)
    self.type = 'User'
    self.diracinstance = None
    self.usergroup = ['ilc_user', 'calice_user', 'fcc_user']
    self.proxyinfo = getProxyInfo()
    SplitMixin._initialize(self)

  def submit(self, diracinstance=None, mode="wms"):
    """Submit call: when your job is defined, and all applications are set, you need to call this to add the job to DIRAC.

    :param diracinstance: DiracILC instance
    :type diracinstance: ~ILCDIRAC.Interfaces.API.DiracILC.DiracILC
    :param str mode: "wms" (default), "agent", or "local"

    .. note ::
      The *local* mode means that the job will be run on the submission machine. Use this mode for testing of
      submission scripts
    """
    if self._splittingOption:
      result = self._split()
      if 'OK' in result and not result['OK']:
        return result

    # Check the credentials. If no proxy or not user proxy, return an error
    if not self.proxyinfo['OK']:
      LOG.error("Not allowed to submit a job, you need a %s proxy." % self.usergroup)
      return self._reportError("Not allowed to submit a job, you need a %s proxy." % self.usergroup,
                               self.__class__.__name__)
    if 'group' in self.proxyinfo['Value']:
      group = self.proxyinfo['Value']['group']
      if group not in self.usergroup:
        LOG.error("Not allowed to submit a job, you need a %s proxy." % self.usergroup)
        return self._reportError("Not allowed to submit job, you need a %s proxy." % self.usergroup,
                                 self.__class__.__name__)
    else:
      LOG.error("Could not determine group, you do not have the right proxy.")
      return self._reportError("Could not determine group, you do not have the right proxy.")

    res = self._addToWorkflow()
    if not res['OK']:
      return res
    self.oktosubmit = True
    if not diracinstance:
      self.diracinstance = DiracILC()
    else:
      self.diracinstance = diracinstance
    return self.diracinstance.submitJob(self, mode)

  #############################################################################
  def setInputData(self, lfns):
    """Specify input data by Logical File Name (LFN).

    Input files specified via this function will be automatically staged if necessary.

    Example usage:

    >>> job = UserJob()
    >>> job.setInputData(['/ilc/prod/whizard/processlist.whiz'])

    :param lfns: Logical File Names
    :type lfns: Single LFN string or list of LFNs
    """
    if isinstance(lfns, list) and lfns:
      for i, lfn in enumerate(lfns):
        lfns[i] = lfn.replace('LFN:', '')
      #inputData = map( lambda x: 'LFN:' + x, lfns )
      inputData = lfns  # because we don't need the LFN: for inputData, and it breaks the
      # resolution of the metadata in the InputFilesUtilities
      inputDataStr = ';'.join(inputData)
      description = 'List of input data specified by LFNs'
      self._addParameter(self.workflow, 'InputData', 'JDL', inputDataStr, description)
    elif isinstance(lfns, six.string_types):  # single LFN
      description = 'Input data specified by LFN'
      self._addParameter(self.workflow, 'InputData', 'JDL', lfns, description)
    else:
      kwargs = {'lfns': lfns}
      return self._reportError('Expected lfn string or list of lfns for input data', **kwargs)

    return S_OK()

  def setInputSandbox(self, flist):
    """Add files to the input sandbox, can be on the local machine or on the grid.

    >>> job = UserJob()
    >>> job.setInputSandbox( ['LFN:/ilc/user/u/username/libraries.tar.gz',
    >>>                       'mySteeringFile.xml'] )

    :param flist: Files for the inputsandbox
    :type flist: `python:list` or `str`
    """
    if isinstance(flist, six.string_types):
      flist = [flist]
    if not isinstance(flist, list):
      return self._reportError("File passed must be either single file or list of files.")
    self.inputsandbox.extend(flist)
    return S_OK()

  #############################################################################
  def setOutputData(self, lfns, OutputPath='', OutputSE=''):
    """For specifying output data to be registered in Grid storage.  If a list of OutputSEs are specified the job wrapper will try each in turn until successful.

    Example usage:

    >>> job = UserJob()
    >>> job.setOutputData(['Ntuple.root'])

    :param lfns: Output data file or files
    :type lfns: Single `str` or `python:list` of strings ['','']
    :param str OutputPath: Optional parameter to specify the Path in the Storage, postpended to /ilc/user/u/username/
    :param OutputSE: Optional parameter to specify the Storage Element to store data or files, e.g. CERN-SRM
    :type OutputSE: `python:list` or `str`
    """
    kwargs = {'lfns': lfns, 'OutputSE': OutputSE, 'OutputPath': OutputPath}
    if isinstance(lfns, list) and lfns:
      outputDataStr = ';'.join(lfns)
      description = 'List of output data files'
      self._addParameter(self.workflow, 'UserOutputData', 'JDL', outputDataStr, description)
    elif isinstance(lfns, six.string_types):
      description = 'Output data file'
      self._addParameter(self.workflow, 'UserOutputData', 'JDL', lfns, description)
    else:
      return self._reportError('Expected file name string or list of file names for output data', **kwargs)

    if OutputSE:
      description = 'User specified Output SE'
      if isinstance(OutputSE, six.string_types):
        OutputSE = [OutputSE]
      elif not isinstance(OutputSE, list):
        return self._reportError('Expected string or list for OutputSE', **kwargs)
      OutputSE = ';'.join(OutputSE)
      self._addParameter(self.workflow, 'UserOutputSE', 'JDL', OutputSE, description)

    if OutputPath:
      description = 'User specified Output Path'
      if not isinstance(OutputPath, six.string_types):
        return self._reportError('Expected string for OutputPath', **kwargs)
      # Remove leading "/" that might cause problems with os.path.join
      while OutputPath[0] == '/':
        OutputPath = OutputPath[1:]
      if OutputPath.count("ilc/user"):
        return self._reportError('Output path contains /ilc/user/ which is not what you want', **kwargs)
      self._addParameter(self.workflow, 'UserOutputPath', 'JDL', OutputPath, description)

    return S_OK()

  #############################################################################
  def setOutputSandbox(self, files):
    """Specify output sandbox files.  If specified files are over 10MB, these may be uploaded to Grid storage with a notification returned in the output sandbox.

    .. Note ::
       Sandbox files are removed after 2 weeks.

    Example usage:

    >>> job = UserJob()
    >>> job.setOutputSandbox(['*.log','*.sh', 'myfile.txt'])

    Use the output sandbox only for small files. Larger files should be stored
    on the grid and downloaded later if necessary. See :func:`setOutputData`

    :param files: Output sandbox files
    :type files: Single `str` or `python:list` of strings ['','']
    """
    if isinstance(files, list) and files:
      fileList = ";".join(files)
      description = 'Output sandbox file list'
      self._addParameter(self.workflow, 'OutputSandbox', 'JDL', fileList, description)
    elif isinstance(files, six.string_types):
      description = 'Output sandbox file'
      self._addParameter(self.workflow, 'OutputSandbox', 'JDL', files, description)
    else:
      kwargs = {'files': files}
      return self._reportError('Expected file string or list of files for output sandbox contents', **kwargs)

    return S_OK()

  def setILDConfig(self, version):
    """Define the Configuration package to obtain."""
    appName = 'ILDConfig'
    self._addSoftware(appName.lower(), version)
    self._addParameter(self.workflow, 'ILDConfigPackage', 'JDL', appName + version, 'ILDConfig package')
    return S_OK()
