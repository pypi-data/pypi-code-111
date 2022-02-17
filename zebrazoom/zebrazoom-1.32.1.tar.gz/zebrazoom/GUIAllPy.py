import contextlib
import os
import sys
import traceback

try:
  from PyQt6.QtCore import Qt, QSize
  from PyQt6.QtGui import QFont
  from PyQt6.QtWidgets import QWidget, QDialog, QFileDialog, QApplication, QLabel, QMainWindow, QStackedLayout, QVBoxLayout, QMessageBox, QTextEdit, QSpacerItem
except ImportError:
  from PyQt5.QtCore import Qt, QSize
  from PyQt5.QtGui import QFont
  from PyQt5.QtWidgets import QWidget, QDialog, QFileDialog, QApplication, QLabel, QMainWindow, QStackedLayout, QVBoxLayout, QMessageBox, QTextEdit, QSpacerItem
  QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
  QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
  QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

import zebrazoom.code.util as util
import zebrazoom.code.GUI.configFilePrepareFunctions as configFilePrepareFunctions
import zebrazoom.code.GUI.GUI_InitialFunctions as GUI_InitialFunctions
import zebrazoom.code.GUI.configFileZebrafishFunctions as configFileZebrafishFunctions
import zebrazoom.code.GUI.adjustParameterInsideAlgoFunctions as adjustParameterInsideAlgoFunctions
import zebrazoom.code.GUI.dataAnalysisGUIFunctions as dataAnalysisGUIFunctions
import zebrazoom.code.GUI.troubleshootingFunction as troubleshootingFunction
from zebrazoom.code.GUI.GUI_InitialClasses import StartPage, VideoToAnalyze, ConfigFilePromp, Patience, ZZoutro, ZZoutroSbatch, SeveralVideos, FolderToAnalyze, TailExtremityHE, FolderMultipleROIInitialSelect, EnhanceZZOutput, ResultsVisualization, ViewParameters, Error
from zebrazoom.code.GUI.configFilePrepare import ChooseVideoToCreateConfigFileFor, OptimizeConfigFile, ChooseGeneralExperiment, WellOrganisation, FreelySwimmingExperiment, NbRegionsOfInterest, HomegeneousWellsLayout, CircularOrRectangularWells, NumberOfAnimals, NumberOfAnimals2, NumberOfAnimalsCenterOfMass, IdentifyHeadCenter, IdentifyBodyExtremity, FinishConfig, ChooseCircularWellsLeft, ChooseCircularWellsRight, GoToAdvanceSettings
from zebrazoom.code.GUI.configFileZebrafish import HeadEmbeded
from zebrazoom.code.GUI.adjustParameterInsideAlgo import AdujstParamInsideAlgo, AdujstParamInsideAlgoFreelySwim, AdujstParamInsideAlgoFreelySwimAutomaticParameters, AdujstBoutDetectionOnly
from zebrazoom.code.GUI.dataAnalysisGUI import CreateExperimentOrganizationExcel, ChooseExperimentOrganizationExcel, ChooseDataAnalysisMethod, PopulationComparison, BoutClustering, AnalysisOutputFolderPopulation, AnalysisOutputFolderClustering
from zebrazoom.code.GUI.troubleshooting import ChooseVideoToTroubleshootSplitVideo, VideoToTroubleshootSplitVideo


LARGE_FONT= ("Verdana", 12)


def getCurrentResultFolder():
  return currentResultFolder


def excepthook(excType, excValue, traceback_):
  errorMessage = QMessageBox(QApplication.instance().window)
  errorMessage.setIcon(QMessageBox.Icon.Critical)
  errorMessage.setWindowTitle("Error")
  formattedTraceback = traceback.format_exception(excType, excValue, traceback_)
  errorMessage.setText("An error has ocurred: %s" % formattedTraceback[-1])
  errorMessage.setInformativeText('Please report the issue on <a href="https://github.com/oliviermirat/ZebraZoom/issues">Github</a>.')
  errorMessage.setDetailedText("    %s" % "    ".join(formattedTraceback))
  errorMessage.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel);
  errorMessage.setDefaultButton(QMessageBox.StandardButton.Cancel);
  errorMessage.button(QMessageBox.StandardButton.Ok).setText("Continue")
  errorMessage.button(QMessageBox.StandardButton.Cancel).setText("Exit")
  textEdit = errorMessage.findChild(QTextEdit)
  textEdit.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
  textEdit.setMarkdown(textEdit.toPlainText())
  layout = errorMessage.layout()
  layout.addItem(QSpacerItem(600, 0), layout.rowCount(), 0, 1, layout.columnCount())
  try:
    if errorMessage.exec() != QMessageBox.StandardButton.Ok:
      sys.exit(1)
  finally:
    sys.__excepthook__(excType, excValue, traceback_)


