import importlib.util
from collections import namedtuple,Mapping
import os
import sys


CMSSW_BASE = os.environ.get("CMSSW_BASE")


def namedtuple_with_defaults(typename, field_names, default_values=()):
    T = namedtuple(typename, field_names)
    T.__new__.__defaults__ = (None,) * len(T._fields)
    if isinstance(default_values, Mapping):
        prototype = T(**default_values)
    else:
        prototype = T(*default_values)
    T.__new__.__defaults__ = tuple(prototype)
    return T


class MCSampleValuesHelperPrototype():
    """
    Prototype class for MCSampleValuesHelper
    """

    __years = ["2022","2022preEE","2022postEE","2023preBPix","2023postBPix"]
    __energies = ["13TeV"]
    __xs_field_names = []
    __nevt_field_names = []
    __br_field_names = []
    __kfactor_field_names = []
    __corr_field_names = []
    __xml_field_names = []
    _key_field_map = {
        "CrossSection"   : ("XSec",-1.0),
        "NEvents"        : ("NEVT",-1.0),
        "BranchingRatio" : ("BRat",1.0),
        "kFactor"        : ("kFac",1.0),
        "Correction"     : ("Corr",1.0),
        "XMLname"        : ("Xml",""),
    }
    for __val in __years+__energies:
        for mode in ["", "Source"]:
            __xs_field_names.append("XSec"+mode+"_"+__val)
            __nevt_field_names.append("NEVT"+mode+"_"+__val)
            __br_field_names.append("BRat"+mode+"_"+__val)
            __kfactor_field_names.append("kFac"+mode+"_"+__val)
            __corr_field_names.append("Corr"+mode+"_"+__val)
            __xml_field_names.append("Xml"+mode+"_"+__val)
    XSValues      = namedtuple_with_defaults("XSValues",      __xs_field_names,       [_key_field_map["CrossSection"][1],""]*len(__years+__energies))
    NEventsValues = namedtuple_with_defaults("NEventsValues", __nevt_field_names,     [_key_field_map["NEvents"][1],""]*len(__years+__energies))
    BRValues      = namedtuple_with_defaults("BRValues",      __br_field_names,       [_key_field_map["BranchingRatio"][1],""]*len(__years+__energies))
    kFactorValues = namedtuple_with_defaults("kFactorValues", __kfactor_field_names,  [_key_field_map["kFactor"][1],""]*len(__years+__energies))
    CorrValues    = namedtuple_with_defaults("CorrValues",    __corr_field_names,     [_key_field_map["Correction"][1],""]*len(__years+__energies))
    XMLValues     = namedtuple_with_defaults("XMLValues",     __xml_field_names,      [_key_field_map["XMLname"][1],""]*len(__years+__energies))


