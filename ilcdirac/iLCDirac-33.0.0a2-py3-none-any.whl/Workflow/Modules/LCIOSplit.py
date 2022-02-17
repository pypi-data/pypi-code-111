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
"""Module to concatenate LCIO files.

:author: Ching Bon Lam
:since: Dec 17, 2011
"""

from __future__ import absolute_import
import os

from DIRAC import S_OK, S_ERROR, gLogger
from DIRAC.Core.Utilities.Subprocess import shellCall

from ILCDIRAC.Core.Utilities.PrepareLibs import removeLibc
from ILCDIRAC.Core.Utilities.resolvePathsAndNames import getProdFilename, resolveIFpaths
from ILCDIRAC.Workflow.Modules.ModuleBase import ModuleBase

__RCSID__ = '$Id$'
LOG = gLogger.getSubLogger(__name__)


class LCIOSplit(ModuleBase):
  """LCIO split module."""

  def __init__(self):

    super(LCIOSplit, self).__init__()

    self.STEP_NUMBER = ''
    self.nbEventsPerSlice = 0
    # Step parameters
    self.prod_outputdata = []
    self.applicationName = "lcio"
    #
    self.listoutput = {}
    LOG.info("%s initialized" % (self.__str__()))

  def applicationSpecificInputs(self):
    """Resolve LCIO concatenate specific parameters, called from ModuleBase."""

    if not self.OutputFile:
      return S_ERROR('No output file defined')

    if 'IS_PROD' in self.workflow_commons:
      if self.workflow_commons["IS_PROD"]:
        if 'ProductionOutputData' in self.workflow_commons:
          self.prod_outputdata = self.workflow_commons['ProductionOutputData'].split(";")
          for obj in self.prod_outputdata:
            if obj.lower().count("_sim_") or obj.lower().count("_rec_") or obj.lower().count("_dst_"):
              self.OutputFile = os.path.basename(obj)
        else:
          self.OutputFile = getProdFilename(self.OutputFile, int(self.workflow_commons["PRODUCTION_ID"]),
                                            int(self.workflow_commons["JOB_ID"]))

    if not len(self.InputFile) and len(self.InputData):
      for files in self.InputData:
        if files.lower().find(".slcio") > -1:
          self.InputFile.append(files)

    if 'listoutput' in self.step_commons:
      if len(self.step_commons['listoutput']):
        self.listoutput = self.step_commons['listoutput'][0]

    return S_OK('Parameters resolved')

  def execute(self):
    """Execute the module, called by JobAgent."""
    # Checks
    resultRIV = self.resolveInputVariables()
    if not resultRIV['OK']:
      LOG.error("Failed to resolve input variables", resultRIV['Message'])
      return resultRIV

    if not self.platform:
      return S_ERROR('No ILC platform selected')

    if "LCIO" not in os.environ:
      LOG.error("Environment variable LCIO was not defined, cannot do anything")
      return S_ERROR("Environment variable LCIO was not defined, cannot do anything")

    if len(self.InputFile):
      res = resolveIFpaths(self.InputFile)
      if not res['OK']:
        LOG.error("Missing slcio file!")
        self.setApplicationStatus('LCIOSplit: missing input slcio file')
        return S_ERROR('Missing slcio file!')
      runonslcio = res['Value'][0]
    else:
      return S_OK("No files found to process")

    removeLibc(os.path.join(os.environ["LCIO"], "lib"))

    # Setting up script

    LD_LIBRARY_PATH = os.path.join("$LCIO", "lib")
    if 'LD_LIBRARY_PATH' in os.environ:
      LD_LIBRARY_PATH += ":" + os.environ['LD_LIBRARY_PATH']

    PATH = "$LCIO/bin"
    if 'PATH' in os.environ:
      PATH += ":" + os.environ['PATH']

    scriptContent = """
#!/bin/sh

################################################################################
# Dynamically generated script by LCIOConcatenate module                       #
################################################################################

declare -x LD_LIBRARY_PATH=%s
declare -x PATH=%s

lcio split -i %s -n %s

exit $?

""" % (
        LD_LIBRARY_PATH,
        PATH,
        runonslcio,
        self.nbEventsPerSlice
        )

    # Write script to file

    scriptPath = 'LCIOSplit_%s_Run_%s.tcl' % (self.applicationVersion, self.STEP_NUMBER)

    if os.path.exists(scriptPath):
      os.remove(scriptPath)

    script = open(scriptPath, 'w')
    script.write(scriptContent)
    script.close()

    # Setup log file for application stdout

    if os.path.exists(self.applicationLog):
      os.remove(self.applicationLog)

    # Run code

    os.chmod(scriptPath, 0o755)

    command = '"./%s"' % (scriptPath)

    self.setApplicationStatus('LCIOSplit %s step %s' % (self.applicationVersion, self.STEP_NUMBER))
    self.stdError = ''

    result = shellCall(0,
                        command,
                        callbackFunction=self.redirectLogOutput,
                        bufferLimit=20971520
                      )

    # Check results
    status = result['Value'][0]

    if not os.path.exists(self.applicationLog):
      LOG.error("Cannot access log file, cannot proceed")
      return S_ERROR("Failed reading the log file")

    baseinputfilename = os.path.basename(runonslcio).split(".slcio")[0]
    output_file_base_name = ''
    if self.OutputFile:
      output_file_base_name = self.OutputFile.split('.slcio')[0]
    LOG.info("Will rename all files using '%s' as base." % output_file_base_name)
    numberofeventsdict = {}
    fname = ''
    with open(self.applicationLog, "r") as logf:
      for line in logf:
        line = line.rstrip()
        if line.count(baseinputfilename):
          # First, we need to rename those guys
          current_file = os.path.basename(line).replace(".slcio", "")
          current_file_extension = current_file.replace(baseinputfilename, "")
          newfile = output_file_base_name + current_file_extension + ".slcio"
          os.rename(line, newfile)
          fname = newfile
          numberofeventsdict[fname] = 0
        elif line.count("events"):
          numberofeventsdict[fname] = int(line.split()[0])

    LOG.verbose("Number of eventsdict dict: %s" % numberofeventsdict)

    # Now update the workflow_commons dict with the relation between filename and number of events: needed for
    # the registerOutputData
    self.workflow_commons['file_number_of_event_relation'] = numberofeventsdict
    if self.listoutput:
      outputlist = []
      for fileName in numberofeventsdict:
        item = {}
        item['outputFile'] = fileName
        item['outputPath'] = self.listoutput['outputPath']
        item['outputDataSE'] = self.listoutput['outputDataSE']
        outputlist.append(item)
      self.step_commons['listoutput'] = outputlist

    # Not only the step_commons must be updated
    if 'ProductionOutputData' in self.workflow_commons:
      proddata = self.workflow_commons['ProductionOutputData'].split(";")
      finalproddata = []
      this_split_data = ''
      for item in proddata:
        if not item.count(output_file_base_name):
          finalproddata.append(item)
        else:
          this_split_data = item
      path = os.path.dirname(this_split_data)
      for fileName in numberofeventsdict:
        finalproddata.append(os.path.join(path, fileName))
      self.workflow_commons['ProductionOutputData'] = ";".join(finalproddata)

    LOG.info("Status after the application execution is %s" % str(status))
    self.listDir()
    return self.finalStatusReport(status)