sys.excepthook = excepthook


class ZebraZoomApp(QApplication):
    def __init__(self, args):
        super().__init__(args)
        self.homeDirectory = os.path.dirname(os.path.realpath(__file__))

        self.configFile = {}
        self.videoToCreateConfigFileFor = ''
        self.wellLeftBorderX = 0
        self.wellLeftBorderY = 0
        self.headCenterX = 0
        self.headCenterY = 0
        self.organism = ''

        curZZoutputPath = os.path.dirname(os.path.realpath(__file__))
        curZZoutputPath = os.path.join(curZZoutputPath, 'ZZoutput')
        self.ZZoutputLocation = curZZoutputPath

        self.title_font = QFont('Helvetica', 18, QFont.Weight.Bold, True)

        self._busyCursor = False

        self._windows = set()
        self.window = QMainWindow()
        self.window.closeEvent = self._windowClosed(self.window, self.window.closeEvent)
        layout = QStackedLayout()
        self.frames = {}
        for idx, F in enumerate((StartPage, VideoToAnalyze, ConfigFilePromp, Patience, ZZoutro, ZZoutroSbatch, SeveralVideos, FolderToAnalyze, EnhanceZZOutput, TailExtremityHE, FolderMultipleROIInitialSelect, ResultsVisualization, ViewParameters, Error, ChooseVideoToCreateConfigFileFor, OptimizeConfigFile, ChooseGeneralExperiment, WellOrganisation, FreelySwimmingExperiment, NbRegionsOfInterest, HomegeneousWellsLayout, CircularOrRectangularWells, NumberOfAnimals, NumberOfAnimals2, NumberOfAnimalsCenterOfMass, IdentifyHeadCenter, IdentifyBodyExtremity, FinishConfig, ChooseCircularWellsLeft, ChooseCircularWellsRight, GoToAdvanceSettings, HeadEmbeded, AdujstParamInsideAlgo, AdujstParamInsideAlgoFreelySwim, AdujstParamInsideAlgoFreelySwimAutomaticParameters, AdujstBoutDetectionOnly, CreateExperimentOrganizationExcel, ChooseExperimentOrganizationExcel, ChooseDataAnalysisMethod, PopulationComparison, BoutClustering, AnalysisOutputFolderPopulation, AnalysisOutputFolderClustering, ChooseVideoToTroubleshootSplitVideo, VideoToTroubleshootSplitVideo)):
            self.frames[F.__name__] = idx
            page = F(self)
            if hasattr(page, 'preferredSize'):
                page.sizeHint = lambda *args, page=page: QSize(*page.preferredSize)
                wrapperWidget = QWidget(self.window)
                wrapperLayout = QVBoxLayout()
                wrapperLayout.addWidget(page, alignment=Qt.AlignmentFlag.AlignCenter)
                wrapperWidget.setLayout(wrapperLayout)
                layout.addWidget(wrapperWidget)
            else:
                layout.addWidget(page)
        central_widget = QWidget(self.window)
        central_widget.setLayout(layout)
        self.window.setWindowTitle('ZebraZoom')
        self.window.setCentralWidget(central_widget)
        self.window.showMaximized()

    def askForZZoutputLocation(self):
        self.ZZoutputLocation = QFileDialog.getExistingDirectory(self.window, "Select ZZoutput folder", os.path.expanduser("~"))

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        self.window.centralWidget().layout().setCurrentIndex(self.frames[page_name])

    def _windowClosed(self, window, fn):
        def inner(*args, **kwargs):
            if window is self.window:
                for win in tuple(self._windows):
                    win.close()
                sys.exit(0)
            else:
                if window in self._windows:
                    self._windows.remove(window)
            return fn(*args, **kwargs)
        return inner

    def registerWindow(self, window):
        self._windows.add(window)
        window.closeEvent = self._windowClosed(window, window.closeEvent)

    @contextlib.contextmanager
    def busyCursor(self):
        self.setOverrideCursor(Qt.CursorShape.BusyCursor)
        self._busyCursor = True
        yield
        self.restoreOverrideCursor()
        self._busyCursor = False

    @contextlib.contextmanager
    def suppressBusyCursor(self):
        if self._busyCursor:
            self.restoreOverrideCursor()
        yield
        if self._busyCursor:
            self.setOverrideCursor(Qt.CursorShape.BusyCursor)

    def chooseVideoToAnalyze(self, justExtractParams, noValidationVideo, debugMode):
        GUI_InitialFunctions.chooseVideoToAnalyze(self, justExtractParams, noValidationVideo, debugMode)

    def chooseFolderToAnalyze(self, justExtractParams, noValidationVideo, sbatchMode):
        GUI_InitialFunctions.chooseFolderToAnalyze(self, justExtractParams, noValidationVideo, sbatchMode)

    def chooseFolderForTailExtremityHE(self):
        GUI_InitialFunctions.chooseFolderForTailExtremityHE(self)

    def chooseFolderForMultipleROIs(self):
        GUI_InitialFunctions.chooseFolderForMultipleROIs(self)

    def chooseConfigFile(self):
        GUI_InitialFunctions.chooseConfigFile(self)

    def launchZebraZoom(self):
        GUI_InitialFunctions.launchZebraZoom(self)

    def showResultsVisualization(self):
        self.show_frame("ResultsVisualization")
        self.window.centralWidget().layout().currentWidget().refresh()

    def showViewParameters(self, folder):
        self.show_frame("ViewParameters")
        self.window.centralWidget().layout().currentWidget().setFolder(folder)

    def openConfigurationFileFolder(self, homeDirectory):
        GUI_InitialFunctions.openConfigurationFileFolder(self, homeDirectory)

    def openZZOutputFolder(self, homeDirectory):
        GUI_InitialFunctions.openZZOutputFolder(self, homeDirectory)

    # Config File preparation functions

    def chooseVideoToCreateConfigFileFor(self, controller, reloadConfigFile, freelySwimAutomaticParameters=False, boutDetectionsOnly=False):
        configFilePrepareFunctions.chooseVideoToCreateConfigFileFor(self, controller, reloadConfigFile, freelySwimAutomaticParameters, boutDetectionsOnly)

    def chooseGeneralExperimentFirstStep(self, controller, freeZebra, headEmbZebra, drosophilia, rodent, other, fastScreen):
        configFilePrepareFunctions.chooseGeneralExperimentFirstStep(self, controller, freeZebra, headEmbZebra, drosophilia, rodent, other, fastScreen)

    def chooseGeneralExperiment(self, controller, freeZebra, headEmbZebra, drosophilia, rodent, other, freeZebra2):
        configFilePrepareFunctions.chooseGeneralExperiment(self, controller, freeZebra, headEmbZebra, drosophilia, rodent, other, freeZebra2)

    def wellOrganisation(self, controller, circular, rectangular, roi, other, multipleROIs, groupSameSizeAndShapeEquallySpacedWells):
        configFilePrepareFunctions.wellOrganisation(self, controller, circular, rectangular, roi, other, multipleROIs, groupSameSizeAndShapeEquallySpacedWells)

    def regionsOfInterest(self, controller, nbwells):
        configFilePrepareFunctions.regionsOfInterest(self, controller, nbwells)

    def homegeneousWellsLayout(self, controller, nbwells, nbRowsOfWells, nbWellsPerRows):
        configFilePrepareFunctions.homegeneousWellsLayout(self, controller, nbwells, nbRowsOfWells, nbWellsPerRows)

    def morePreciseFastScreen(self, controller, nbwells, nbRowsOfWells, nbWellsPerRows):
        configFilePrepareFunctions.morePreciseFastScreen(self, controller, nbwells, nbRowsOfWells, nbWellsPerRows)

    def circularOrRectangularWells(self, controller, nbwells, nbRowsOfWells, nbWellsPerRows):
        configFilePrepareFunctions.circularOrRectangularWells(self, controller, nbwells, nbRowsOfWells, nbWellsPerRows)

    def finishConfig(self):
        config_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configuration')
        reference, _ = QFileDialog.getSaveFileName(self.window, "Save config", config_dir, "JSON (*.json)")
        if not reference:
          return
        configFilePrepareFunctions.finishConfig(self, self, reference)

    def chooseCircularWellsLeft(self, controller):
        configFilePrepareFunctions.chooseCircularWellsLeft(self, controller)

    def chooseCircularWellsRight(self, controller):
        configFilePrepareFunctions.chooseCircularWellsRight(self, controller)

    def numberOfAnimals(self, controller, nbanimals, yes, noo, forceBlobMethodForHeadTracking, yesBouts, nooBouts, recommendedMethod, alternativeMethod, yesBends, nooBends, adjustBackgroundExtractionBasedOnNumberOfBlackPixels):
      configFilePrepareFunctions.numberOfAnimals(self, controller, nbanimals, yes, noo, forceBlobMethodForHeadTracking, yesBouts, nooBouts, recommendedMethod, alternativeMethod, yesBends, nooBends, adjustBackgroundExtractionBasedOnNumberOfBlackPixels)

    def chooseHeadCenter(self, controller):
        configFilePrepareFunctions.chooseHeadCenter(self, controller)

    def chooseBodyExtremity(self, controller):
        configFilePrepareFunctions.chooseBodyExtremity(self, controller)

    def chooseBeginningAndEndOfVideo(self, controller):
        configFilePrepareFunctions.chooseBeginningAndEndOfVideo(self, controller)

    def headEmbededGUI(self, controller, blackBack, whiteBack, noBoutDetect, boutDetection, optionExtendedDescentSearchOption, optionBackgroundExtractionOption):
        configFileZebrafishFunctions.headEmbededGUI(self, controller, blackBack, whiteBack, noBoutDetect, boutDetection, optionExtendedDescentSearchOption, optionBackgroundExtractionOption)

    def detectBouts(self, controller, wellNumber, firstFrameParamAdjust, adjustOnWholeVideo):
      adjustParameterInsideAlgoFunctions.detectBouts(self, controller, wellNumber, firstFrameParamAdjust, adjustOnWholeVideo)

    def adjustHeadEmbededTracking(self, controller, wellNumber, firstFrameParamAdjust, adjustOnWholeVideo):
      adjustParameterInsideAlgoFunctions.adjustHeadEmbededTracking(self, controller, wellNumber, firstFrameParamAdjust, adjustOnWholeVideo)

    def adjustFreelySwimTracking(self, controller, wellNumber, firstFrameParamAdjust, adjustOnWholeVideo):
      adjustParameterInsideAlgoFunctions.adjustFreelySwimTracking(self, controller, wellNumber, firstFrameParamAdjust, adjustOnWholeVideo)

    def adjustFreelySwimTrackingAutomaticParameters(self, controller, wellNumber, firstFrameParamAdjust, adjustOnWholeVideo):
      adjustParameterInsideAlgoFunctions.adjustFreelySwimTrackingAutomaticParameters(self, controller, wellNumber, firstFrameParamAdjust, adjustOnWholeVideo)

    def calculateBackground(self, controller, nbImagesForBackgroundCalculation):
      adjustParameterInsideAlgoFunctions.calculateBackground(self, controller, nbImagesForBackgroundCalculation)

    def calculateBackgroundFreelySwim(self, controller, nbImagesForBackgroundCalculation, morePreciseFastScreen=False, automaticParameters=False, boutDetectionsOnly=False):
      adjustParameterInsideAlgoFunctions.calculateBackgroundFreelySwim(self, controller, nbImagesForBackgroundCalculation, morePreciseFastScreen, automaticParameters, boutDetectionsOnly)

    def updateFillGapFrameNb(self, fillGapFrameNb):
      adjustParameterInsideAlgoFunctions.updateFillGapFrameNb(self, fillGapFrameNb)

    def goToAdvanceSettings(self, controller, yes, no):
      configFilePrepareFunctions.goToAdvanceSettings(self, controller, yes, no)

    def openExperimentOrganizationExcelFolder(self, homeDirectory):
      dataAnalysisGUIFunctions.openExperimentOrganizationExcelFolder(self, homeDirectory)

    def chooseExperimentOrganizationExcel(self, controller):
      dataAnalysisGUIFunctions.chooseExperimentOrganizationExcel(self, controller)

    def populationComparison(self, controller, TailTrackingParameters, saveInMatlabFormat, saveRawData, minNbBendForBoutDetect, discard, keep, frameStepForDistanceCalculation):
      dataAnalysisGUIFunctions.populationComparison(self, controller, TailTrackingParameters, saveInMatlabFormat, saveRawData, minNbBendForBoutDetect, discard, keep, frameStepForDistanceCalculation)
      
    def boutClustering(self, controller, nbClustersToFind, FreelySwimming, HeadEmbeded, minNbBendForBoutDetect=3, nbVideosToSave=0, modelUsedForClustering='', removeOutliers=False, frameStepForDistanceCalculation='4'):
      dataAnalysisGUIFunctions.boutClustering(self, controller, nbClustersToFind, FreelySwimming, HeadEmbeded, minNbBendForBoutDetect, nbVideosToSave, modelUsedForClustering, removeOutliers, frameStepForDistanceCalculation)

    def openAnalysisFolder(self, homeDirectory, specificDirectory):
      dataAnalysisGUIFunctions.openAnalysisFolder(self, homeDirectory, specificDirectory)

    def chooseVideoToTroubleshootSplitVideo(self, controller):
      troubleshootingFunction.chooseVideoToTroubleshootSplitVideo(self, controller)