class MCSampleValuesHelper(MCSampleValuesHelperPrototype):
    """Stores the cross sections and k-factors associated to a given physics process.

    The lists of years and energies used to identify a given cross section are also stored within this class.
    Given a process name, and year the appropriate cross section will be returned.

    Args:
        extra_dicts (:obj:`dict` of :obj:`dict` of :obj:`namedtuple_with_defaults`): Extra cross sections and k-factors to add to the __values_dict.

    Example:
        from CrossSectionHelper import *
        helper = MCSampleValuesHelper()
        helper.get_lumi("TTbarTo2L2Nu","13TeV","2018")
        helper.get_xs("TTbarTo2L2Nu","13TeV","2018")
        helper.get_nevt("TTbarTo2L2Nu","13TeV","2018")
        helper.get_br("TTbarTo2L2Nu","13TeV","2018")
        helper.get_xml("TTbar","13TeV","2016")
    """

    __values_dict = {
      
        "JetHT_RunC": {

            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                # NEVT_2022preEE=15621241,
                NEVT_2022preEE=15620904,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                # Xml_2022preEE="RunII_124X_v1/2022/JetHT_Run2022C-PromptReco-v1.xml", XmlSource_2022preEE="",
                Xml_2022preEE="Run3_130X_v1/data/2022preEE/JetHT_Run2022C-22Sep2023-v1.xml", XmlSource_2022preEE="",
            ),
        },

        "JetMET_RunC": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2023preBPix=176177366,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2023preBPix="RunII_130X_v1/data/2023/JetMET_Run2023C-PromptReco-v123.xml", XmlSource_2023preBPix="",
            ),
        },

        "JetMET_RunCv4": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2023preBPix=211784480,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2023preBPix="RunII_130X_v1/data/2023/JetMET_Run2023C-PromptReco-v4.xml", XmlSource_2023preBPix="",
            ),
        },

        "JetMET_RunD": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2023postBPix=149505772,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2023postBPix="RunII_130X_v1/data/2023/JetMET_Run2023D-22Sep2023_v1.xml", XmlSource_2023postBPix="",
            ),
        },

        "JetMET_RunC": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                # NEVT_2022preEE=169113266,  # Prompt
                # NEVT_2022preEE=169113266,  # ReReco
                NEVT_2022preEE=185569454,  # Dec
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                # Xml_2022preEE="RunII_124X_v1/2022/JetMETandHT_Run2022C-PromptReco-v1.xml", XmlSource_2022preEE="",
                # Xml_2022preEE="RunII_130X_v1/data/2022preEE/JetMET_Run2022C-22Sep2023-v1.xml", XmlSource_2022preEE="",
                Xml_2022preEE="RunII_130X_v1/data/2022preEE/JetMET_Run2022C-19Dec2023-v1.xml", XmlSource_2022preEE="",
            ),
        },

        "JetMET_RunD": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                # NEVT_2022preEE=101350932,  # Prompt
                # NEVT_2022preEE=100853361,  # ReReco
                NEVT_2022preEE=101270969,  # Dec
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                # Xml_2022="RunII_124X_v1/2022/JetMET_Run2022C-PromptReco-v12.xml", XmlSource_2022preEE="",
                # Xml_2022preEE="RunII_130X_v1/data/2022preEE/JetMET_Run2022D-22Sep2023-v1.xml", XmlSource_2022preEE="",
                Xml_2022preEE="RunII_130X_v1/data/2022preEE/JetMET_Run2022D-19Dec2023-v1.xml", XmlSource_2022preEE="",
            ),
        },

        "JetMET_RunE": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022postEE=138964668,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022postEE="RunII_130X_v1/data/2022postEE/JetMET_Run2022E-22Sep2023-v1.xml", XmlSource_2022postEE="",
            ),
        },

        "JetMET_RunF": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022postEE=514335384,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022postEE="RunII_130X_v1/data/2022postEE/JetMET_Run2022F-22Sep2023-v1.xml", XmlSource_2022postEE="",
            ),
        },

        "JetMET_RunG": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022postEE=84696790,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022postEE="RunII_130X_v1/data/2022postEE/JetMET_Run2022G-22Sep2023-v1.xml", XmlSource_2022postEE="",
            ),
        },

        "QCD_HT40to70" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=312000000, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=2.28443118822e+16,
                NEVT_2023preBPix=4.19474852979e+16,
                NEVT_2023postBPix=1.60703428824e+16,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="RunII_130X_v1/SM/QCD-4Jets_HT-40to70_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022preEE="",
                # Xml_2022postEE="RunII_130X_v1/SM/QCD-4Jets_HT-40to70_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022postEE="",
                Xml_2023preBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-40to70_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023preBPix="",
                Xml_2023postBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-40to70_BPix_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023postBPix="",
            ),
        },

        "QCD_HT70to100" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=58600000, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=5.92404059224e+15,
                NEVT_2022postEE=2.00312576064e+16,
                NEVT_2023preBPix=1.21681293497e+16,
                NEVT_2023postBPix=5.12547190443e+15,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="RunII_130X_v1/SM/QCD-4Jets_HT-70to100_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022preEE="",
                Xml_2022postEE="RunII_130X_v1/SM/QCD-4Jets_HT-70to100_EE_EE_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022postEE="",
                Xml_2023preBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-70to100_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023preBPix="",
                Xml_2023postBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-70to100_BPix_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023postBPix="",
            ),
        },

        "QCD_HT100to200" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=25200000, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=3.16286491816e+15,
                NEVT_2022postEE=1.14254723313e+16,
                NEVT_2023preBPix=6.46257153127e+15,
                NEVT_2023postBPix=3.34237269299e+15,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="RunII_130X_v1/SM/QCD-4Jets_HT-100to200_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022preEE="",
                Xml_2022postEE="RunII_130X_v1/SM/QCD-4Jets_HT-100to200_EE_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022postEE="",
                Xml_2023preBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-100to200_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023preBPix="",
                Xml_2023postBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-100to200_BPix_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023postBPix="",
            ),
        },

        "QCD_HT200to400" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1950000, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=3.57650656118e+14,
                NEVT_2022postEE=1.20916792738e+15,
                NEVT_2023preBPix=6.44757206008e+14,
                NEVT_2023postBPix=2.93735035945e+14,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="RunII_130X_v1/SM/QCD-4Jets_HT-200to400_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022preEE="",
                Xml_2022postEE="RunII_130X_v1/SM/QCD-4Jets_HT-200to400_EE_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022postEE="",
                Xml_2023preBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-200to400_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023preBPix="",
                Xml_2023postBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-200to400_BPix_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023postBPix="",
            ),
        },

        "QCD_HT400to600" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=96100, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=2.06936384343e+13,
                NEVT_2022postEE=7.30143254524e+13,
                NEVT_2023preBPix=3.88929544249e+13,
                NEVT_2023postBPix=2.16833036017e+13,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="RunII_130X_v1/SM/QCD-4Jets_HT-400to600_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022preEE="",
                Xml_2022postEE="RunII_130X_v1/SM/QCD-4Jets_HT-400to600_EE_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022postEE="",
                Xml_2023preBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-400to600_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023preBPix="",
                Xml_2023postBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-400to600_BPix_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023postBPix="",
            ),
        },

        "QCD_HT600to800" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=13500, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=3.15279581507e+12,
                NEVT_2022postEE=1.0371890249e+13,
                NEVT_2023preBPix=5.54349727767e+12,
                NEVT_2023postBPix=3.17035628119e+12,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="RunII_130X_v1/SM/QCD-4Jets_HT-600to800_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022preEE="",
                Xml_2022postEE="RunII_130X_v1/SM/QCD-4Jets_HT-600to800_EE_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022postEE="",
                Xml_2023preBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-600to800_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023preBPix="",
                Xml_2023postBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-600to800_BPix_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023postBPix="",
            ),
        },

        "QCD_HT800to1000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=3020, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=8.33813426982e+11,
                NEVT_2022postEE=2.60183892953e+12,
                NEVT_2023preBPix=1.4361911085e+12,
                NEVT_2023postBPix=6.8208971755e+11,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="RunII_130X_v1/SM/QCD-4Jets_HT-800to1000_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022preEE="",
                Xml_2022postEE="RunII_130X_v1/SM/QCD-4Jets_HT-800to1000_EE_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022postEE="",
                Xml_2023preBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-800to1000_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023preBPix="",
                Xml_2023postBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-800to1000_BPix_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023postBPix="",
            ),
        },

        "QCD_HT1000to1200" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=883, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=2.4061544748e+11,
                NEVT_2022postEE=8.09962206037e+11,
                NEVT_2023preBPix=3.67516261641e+11,
                NEVT_2023postBPix=2.08310438149e+11,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="RunII_130X_v1/SM/QCD-4Jets_HT-1000to1200_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022preEE="",
                Xml_2022postEE="RunII_130X_v1/SM/QCD-4Jets_HT-1000to1200_EE_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022postEE="",
                Xml_2023preBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-1000to1200_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023preBPix="",
                Xml_2023postBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-1000to1200_BPix_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023postBPix="",
            ),
        },

        "QCD_HT1200to1500" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=382, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=1.09322084169e+11,
                NEVT_2022postEE=3.69302092497e+11,
                NEVT_2023preBPix=2.03844808352e+11,
                NEVT_2023postBPix=97279236932.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="RunII_130X_v1/SM/QCD-4Jets_HT-1200to1500_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022preEE="",
                Xml_2022postEE="RunII_130X_v1/SM/QCD-4Jets_HT-1200to1500_EE_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022postEE="",
                Xml_2023preBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-1200to1500_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023preBPix="",
                Xml_2023postBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-1200to1500_BPix_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023postBPix="",
            ),
        },

        "QCD_HT1500to2000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=126, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=37109821387.0,
                NEVT_2022postEE=1.08055958125e+11,
                NEVT_2023preBPix=66548359005.0,
                NEVT_2023postBPix=28684037990.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="RunII_130X_v1/SM/QCD-4Jets_HT-1500to2000_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022preEE="",
                Xml_2022postEE="RunII_130X_v1/SM/QCD-4Jets_HT-1500to2000_EE_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022postEE="",
                Xml_2023preBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-1500to2000_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023preBPix="",
                Xml_2023postBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-1500to2000_BPix_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023postBPix="",
            ),
        },

        "QCD_HT2000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=26.3, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=6415477993.0,
                NEVT_2022postEE=22749716909.0,
                NEVT_2023preBPix=14772287168.0,
                NEVT_2023postBPix=7192509611.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="RunII_130X_v1/SM/QCD-4Jets_HT-2000_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022preEE="",
                Xml_2022postEE="RunII_130X_v1/SM/QCD-4Jets_HT-2000_EE_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2022postEE="",
                Xml_2023preBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-2000_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023preBPix="",
                Xml_2023postBPix="RunII_130X_v1/SM/2023/QCD-4Jets_HT-2000_BPix_CP5_13p6TeV_madgraphMLM-pythia8_v2.xml", XmlSource_2023postBPix="",
            ),
        },

        "QCDPT50to80" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=16760000, XSecSource_13TeV="GenXSecAnalyzer averaged over years" # 13p6 TeV!
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022=19670669.0,
                NEVT_2022preEE=21136440.0,
                NEVT_2022postEE=19940303.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022="Run3_124X_v1/2022/QCD_Pt-50to80_CP5_13p6TeV_pythia8_v2.xml", XmlSource_2022="",
                Xml_2022preEE="Run3_126X_v1/2022/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_PT-50to80_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT80to120" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=2517000, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=29505225.5061,
                # NEVT_2022preEE=30781516.0,
                NEVT_2022postEE=40071820.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_124X_v1/2022/QCD_Pt-80to120_CP5_13p6TeV_pythia8_v2.xml", XmlSource_2022preEE="",
                # Xml_2022preEE="Run3_126X_v1/2022/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_PT-80to120_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT120to170" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=442200, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=29409986.2426,
                # NEVT_2022preEE=31356801.0,
                NEVT_2022postEE=40071820.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_124X_v1/2022/QCD_Pt-120to170_CP5_13p6TeV_pythia8_v2.xml", XmlSource_2022preEE="",
                # Xml_2022preEE="Run3_126X_v1/2022/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_PT-120to170_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT170to300" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=113400, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=29524592.0,
                # NEVT_2022preEE=29860794.0,
                NEVT_2022postEE=41065808.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_124X_v1/2022/QCD_Pt-170to300_CP5_13p6TeV_pythia8_v2.xml", XmlSource_2022preEE="",
                # Xml_2022preEE="Run3_126X_v1/2022/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_PT-170to300_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT300to470" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=7619, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=56963005.9329,
                # NEVT_2022preEE=58535897.0,
                NEVT_2022postEE=80355820.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_124X_v1/2022/QCD_Pt-300to470_CP5_13p6TeV_pythia8_v2.xml", XmlSource_2022preEE="",
                # Xml_2022preEE="Run3_126X_v1/2022/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_PT-300to470_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT470to600" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=625.1, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=27517265.8289,
                # NEVT_2022preEE=28540568.0,
                NEVT_2022postEE=48417913.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_124X_v1/2022/QCD_Pt-470to600_CP5_13p6TeV_pythia8_v2.xml", XmlSource_2022preEE="",
                # Xml_2022preEE="Run3_126X_v1/2022/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_PT-470to600_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT600to800" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=179.7, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=66904840.0,
                # NEVT_2022preEE=75092875.0,
                NEVT_2022postEE=92473677.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_124X_v1/2022/QCD_Ht-600to800_CP5_13p6TeV_pythia8_v2.xml", XmlSource_2022preEE="",
                # Xml_2022preEE="Run3_126X_v1/2022/QCD_HT-600to800_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-600to800_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_HT-600to800_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-600to800_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT800to1000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=30.71, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=39361952.0,
                # NEVT_2022preEE=43868300.0,
                NEVT_2022postEE=53572105.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_124X_v1/2022/QCD_Ht-800to1000_CP5_13p6TeV_pythia8_v2.xml", XmlSource_2022preEE="",
                # Xml_2022preEE="Run3_126X_v1/2022/QCD_HT-800to1000_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_HT-800to1000_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT1000to1400" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=8.944, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=19587794.0,
                # NEVT_2022preEE=22322802.0,
                NEVT_2022postEE=27675691.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_124X_v1/2022/QCD_Ht-1000to1400_CP5_13p6TeV_pythia8_v2.xml", XmlSource_2022preEE="",
                # Xml_2022preEE="Run3_126X_v1/2022/QCD_HT-1000to1400_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_HT-1000to1400_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT1400to1800" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.8096, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=5875299.0,
                # NEVT_2022preEE=7466758.0,
                NEVT_2022postEE=9974680.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_124X_v1/2022/QCD_Pt-1400to1800_CP5_13p6TeV_pythia8_v2.xml", XmlSource_2022preEE="",
                # Xml_2022preEE="Run3_126X_v1/2022/QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_PT-1400to1800_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT1800to2400" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.1151, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=2948168.0,
                # NEVT_2022preEE=3683361.0,
                NEVT_2022postEE=3683361.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_124X_v1/2022/QCD_Pt-1800to2400_CP5_13p6TeV_pythia8_v2.xml", XmlSource_2022preEE="",
                # Xml_2022preEE="Run3_126X_v1/2022/QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_PT-1800to2400_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT2400to3200" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.007592, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=1972700.0,
                # NEVT_2022preEE=2158928.0,
                NEVT_2022postEE=2694345.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_124X_v1/2022/QCD_Pt-2400to3200_CP5_13p6TeV_pythia8_v2.xml", XmlSource_2022preEE="",
                # Xml_2022preEE="Run3_126X_v1/2022/QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_PT-2400to3200_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT3200toInf" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.0002311, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=785825.0,
                # NEVT_2022preEE=864567.0,
                NEVT_2022postEE=1294987.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_124X_v1/2022/QCD_Pt-3200_CP5_13p6TeV_pythia8_v2.xml", XmlSource_2022preEE="",
                # Xml_2022preEE="Run3_126X_v1/2022/QCD_PT-3200_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-3200_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_PT-3200_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-3200_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },
    }

    def __init__(self, extra_dicts=None, import_signal=None):

        if extra_dicts is not None:
            if type(extra_dicts) == dict:
                self.__values_dict.update(extra_dicts)
            elif type(extra_dicts) == list:
                for ed in extra_dicts:
                    self.__values_dict.update(ed)

        if import_signal is not None:
            imported_dict = self._import_signal(import_signal)
            self.__values_dict = {**self.__values_dict, **imported_dict}

    def _import_signal(self, signal_name):
        spec = importlib.util.spec_from_file_location(
            "MCSignalValuesHelper",
            f"{CMSSW_BASE}/src/UHH2/common/UHH2-datasets/xsec_signal_dicts/{signal_name}.py"
        )
        module = importlib.util.module_from_spec(spec)
        sys.modules["MCSignalHelper"] = module
        spec.loader.exec_module(module)
        return module.MCSignalValuesHelper.signal_values_dict

    def get_value(self, name, energy, year, key, strict=False, info = ""):
        """Return the value for a given MC sample, energy or year, and information type

        If information is stored for both an energy and a year, the value for the given energy will be preferentially returned.
        If strict checking is turned on the function will raise an error if a given dictionary or piece of information isn't found.
          Otherwise the default value will be returned with no error (i.e. will return 1.0 for kFactors)

        Args:
            name (`str`): The process name for a given MC sample
            energy (`str`): The simulated energy used during production of the MC sample
            year (`str`): The production year of the MC sample
            key (`str`): The type of information being requested. The Options can be found in the _key_field_map.
            strict (`bool`): Whether or not to perform strict checking of the dictionary

        """
        fields = [self._key_field_map[key][0]+info+"_"+energy,self._key_field_map[key][0]+info+"_"+year]
        if not name in self.__values_dict:
            print(name)
            print("=======================================")
            raise KeyError("ERROR MCSampleValuesHelper::Unknown process \"" + str(name) + "\"")
        if not key in self.__values_dict[name]:
            if strict:
                print(self.__values_dict[name])
                raise KeyError("ERROR MCSampleValuesHelper::The process \"" + str(name) + "\" does not contain a " + str(key) + " tuple")
            else:
                return self._key_field_map[key][1]
        if not any(f in self.__values_dict[name][key]._fields for f in fields):
            if strict:
                print(self.__values_dict[name][key])
                raise KeyError("ERROR MCSampleValuesHelper::The " + str(key) + " tuple for process \"" + str(name) + "\" does contain the key(s) \"" + str(fields) + "\"")
            else:
                self._key_field_map[key][1]

        if self.__values_dict[name][key].__getattribute__(fields[0]) != self._key_field_map[key][1]:
            return self.__values_dict[name][key].__getattribute__(fields[0])
        else:
            return self.__values_dict[name][key].__getattribute__(fields[1])

    def get_xs(self, name, energy, year, info=""):
        return self.get_value(name, energy, year, "CrossSection", True, info)

    def get_nevt(self, name, energy, year, info=""):
        return self.get_value(name, energy, year, "NEvents", True, info)

    def get_br(self, name, energy, year, info=""):
        return self.get_value(name, energy, year, "BranchingRatio", False, info)

    def get_kfactor(self, name, energy, year, info=""):
        return self.get_value(name, energy, year, "kFactor", False, info)

    def get_corr(self, name, energy, year, info=""):
        return self.get_value(name, energy, year, "Correction", False, info)

    def get_xml(self, name, energy, year, info=""):
        return self.get_value(name, energy, year, "XMLname", False, info)

    def get_lumi(self, name, energy, year, kFactor=False, Corrections=False):
        xsec = self.get_xs(name, energy, year)
        xsec *= self.get_br(name, energy, year)
        if kFactor: xsec *= self.get_kfactor(name, energy, year)
        if Corrections: xsec *= self.get_corr(name, energy, year)
        return abs(self.get_nevt(name, energy, year))/xsec

def print_database(raise_errors=False):
    helper = MCSampleValuesHelper()
    samples = list(MCSampleValuesHelper.__dict__["_MCSampleValuesHelper__values_dict"].keys())
    samples.sort()
    energies = MCSampleValuesHelperPrototype.__dict__["_MCSampleValuesHelperPrototype__energies"]
    years = MCSampleValuesHelperPrototype.__dict__["_MCSampleValuesHelperPrototype__years"]
    import re
    run_pattern = re.compile("(?P<run>(Run)+[ABCDEFGH]{1})")

    max_sample_length = max(len(s) for s in samples)
    abspath_uhh2datasets = os.path.dirname(os.path.abspath(__file__))
    wrong_xmlpaths = []

    def banner(text, decorator = "#", line_width = 30):
        print("")
        print(decorator*line_width)
        print("{text:{deco}^{width}s}".format(text=text,deco=decorator,width=line_width))
        print(decorator*line_width)
        print("")

    for energy in energies:
        banner(energy)
        for year in years:
            banner(year)
            for sample in samples:
                run_match = run_pattern.search(sample)
                isData = run_match is not None
                nevt = helper.get_nevt(sample,energy,year)
                lumi = "/" if (isData or nevt<0) else "%10.2g"%helper.get_lumi(sample,energy,year)
                nevt = "%10.2g"%nevt
                line = '{sample: <{width}}-> nevt:{nevt: >5}, lumi:{lumi: >5}'.format(sample=sample, width=max_sample_length+3, nevt=nevt, lumi=lumi)
                xmlpath = helper.get_xml(sample,energy,year)
                xmlabspath = os.path.join(abspath_uhh2datasets, xmlpath)
                if xmlpath != "" and not os.path.isfile(xmlabspath):
                    line += " "*3+"Error: XML not found!"
                    wrong_xmlpaths.append(xmlpath)
                print(line)

    if len(wrong_xmlpaths) > 0:
        print("")
        print("Error: Cannot find the following XML file(s):")
        for xmlpath in wrong_xmlpaths:
            print(xmlpath)
        print("")
        if raise_errors: raise ValueError("One or multiple XML path(s) are invalid")
    return 0


if(__name__ == "__main__"):
    import argparse
    parser = argparse.ArgumentParser(description="CrossSectionHelper Database: find and calculate crucial information for your Analysis!")

    parser.add_argument("--print", action="store_true", help="print number of events and calculated luminosity of all samples in database (This is primarily to test the integrety of the database).")
    parser.add_argument("--throw", action="store_true", help="raise erros if they occur. Should be used together with --print option.")

    args = parser.parse_args()

    if(args.print):
        print_database(args.throw)
