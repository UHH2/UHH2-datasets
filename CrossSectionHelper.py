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

    __years = ["UL16preVFP","UL16postVFP","UL17","UL18"]
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

        "SingleMuon_RunA": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL18=241591525,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/SingleMuon_Run2018A-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/SingleMuon/Run2018A-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "SingleMuon_RunB": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=2789243+158145722,
                NEVT_UL17=136300266,
                NEVT_UL18=119918017,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleMuon_Run2016B-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleMuon/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleMuon_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleMuon/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/SingleMuon_Run2018B-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/SingleMuon/Run2018B-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "SingleMuon_RunC": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=67441308,
                NEVT_UL17=165652756,
                NEVT_UL18=110032072,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleMuon_Run2016C-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleMuon/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleMuon_Run2017C-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleMuon/Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/SingleMuon_Run2018C-UL2018_MiniAODv2_GT36-v2.xml", XmlSource_UL18="/SingleMuon/Run2018C-UL2018_MiniAODv2_GT36-v2/MINIAOD",
            ),
        },

        "SingleMuon_RunD": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=98017996,
                NEVT_UL17=70361660,
                NEVT_UL18=513884680,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleMuon_Run2016D-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleMuon/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleMuon_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleMuon/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/SingleMuon_Run2018D-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/SingleMuon/Run2018D-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "SingleMuon_RunE": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=90984718,
                NEVT_UL17=154618774,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleMuon_Run2016E-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleMuon/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleMuon_Run2017E-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleMuon/Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleMuon_RunF": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=57465359,
                NEVT_UL16postVFP=8024195,
                NEVT_UL17=242140980,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleMuon_Run2016F-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleMuon/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SingleMuon_Run2016F-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SingleMuon/Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleMuon_Run2017F-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleMuon/Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleMuon_RunG": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=149916849,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SingleMuon_Run2016G-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SingleMuon/Run2016G-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "SingleMuon_RunH": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=174035164,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SingleMuon_Run2016H-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SingleMuon/Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "SingleMuon_Recount_RunA": {
            "NEvents" : NEventsValues(
                NEVT_UL18=238999079,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="RunII_106X_v2/data-recount/UL18/SingleMuon_Run2018A-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/SingleMuon/Run2018A-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "SingleMuon_Recount_RunB": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=160735593,
                NEVT_UL17=134661714,
                NEVT_UL18=119877871,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data-recount/UL16preVFP/SingleMuon_Run2016B-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleMuon/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data-recount/UL17/SingleMuon_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleMuon/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data-recount/UL18/SingleMuon_Run2018B-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/SingleMuon/Run2018B-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "SingleMuon_Recount_RunC": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=67369994,
                NEVT_UL17=164383789,
                NEVT_UL18=109741163,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data-recount/UL16preVFP/SingleMuon_Run2016C-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleMuon/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data-recount/UL17/SingleMuon_Run2017C-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleMuon/Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data-recount/UL18/SingleMuon_Run2018C-UL2018_MiniAODv2_GT36-v2.xml", XmlSource_UL18="/SingleMuon/Run2018C-UL2018_MiniAODv2_GT36-v2/MINIAOD",
            ),
        },

        "SingleMuon_Recount_RunD": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=97977441,
                NEVT_UL17=69722390,
                NEVT_UL18=513724019,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data-recount/UL16preVFP/SingleMuon_Run2016D-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleMuon/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data-recount/UL17/SingleMuon_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleMuon/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data-recount/UL18/SingleMuon_Run2018D-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/SingleMuon/Run2018D-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "SingleMuon_Recount_RunE": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=90961745,
                NEVT_UL17=152020221,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data-recount/UL16preVFP/SingleMuon_Run2016E-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleMuon/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data-recount/UL17/SingleMuon_Run2017E-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleMuon/Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleMuon_Recount_RunF": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=57213127,
                NEVT_UL16postVFP=8024195,
                NEVT_UL17=238755357,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data-recount/UL16preVFP/SingleMuon_Run2016F-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleMuon/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data-recount/UL16postVFP/SingleMuon_Run2016F-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SingleMuon/Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data-recount/UL17/SingleMuon_Run2017F-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleMuon/Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleMuon_Recount_RunG": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=147188777,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data-recount/UL16postVFP/SingleMuon_Run2016G-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SingleMuon/Run2016G-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "SingleMuon_Recount_RunH": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=172247673,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data-recount/UL16postVFP/SingleMuon_Run2016H-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SingleMuon/Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },
        
        "SingleElectron_RunB": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=1422819+246433497,
                NEVT_UL17=60537490,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleElectron_Run2016B-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleElectron/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleElectron_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleElectron/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleElectron_RunC": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=97259854,
                NEVT_UL17=136637888,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleElectron_Run2016C-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleElectron/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleElectron_Run2017C-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleElectron/Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleElectron_RunD": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=148167727,
                NEVT_UL17=51526521,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleElectron_Run2016D-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleElectron/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleElectron_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleElectron/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleElectron_RunE": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=117269446,
                NEVT_UL17=102122055,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleElectron_Run2016E-HIPM_UL2016_MiniAODv2-v5.xml", XmlSource_UL16preVFP="/SingleElectron/Run2016E-HIPM_UL2016_MiniAODv2-v5/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleElectron_Run2017E-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleElectron/Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleElectron_RunF": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=61735326,
                NEVT_UL16postVFP=8858206,
                NEVT_UL17=128467223,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleElectron_Run2016F-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleElectron/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SingleElectron_Run2016F-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SingleElectron/Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleElectron_Run2017F-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleElectron/Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleElectron_RunG": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=153363109,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SingleElectron_Run2016G-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SingleElectron/Run2016G-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "SingleElectron_RunH": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=128998505,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SingleElectron_Run2016H-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SingleElectron/Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "SinglePhoton_RunB": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=13119462+56878553,
                NEVT_UL17=15950935,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SinglePhoton_Run2016B-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SinglePhoton/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SinglePhoton_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SinglePhoton/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SinglePhoton_RunC": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=23147235,
                NEVT_UL17=42182948,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SinglePhoton_Run2016C-HIPM_UL2016_MiniAODv2-v4.xml", XmlSource_UL16preVFP="/SinglePhoton/Run2016C-HIPM_UL2016_MiniAODv2-v4/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SinglePhoton_Run2017C-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SinglePhoton/Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SinglePhoton_RunD": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=29801360,
                NEVT_UL17=9753462,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SinglePhoton_Run2016D-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SinglePhoton/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SinglePhoton_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SinglePhoton/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SinglePhoton_RunE": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=22322869,
                NEVT_UL17=19011446,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SinglePhoton_Run2016E-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SinglePhoton/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SinglePhoton_Run2017E-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SinglePhoton/Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SinglePhoton_RunF": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=12806145,
                NEVT_UL16postVFP=1860761,
                NEVT_UL17=29783015,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SinglePhoton_Run2016F-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SinglePhoton/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SinglePhoton_Run2016F-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SinglePhoton/Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SinglePhoton_Run2017F-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SinglePhoton/Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SinglePhoton_RunG": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=33288854,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SinglePhoton_Run2016G-UL2016_MiniAODv2-v3.xml", XmlSource_UL16postVFP="/SinglePhoton/Run2016G-UL2016_MiniAODv2-v3/MINIAOD",
            ),
        },

        "SinglePhoton_RunH": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=35035661,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SinglePhoton_Run2016H-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SinglePhoton/Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "EGamma_RunA": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL18=339013231,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/EGamma_Run2018A-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/EGamma/Run2018A-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "EGamma_RunB": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL18=153792795,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/EGamma_Run2018B-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/EGamma/Run2018B-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "EGamma_RunC": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL18=147827904,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/EGamma_Run2018C-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/EGamma/Run2018C-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "EGamma_RunD": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL18=752497815,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/EGamma_Run2018D-UL2018_MiniAODv2-v2.xml", XmlSource_UL18="/EGamma/Run2018D-UL2018_MiniAODv2-v2/MINIAOD",
            ),
        },

        "MuonEG_RunA": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL18=32958503,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/MuonEG_Run2018A-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/MuonEG/Run2018A-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "MuonEG_RunB": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=225271+32727796,
                NEVT_UL17=4453465,
                NEVT_UL18=16204062,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/MuonEG_Run2016B-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/MuonEG/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v2/MINIAOD ",
                Xml_UL17="RunII_106X_v2/data/UL17/MuonEG_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/MuonEG/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/MuonEG_Run2018B-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/MuonEG/Run2018B-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "MuonEG_RunC": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=15405678,
                NEVT_UL18=15652198,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/MuonEG_Run2016C-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/MuonEG/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD ",
                Xml_UL18="RunII_106X_v2/data/UL18/MuonEG_Run2018C-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/MuonEG/Run2018C-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },


        "MuonEG_RunD": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=23482352,
                NEVT_UL17=9164365,
                NEVT_UL18=71947999,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/MuonEG_Run2016D-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/MuonEG/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/MuonEG_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/MuonEG/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/MuonEG_Run2018D-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/MuonEG/Run2018D-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "MuonEG_RunE": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=22519303,
                NEVT_UL17=19043421,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/MuonEG_Run2016E-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/MuonEG/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/MuonEG_Run2017E-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/MuonEG/Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "MuonEG_RunF": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=14100826,
                NEVT_UL16postVFP=1901339,
                NEVT_UL17=25776363,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/MuonEG_Run2016F-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/MuonEG/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/MuonEG_Run2016F-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/MuonEG/Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/MuonEG_Run2017F-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/MuonEG/Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "MuonEG_RunG": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=33854612,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/MuonEG_Run2016G-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/MuonEG/Run2016G-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "MuonEG_RunH": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=29236516,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/MuonEG_Run2016H-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/MuonEG/Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "DoubleMuon_RunA": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL18=75499908,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/DoubleMuon_Run2018A-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/DoubleMuon/Run2018A-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "DoubleMuon_RunB": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=4199947+82535526,
                NEVT_UL17=14501767,
                NEVT_UL18=35057758,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/DoubleMuon_Run2016B-HIPM_UL2016_MiniAODv2-v1.xml", XmlSource_UL16preVFP="/DoubleMuon/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/DoubleMuon_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/DoubleMuon/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/DoubleMuon_Run2018B-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/DoubleMuon/Run2018B-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "DoubleMuon_RunC": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=27934629,
                NEVT_UL17=49636525,
                NEVT_UL18=34565869,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/DoubleMuon_Run2016C-HIPM_UL2016_MiniAODv2-v1.xml", XmlSource_UL16preVFP="/DoubleMuon/Run2016C-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/DoubleMuon_Run2017C-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/DoubleMuon/Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/DoubleMuon_Run2018C-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/DoubleMuon/Run2018C-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "DoubleMuon_RunD": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=33861745,
                NEVT_UL17=23075733,
                NEVT_UL18=168618482,  # DAS value: 168620231
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/DoubleMuon_Run2016D-HIPM_UL2016_MiniAODv2-v1.xml", XmlSource_UL16preVFP="/DoubleMuon/Run2016D-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/DoubleMuon_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/DoubleMuon/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/DoubleMuon_Run2018D-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/DoubleMuon/Run2018D-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "DoubleMuon_RunE": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=28246946,
                NEVT_UL17=51531477,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/DoubleMuon_Run2016E-HIPM_UL2016_MiniAODv2-v1.xml", XmlSource_UL16preVFP="/DoubleMuon/Run2016E-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/DoubleMuon_Run2017E-UL2017_MiniAODv2-v2.xml", XmlSource_UL17="/DoubleMuon/Run2017E-UL2017_MiniAODv2-v2/MINIAOD",
            ),
        },

        "DoubleMuon_RunF": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=17900759,
                NEVT_UL16postVFP=2429162,
                NEVT_UL17=79756560,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/DoubleMuon_Run2016F-HIPM_UL2016_MiniAODv2-v1.xml", XmlSource_UL16preVFP="/DoubleMuon/Run2016F-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/DoubleMuon_Run2016F-UL2016_MiniAODv2-v1.xml", XmlSource_UL16postVFP="/DoubleMuon/Run2016F-UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/DoubleMuon_Run2017F-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/DoubleMuon/Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "DoubleMuon_RunG": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=45235604,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/DoubleMuon_Run2016G-UL2016_MiniAODv2-v1.xml", XmlSource_UL16postVFP="/DoubleMuon/Run2016G-UL2016_MiniAODv2-v1/MINIAOD",
            ),
        },

        "DoubleMuon_RunH": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=48912812,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/DoubleMuon_Run2016H-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/DoubleMuon/Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "DoubleEG_RunB": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=5686987+143073268,
                NEVT_UL17=58088760
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/DoubleEG_Run2016B-HIPM_UL2016_MiniAODv2.xml", XmlSource_UL16preVFP="/DoubleEG/{Run2016B-ver1_HIPM_UL2016_MiniAODv2-v1,Run2016B-ver2_HIPM_UL2016_MiniAODv2-v3}/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/DoubleEG_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/DoubleEG/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "DoubleEG_RunC": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=47677856,
                NEVT_UL17=65181125
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/DoubleEG_Run2016C-HIPM_UL2016_MiniAODv2-v1.xml", XmlSource_UL16preVFP="/DoubleEG/Run2016C-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/DoubleEG_Run2017C-UL2017_MiniAODv2-v2.xml", XmlSource_UL17="/DoubleEG/Run2017C-UL2017_MiniAODv2-v2/MINIAOD",
            ),
        },

        "DoubleEG_RunD": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=53324960,
                NEVT_UL17=25911432
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/DoubleEG_Run2016D-HIPM_UL2016_MiniAODv2-v1.xml", XmlSource_UL16preVFP="/DoubleEG/Run2016D-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/DoubleEG_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/DoubleEG/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "DoubleEG_RunE": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=49877710,
                NEVT_UL17=56241190
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/DoubleEG_Run2016E-HIPM_UL2016_MiniAODv2-v1.xml", XmlSource_UL16preVFP="/DoubleEG/Run2016E-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/DoubleEG_Run2017E-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/DoubleEG/Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "DoubleEG_RunF": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=30216940,
                NEVT_UL16postVFP=4360689,
                NEVT_UL17=74265012
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/DoubleEG_Run2016F-HIPM_UL2016_MiniAODv2-v1.xml", XmlSource_UL16preVFP="/DoubleEG/Run2016F-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/DoubleEG_Run2016F-UL2016_MiniAODv2-v1.xml", XmlSource_UL16postVFP="/DoubleEG/Run2016F-UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/DoubleEG_Run2017F-UL2017_MiniAODv2-v2.xml", XmlSource_UL17="/DoubleEG/Run2017F-UL2017_MiniAODv2-v2/MINIAOD",
            ),
        },

        "DoubleEG_RunG": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=78797031,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/DoubleEG_Run2016G-UL2016_MiniAODv2-v1.xml", XmlSource_UL16postVFP="/DoubleEG/Run2016G-UL2016_MiniAODv2-v1/MINIAOD",
            ),
        },

        "DoubleEG_RunH": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=85388734,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/DoubleEG_Run2016H-UL2016_MiniAODv2-v1.xml", XmlSource_UL16postVFP="/DoubleEG/Run2016H-UL2016_MiniAODv2-v1/MINIAOD",
            ),
        },

        "JetHT_RunA": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL18=171502033,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/JetHT_Run2018A-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/JetHT/Run2018A-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "JetHT_RunB": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=9726665+133752091,
                NEVT_UL17=63043590,
                NEVT_UL18=78253065,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016B-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/JetHT_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/JetHT_Run2018B-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/JetHT/Run2018B-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "JetHT_RunC": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=46495988,
                NEVT_UL17=96264601,
                NEVT_UL18=70027804,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016C-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/JetHT_Run2017C-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/JetHT_Run2018C-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/JetHT/Run2018C-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "JetHT_RunD": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=73330042,
                NEVT_UL17=46145204,
                NEVT_UL18=356976276,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016D-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/JetHT_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/JetHT_Run2018D-UL2018_MiniAODv2-v2.xml", XmlSource_UL18="/JetHT/Run2018D-UL2018_MiniAODv2-v2/MINIAOD",
            ),
        },

        "JetHT_RunE": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=69219288,
                NEVT_UL17=89630771,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016E-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/JetHT_Run2017E-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "JetHT_RunF": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=41564915,
                NEVT_UL16postVFP=6613811,
                NEVT_UL17=115429972,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016F-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/JetHT_Run2016F-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/JetHT/JetHT_Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/JetHT_Run2017F-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "JetHT_RunG": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=120745085,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/JetHT_Run2016G-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/JetHT/JetHT_Run2016G-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "JetHT_RunH": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=124054791,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/JetHT_Run2016H-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/JetHT/JetHT_Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "JetHT_Recount_RunA": {
            "NEvents" : NEventsValues(
                NEVT_UL18=171484635,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="RunII_106X_v2/data-recount/UL18/JetHT_Run2018A-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/JetHT/Run2018A-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "JetHT_Recount_RunB": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=9726665+133752091,
                NEVT_UL17=61999044,
                NEVT_UL18=78255208,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data-recount/UL16preVFP/JetHT_Run2016B-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data-recount/UL17/JetHT_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data-recount/UL18/JetHT_Run2018B-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/JetHT/Run2018B-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "JetHT_Recount_RunC": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=46335578,
                NEVT_UL17=95387879,
                NEVT_UL18=69805746,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data-recount/UL16preVFP/JetHT_Run2016C-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data-recount/UL17/JetHT_Run2017C-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data-recount/UL18/JetHT_Run2018C-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/JetHT/Run2018C-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "JetHT_Recount_RunD": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=72910640,
                NEVT_UL17=45884861,
                NEVT_UL18=353299566,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data-recount/UL16preVFP/JetHT_Run2016D-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data-recount/UL17/JetHT_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data-recount/UL18/JetHT_Run2018D-UL2018_MiniAODv2-v2.xml", XmlSource_UL18="/JetHT/Run2018D-UL2018_MiniAODv2-v2/MINIAOD",
            ),
        },

        "JetHT_Recount_RunE": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=68137485,
                NEVT_UL17=88766313,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data-recount/UL16preVFP/JetHT_Run2016E-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data-recount/UL17/JetHT_Run2017E-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "JetHT_Recount_RunF": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=41448546,
                NEVT_UL16postVFP=6542357,
                NEVT_UL17=114132344,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data-recount/UL16preVFP/JetHT_Run2016F-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data-recount/UL16postVFP/JetHT_Run2016F-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/JetHT/JetHT_Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data-recount/UL17/JetHT_Run2017F-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "JetHT_Recount_RunG": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=119175632,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data-recount/UL16postVFP/JetHT_Run2016G-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/JetHT/JetHT_Run2016G-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "JetHT_Recount_RunH": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=123206820,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data-recount/UL16postVFP/JetHT_Run2016H-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/JetHT/JetHT_Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "MET_RunA": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL18=52759851,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/MET_Run2018A-UL2018_MiniAODv2-v2.xml", XmlSource_UL18="/MET/Run2018A-UL2018_MiniAODv2-v2/MINIAOD",
            ),
        },

        "MET_RunB": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=583427+35987712,
                NEVT_UL17=51623474,
                NEVT_UL18=29713483,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/MET_Run2016B-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/MET/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/MET_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/MET/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/MET_Run2018B-UL2018_MiniAODv2-v2.xml", XmlSource_UL18="/MET/Run2018B-UL2018_MiniAODv2-v2/MINIAOD",
            ),
        },

        "MET_RunC": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=17381222,
                NEVT_UL17=115906496,
                NEVT_UL18=31237456,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/MET_Run2016C-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/MET/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/MET_Run2017C-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/MET/Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/MET_Run2018C-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/MET/Run2018C-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "MET_RunD": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=20947429,
                NEVT_UL17=20075033,
                NEVT_UL18=160411782,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/MET_Run2016D-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/MET/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/MET_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/MET/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/MET_Run2018D-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/MET/Run2018D-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "MET_RunE": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=22348402,
                NEVT_UL17=71418865,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/MET_Run2016E-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/MET/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/MET_Run2017E-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/MET/Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "MET_RunF": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=11936579,
                NEVT_UL16postVFP=1383250,
                NEVT_UL17=177521562,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/MET_Run2016F-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/MET/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/MET_Run2016F-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/MET/Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/MET_Run2017F-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/MET/Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "MET_RunG": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=26974131,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/MET_Run2016G-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/MET/Run2016G-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "MET_RunH": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=39773485,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/MET_Run2016H-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/MET/Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "TTTo2L2Nu" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=2680294258.52,
                NEVT_UL16postVFP=3091955525.07,
                NEVT_UL17=7545276778.28,
                NEVT_UL18=10319109327.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=39046225860.2,
                NEVT_UL16postVFP=42833982385.9,
                NEVT_UL17=1.04665737783e+11,
                NEVT_UL18=1.40602835351e+11,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TTToHadronic" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=30289246641.2,
                NEVT_UL16postVFP=33636223378.5,
                NEVT_UL17=72581777583.5,
                NEVT_UL18=1.05390931299e+11,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_hdampDOWN" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=1197862430.31,
                NEVT_UL16postVFP=1281174098.73,
                NEVT_UL17=2901238789.09,
                NEVT_UL18=4269966880.49,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_hdampDOWN_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_hdampDOWN_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_hdampDOWN_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_hdampDOWN_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_hdampDOWN" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=13961893555.7,
                NEVT_UL16postVFP=17836654362.5,
                NEVT_UL17=39925842861.7,
                NEVT_UL18=57506966984.8,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_hdampDOWN_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_hdampDOWN_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_hdampDOWN_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_hdampDOWN_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToHadronic_hdampDOWN" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=11446167870.6,
                NEVT_UL16postVFP=12607597136.2,
                NEVT_UL17=29564356917.2,
                NEVT_UL18=43215068981.3,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_hdampDOWN_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_hdampDOWN_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_hdampDOWN_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_hdampDOWN_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_hdampUP" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=1061555213.51,
                NEVT_UL16postVFP=1340936356.64,
                NEVT_UL17=2865635907.54,
                NEVT_UL18=3887613377.53,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_hdampUP_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_hdampUP_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_hdampUP_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_hdampUP_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_hdampUP" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=16817574381.2,
                NEVT_UL16postVFP=17893282815.6,
                NEVT_UL17=39539431122.1,
                NEVT_UL18=58441433820.4,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_hdampUP_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_hdampUP_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_hdampUP_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_hdampUP_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToHadronic_hdampUP" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=9358050857.84,
                NEVT_UL16postVFP=12920242862.1,
                NEVT_UL17=30761655119.2,
                NEVT_UL18=42686125502.6,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_hdampUP_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_hdampUP_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_hdampUP_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_hdampUP_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_CR1" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=1023859348.4,
                NEVT_UL16postVFP=1250498489.52,
                NEVT_UL17=2955966079.08,
                NEVT_UL18=4152998892.44,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_CP5CR1_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_CP5CR1_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_CP5CR1_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TTTo2L2Nu_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_CP5CR1_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TTTo2L2Nu_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_CR1" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=15563564465.2,
                NEVT_UL16postVFP=16716846647.5,
                NEVT_UL17=40131552815.2,
                NEVT_UL18=58767892364.7,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_CP5CR1_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_CP5CR1_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_CP5CR1_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TTToSemiLeptonic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_CP5CR1_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TTToSemiLeptonic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TTToHadronic_CR1" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=11268884747.0,
                NEVT_UL16postVFP=12718350943.3,
                NEVT_UL17=29105749551.3,
                NEVT_UL18=41545320212.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_CP5CR1_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_CP5CR1_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_CP5CR1_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TTToHadronic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_CP5CR1_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TTToHadronic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_CR2" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=1209778279.97,
                NEVT_UL16postVFP=1255635933.36,
                NEVT_UL17=2963180077.1,
                NEVT_UL18=3972564611.91,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_CP5CR2_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_CP5CR2_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_CP5CR2_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TTTo2L2Nu_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_CP5CR2_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_CR2" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=16948358553.1,
                NEVT_UL16postVFP=18382760775.3,
                NEVT_UL17=40933451783.8,
                NEVT_UL18=56497445197.3,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_CP5CR2_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_CP5CR2_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_CP5CR2_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TTToSemiLeptonic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_CP5CR2_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TTToSemiLeptonic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TTToHadronic_CR2" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=12523219904.4,
                NEVT_UL16postVFP=12838937782.3,
                NEVT_UL17=30384752917.0,
                NEVT_UL18=38597247611.8,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_CP5CR2_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_CP5CR2_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_CP5CR2_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TTToHadronic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_CP5CR2_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TTToHadronic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_erdON" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=1166883518.38,
                NEVT_UL16postVFP=1238456161.15,
                NEVT_UL17=3020202881.21,
                NEVT_UL18=3914681059.69,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_CP5_erdON_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_CP5_erdON_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_CP5_erdON_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_CP5_erdON_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_erdON" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=16726593539.7,
                NEVT_UL16postVFP=16039338414.0,
                NEVT_UL17=37734192187.5,
                NEVT_UL18=57807995448.1,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_CP5_erdON_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_CP5_erdON_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_CP5_erdON_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_CP5_erdON_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToHadronic_erdON" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=11871224618.2,
                NEVT_UL16postVFP=11475398435.2,
                NEVT_UL17=27839310518.9,
                NEVT_UL18=36718967449.4,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_CP5_erdON_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_CP5_erdON_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_CP5_erdON_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_CP5_erdON_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_TuneCP5down" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=1200799748.55,
                NEVT_UL16postVFP=1313795448.26,
                NEVT_UL17=2798334638.8,
                NEVT_UL18=4255052479.61,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_CP5down_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_CP5down_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_CP5down_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_CP5down_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_TuneCP5down" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=16533387862.2,
                NEVT_UL16postVFP=5694154674.83,
                NEVT_UL17=39621941101.6,
                NEVT_UL18=56302694820.2,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_CP5down_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_CP5down_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_CP5down_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_CP5down_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToHadronic_TuneCP5down" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=11678002502.4,
                NEVT_UL16postVFP=11943221900.2,
                NEVT_UL17=30091840845.2,
                NEVT_UL18=43235503109.4,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_CP5down_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_CP5down_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_CP5down_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_CP5down_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_TuneCP5up" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=734714642.148,
                NEVT_UL16postVFP=1275998582.74,
                NEVT_UL17=3040581960.46,
                NEVT_UL18=4077753822.45,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_CP5up_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_CP5up_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_CP5up_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_CP5up_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_TuneCP5up" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=13853464424.1,
                NEVT_UL16postVFP=17294333500.5,
                NEVT_UL17=41350185591.3,
                NEVT_UL18=59180771705.3,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_CP5up_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_CP5up_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_CP5up_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_CP5up_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToHadronic_TuneCP5up" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=8903470364.36,
                NEVT_UL16postVFP=12608570785.4,
                NEVT_UL17=29815196708.6,
                NEVT_UL18=42471162708.9,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_CP5up_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_CP5up_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_CP5up_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_CP5up_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_mtop171p5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=1225860665.17,
                NEVT_UL16postVFP=1254090512.99,
                NEVT_UL17=3011632940.44,
                NEVT_UL18=4353594545.1,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_mtop171p5_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_mtop171p5_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_mtop171p5_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_mtop171p5_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_mtop171p5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=16178279103.6,
                NEVT_UL16postVFP=19073535892.2,
                NEVT_UL17=40325014927.6,
                NEVT_UL18=59484391520.3,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_mtop171p5_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_mtop171p5_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_mtop171p5_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToSemiLeptonic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_mtop171p5_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToSemiLeptonic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToHadronic_mtop171p5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=10181482920.6,
                NEVT_UL16postVFP=13450184532.8,
                NEVT_UL17=30730586945.0,
                NEVT_UL18=42478511401.7,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_mtop171p5_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_mtop171p5_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_mtop171p5_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToHadronic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_mtop171p5_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToHadronic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_mtop173p5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=1159308909.57,
                NEVT_UL16postVFP=1292194785.83,
                NEVT_UL17=2947067430.65,
                NEVT_UL18=4130918265.75,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_mtop173p5_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_mtop173p5_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_mtop173p5_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTTo2L2Nu_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_mtop173p5_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_mtop173p5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=15587693502.1,
                NEVT_UL16postVFP=18155704147.0,
                NEVT_UL17=39981036953.5,
                NEVT_UL18=56612077174.6,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_mtop173p5_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_mtop173p5_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_mtop173p5_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToSemiLeptonic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_mtop173p5_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToSemiLeptonic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToHadronic_mtop173p5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=11586470023.2,
                NEVT_UL16postVFP=11822443510.9,
                NEVT_UL17=27213210232.2,
                NEVT_UL18=41353875034.7,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_mtop173p5_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_mtop173p5_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_mtop173p5_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToHadronic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_mtop173p5_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToHadronic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TT_Mtt-700to1000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=6.472e+01, XSecSource_13TeV="GenXSecAnalyzer (NLO) run on UL17 (other years and also XSDB give similar results); accuracy: NLO"),
            "Correction" : MCSampleValuesHelperPrototype.CorrValues(Corr_13TeV=1.20965315498, CorrSource_13TeV="Scales to NNLO+NNLL x-section of TTTo2L2Nu/TTToSemiLeptonic/TTToHadronic. This correction factor should always be used"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=15428671630.7,
                NEVT_UL16postVFP=22114826074.8,
                NEVT_UL17=23707720935.1,
                NEVT_UL18=20186431496.3,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TT_Mtt-700to1000_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TT_Mtt-700to1000_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TT_Mtt-700to1000_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TT_Mtt-700to1000_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TT_Mtt-1000toInf" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=1.644e+01, XSecSource_13TeV="GenXSecAnalyzer (NLO) run on UL17 (other years and also XSDB give similar results); accuracy: NLO"),
            "Correction" : MCSampleValuesHelperPrototype.CorrValues(Corr_13TeV=1.21062828535, CorrSource_13TeV="Scales to NNLO+NNLL x-section of TTTo2L2Nu/TTToSemiLeptonic/TTToHadronic. This correction factor should always be used"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=15067133331.4,
                NEVT_UL16postVFP=15423276754.0,
                NEVT_UL17=14453168259.4,
                NEVT_UL18=15100961220.6,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TT_Mtt-1000toInf_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TT_Mtt-1000toInf_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TT_Mtt-1000toInf_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TT_Mtt-1000toInf_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTZToLLNuNu_M-10_TuneCP5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=0.86, XSecSource_13TeV="Phys. Rev. Lett. 113 (2014) 212001 [doi:10.1103/PhysRevLett.113.212001]"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=3*(0.0337+0.0667), BRatSource_13TeV="P.A. Zyla et al. (Particle Data Group), Prog. Theor. Exp. Phys. 2020, 083C01 (2020) and 2021 update"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=1240740.28786,
                NEVT_UL16postVFP=1302013.01608,
                NEVT_UL17=3147863.98856,
                NEVT_UL18=4163657.45538,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTZToLLNuNu_M-10_CP5_amcatnlo-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTZToLLNuNu_M-10_CP5_amcatnlo-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTZToLLNuNu_M-10_CP5_amcatnlo-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTZToLLNuNu_M-10_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TTZToQQ_TuneCP5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=0.86, XSecSource_13TeV="Phys. Rev. Lett. 113 (2014) 212001 [doi:10.1103/PhysRevLett.113.212001]"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.69911, BRatSource_13TeV="P.A. Zyla et al. (Particle Data Group), Prog. Theor. Exp. Phys. 2020, 083C01 (2020) and 2021 update"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=2820246.42682,
                NEVT_UL16postVFP=2501912.28784,
                NEVT_UL17=6251604.96937,
                NEVT_UL18=9076765.172,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTZToQQ_CP5_amcatnlo-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTZToQQ_CP5_amcatnlo-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTZToQQ_CP5_amcatnlo-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTZToQQ_CP5_amcatnlo-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTWJetsToLNu_TuneCP5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=0.55, XSecSource_13TeV="Phys. Rev. Lett. 113 (2014) 212001 [doi:10.1103/PhysRevLett.113.212001]"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.3259, BRatSource_13TeV="P.A. Zyla et al. (Particle Data Group), Prog. Theor. Exp. Phys. 2020, 083C01 (2020) and 2021 update"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=897958.076616,
                NEVT_UL16postVFP=1011158.23988,
                NEVT_UL17=2274937.44366,
                NEVT_UL18=3308394.87692,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTWJetsToLNu_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTWJetsToLNu_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTWJetsToLNu_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTWJetsToLNu_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTWJetsToQQ_TuneCP5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=0.55, XSecSource_13TeV="Phys. Rev. Lett. 113 (2014) 212001 [doi:10.1103/PhysRevLett.113.212001]"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.6741, BRatSource_13TeV="P.A. Zyla et al. (Particle Data Group), Prog. Theor. Exp. Phys. 2020, 083C01 (2020) and 2021 update"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=184218.52966,
                NEVT_UL16postVFP=192966.440722,
                NEVT_UL17=396359.08415,
                NEVT_UL18=618644.88861,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTWJetsToQQ_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTWJetsToQQ_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTWJetsToQQ_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTWJetsToQQ_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ST_tW_top_5f_inclusiveDecays" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=73865468.5159,
                NEVT_UL16postVFP=77706568.1571,
                NEVT_UL17=180170155.832,
                NEVT_UL18=252686664.443,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_top_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_top_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_top_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_top_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_antitop_5f_inclusiveDecays" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=73231461.292,
                NEVT_UL16postVFP=81463780.1346,
                NEVT_UL17=183146011.973,
                NEVT_UL18=246440837.735,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_antitop_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_antitop_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_antitop_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_antitop_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_top_5f_NoFullyHadronicDecays" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=106897142.991,
                NEVT_UL16postVFP=106203776.64,
                NEVT_UL17=269090098.502,
                NEVT_UL18=353991930.706,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_top_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_top_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_top_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_top_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ST_tW_antitop_5f_NoFullyHadronicDecays" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=100955860.943,
                NEVT_UL16postVFP=115715265.781,
                NEVT_UL17=268785976.757,
                NEVT_UL18=347367542.617,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_antitop_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_antitop_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_antitop_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_antitop_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ST_tW_top_5f_NoFullyHadronicDecays_PDFWeights" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=114967927.655,
                NEVT_UL16postVFP=111065113.447,
                NEVT_UL17=262331789.493,
                NEVT_UL18=395200091.524,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_top_5f_NoFullyHadronicDecays_CP5_PDFWeights-powheg-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV_PDFWeights-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_top_5f_NoFullyHadronicDecays_CP5_PDFWeights-powheg-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV_PDFWeights-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_top_5f_NoFullyHadronicDecays_CP5_PDFWeights-powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV_PDFWeights-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_top_5f_NoFullyHadronicDecays_CP5_PDFWeights-powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV_PDFWeights-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_antitop_5f_NoFullyHadronicDecays_PDFWeights" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=113759617.464,
                NEVT_UL16postVFP=127021370.972,
                NEVT_UL17=267315093.384,
                NEVT_UL18=379830884.034,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_antitop_5f_NoFullyHadronicDecays_CP5_PDFWeights-powheg-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV_PDFWeights-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_antitop_5f_NoFullyHadronicDecays_CP5_PDFWeights-powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV_PDFWeights-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_antitop_5f_NoFullyHadronicDecays_CP5_PDFWeights-powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV_PDFWeights-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_antitop_5f_NoFullyHadronicDecays_CP5_PDFWeights-powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV_PDFWeights-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_top_5f_DS_NoFullyHadronicDecays" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=43834506.9753,
                NEVT_UL16postVFP=47205739.4822,
                NEVT_UL17=99703619.0356,
                NEVT_UL18=147027059.792,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_top_5f_DS_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ST_tW_top_5f_DS_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_top_5f_DS_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ST_tW_top_5f_DS_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_top_5f_DS_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ST_tW_top_5f_DS_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_top_5f_DS_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_top_5f_DS_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_antitop_5f_DS_NoFullyHadronicDecays" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=45820915.7075,
                NEVT_UL16postVFP=48677195.4038,
                NEVT_UL17=108470112.622,
                NEVT_UL18=151570067.836,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_antitop_5f_DS_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ST_tW_antitop_5f_DS_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_antitop_5f_DS_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ST_tW_antitop_5f_DS_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_antitop_5f_DS_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_tW_antitop_5f_DS_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_antitop_5f_DS_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_antitop_5f_DS_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_top_5f_hdampdown_NoFullyHadronicDecays" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=45069892.8416,
                NEVT_UL16postVFP=46832452.8296,
                NEVT_UL17=112933709.709,
                NEVT_UL18=152124659.855,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_top_5f_hdampdown_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ST_tW_top_5f_hdampdown_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_top_5f_hdampdown_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ST_tW_top_5f_hdampdown_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_top_5f_hdampdown_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ST_tW_top_5f_hdampdown_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_top_5f_hdampdown_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_top_5f_hdampdown_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_antitop_5f_hdampdown_NoFullyHadronicDecays" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=44858915.6433,
                NEVT_UL16postVFP=50345517.9472,
                NEVT_UL17=108841119.452,
                NEVT_UL18=152035456.84,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_antitop_5f_hdampdown_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ST_tW_antitop_5f_hdampdown_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_antitop_5f_hdampdown_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ST_tW_antitop_5f_hdampdown_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_antitop_5f_hdampdown_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ST_tW_antitop_5f_hdampdown_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_antitop_5f_hdampdown_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_antitop_5f_hdampdown_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_top_5f_hdampup_NoFullyHadronicDecays" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=44499753.1117,
                NEVT_UL16postVFP=48701601.1062,
                NEVT_UL17=111075592.757,
                NEVT_UL18=148292224.868,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_top_5f_hdampup_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ST_tW_top_5f_hdampup_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_top_5f_hdampup_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ST_tW_top_5f_hdampup_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_top_5f_hdampup_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ST_tW_top_5f_hdampup_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_top_5f_hdampup_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_top_5f_hdampup_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_antitop_5f_hdampup_NoFullyHadronicDecays" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=44764839.0862,
                NEVT_UL16postVFP=48895564.3112,
                NEVT_UL17=106200092.194,
                NEVT_UL18=150756696.573,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_antitop_5f_hdampup_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ST_tW_antitop_5f_hdampup_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_antitop_5f_hdampup_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ST_tW_antitop_5f_hdampup_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_antitop_5f_hdampup_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ST_tW_antitop_5f_hdampup_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_antitop_5f_hdampup_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_antitop_5f_hdampup_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_top_5f_NoFullyHadronicDecays_mtop1715" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=46690549.1713,
                NEVT_UL16postVFP=49730422.565,
                NEVT_UL17=105718613.199,
                NEVT_UL18=156581260.414,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_top_5f_NoFullyHadronicDecays_mtop1715_CP5_powheg-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ST_tW_top_5f_NoFullyHadronicDecays_mtop1715_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_top_5f_NoFullyHadronicDecays_mtop1715_CP5_powheg-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ST_tW_top_5f_NoFullyHadronicDecays_mtop1715_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_top_5f_NoFullyHadronicDecays_mtop1715_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ST_tW_top_5f_NoFullyHadronicDecays_mtop1715_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_top_5f_NoFullyHadronicDecays_mtop1715_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_top_5f_NoFullyHadronicDecays_mtop1715_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_antitop_5f_NoFullyHadronicDecays_mtop1715" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=45061386.5283,
                NEVT_UL16postVFP=47023511.4875,
                NEVT_UL17=102659446.378,
                NEVT_UL18=156251109.018,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_antitop_5f_NoFullyHadronicDecays_mtop1715_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ST_tW_antitop_5f_NoFullyHadronicDecays_mtop1715_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_antitop_5f_NoFullyHadronicDecays_mtop1715_CP5_powheg-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ST_tW_antitop_5f_NoFullyHadronicDecays_mtop1715_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_antitop_5f_NoFullyHadronicDecays_mtop1715_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ST_tW_antitop_5f_NoFullyHadronicDecays_mtop1715_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_antitop_5f_NoFullyHadronicDecays_mtop1715_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ST_tW_antitop_5f_NoFullyHadronicDecays_mtop1715_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ST_tW_top_5f_NoFullyHadronicDecays_mtop1735" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=40488608.3189,
                NEVT_UL16postVFP=45440156.4509,
                NEVT_UL17=107331424.929,
                NEVT_UL18=148731209.598,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_top_5f_NoFullyHadronicDecays_mtop1735_CP5_powheg-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ST_tW_top_5f_NoFullyHadronicDecays_mtop1735_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_top_5f_NoFullyHadronicDecays_mtop1735_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ST_tW_top_5f_NoFullyHadronicDecays_mtop1735_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_top_5f_NoFullyHadronicDecays_mtop1735_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_tW_top_5f_NoFullyHadronicDecays_mtop1735_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_top_5f_NoFullyHadronicDecays_mtop1735_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_top_5f_NoFullyHadronicDecays_mtop1735_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_antitop_5f_NoFullyHadronicDecays_mtop1735" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=43156767.7019,
                NEVT_UL16postVFP=44011904.1896,
                NEVT_UL17=107878602.749,
                NEVT_UL18=150299346.137,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_antitop_5f_NoFullyHadronicDecays_mtop1735_CP5_powheg-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ST_tW_antitop_5f_NoFullyHadronicDecays_mtop1735_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_antitop_5f_NoFullyHadronicDecays_mtop1735_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ST_tW_antitop_5f_NoFullyHadronicDecays_mtop1735_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_antitop_5f_NoFullyHadronicDecays_mtop1735_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ST_tW_antitop_5f_NoFullyHadronicDecays_mtop1735_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_antitop_5f_NoFullyHadronicDecays_mtop1735_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_antitop_5f_NoFullyHadronicDecays_mtop1735_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_t-channel_top_4f_InclusiveDecays" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=136.02, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=5839194102.46,
                NEVT_UL16postVFP=6550100937.74,
                NEVT_UL17=13637101356.5,
                NEVT_UL18=18666369783.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_t-channel_top_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL16APV_v3.xml", XmlSource_UL16preVFP="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_t-channel_top_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL16_v3.xml", XmlSource_UL16postVFP="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v3/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_t-channel_top_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_t-channel_top_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ST_t-channel_antitop_4f_InclusiveDecays" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=80.95, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=1951751224.72,
                NEVT_UL16postVFP=1917634040.7,
                NEVT_UL17=4382086260.65,
                NEVT_UL18=6065207113.78,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_t-channel_antitop_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL16APV_v3.xml", XmlSource_UL16preVFP="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_t-channel_antitop_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL16_v3.xml", XmlSource_UL16postVFP="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v3/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_t-channel_antitop_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_t-channel_antitop_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ST_s-channel_4f_leptonDecays" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=10.32, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : MCSampleValuesHelperPrototype.BRValues(BRat_13TeV=0.326, BRatSource_13TeV="https://pdg.lbl.gov/2021/listings/rpp2021-list-w-boson.pdf (page 5, W->lnu times 3, rounded)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=19340375.1886,
                NEVT_UL16postVFP=19261701.7576,
                NEVT_UL17=48676781.164,
                NEVT_UL18=67080834.7781,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_s-channel_4f_leptonDecays_CP5_amcatnlo-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_s-channel_4f_leptonDecays_CP5_amcatnlo-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_s-channel_4f_leptonDecays_CP5_amcatnlo-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_s-channel_4f_leptonDecays_CP5_amcatnlo-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WW" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=75.91, XSecSource_13TeV="GenXSecAnalyzer (LO) for UL 16",
                XSec_UL16preVFP=75.96,
                XSec_UL16postVFP=75.91,
                XSec_UL17=75.92,
                XSec_UL18=75.91,
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=15739128.5188,
                NEVT_UL16postVFP=15796137.099,
                NEVT_UL17=15490115.1417,
                NEVT_UL18=15463122.6562,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WW_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WW_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WW_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WW_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WZ" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=27.56, XSecSource_13TeV="GenXSecAnalyzer (LO) for UL 16",
                XSec_UL16preVFP=27.55,
                XSec_UL16postVFP=27.56,
                XSec_UL17=27.54,
                XSec_UL18=27.58,
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=7910000.0,
                NEVT_UL16postVFP=7536000.0,
                NEVT_UL17=7793000.0,
                NEVT_UL18=7868000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WZ_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WZ_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WZ_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WZ_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZZ" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=12.13, XSecSource_13TeV="GenXSecAnalyzer (LO) for UL 16",
                XSec_UL16preVFP=12.12,
                XSec_UL16postVFP=12.13,
                XSec_UL17=12.14,
                XSec_UL18=12.13,
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=1282000.0,
                NEVT_UL16postVFP=1151000.0,
                NEVT_UL17=2706000.0,
                NEVT_UL18=3502000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZZ_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZZ_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZZ_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZZ_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-70to100" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=140.1, XSecSource_13TeV="GenXSecAnalyzer"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=6570903.0,
                NEVT_UL16postVFP=5847430.0,
                NEVT_UL17=11968211.0,
                NEVT_UL18=16650708.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-70to100_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-70to100_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-70to100_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-70to100_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-100to200" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=140.2, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.2245, kFacSource_UL16preVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL16postVFP=1.2245, kFacSource_UL16postVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL17=1.1374, kFacSource_UL17="XSDB NNLO/LO=6077.22/5343",
                kFac_UL18=1.1421, kFacSource_UL18="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : MCSampleValuesHelperPrototype.CorrValues(
                CorrSource_UL17="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                CorrSource_UL18="Same as 2017",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=9453373.0,
                NEVT_UL16postVFP=8247137.0,
                NEVT_UL17=18464589.0,
                NEVT_UL18=25632615.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-100to200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-100to200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-100to200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-100to200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-200to400" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=38.399, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.2245, kFacSource_UL16preVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL16postVFP=1.2245, kFacSource_UL16postVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL17=1.1374, kFacSource_UL17="XSDB NNLO/LO=6077.22/5343",
                kFac_UL18=1.1421, kFacSource_UL18="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : MCSampleValuesHelperPrototype.CorrValues(
                Corr_UL17=0.999, CorrSource_UL17="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_UL18=0.999, CorrSource_UL18="Same as 2017",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=5754714.0,
                NEVT_UL16postVFP=5583138.0,
                NEVT_UL17=12228714.0,
                NEVT_UL18=17924098.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-200to400_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-200to400_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-200to400_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-200to400_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-400to600" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=5.21278, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.2245, kFacSource_UL16preVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL16postVFP=1.2245, kFacSource_UL16postVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL17=1.1374, kFacSource_UL17="XSDB NNLO/LO=6077.22/5343",
                kFac_UL18=1.1421, kFacSource_UL18="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : MCSampleValuesHelperPrototype.CorrValues(
                Corr_UL17=0.990, CorrSource_UL17="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_UL18=0.990, CorrSource_UL18="Same as 2017",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=2645509.0,
                NEVT_UL16postVFP=2491416.0,
                NEVT_UL17=5376442.0,
                NEVT_UL18=8693539.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-400to600_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-400to600_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-400to600_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-400to600_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-600to800" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=1.26567, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.2245, kFacSource_UL16preVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL16postVFP=1.2245, kFacSource_UL16postVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL17=1.1374, kFacSource_UL17="XSDB NNLO/LO=6077.22/5343",
                kFac_UL18=1.1421, kFacSource_UL18="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : MCSampleValuesHelperPrototype.CorrValues(
                Corr_UL17=0.975, CorrSource_UL17="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_UL18=0.975, CorrSource_UL18="Same as 2017",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=2634755.0,
                NEVT_UL16postVFP=2252180.0,
                NEVT_UL17=5184253.0,
                NEVT_UL18=6916920.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-600to800_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-600to800_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-600to800_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-600to800_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-800to1200" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=0.5684304, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.2245, kFacSource_UL16preVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL16postVFP=1.2245, kFacSource_UL16postVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL17=1.1374, kFacSource_UL17="XSDB NNLO/LO=6077.22/5343",
                kFac_UL18=1.1421, kFacSource_UL18="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : MCSampleValuesHelperPrototype.CorrValues(
                Corr_UL17=0.907, CorrSource_UL17="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_UL18=0.907, CorrSource_UL18="Same as 2017",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=2387368.0,
                NEVT_UL16postVFP=2324690.0,
                NEVT_UL17=4411064.0,
                NEVT_UL18=6487114.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-800to1200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-800to1200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-800to1200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-800to1200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-1200to2500" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=0.1331514, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.2245, kFacSource_UL16preVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL16postVFP=1.2245, kFacSource_UL16postVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL17=1.1374, kFacSource_UL17="XSDB NNLO/LO=6077.22/5343",
                kFac_UL18=1.1421, kFacSource_UL18="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : MCSampleValuesHelperPrototype.CorrValues(
                Corr_UL17=0.833, CorrSource_UL17="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_UL18=0.833, CorrSource_UL18="Same as 2017",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=2118636.0,
                NEVT_UL16postVFP=1970857.0,
                NEVT_UL17=4683964.0,
                NEVT_UL18=5953693.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-1200to2500_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-1200to2500_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-1200to2500_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-1200to2500_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-2500toInf" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=0.00297803565, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.2245, kFacSource_UL16preVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL16postVFP=1.2245, kFacSource_UL16postVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL17=1.1374, kFacSource_UL17="XSDB NNLO/LO=6077.22/5343",
                kFac_UL18=1.1421, kFacSource_UL18="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : MCSampleValuesHelperPrototype.CorrValues(
                Corr_UL17=1.015, CorrSource_UL17="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_UL18=1.015, CorrSource_UL18="Same as 2017",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=721404.0,
                NEVT_UL16postVFP=696811.0,
                NEVT_UL17=1362586.0,
                NEVT_UL18=1897623.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-2500toInf_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-2500toInf_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-2500toInf_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-2500toInf_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-70to100" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1271, XSecSource_13TeV="GenXSecAnalyzer on UL16postVFP",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=16823170.0,
                NEVT_UL16postVFP=19174410.0,
                NEVT_UL17=43970121.0,
                NEVT_UL18=65413171.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-70To100_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-70To100_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-70To100_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-70To100_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-100to200" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1253, XSecSource_13TeV="GenXSecAnalyzer on UL16preVFP",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=21265181.0,
                NEVT_UL16postVFP=19477663.0,
                NEVT_UL17=46725549.0,
                NEVT_UL18=50895921.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-200to400" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=335.9, XSecSource_13TeV="GenXSecAnalyzer on UL16preVFP",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=17590327.0,
                NEVT_UL16postVFP=14678930.0,
                NEVT_UL17=41674635.0,
                NEVT_UL18=57390500.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-400to600" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=45.21, XSecSource_13TeV="GenXSecAnalyzer on UL16preVFP",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=2467498.0,
                NEVT_UL16postVFP=2091680.0,
                NEVT_UL17=5417430.0,
                NEVT_UL18=7235634.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-600to800" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=10.99, XSecSource_13TeV="GenXSecAnalyzer on UL16preVFP",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=2288109.0,
                NEVT_UL16postVFP=2194792.0,
                NEVT_UL17=5370870.0,
                NEVT_UL18=7529681.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-800to1200" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=4.936, XSecSource_13TeV="GenXSecAnalyzer on UL16preVFP",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=2486912.0,
                NEVT_UL16postVFP=2060965.0,
                NEVT_UL17=5064869.0,
                NEVT_UL18=7141063.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-1200to2500" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1.156, XSecSource_13TeV="GenXSecAnalyzer on UL16preVFP",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=2072226.0,
                NEVT_UL16postVFP=2059841.0,
                NEVT_UL17=4860758.0,
                NEVT_UL18=6434664.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-2500toInf" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.02623, XSecSource_13TeV="GenXSecAnalyzer on UL16preVFP",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=808649.0,
                NEVT_UL16postVFP=709514.0,
                NEVT_UL17=1185699.0,
                NEVT_UL18=2080066.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZJetsToNuNu_HT-100to200" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=266.6, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.23, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.23, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.23, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.23, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=7784090,
                NEVT_UL16postVFP=7083216,
                NEVT_UL17=18983897,
                NEVT_UL18=28876062,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToNuNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToNuNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToNuNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZJetsToNuNu_HT-200to400" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=73.08, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.23, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.23, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.23, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.23, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=7531529,
                NEVT_UL16postVFP=6814106,
                NEVT_UL17=17349597,
                NEVT_UL18=22749608,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToNuNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToNuNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToNuNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZJetsToNuNu_HT-400to600" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=9.932, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.23, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.23, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.23, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.23, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=6632524,
                NEVT_UL16postVFP=6114046,
                NEVT_UL17=13963690,
                NEVT_UL18=19810491,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToNuNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToNuNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToNuNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZJetsToNuNu_HT-600to800" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=2.407, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.23, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.23, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.23, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.23, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=2030858,
                NEVT_UL16postVFP=1881671,
                NEVT_UL17=4418971,
                NEVT_UL18=5968910,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToNuNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToNuNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToNuNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZJetsToNuNu_HT-800to1200" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=1.078, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.23, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.23, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.23, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.23, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=703970,
                NEVT_UL16postVFP=633500,
                NEVT_UL17=1513585,
                NEVT_UL18=2129122,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToNuNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToNuNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToNuNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZJetsToNuNu_HT-1200to2500" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=0.2514, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.23, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.23, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.23, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.23, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=136393,
                NEVT_UL16postVFP=115609,
                NEVT_UL17=267125,
                NEVT_UL18=381695,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToNuNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToNuNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToNuNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZJetsToNuNu_HT-2500toInf" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=0.005569, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_UL16preVFP=1.23, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.23, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.23, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.23, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=111838,
                NEVT_UL16postVFP=110461,
                NEVT_UL17=176201,
                NEVT_UL18=268224,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToNuNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToNuNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToNuNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WJetsToQQ_HT200to400" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=2565.301991, XSecSource_13TeV="GenXSecAnalyzer run on UL17"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=7715093.0,
                NEVT_UL16postVFP=6970485.0,
                NEVT_UL17=15693659.0,
                NEVT_UL18=14148127.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "WJetsToQQ_HT400to600" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=276.629780, XSecSource_13TeV="GenXSecAnalyzer run on UL17"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=5121341.0,
                NEVT_UL16postVFP=4316747.0,
                NEVT_UL17=9741981.0,
                NEVT_UL18=9125992.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "WJetsToQQ_HT600to800" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=59.078057, XSecSource_13TeV="GenXSecAnalyzer run on UL17"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=7526382.0,
                NEVT_UL16postVFP=6752725.0,
                NEVT_UL17=14219925.0,
                NEVT_UL18=13397426.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "WJetsToQQ_HT800toInf" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=28.761363, XSecSource_13TeV="GenXSecAnalyzer run on UL17"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=7465630.0,
                NEVT_UL16postVFP=6604197.0,
                NEVT_UL17=14257025.0,
                NEVT_UL18=13365710.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZJetsToQQ_HT200to400" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1010.200257, XSecSource_13TeV="GenXSecAnalyzer run on UL18"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=8349623.0,
                NEVT_UL16postVFP=7215420.0,
                NEVT_UL17=15064583.0,
                NEVT_UL18=14597666.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZJetsToQQ_HT400to600" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=114.207953, XSecSource_13TeV="GenXSecAnalyzer run on UL17"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=7638105.0,
                NEVT_UL16postVFP=6800886.0,
                NEVT_UL17=14716450.0,
                NEVT_UL18=13693373.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZJetsToQQ_HT600to800" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=25.348623, XSecSource_13TeV="GenXSecAnalyzer run on UL17"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=5997775.0,
                NEVT_UL16postVFP=5405979.0,
                NEVT_UL17=11371140.0,
                NEVT_UL18=11548405.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZJetsToQQ_HT800toInf" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=12.914550, XSecSource_13TeV="GenXSecAnalyzer run on UL17"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=3395616.0,
                NEVT_UL16postVFP=4256541.0,
                NEVT_UL17=9074076.0,
                NEVT_UL18=9428426.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-15To20_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=2.804e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=4702434.35096,
                NEVT_UL16postVFP=4351376.89588,
                NEVT_UL17=8303461.32576,
                NEVT_UL18=8855628.80125,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-15To20_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-15To20_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-15To20_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-15To20_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-20To30_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=2.525e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=29577312.2432,
                NEVT_UL16postVFP=29444607.714,
                NEVT_UL17=63163429.4457,
                NEVT_UL18=56254769.7319,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-20To30_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-20To30_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-20To30_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-20To30_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-30To50_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=1.366e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=26234818.0,
                NEVT_UL16postVFP=34132958.0,
                NEVT_UL17=57541818.0,
                NEVT_UL18=54774188.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-30To50_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-30To50_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-30To50_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-30To50_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-50To80_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=3.777e+05, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=18641525.0,
                NEVT_UL16postVFP=20634072.0,
                NEVT_UL17=37145092.0,
                NEVT_UL18=37496434.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-50To80_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-50To80_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-50To80_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-50To80_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-80To120_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=8.862e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=20304318.4332,
                NEVT_UL16postVFP=21067289.5974,
                NEVT_UL17=42429014.0691,
                NEVT_UL18=42790996.6794,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-80To120_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-80To120_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-80To120_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-80To120_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-120To170_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=2.118e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=17582197.0466,
                NEVT_UL16postVFP=18915898.1684,
                NEVT_UL17=36756675.8228,
                NEVT_UL18=36907183.365,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-120To170_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-120To170_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-120To170_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-120To170_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-170To300_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=7.015e+03, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=34986547.0,
                NEVT_UL16postVFP=32519689.0,
                NEVT_UL17=68143863.0,
                NEVT_UL18=68405126.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-170To300_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-170To300_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-170To300_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-170To300_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-300To470_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=6.201e+02, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=26598488.6412,
                NEVT_UL16postVFP=28533156.0495,
                NEVT_UL17=54139451.5127,
                NEVT_UL18=56123430.7554,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-300To470_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-300To470_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-300To470_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-300To470_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-470To600_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=5.908e+01, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=19033401.1611,
                NEVT_UL16postVFP=18786627.538,
                NEVT_UL17=36772363.2966,
                NEVT_UL18=36226532.3567,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-470To600_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-470To600_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-470To600_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-470To600_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-600To800_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=1.825e+01, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=19147516.5358,
                NEVT_UL16postVFP=17852444.5469,
                NEVT_UL17=36664638.0857,
                NEVT_UL18=36450873.0597,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-600To800_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-600To800_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-600To800_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-600To800_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-800To1000_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=3.276e+00, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=34818002.0,
                NEVT_UL16postVFP=36874214.0,
                NEVT_UL17=72233265.0,
                NEVT_UL18=75504652.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-800To1000_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-800To1000_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-800To1000_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-800To1000_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-1000_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=1.077e+00, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=12037432.0,
                NEVT_UL16postVFP=13437681.0,
                NEVT_UL17=25762679.0,
                NEVT_UL18=26237172.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-1000_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-1000_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-1000_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-1000_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-15to20_EMEnriched" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=1.322e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=3955016.88151,
                NEVT_UL17=7872865.56044,
                NEVT_UL18=7734191.6292,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-15to20_EMEnriched_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-15to20_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-15to20_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-20to30_EMEnriched" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=4.915e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=6944461.1873,
                NEVT_UL17=13911351.1134,
                NEVT_UL18=14097326.3763,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-20to30_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-20to30_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-20to30_EMEnriched_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_Pt-30to50_EMEnriched" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=6.418e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=4195275.0,
                NEVT_UL16postVFP=4256783.0,
                NEVT_UL17=8549222.0,
                NEVT_UL18=8433047.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-30to50_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-30to50_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-30to50_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-30to50_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-50to80_EMEnriched" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=1.987e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=5199617.0,
                NEVT_UL16postVFP=5350943.0,
                NEVT_UL17=10094541.0,
                NEVT_UL18=10338693.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-50to80_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-50to80_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-50to80_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-50to80_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-80to120_EMEnriched" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=3.671e+05, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=4430933.68065,
                NEVT_UL16postVFP=4759037.9018,
                NEVT_UL17=9454898.89424,
                NEVT_UL18=9260620.50861,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-80to120_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-80to120_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-80to120_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-80to120_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-120to170_EMEnriched" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=6.661e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=4667710.26898,
                NEVT_UL16postVFP=4799237.98617,
                NEVT_UL17=9671184.56819,
                NEVT_UL18=9539918.29005,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-120to170_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-120to170_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-120to170_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-120to170_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-170to300_EMEnriched" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=1.654e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=1797043.0,
                NEVT_UL16postVFP=1791497.0,
                NEVT_UL17=3631617.0,
                NEVT_UL18=3668140.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-170to300_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-170to300_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-170to300_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-170to300_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-300toInf_EMEnriched" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=1.100e+03, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=1118836.0,
                NEVT_UL16postVFP=1090760.0,
                NEVT_UL17=2158056.0,
                NEVT_UL18=2215994.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-300toInf_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-300toInf_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-300toInf_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-300toInf_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt_15to20_bcToE" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=1.869e+05, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=8265331.06524,
                NEVT_UL17=-1,
                NEVT_UL18=16182982.3804,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_15to20_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_15to20_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_15to20_bcToE_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt_15to20_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt_20to30_bcToE" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=3.055e+05, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=7913585.84161,
                NEVT_UL16postVFP=7164608.24167,
                NEVT_UL17=13974982.5352,
                NEVT_UL18=13965314.3132,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt_20to30_bcToE_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_20to30_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt_20to30_bcToE_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_20to30_bcToE_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt_30to80_bcToE" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=3.612e+05, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=7829691.54456,
                NEVT_UL16postVFP=7621532.16967,
                NEVT_UL17=14954896.9288,
                NEVT_UL18=15128473.4127,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt_30to80_bcToE_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_30to80_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt_30to80_bcToE_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_30to80_bcToE_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt_80to170_bcToE" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=3.376e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=7690702.0,
                NEVT_UL16postVFP=7808513.0,
                NEVT_UL17=15312170.0,
                NEVT_UL18=14742089.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt_80to170_bcToE_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_80to170_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt_80to170_bcToE_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_80to170_bcToE_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt_170to250_bcToE" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=2.127e+03, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=7343309.67453,
                NEVT_UL16postVFP=7723899.25939,
                NEVT_UL17=14990835.6594,
                NEVT_UL18=15407532.0851,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt_170to250_bcToE_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_170to250_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt_170to250_bcToE_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_170to250_bcToE_CP5_pythia8_Summer20UL18_v3.xml", XmlSource_UL18="/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3/MINIAODSIM",
            ),
        },

        "QCD_Pt_250toInf_bcToE" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=5.634e+02, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=6856820.0,
                NEVT_UL16postVFP=8044441.0,
                NEVT_UL17=15487120.0,
                NEVT_UL18=15486264.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt_250toInf_bcToE_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_250toInf_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt_250toInf_bcToE_CP5_pythia8_Summer20UL17_v3.xml", XmlSource_UL17="/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v3/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_250toInf_bcToE_CP5_pythia8_Summer20UL18_v3.xml", XmlSource_UL18="/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3/MINIAODSIM",
            ),
        },

        "QCD_HT50to100" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=185900000, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=35729712.0,
                NEVT_UL16postVFP=11080132.0,
                NEVT_UL17=26032341.0,
                NEVT_UL18=38225118.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT50to100_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT50to100_CP5_PSWeights_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT50to100_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT50to100_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT100to200" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=23610000, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=65503645.0,
                NEVT_UL16postVFP=72640095.0,
                NEVT_UL17=53299606.0,
                NEVT_UL18=82213301.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT100to200_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT100to200_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT100to200_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT100to200_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT200to300" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1551000, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=17969592.0,
                NEVT_UL16postVFP=42723038.0,
                NEVT_UL17=42316128.0,
                NEVT_UL18=56298746.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT200to300_CP5_PSWeights_madgraph-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT200to300_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT200to300_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT200to300_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT300to500" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=324300, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=13586390.0,
                NEVT_UL16postVFP=45502889.0,
                NEVT_UL17=42914024.0,
                NEVT_UL18=60991701.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT300to500_CP5_PSWeights_madgraph-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT300to500_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT300to500_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT300to500_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT500to700" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=30340, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=55497082.0,
                NEVT_UL16postVFP=15066884.0,
                NEVT_UL17=35745565.0,
                NEVT_UL18=48640047.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT500to700_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT500to700_CP5_PSWeights_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT500to700_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT500to700_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT700to1000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=6440, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=15242034.0,
                NEVT_UL16postVFP=13714842.0,
                NEVT_UL17=33646855.0,
                NEVT_UL18=47925782.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT700to1000_CP5_PSWeights_madgraph-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT700to1000_CP5_PSWeights_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT700to1000_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT700to1000_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_HT1000to1500" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1118, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=13559959.0,
                NEVT_UL16postVFP=12416669.0,
                NEVT_UL17=10136610.0,
                NEVT_UL18=14244456.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT1000to1500_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT1000to1500_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT1000to1500_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT1000to1500_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT1500to2000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=108, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=9661950.0,
                NEVT_UL16postVFP=9244228.0,
                NEVT_UL17=7528926.0,
                NEVT_UL18=10751607.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT1500to2000_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT1500to2000_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT1500to2000_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT1500to2000_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT2000toInf" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=22, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=4827641.0,
                NEVT_UL16postVFP=4843949.0,
                NEVT_UL17=4089387.0,
                NEVT_UL18=5278880.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT2000toInf_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT2000toInf_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT2000toInf_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT2000toInf_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZlepHinc-600": {
                "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=100000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-600_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="ZprimeToZHToZlepHinc_narrow_M-600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-600_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-600_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-800": {
                "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=100000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-800_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-800_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-800_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-1000": {
                "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=44000,
                    NEVT_UL17=100000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-1000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-1000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-1000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-1200": {
                "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=45000,
                    NEVT_UL17=100000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-1200_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-1200_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-1200_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-1400": {
                "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=45000,
                    NEVT_UL17=100000,
                    NEVT_UL18=97000,
                ),
                "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-1400_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-1400_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-1400_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-1600": {
                "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=93000,
                    NEVT_UL18=98000,
                ),
                "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-1600_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-1600_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-1600_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-1800": {
                "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=97000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-1800_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-1800_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-1800_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-2000": {
                "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=100000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-2000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-2000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-2000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-2500": {
                "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=100000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-2500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-2500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-2500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-3000": {
                "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=99000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-3000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-3000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-3000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-3500": {
                "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=97000,
                    NEVT_UL18=97000,
                ),
                "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-3500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-3500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-3500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-3500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-3500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-3500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-4000": {
                "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=45000,
                    NEVT_UL17=97000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-4000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-4000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-4000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-4000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-4000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-4000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-4500": {
                "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=100000,
                    NEVT_UL18=97000,
                ),
                "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-4500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-4500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-4500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-4500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-4500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-4500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-5000": {
                "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=44000,
                    NEVT_UL17=100000,
                    NEVT_UL18=97000,
                ),
                "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-5000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-5000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-5000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-5000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-5000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-5000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-5500": {
                "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=44000,
                    NEVT_UL17=97000,
                    NEVT_UL18=94000,
                ),
                "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-5500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-5500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-5500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-5500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-5500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-5500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-6000": {
                "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=45000,
                    NEVT_UL17=100000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-6000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-6000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-6000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-6000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-6000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-6000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-7000": {
                "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=100000,
                    NEVT_UL18=97000,
                ),
                "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-7000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-7000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-7000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-7000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-7000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-7000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-8000": {
                "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=97000,
                    NEVT_UL18=97000,
                ),
                "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-8000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-8000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-8000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-8000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-8000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-8000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

    "ZprimeToZHToZinvHinc-600": {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
            Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-600_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP=    "ZprimeToZHToZinvHinc_narrow_M-600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-600_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-600_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-800": {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=91000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-800_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-800_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-800_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-1000": {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=98000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-1000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-1000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-1000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-1200": {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-1200_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-1200_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-1200_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-1400": {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=97000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-1400_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-1400_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-1400_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-1600": {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-1600_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-1600_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-1600_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-1800": {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=96000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-1800_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-1800_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-1800_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-2000": {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-2000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-2000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-2000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-2500": {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=97000,
                NEVT_UL17=100000,
                NEVT_UL18=97000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-2500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-2500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-2500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-3000": {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=97000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-3000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-3000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-3000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-3500": {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=44000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-3500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-3500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-3500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-3500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-3500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-3500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-4000": {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-4000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-4000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-4000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-4000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-4000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-4000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-4500": {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=97000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-4500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-4500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-4500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-4500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-4500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-4500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-5000": {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-5000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-5000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-5000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-5000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-5000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-5000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-5500": {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=97000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-5500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-5500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-5500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-5500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-5500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-5500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-6000": {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=97000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-6000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-6000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-6000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-6000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-6000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-6000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-7000": {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=97000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-7000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-7000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-7000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-7000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-7000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-7000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-8000": {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-8000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-8000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-8000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-8000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-8000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-8000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ALP_ttbar_signal": {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=7.048, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=5308000.0,
                NEVT_UL16postVFP=4528000.0,
                NEVT_UL17=9802000.0,
                NEVT_UL18=9493000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ALP_ttbar_signal_CP5_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ALP_ttbar_signal_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ALP_ttbar_signal_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ALP_ttbar_signal_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ALP_ttbar_signal_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ALP_ttbar_signal_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ALP_ttbar_signal_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ALP_ttbar_signal_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ALP_ttbar_interference": {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues( XSec_13TeV=-28.248020, XSecSource_13TeV="GenXSecAnalyzer run on UL18"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=5398990.0,
                NEVT_UL16postVFP=4540996.0,
                NEVT_UL17=9831978.0,
                NEVT_UL18=9617976.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ALP_ttbar_interference_CP5_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ALP_ttbar_interference_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ALP_ttbar_interference_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ALP_ttbar_interference_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ALP_ttbar_interference_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ALP_ttbar_interference_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ALP_ttbar_interference_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ALP_ttbar_interference_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M400_W4" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=545137.0,
                NEVT_UL16postVFP=570127.0,
                NEVT_UL17=195849.0,
                NEVT_UL18=200177.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M400_W4_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M400_W4_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M400_W4_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M400_W4_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M400_W4_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M400_W4_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M400_W4_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M400_W4_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M500_W5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=537434.0,
                NEVT_UL16postVFP=526301.0,
                NEVT_UL17=188083.0,
                NEVT_UL18=191959.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M500_W5_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M500_W5_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M500_W5_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M500_W5_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M500_W5_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M500_W5_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M500_W5_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M500_W5_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M600_W6" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=509112.0,
                NEVT_UL16postVFP=510991.0,
                NEVT_UL17=198225.0,
                NEVT_UL18=190965.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M600_W6_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M600_W6_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M600_W6_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M600_W6_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M600_W6_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M600_W6_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M600_W6_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M600_W6_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M700_W7" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=444498.0,
                NEVT_UL16postVFP=444141.0,
                NEVT_UL17=197226.0,
                NEVT_UL18=199814.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M700_W7_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M700_W7_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M700_W7_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M700_W7_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M700_W7_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M700_W7_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M700_W7_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M700_W7_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M800_W8" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=425095.0,
                NEVT_UL16postVFP=474239.0,
                NEVT_UL17=193169.0,
                NEVT_UL18=191956.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M800_W8_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M800_W8_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M800_W8_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M800_W8_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M800_W8_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M800_W8_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M800_W8_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M800_W8_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M900_W9" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=463051.0,
                NEVT_UL16postVFP=461916.0,
                NEVT_UL17=199844.0,
                NEVT_UL18=197077.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M900_W9_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M900_W9_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M900_W9_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M900_W9_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M900_W9_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M900_W9_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M900_W9_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M900_W9_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M1000_W10" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=428524.0,
                NEVT_UL16postVFP=449628.0,
                NEVT_UL17=167704.0,
                NEVT_UL18=201398.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M1000_W10_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M1000_W10_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M1000_W10_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M1000_W10_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M1000_W10_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M1000_W10_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M1000_W10_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M1000_W10_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M1200_W12" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=464061.0,
                NEVT_UL16postVFP=497321.0,
                NEVT_UL17=195613.0,
                NEVT_UL18=198217.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M1200_W12_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M1200_W12_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M1200_W12_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M1200_W12_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTT_M1200_W12_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZprimeToTT_M1200_W12_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTT_M1200_W12_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZprimeToTT_M1200_W12_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M1400_W14" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=481700.0,
                NEVT_UL16postVFP=548913.0,
                NEVT_UL17=208708.0,
                NEVT_UL18=217763.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M1400_W14_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M1400_W14_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M1400_W14_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M1400_W14_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTT_M1400_W14_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZprimeToTT_M1400_W14_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTT_M1400_W14_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZprimeToTT_M1400_W14_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M1600_W16" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=534876.0,
                NEVT_UL16postVFP=548012.0,
                NEVT_UL17=219802.0,
                NEVT_UL18=207930.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M1600_W16_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M1600_W16_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M1600_W16_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M1600_W16_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTT_M1600_W16_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZprimeToTT_M1600_W16_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTT_M1600_W16_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZprimeToTT_M1600_W16_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M1800_W18" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=495243.0,
                NEVT_UL16postVFP=533048.0,
                NEVT_UL17=208252.0,
                NEVT_UL18=203473.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M1800_W18_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M1800_W18_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M1800_W18_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M1800_W18_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTT_M1800_W18_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZprimeToTT_M1800_W18_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTT_M1800_W18_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZprimeToTT_M1800_W18_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M2000_W20" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=457884.0,
                NEVT_UL16postVFP=527279.0,
                NEVT_UL17=211425.0,
                NEVT_UL18=196868.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M2000_W20_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M2000_W20_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M2000_W20_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M2000_W20_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTT_M2000_W20_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZprimeToTT_M2000_W20_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTT_M2000_W20_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZprimeToTT_M2000_W20_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M2500_W25" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=456081.0,
                NEVT_UL16postVFP=508484.0,
                NEVT_UL17=203518.0,
                NEVT_UL18=201970.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M2500_W25_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M2500_W25_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M2500_W25_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M2500_W25_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTT_M2500_W25_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZprimeToTT_M2500_W25_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTT_M2500_W25_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZprimeToTT_M2500_W25_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M3000_W30" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=482947.0,
                NEVT_UL16postVFP=490008.0,
                NEVT_UL17=192535.0,
                NEVT_UL18=171190.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M3000_W30_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M3000_W30_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M3000_W30_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M3000_W30_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTT_M3000_W30_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZprimeToTT_M3000_W30_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTT_M3000_W30_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZprimeToTT_M3000_W30_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M3500_W35" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=466444.0,
                NEVT_UL16postVFP=426819.0,
                NEVT_UL17=189565.0,
                NEVT_UL18=187591.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M3500_W35_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M3500_W35_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M3500_W35_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M3500_W35_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTT_M3500_W35_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZprimeToTT_M3500_W35_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTT_M3500_W35_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZprimeToTT_M3500_W35_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M4000_W40" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=422942.0,
                NEVT_UL16postVFP=429056.0,
                NEVT_UL17=184083.0,
                NEVT_UL18=184021.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M4000_W40_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M4000_W40_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M4000_W40_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M4000_W40_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTT_M4000_W40_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZprimeToTT_M4000_W40_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTT_M4000_W40_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZprimeToTT_M4000_W40_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),

        },
        "ZprimeToTT_M4500_W45" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=413509.0,
                NEVT_UL16postVFP=417527.0,
                NEVT_UL17=174039.0,
                NEVT_UL18=179341.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M4500_W45_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M4500_W45_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M4500_W45_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M4500_W45_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTT_M4500_W45_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZprimeToTT_M4500_W45_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTT_M4500_W45_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZprimeToTT_M4500_W45_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M5000_W50" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=109600.0,
                NEVT_UL16postVFP=90300.0,
                NEVT_UL17=191207.0,
                NEVT_UL18=193733.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTTJets_M5000_W50_CP2_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZprimeToTTJets_M5000_W50_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTTJets_M5000_W50_CP2_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToTTJets_M5000_W50_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M5000_W50_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M5000_W50_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M5000_W50_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M5000_W50_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M6000_W60" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=107673.0,
                NEVT_UL16postVFP=91498.0,
                NEVT_UL17=202610.0,
                NEVT_UL18=192170.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTTJets_M6000_W60_CP2_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZprimeToTTJets_M6000_W60_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTTJets_M6000_W60_CP2_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToTTJets_M6000_W60_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M6000_W60_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M6000_W60_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M6000_W60_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M6000_W60_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M7000_W70" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=107295.0,
                NEVT_UL16postVFP=89723.0,
                NEVT_UL17=192854.0,
                NEVT_UL18=197279.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTTJets_M7000_W70_CP2_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZprimeToTTJets_M7000_W70_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTTJets_M7000_W70_CP2_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToTTJets_M7000_W70_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M7000_W70_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M7000_W70_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M7000_W70_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M7000_W70_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M8000_W80" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=105321.0,
                NEVT_UL16postVFP=89233.0,
                NEVT_UL17=191551.0,
                NEVT_UL18=170678.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTTJets_M8000_W80_CP2_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZprimeToTTJets_M8000_W80_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTTJets_M8000_W80_CP2_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToTTJets_M8000_W80_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M8000_W80_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M8000_W80_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M8000_W80_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M8000_W80_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M9000_W90" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=106005.0,
                NEVT_UL16postVFP=91144.0,
                NEVT_UL17=182122.0,
                NEVT_UL18=201986.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTTJets_M9000_W90_CP2_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZprimeToTTJets_M9000_W90_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTTJets_M9000_W90_CP2_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToTTJets_M9000_W90_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M9000_W90_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M9000_W90_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M9000_W90_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M9000_W90_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M400_W40" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=261000.0,
                NEVT_UL16postVFP=206000.0,
                NEVT_UL17=473000.0,
                NEVT_UL18=482000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M400_W40_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M400_W40_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M400_W40_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M400_W40_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M400_W40_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M400_W40_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M400_W40_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M400_W40_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M500_W50" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=246000.0,
                NEVT_UL16postVFP=205000.0,
                NEVT_UL17=491000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M500_W50_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M500_W50_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M500_W50_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M500_W50_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M500_W50_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M500_W50_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M500_W50_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M500_W50_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M600_W60" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=244000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=494000.0,
                NEVT_UL18=467000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M600_W60_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M600_W60_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M600_W60_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M600_W60_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M600_W60_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M600_W60_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M600_W60_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M600_W60_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M700_W70" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=464000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M700_W70_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M700_W70_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M700_W70_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M700_W70_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M700_W70_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M700_W70_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M700_W70_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M700_W70_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M800_W80" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=266000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=434000.0,
                NEVT_UL18=482000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M800_W80_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M800_W80_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M800_W80_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M800_W80_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M800_W80_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M800_W80_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M800_W80_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M800_W80_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M900_W90" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=246000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=428000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M900_W90_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M900_W90_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M900_W90_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M900_W90_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M900_W90_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M900_W90_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M900_W90_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M900_W90_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M1000_W100" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=206000.0,
                NEVT_UL17=452000.0,
                NEVT_UL18=488000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M1000_W100_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M1000_W100_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M1000_W100_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M1000_W100_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M1000_W100_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M1000_W100_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M1000_W100_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M1000_W100_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M1200_W120" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=464000.0,
                NEVT_UL18=455000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M1200_W120_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M1200_W120_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M1200_W120_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M1200_W120_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M1200_W120_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M1200_W120_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M1200_W120_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M1200_W120_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M1400_W140" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=262000.0,
                NEVT_UL16postVFP=197000.0,
                NEVT_UL17=488000.0,
                NEVT_UL18=467000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M1400_W140_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M1400_W140_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M1400_W140_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M1400_W140_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M1400_W140_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M1400_W140_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M1400_W140_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M1400_W140_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M1600_W160" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=246000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=470000.0,
                NEVT_UL18=456000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M1600_W160_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M1600_W160_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M1600_W160_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M1600_W160_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M1600_W160_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M1600_W160_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M1600_W160_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M1600_W160_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M1800_W180" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=264000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=464000.0,
                NEVT_UL18=458000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M1800_W180_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M1800_W180_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M1800_W180_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M1800_W180_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M1800_W180_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M1800_W180_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M1800_W180_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M1800_W180_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M2000_W200" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=473000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M2000_W200_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M2000_W200_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M2000_W200_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M2000_W200_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M2000_W200_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M2000_W200_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M2000_W200_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M2000_W200_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M2500_W250" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=267000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=462000.0,
                NEVT_UL18=476000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M2500_W250_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M2500_W250_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M2500_W250_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M2500_W250_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M2500_W250_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M2500_W250_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M2500_W250_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M2500_W250_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M3000_W300" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=467000.0,
                NEVT_UL18=470000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M3000_W300_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M3000_W300_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M3000_W300_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M3000_W300_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M3000_W300_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M3000_W300_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M3000_W300_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M3000_W300_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M3500_W350" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=246000.0,
                NEVT_UL16postVFP=182000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=452000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M3500_W350_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M3500_W350_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M3500_W350_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M3500_W350_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M3500_W350_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M3500_W350_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M3500_W350_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M3500_W350_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M4000_W400" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=267000.0,
                NEVT_UL16postVFP=202000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=476000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M4000_W400_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M4000_W400_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M4000_W400_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M4000_W400_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M4000_W400_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M4000_W400_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M4000_W400_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M4000_W400_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M4500_W450" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=497000.0,
                NEVT_UL18=497000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M4500_W450_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M4500_W450_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM ",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M4500_W450_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M4500_W450_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M4500_W450_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M4500_W450_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M4500_W450_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M4500_W450_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M5000_W500" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=72000.0,
                NEVT_UL17=188000.0,
                NEVT_UL18=194000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M5000_W500_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M5000_W500_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M5000_W500_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M5000_W500_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M5000_W500_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M5000_W500_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M5000_W500_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M5000_W500_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M6000_W600" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=88000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=192000.0,
                NEVT_UL18=200000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M6000_W600_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M6000_W600_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M6000_W600_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M6000_W600_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M6000_W600_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M6000_W600_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M6000_W600_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M6000_W600_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M7000_W700" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=98000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=200000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M7000_W700_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M7000_W700_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M7000_W700_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M7000_W700_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M7000_W700_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M7000_W700_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M7000_W700_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M7000_W700_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M8000_W800" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=84000.0,
                NEVT_UL16postVFP=90000.0,
                NEVT_UL17=166000.0,
                NEVT_UL18=200000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M8000_W800_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M8000_W800_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M8000_W800_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M8000_W800_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M8000_W800_CP2_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZPrimeToTT_M8000_W800_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M8000_W800_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M8000_W800_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M9000_W900" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=72000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=194000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M9000_W900_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M9000_W900_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M9000_W900_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M9000_W900_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M9000_W900_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M9000_W900_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M9000_W900_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M9000_W900_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M400_W120" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=476000.0,
                NEVT_UL18=482000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M400_W120_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M400_W120_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M400_W120_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M400_W120_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M400_W120_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M400_W120_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M400_W120_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M400_W120_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M500_W150" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=182000.0,
                NEVT_UL17=446000.0,
                NEVT_UL18=485000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M500_W150_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M500_W150_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM ",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M500_W150_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M500_W150_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M500_W150_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M500_W150_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M500_W150_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M500_W150_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M600_W180" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=228000.0,
                NEVT_UL17=452000.0,
                NEVT_UL18=497000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M600_W180_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M600_W180_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M600_W180_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M600_W180_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M600_W180_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M600_W180_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M600_W180_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M600_W180_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M700_W210" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=494000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M700_W210_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M700_W210_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M700_W210_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M700_W210_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M700_W210_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M700_W210_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M700_W210_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M700_W210_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M800_W240" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=246000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=452000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M800_W240_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M800_W240_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M800_W240_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M800_W240_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M800_W240_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M800_W240_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M800_W240_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M800_W240_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M900_W270" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=267000.0,
                NEVT_UL16postVFP=225000.0,
                NEVT_UL17=437000.0,
                NEVT_UL18=407000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M900_W270_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M900_W270_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M900_W270_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M900_W270_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M900_W270_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M900_W270_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M900_W270_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M900_W270_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M1000_W300" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=244000.0,
                NEVT_UL16postVFP=229000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=363000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M1000_W300_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M1000_W300_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M1000_W300_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M1000_W300_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M1000_W300_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M1000_W300_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M1000_W300_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M1000_W300_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M1200_W360" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=246000.0,
                NEVT_UL16postVFP=228000.0,
                NEVT_UL17=452000.0,
                NEVT_UL18=465000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M1200_W360_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M1200_W360_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M1200_W360_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M1200_W360_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M1200_W360_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M1200_W360_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M1200_W360_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M1200_W360_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M1400_W420" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=481000.0,
                NEVT_UL18=452000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M1400_W420_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M1400_W420_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M1400_W420_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M1400_W420_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M1400_W420_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M1400_W420_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M1400_W420_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M1400_W420_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M1600_W480" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=228000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=497000.0,
                NEVT_UL18=476000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M1600_W480_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M1600_W480_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M1600_W480_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M1600_W480_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M1600_W480_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M1600_W480_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M1600_W480_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M1600_W480_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M1800_W540" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=256000.0,
                NEVT_UL16postVFP=228000.0,
                NEVT_UL17=486000.0,
                NEVT_UL18=476000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M1800_W540_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M1800_W540_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M1800_W540_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M1800_W540_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M1800_W540_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M1800_W540_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M1800_W540_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M1800_W540_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M2000_W600" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=249000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=476000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M2000_W600_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M2000_W600_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M2000_W600_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M2000_W600_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M2000_W600_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M2000_W600_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M2000_W600_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M2000_W600_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M2500_W750" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=247000.0,
                NEVT_UL16postVFP=206000.0,
                NEVT_UL17=455000.0,
                NEVT_UL18=465000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M2500_W750_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M2500_W750_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M2500_W750_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M2500_W750_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M2500_W750_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M2500_W750_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M2500_W750_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M2500_W750_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M3000_W900" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=464000.0,
                NEVT_UL18=408000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M3000_W900_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M3000_W900_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M3000_W900_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M3000_W900_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M3000_W900_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M3000_W900_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M3000_W900_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M3000_W900_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M3500_W1050" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=221000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=476000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M3500_W1050_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M3500_W1050_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M3500_W1050_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M3500_W1050_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M3500_W1050_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M3500_W1050_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M3500_W1050_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M3500_W1050_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M4000_W1200" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=246000.0,
                NEVT_UL16postVFP=228000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M4000_W1200_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M4000_W1200_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M4000_W1200_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M4000_W1200_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M4000_W1200_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M4000_W1200_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M4000_W1200_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M4000_W1200_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M4500_W1350" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=268000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=473000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M4500_W1350_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M4500_W1350_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M4500_W1350_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M4500_W1350_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM ",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M4500_W1350_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M4500_W1350_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M4500_W1350_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M4500_W1350_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M5000_W1500" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=88000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=200000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M5000_W1500_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M5000_W1500_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M5000_W1500_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M5000_W1500_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M5000_W1500_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M5000_W1500_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M5000_W1500_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M5000_W1500_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M6000_W1800" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=90000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=200000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M6000_W1800_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M6000_W1800_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M6000_W1800_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M6000_W1800_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M6000_W1800_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M6000_W1800_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M6000_W1800_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M6000_W1800_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M7000_W2100" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=86000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=200000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M7000_W2100_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M7000_W2100_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M7000_W2100_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M7000_W2100_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M7000_W2100_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M7000_W2100_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M7000_W2100_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M7000_W2100_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M8000_W2400" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=197000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M8000_W2400_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M8000_W2400_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M8000_W2400_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M8000_W2400_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M8000_W2400_CP2_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZPrimeToTT_M8000_W2400_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M8000_W2400_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M8000_W2400_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M9000_W2700" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=176000.0,
                NEVT_UL18=194000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M9000_W2700_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M9000_W2700_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M9000_W2700_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M9000_W2700_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M9000_W2700_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M9000_W2700_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M9000_W2700_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M9000_W2700_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-500" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=235000,
                NEVT_UL16postVFP=200000,
                NEVT_UL17=500000,
                NEVT_UL18=500000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-500_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-500_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-500_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-500_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-500_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-500_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-1000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=244000,
                NEVT_UL16postVFP=250000,
                NEVT_UL17=485000,
                NEVT_UL18=479000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-1000_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-1000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-1000_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-1000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-1000_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-1000_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-1000_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-1000_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-1500" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=240000,
                NEVT_UL16postVFP=228000,
                NEVT_UL17=500000,
                NEVT_UL18=500000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-1500_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-1500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-1500_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-1500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-1500_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-1500_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-1500_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-1500_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-2000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=250000,
                NEVT_UL16postVFP=208000,
                NEVT_UL17=494000,
                NEVT_UL18=494000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-2000_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-2000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-2000_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-2000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-2000_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-2000_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-2000_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-2000_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-2500" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=213000,
                NEVT_UL16postVFP=196000,
                NEVT_UL17=497000,
                NEVT_UL18=488000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-2500_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-2500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-2500_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-2500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-2500_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-2500_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-2500_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-2500_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-3000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=241000,
                NEVT_UL16postVFP=248000,
                NEVT_UL17=500000,
                NEVT_UL18=500000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-3000_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-3000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-3000_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-3000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-3000_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-3000_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-3000_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-3000_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-3500" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=226000,
                NEVT_UL16postVFP=250000,
                NEVT_UL17=494000,
                NEVT_UL18=500000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-3500_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-3500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-3500_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-3500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-3500_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-3500_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-3500_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-3500_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-4000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=250000,
                NEVT_UL16postVFP=239000,
                NEVT_UL17=473000,
                NEVT_UL18=484000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-4000_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-4000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-4000_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-4000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-4000_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-4000_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-4000_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-4000_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-4500" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=250000,
                NEVT_UL16postVFP=249000,
                NEVT_UL17=440000,
                NEVT_UL18=479000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-4500_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-4500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-4500_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-4500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-4500_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-4500_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-4500_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-4500_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-5000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=250000,
                NEVT_UL16postVFP=234000,
                NEVT_UL17=500000,
                NEVT_UL18=476000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-5000_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-5000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-5000_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-5000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-5000_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-5000_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-5000_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-5000_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-5500" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=214000,
                NEVT_UL16postVFP=248000,
                NEVT_UL17=494000,
                NEVT_UL18=479000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-5500_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-5500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-5500_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-5500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-5500_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-5500_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-5500_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-5500_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-6000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=250000,
                NEVT_UL16postVFP=242000,
                NEVT_UL17=476000,
                NEVT_UL18=431000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-6000_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-6000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-6000_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-6000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-6000_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-6000_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-6000_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-6000_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m365_w91p25_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.384058, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.37211, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=64680.92003,
                NEVT_UL16postVFP=82251.48621,
                NEVT_UL17=157751.99081,
                NEVT_UL18=163269.568709,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m365_w91p25_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m365_w91p25_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m365_w91p25_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m365_w91p25_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m365_w91p25_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m365_w91p25_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m365_w91p25_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m365_w91p25_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM ",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m400_w100p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.392964, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.25867, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=73647.882137,
                NEVT_UL16postVFP=88492.02305,
                NEVT_UL17=168613.18007,
                NEVT_UL18=151475.84016,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m400_w100p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m400_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m400_w100p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m400_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m400_w100p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m400_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m400_w100p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m400_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m500_w125p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.222718, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.13856, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=50395.421986,
                NEVT_UL16postVFP=50202.848086,
                NEVT_UL17=91090.577906,
                NEVT_UL18=91718.53508,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m500_w125p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m500_w125p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m500_w125p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m500_w125p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m500_w125p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m500_w125p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m500_w125p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m500_w125p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m600_w150p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.108418, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.0793, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=21997.71063,
                NEVT_UL16postVFP=23560.2129205,
                NEVT_UL17=46446.79508,
                NEVT_UL18=44068.209683,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m600_w150p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m600_w150p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m600_w150p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m600_w150p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m600_w150p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m600_w150p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m600_w150p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m600_w150p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m800_w200p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.02871, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.01433, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=6505.440998,
                NEVT_UL16postVFP=6501.2446068,
                NEVT_UL17=12385.4098694,
                NEVT_UL18=12387.165582,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m800_w200p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m800_w200p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m800_w200p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m800_w200p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m800_w200p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m800_w200p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m800_w200p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m800_w200p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m1000_w250p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.00935898, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.97913, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=1916.0551067,
                NEVT_UL16postVFP=2069.06411289,
                NEVT_UL17=3817.0451744,
                NEVT_UL18=4039.0823757,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m1000_w250p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m1000_w250p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m1000_w250p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m1000_w250p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m1000_w250p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m1000_w250p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m1000_w250p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m1000_w250p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m365_w91p25_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-3.51387, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.88314, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-717780.8378,
                NEVT_UL16postVFP=-795879.67662,
                NEVT_UL17=-1357975.6425,
                NEVT_UL18=-1358395.68712,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m365_w91p25_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m365_w91p25_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m365_w91p25_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m365_w91p25_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m365_w91p25_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m365_w91p25_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m365_w91p25_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m365_w91p25_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m400_w100p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-2.80865, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.83756, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-639506.25796,
                NEVT_UL16postVFP=-643622.5466,
                NEVT_UL17=-1002533.8646,
                NEVT_UL18=-1154813.36379,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m400_w100p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m400_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m400_w100p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m400_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m400_w100p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m400_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m400_w100p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m400_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m500_w125p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-1.06139, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.78803, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-195455.45433,
                NEVT_UL16postVFP=-246766.59487,
                NEVT_UL17=-417110.50365,
                NEVT_UL18=-394123.7947,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m500_w125p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m500_w125p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m500_w125p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m500_w125p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m500_w125p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m500_w125p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m500_w125p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m500_w125p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m600_w150p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-0.354892, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.76308, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-67339.095251,
                NEVT_UL16postVFP=-77250.552213,
                NEVT_UL17=-141217.836301,
                NEVT_UL18=-141737.87394,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m600_w150p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m600_w150p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m600_w150p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m600_w150p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m600_w150p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m600_w150p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m600_w150p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m600_w150p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m800_w200p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.0131675, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.73532, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=2077.4934433,
                NEVT_UL16postVFP=1220.2306676,
                NEVT_UL17=2981.38010371,
                NEVT_UL18=3542.98394915,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m800_w200p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m800_w200p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m800_w200p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m800_w200p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m800_w200p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m800_w200p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m800_w200p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m800_w200p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m1000_w250p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.0630704, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.72009, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=11378.874635,
                NEVT_UL16postVFP=13721.556921,
                NEVT_UL17=25293.435066,
                NEVT_UL18=23694.371845,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m1000_w250p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m1000_w250p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m1000_w250p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m1000_w250p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m1000_w250p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m1000_w250p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m1000_w250p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m1000_w250p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m365_w36p5_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1.18764, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.37207, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=256294.89633,
                NEVT_UL16postVFP=145074.15602,
                NEVT_UL17=523391.4965,
                NEVT_UL18=529368.49437,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m365_w36p5_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m365_w36p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m365_w36p5_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m365_w36p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m365_w36p5_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m365_w36p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m365_w36p5_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m365_w36p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m400_w40p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1.28105, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.2587, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=288659.16832,
                NEVT_UL16postVFP=286415.1199,
                NEVT_UL17=574027.6727,
                NEVT_UL18=546129.04975,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m400_w40p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m400_w40p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m400_w40p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m400_w40p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m400_w40p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m400_w40p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m400_w40p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m400_w40p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m500_w50p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.660745, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.13856, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=149616.08465,
                NEVT_UL16postVFP=149629.914053,
                NEVT_UL17=284804.3597,
                NEVT_UL18=296686.89491,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m500_w50p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m500_w50p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m500_w50p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m500_w50p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m500_w50p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m500_w50p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m500_w50p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m500_w50p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m600_w60p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.29944, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.07916, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=60298.344118,
                NEVT_UL16postVFP=67582.717264,
                NEVT_UL17=135699.902294,
                NEVT_UL18=134971.091663,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m600_w60p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m600_w60p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m600_w60p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m600_w60p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m600_w60p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m600_w60p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m600_w60p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m600_w60p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m800_w80p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.0709866, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.01441, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=16087.587782,
                NEVT_UL16postVFP=16093.945433,
                NEVT_UL17=32174.2228,
                NEVT_UL18=31987.80998,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m800_w80p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m800_w80p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m800_w80p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m800_w80p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m800_w80p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m800_w80p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m800_w80p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m800_w80p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m1000_w100p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.0209362, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.97917, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=4745.017413,
                NEVT_UL16postVFP=4747.91728,
                NEVT_UL17=9039.4604787,
                NEVT_UL18=9206.9614697,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m1000_w100p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m1000_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m1000_w100p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m1000_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m1000_w100p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m1000_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m1000_w100p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m1000_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m365_w36p5_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-4.92926, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.88312, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1112972.69016,
                NEVT_UL16postVFP=-1117513.98756,
                NEVT_UL17=-2090113.8991,
                NEVT_UL18=-2171094.16728,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m365_w36p5_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m365_w36p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m365_w36p5_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m365_w36p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m365_w36p5_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m365_w36p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m365_w36p5_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m365_w36p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m400_w40p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-3.44265, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.83757, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-786867.006,
                NEVT_UL16postVFP=-789101.34692,
                NEVT_UL17=-1428087.7179,
                NEVT_UL18=-1579689.1022,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m400_w40p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m400_w40p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m400_w40p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m400_w40p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m400_w40p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m400_w40p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m400_w40p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m400_w40p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m500_w50p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-0.937263, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.78803, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-219110.9435,
                NEVT_UL16postVFP=-227201.4818,
                NEVT_UL17=-421949.39712,
                NEVT_UL18=-394355.3945,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m500_w50p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m500_w50p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m500_w50p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m500_w50p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m500_w50p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m500_w50p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m500_w50p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m500_w50p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m600_w60p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-0.166936, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.76302, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-37340.34489,
                NEVT_UL16postVFP=-44194.05708,
                NEVT_UL17=-79016.122021,
                NEVT_UL18=-81900.821139,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m600_w60p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m600_w60p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m600_w60p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m600_w60p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m600_w60p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m600_w60p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m600_w60p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m600_w60p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m800_w80p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.135484, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.73535, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=29430.640305,
                NEVT_UL16postVFP=28099.969551,
                NEVT_UL17=58927.923394,
                NEVT_UL18=60225.44581,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m800_w80p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m800_w80p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m800_w80p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m800_w80p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m800_w80p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m800_w80p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m800_w80p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m800_w80p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m1000_w100p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.136502, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.72011, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=30483.761009,
                NEVT_UL16postVFP=30111.835363,
                NEVT_UL17=60562.236841,
                NEVT_UL18=60547.235299,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m1000_w100p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m1000_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m1000_w100p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m1000_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m1000_w100p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m1000_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m1000_w100p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m1000_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m365_w9p125_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=5.86888, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.37207, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=1188521.2589,
                NEVT_UL16postVFP=1303405.7415,
                NEVT_UL17=2357012.387,
                NEVT_UL18=2607045.7854,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m365_w9p125_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m365_w9p125_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m365_w9p125_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m365_w9p125_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m365_w9p125_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m365_w9p125_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m365_w9p125_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m365_w9p125_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m400_w10p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=6.03581, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.2587, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=1274403.1201,
                NEVT_UL16postVFP=1345760.2621,
                NEVT_UL17=2646385.5243,
                NEVT_UL18=2380827.918,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m400_w10p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m400_w10p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m400_w10p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m400_w10p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m400_w10p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m400_w10p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m400_w10p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m400_w10p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m500_w12p5_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=2.8598, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.13858, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=647810.9576,
                NEVT_UL16postVFP=648333.9809,
                NEVT_UL17=1256146.2269,
                NEVT_UL18=1295687.9387,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m500_w12p5_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m500_w12p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m500_w12p5_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m500_w12p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m500_w12p5_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m500_w12p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m500_w12p5_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m500_w12p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m600_w15p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1.23894, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.07926, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=278598.24587,
                NEVT_UL16postVFP=280878.1883,
                NEVT_UL17=450471.02708,
                NEVT_UL18=534780.0445,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m600_w15p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m600_w15p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m600_w15p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m600_w15p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m600_w15p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m600_w15p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m600_w15p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m600_w15p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m800_w20p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.273973, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.0144, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=62120.010172,
                NEVT_UL16postVFP=29574.237047,
                NEVT_UL17=119062.910039,
                NEVT_UL18=124293.07307,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m800_w20p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m800_w20p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m800_w20p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m800_w20p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m800_w20p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m800_w20p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m800_w20p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m800_w20p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m1000_w25p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.0754245, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.97911, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=16831.765625,
                NEVT_UL16postVFP=16626.1296345,
                NEVT_UL17=34005.567704,
                NEVT_UL18=31349.5508702,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m1000_w25p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m1000_w25p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m1000_w25p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m1000_w25p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m1000_w25p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m1000_w25p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m1000_w25p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m1000_w25p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m365_w9p125_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-6.08885, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.88312, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1382651.7808,
                NEVT_UL16postVFP=-1390762.68325,
                NEVT_UL17=-1779358.20887,
                NEVT_UL18=-2770824.941,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m365_w9p125_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m365_w9p125_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m365_w9p125_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m365_w9p125_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m365_w9p125_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m365_w9p125_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m365_w9p125_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m365_w9p125_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m400_w10p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-3.71856, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.83757, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-772318.94793,
                NEVT_UL16postVFP=-839948.9534,
                NEVT_UL17=-1483966.64224,
                NEVT_UL18=-1576404.8251,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m400_w10p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m400_w10p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m400_w10p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m400_w10p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m400_w10p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m400_w10p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m400_w10p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m400_w10p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m500_w12p5_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-0.787467, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.78804, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-183156.43415,
                NEVT_UL16postVFP=-195530.84382,
                NEVT_UL17=-374395.86068,
                NEVT_UL18=-358621.8006,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m500_w12p5_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m500_w12p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m500_w12p5_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m500_w12p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m500_w12p5_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m500_w12p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m500_w12p5_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m500_w12p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m600_w15p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-0.0280567, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.76307, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-5320.2340722,
                NEVT_UL16postVFP=-10244.00829,
                NEVT_UL17=-13291.4155487,
                NEVT_UL18=-22171.938373,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m600_w15p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m600_w15p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m600_w15p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m600_w15p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m600_w15p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m600_w15p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m600_w15p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m600_w15p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m800_w20p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.208417, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.73535, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=47685.614,
                NEVT_UL16postVFP=46310.2176,
                NEVT_UL17=78433.049824,
                NEVT_UL18=83393.19688,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m800_w20p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m800_w20p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m800_w20p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m800_w20p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m800_w20p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m800_w20p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m800_w20p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m800_w20p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m1000_w25p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.17625, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.72008, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=39879.742145,
                NEVT_UL16postVFP=39097.948724,
                NEVT_UL17=74683.795284,
                NEVT_UL18=77868.066327,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m1000_w25p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m1000_w25p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m1000_w25p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m1000_w25p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m1000_w25p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m1000_w25p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m1000_w25p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m1000_w25p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m365_w91p25_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.0399425, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.36163, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=8435.9975912,
                NEVT_UL16postVFP=9012.0945942,
                NEVT_UL17=17015.7646039,
                NEVT_UL18=17628.702098,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m365_w91p25_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m365_w91p25_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m365_w91p25_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m365_w91p25_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m365_w91p25_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m365_w91p25_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m365_w91p25_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m365_w91p25_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m400_w100p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.0530526, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.28739, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=11974.2015662,
                NEVT_UL16postVFP=4893.3040849,
                NEVT_UL17=23944.04088,
                NEVT_UL18=21669.7564164,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m400_w100p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m400_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m400_w100p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m400_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m400_w100p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m400_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m400_w100p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m400_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m500_w125p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.057073, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.17333, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=12707.539589,
                NEVT_UL16postVFP=12912.4057126,
                NEVT_UL17=25483.956336,
                NEVT_UL18=24568.53941,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m500_w125p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m500_w125p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m500_w125p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m500_w125p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m500_w125p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m500_w125p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m500_w125p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m500_w125p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m600_w150p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.0388742, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.11279, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=8736.1115946,
                NEVT_UL16postVFP=8800.454386,
                NEVT_UL17=14220.370494,
                NEVT_UL18=16750.074701,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m600_w150p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m600_w150p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m600_w150p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m600_w150p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m600_w150p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m600_w150p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m600_w150p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m600_w150p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m800_w200p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.0138542, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.04658, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=2788.3372981,
                NEVT_UL16postVFP=3127.4778621,
                NEVT_UL17=5951.5560198,
                NEVT_UL18=5927.7307107,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m800_w200p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m800_w200p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m800_w200p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m800_w200p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m800_w200p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m800_w200p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m800_w200p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m800_w200p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m1000_w250p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.00503847, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.01067, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=1114.33082983,
                NEVT_UL16postVFP=1114.5434492,
                NEVT_UL17=2174.0807555,
                NEVT_UL18=2283.69269757,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m1000_w250p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m1000_w250p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m1000_w250p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m1000_w250p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m1000_w250p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m1000_w250p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m1000_w250p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m1000_w250p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m365_w91p25_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-0.761555, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.87897, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-170318.50717,
                NEVT_UL16postVFP=-171810.31304,
                NEVT_UL17=-327977.97074,
                NEVT_UL18=-339090.83725,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m365_w91p25_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m365_w91p25_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m365_w91p25_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m365_w91p25_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m365_w91p25_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m365_w91p25_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m365_w91p25_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m365_w91p25_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m400_w100p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-0.742658, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.8492, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-158971.77207,
                NEVT_UL16postVFP=-168691.582527,
                NEVT_UL17=-270072.27317,
                NEVT_UL18=-296149.69274,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m400_w100p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m400_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m400_w100p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m400_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m400_w100p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m400_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m400_w100p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m400_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m500_w125p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-0.427226, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.80251, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-88236.618912,
                NEVT_UL16postVFP=-97902.080091,
                NEVT_UL17=-141874.016668,
                NEVT_UL18=-165433.50606,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m500_w125p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m500_w125p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m500_w125p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m500_w125p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m500_w125p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m500_w125p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m500_w125p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m500_w125p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m600_w150p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-0.187834, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.77723, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-43744.150087,
                NEVT_UL16postVFP=-44496.672295,
                NEVT_UL17=-73627.40209,
                NEVT_UL18=-68137.292115,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m600_w150p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m600_w150p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m600_w150p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m600_w150p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m600_w150p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m600_w150p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m600_w150p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m600_w150p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m800_w200p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-0.0147037, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.74916, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-3449.2540378,
                NEVT_UL16postVFP=-4074.59180793,
                NEVT_UL17=-7511.3588611,
                NEVT_UL18=-6124.662187,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m800_w200p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m800_w200p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m800_w200p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m800_w200p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m800_w200p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m800_w200p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m800_w200p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m800_w200p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m1000_w250p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.0194944, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.73374, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=3946.9594208,
                NEVT_UL16postVFP=3866.5128433,
                NEVT_UL17=8502.5593978,
                NEVT_UL18=7326.6616632,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m1000_w250p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m1000_w250p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m1000_w250p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m1000_w250p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m1000_w250p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m1000_w250p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m1000_w250p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m1000_w250p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m365_w36p5_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.0733756, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.36165, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=16269.982433,
                NEVT_UL16postVFP=16550.0099108,
                NEVT_UL17=32682.539549,
                NEVT_UL18=33072.517701,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m365_w36p5_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m365_w36p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m365_w36p5_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m365_w36p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m365_w36p5_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m365_w36p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m365_w36p5_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m365_w36p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m400_w40p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.134601, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.28741, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=30318.763244,
                NEVT_UL16postVFP=30308.935418,
                NEVT_UL17=54843.92047,
                NEVT_UL18=57476.08948,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m400_w40p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m400_w40p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m400_w40p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m400_w40p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m400_w40p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m400_w40p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m400_w40p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m400_w40p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m500_w50p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.172511, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.17323, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=39022.080062,
                NEVT_UL16postVFP=38888.924959,
                NEVT_UL17=77994.05398,
                NEVT_UL18=70544.005991,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m500_w50p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m500_w50p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m500_w50p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m500_w50p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m500_w50p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m500_w50p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m500_w50p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m500_w50p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m600_w60p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.115724, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.11283, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=26205.193565,
                NEVT_UL16postVFP=26193.54991,
                NEVT_UL17=52100.11534,
                NEVT_UL18=51118.092581,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m600_w60p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m600_w60p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m600_w60p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m600_w60p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m600_w60p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m600_w60p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m600_w60p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m600_w60p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m800_w80p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.0381515, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.04663, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=8641.8341922,
                NEVT_UL16postVFP=8643.5531192,
                NEVT_UL17=17186.548258,
                NEVT_UL18=16460.178317,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m800_w80p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m800_w80p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m800_w80p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m800_w80p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m800_w80p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m800_w80p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m800_w80p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m800_w80p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m1000_w100p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.0127637, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.01064, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=2893.9334362,
                NEVT_UL16postVFP=2893.8290827,
                NEVT_UL17=5508.950888,
                NEVT_UL18=4919.8994139,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m1000_w100p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m1000_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m1000_w100p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m1000_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m1000_w100p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m1000_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m1000_w100p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m1000_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m365_w36p5_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-0.941809, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.87898, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-190508.62092,
                NEVT_UL16postVFP=-210239.509572,
                NEVT_UL17=-421755.8942,
                NEVT_UL18=-381133.58825,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m365_w36p5_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m365_w36p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m365_w36p5_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m365_w36p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m365_w36p5_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m365_w36p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m365_w36p5_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m365_w36p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m400_w40p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-0.936429, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.84921, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-211991.76306,
                NEVT_UL16postVFP=-212560.040131,
                NEVT_UL17=-404689.32971,
                NEVT_UL18=-416737.97976,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m400_w40p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m400_w40p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m400_w40p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m400_w40p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m400_w40p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m400_w40p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m400_w40p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m400_w40p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m500_w50p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-0.466654, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.80247, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-107012.401862,
                NEVT_UL16postVFP=-109145.38449,
                NEVT_UL17=-212458.66898,
                NEVT_UL18=-205382.938069,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m500_w50p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m500_w50p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m500_w50p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m500_w50p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m500_w50p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m500_w50p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m500_w50p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m500_w50p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m600_w60p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-0.160288, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.77724, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-37050.257408,
                NEVT_UL16postVFP=-38852.607288,
                NEVT_UL17=-70830.958885,
                NEVT_UL18=-68067.566137,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m600_w60p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m600_w60p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m600_w60p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m600_w60p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m600_w60p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m600_w60p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m600_w60p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m600_w60p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m800_w80p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.0234526, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.74918, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=4014.241068,
                NEVT_UL16postVFP=3859.553408,
                NEVT_UL17=8654.1696319,
                NEVT_UL18=9064.6972729,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m800_w80p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m800_w80p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m800_w80p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m800_w80p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m800_w80p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m800_w80p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m800_w80p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m800_w80p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m1000_w100p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.0452619, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.73373, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=8760.663204,
                NEVT_UL16postVFP=9822.1785528,
                NEVT_UL17=19995.912164,
                NEVT_UL18=19102.002607,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m1000_w100p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m1000_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m1000_w100p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m1000_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m1000_w100p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m1000_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m1000_w100p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m1000_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m365_w9p125_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.202185, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.36181, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=44000.782175,
                NEVT_UL16postVFP=45490.800092,
                NEVT_UL17=86586.017965,
                NEVT_UL18=80112.917962,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m365_w9p125_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m365_w9p125_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m365_w9p125_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m365_w9p125_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m365_w9p125_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m365_w9p125_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m365_w9p125_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m365_w9p125_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m400_w10p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.54795, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.28735, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=110433.410334,
                NEVT_UL16postVFP=119834.460985,
                NEVT_UL17=241956.114212,
                NEVT_UL18=221417.64181,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m400_w10p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m400_w10p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m400_w10p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m400_w10p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m400_w10p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m400_w10p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m400_w10p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m400_w10p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m500_w12p5_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.770716, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.1733, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=174249.05999,
                NEVT_UL16postVFP=174336.8065,
                NEVT_UL17=348465.2412,
                NEVT_UL18=345674.98845,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m500_w12p5_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m500_w12p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m500_w12p5_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m500_w12p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m500_w12p5_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m500_w12p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m500_w12p5_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m500_w12p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m600_w15p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.506278, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.11286, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=112831.104056,
                NEVT_UL16postVFP=114779.796842,
                NEVT_UL17=207170.56805,
                NEVT_UL18=202686.754053,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m600_w15p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m600_w15p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m600_w15p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m600_w15p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m600_w15p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m600_w15p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m600_w15p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m600_w15p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m800_w20p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.158117, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.04658, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=34413.223964,
                NEVT_UL16postVFP=35824.651047,
                NEVT_UL17=56637.54871,
                NEVT_UL18=68839.25611,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m800_w20p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m800_w20p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m800_w20p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m800_w20p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m800_w20p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m800_w20p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m800_w20p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m800_w20p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m1000_w25p0_res" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.0500883, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=2.01071, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=9174.0293902,
                NEVT_UL16postVFP=11358.4466789,
                NEVT_UL17=22709.4169,
                NEVT_UL18=22163.8419044,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m1000_w25p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m1000_w25p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m1000_w25p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m1000_w25p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m1000_w25p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m1000_w25p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m1000_w25p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m1000_w25p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m365_w9p125_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-1.08972, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.87905, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-243891.57659,
                NEVT_UL16postVFP=-244752.00579,
                NEVT_UL17=-455312.22918,
                NEVT_UL18=-464473.78555,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m365_w9p125_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m365_w9p125_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m365_w9p125_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m365_w9p125_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m365_w9p125_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m365_w9p125_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m365_w9p125_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m365_w9p125_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m400_w10p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-1.07602, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.84919, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-217545.27179,
                NEVT_UL16postVFP=-244155.378094,
                NEVT_UL17=-407172.40438,
                NEVT_UL18=-381994.59397,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m400_w10p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m400_w10p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m400_w10p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m400_w10p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m400_w10p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m400_w10p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m400_w10p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m400_w10p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m500_w12p5_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-0.473926, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.8025, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-98109.442139,
                NEVT_UL16postVFP=-110955.45375,
                NEVT_UL17=-198807.1304,
                NEVT_UL18=-199994.69995,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m500_w12p5_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m500_w12p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m500_w12p5_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m500_w12p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m500_w12p5_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m500_w12p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m500_w12p5_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m500_w12p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m600_w15p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=-0.133391, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.77726, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-28958.368656,
                NEVT_UL16postVFP=-33767.930485,
                NEVT_UL17=-57694.816784,
                NEVT_UL18=-54321.671122,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m600_w15p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m600_w15p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m600_w15p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m600_w15p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m600_w15p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m600_w15p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m600_w15p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m600_w15p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m800_w20p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.0478693, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.74916, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=10449.3727671,
                NEVT_UL16postVFP=10966.333264,
                NEVT_UL17=20316.226675,
                NEVT_UL18=18754.358222,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m800_w20p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m800_w20p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m800_w20p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m800_w20p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m800_w20p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m800_w20p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m800_w20p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m800_w20p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m1000_w25p0_int" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.0599909, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : MCSampleValuesHelperPrototype.kFactorValues(
                kFac_13TeV=1.73376, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=13776.0977588,
                NEVT_UL16postVFP=13125.219647,
                NEVT_UL17=24489.585559,
                NEVT_UL18=23710.528481,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m1000_w25p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m1000_w25p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m1000_w25p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m1000_w25p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m1000_w25p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m1000_w25p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m1000_w25p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m1000_w25p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TstarTstarToTgluonTgluon_M-700" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=92000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgluonTgluon_M-700_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/TstarTstarToTgluonTgluon_M-700_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
            ),
        },

        "TstarTstarToTgluonTgluon_M-800" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=92000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgluonTgluon_M-800_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgluonTgluon_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
            ),
        },

        "TstarTstarToTgluonTgluon_M-900" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=92000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgluonTgluon_M-900_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgluonTgluon_M-900_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
            ),
        },

        "TstarTstarToTgluonTgluon_M-1000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=92000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgluonTgluon_M-1000_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgluonTgluon_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
            ),
        },

        "TstarTstarToTgluonTgluon_M-1100" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=92000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgluonTgluon_M-1100_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgluonTgluon_M-1100_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
            ),
        },

        "TstarTstarToTgluonTgluon_M-1200" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=92000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgluonTgluon_M-1200_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgluonTgluon_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
            ),
        },

        "TstarTstarToTgluonTgluon_M-1300" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=92000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgluonTgluon_M-1300_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/TstarTstarToTgluonTgluon_M-1300_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
            ),
        },

        "TstarTstarToTgluonTgluon_M-1400" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=92000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgluonTgluon_M-1400_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgluonTgluon_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
            ),
        },

        "TstarTstarToTgluonTgluon_M-1500" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=92000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgluonTgluon_M-1500_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgluonTgluon_M-1500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
            ),
        },

        "TstarTstarToTgluonTgluon_M-1600" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=137998.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgluonTgluon_M-1600_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgluonTgluon_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
            ),
        },

        "TstarTstarToTgluonTgluon_M-1700" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=138000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgluonTgluon_M-1700_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/TstarTstarToTgluonTgluon_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
            ),
        },

        "TstarTstarToTgluonTgluon_M-1800" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=138000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgluonTgluon_M-1800_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgluonTgluon_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
            ),
        },

        "TstarTstarToTgluonTgluon_M-1900" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=138000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgluonTgluon_M-1900_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgluonTgluon_M-1900_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
            ),
        },

        "TstarTstarToTgluonTgluon_M-2000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=184000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgluonTgluon_M-2000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/TstarTstarToTgluonTgluon_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
            ),
        },

        "TstarTstarToTgluonTgluon_M-2250" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=184000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgluonTgluon_M-2250_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgluonTgluon_M-2250_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
            ),
        },

        "TstarTstarToTgluonTgluon_M-2500" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=184000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgluonTgluon_M-2500_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgluonTgluon_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
            ),
        },

        "TstarTstarToTgluonTgluon_M-2750" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=180000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgluonTgluon_M-2750_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgluonTgluon_M-2750_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
            ),
        },

        "TstarTstarToTgluonTgluon_M-3000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=184000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgluonTgluon_M-3000_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgluonTgluon_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
            ),
        },

        "TstarTstarToTgammaTgamma_M-700" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=200000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/TstarTstarToTgammaTgamma_M-700_CP5_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/TstarTstarToTgammaTgamma_M-700_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgammaTgamma_M-700_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgammaTgamma_M-700_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/TstarTstarToTgammaTgamma_M-700_CP5_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TstarTstarToTgammaTgamma_M-700_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/TstarTstarToTgammaTgamma_M-700_CP5_madgraph-pythia8_Summer20UL18_v3.xml", XmlSource_UL18="/TstarTstarToTgammaTgamma_M-700_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3/MINIAODSIM"
            ),
        },

        "TstarTstarToTgammaTgamma_M-800" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=108000,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=200000,
                NEVT_UL18=200000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/TstarTstarToTgammaTgamma_M-800_CP5_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/TstarTstarToTgammaTgamma_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgammaTgamma_M-800_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgammaTgamma_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/TstarTstarToTgammaTgamma_M-800_CP5_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TstarTstarToTgammaTgamma_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/TstarTstarToTgammaTgamma_M-800_CP5_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TstarTstarToTgammaTgamma_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TstarTstarToTgammaTgamma_M-900" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=197000.0,
                NEVT_UL18=200000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/TstarTstarToTgammaTgamma_M-900_CP5_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/TstarTstarToTgammaTgamma_M-900_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgammaTgamma_M-900_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgammaTgamma_M-900_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/TstarTstarToTgammaTgamma_M-900_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TstarTstarToTgammaTgamma_M-900_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/TstarTstarToTgammaTgamma_M-900_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TstarTstarToTgammaTgamma_M-900_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TstarTstarToTgammaTgamma_M-1000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=191000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/TstarTstarToTgammaTgamma_M-1000_CP5_madgraph-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TstarTstarToTgammaTgamma_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgammaTgamma_M-1000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/TstarTstarToTgammaTgamma_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/TstarTstarToTgammaTgamma_M-1000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TstarTstarToTgammaTgamma_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/TstarTstarToTgammaTgamma_M-1000_CP5_madgraph-pythia8_Summer20UL18_v3.xml", XmlSource_UL18="/TstarTstarToTgammaTgamma_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3/MINIAODSIM",
            ),
        },

        "TstarTstarToTgammaTgamma_M-1100" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=200000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/TstarTstarToTgammaTgamma_M-1100_CP5_madgraph-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TstarTstarToTgammaTgamma_M-1100_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgammaTgamma_M-1100_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgammaTgamma_M-1100_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/TstarTstarToTgammaTgamma_M-1100_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TstarTstarToTgammaTgamma_M-1100_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/TstarTstarToTgammaTgamma_M-1100_CP5_madgraph-pythia8_Summer20UL18_v3.xml", XmlSource_UL18="/TstarTstarToTgammaTgamma_M-1100_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3/MINIAODSIM",
            ),
        },

        "TstarTstarToTgammaTgamma_M-1200" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=96000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=200000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/TstarTstarToTgammaTgamma_M-1200_CP5_madgraph-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TstarTstarToTgammaTgamma_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgammaTgamma_M-1200_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/TstarTstarToTgammaTgamma_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/TstarTstarToTgammaTgamma_M-1200_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TstarTstarToTgammaTgamma_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/TstarTstarToTgammaTgamma_M-1200_CP5_madgraph-pythia8_Summer20UL18_v3.xml", XmlSource_UL18="/TstarTstarToTgammaTgamma_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3/MINIAODSIM",
            ),
        },

        "TstarTstarToTgammaTgamma_M-1300" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=200000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/TstarTstarToTgammaTgamma_M-1300_CP5_madgraph-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TstarTstarToTgammaTgamma_M-1300_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgammaTgamma_M-1300_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgammaTgamma_M-1300_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/TstarTstarToTgammaTgamma_M-1300_CP5_madgraph-pythia8_Summer20UL17_v3.xml", XmlSource_UL17="/TstarTstarToTgammaTgamma_M-1300_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v3/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/TstarTstarToTgammaTgamma_M-1300_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TstarTstarToTgammaTgamma_M-1300_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TstarTstarToTgammaTgamma_M-1400" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=197000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/TstarTstarToTgammaTgamma_M-1400_CP5_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/TstarTstarToTgammaTgamma_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgammaTgamma_M-1400_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgammaTgamma_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/TstarTstarToTgammaTgamma_M-1400_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TstarTstarToTgammaTgamma_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/TstarTstarToTgammaTgamma_M-1400_CP5_madgraph-pythia8_Summer20UL18_v3.xml", XmlSource_UL18="/TstarTstarToTgammaTgamma_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3/MINIAODSIM",
            ),
        },

        "TstarTstarToTgammaTgamma_M-1500" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=200000.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/TstarTstarToTgammaTgamma_M-1500_CP5_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/TstarTstarToTgammaTgamma_M-1500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgammaTgamma_M-1500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/TstarTstarToTgammaTgamma_M-1500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/TstarTstarToTgammaTgamma_M-1500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TstarTstarToTgammaTgamma_M-1500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/TstarTstarToTgammaTgamma_M-1500_CP5_madgraph-pythia8_Summer20UL18_v3.xml", XmlSource_UL18="/TstarTstarToTgammaTgamma_M-1500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3/MINIAODSIM",
            ),
        },

        "TstarTstarToTgammaTgamma_M-1600" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=162000,
                NEVT_UL16postVFP=138000.0,
                NEVT_UL17=276000,
                NEVT_UL18=300000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/TstarTstarToTgammaTgamma_M-1600_CP5_madgraph-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TstarTstarToTgammaTgamma_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgammaTgamma_M-1600_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgammaTgamma_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/TstarTstarToTgammaTgamma_M-1600_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TstarTstarToTgammaTgamma_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/TstarTstarToTgammaTgamma_M-1600_CP5_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TstarTstarToTgammaTgamma_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TstarTstarToTgammaTgamma_M-1700" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=162000,
                NEVT_UL16postVFP=138000,
                NEVT_UL17=297000,
                NEVT_UL18=297000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/TstarTstarToTgammaTgamma_M-1700_CP5_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/TstarTstarToTgammaTgamma_M-1700_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgammaTgamma_M-1700_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgammaTgamma_M-1700_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/TstarTstarToTgammaTgamma_M-1700_CP5_madgraph-pythia8_Summer20UL17_v3.xml", XmlSource_UL17="/TstarTstarToTgammaTgamma_M-1700_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v3/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/TstarTstarToTgammaTgamma_M-1700_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TstarTstarToTgammaTgamma_M-1700_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TstarTstarToTgammaTgamma_M-1800" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=138000,
                NEVT_UL16postVFP=127000,
                NEVT_UL17=281000,
                NEVT_UL18=300000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/TstarTstarToTgammaTgamma_M-1800_CP5_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/TstarTstarToTgammaTgamma_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgammaTgamma_M-1800_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgammaTgamma_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/TstarTstarToTgammaTgamma_M-1800_CP5_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TstarTstarToTgammaTgamma_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/TstarTstarToTgammaTgamma_M-1800_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TstarTstarToTgammaTgamma_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TstarTstarToTgammaTgamma_M-1900" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=158000,
                NEVT_UL16postVFP=138000,
                NEVT_UL17=300000,
                NEVT_UL18=300000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/TstarTstarToTgammaTgamma_M-1900_CP5_madgraph-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TstarTstarToTgammaTgamma_M-1900_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgammaTgamma_M-1900_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/TstarTstarToTgammaTgamma_M-1900_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/TstarTstarToTgammaTgamma_M-1900_CP5_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TstarTstarToTgammaTgamma_M-1900_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/TstarTstarToTgammaTgamma_M-1900_CP5_madgraph-pythia8_Summer20UL18_v3.xml", XmlSource_UL18="/TstarTstarToTgammaTgamma_M-1900_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3/MINIAODSIM",
            ),
        },

        "TstarTstarToTgammaTgamma_M-2000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=216000,
                NEVT_UL16postVFP=184000,
                NEVT_UL17=376000,
                NEVT_UL18=391000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/TstarTstarToTgammaTgamma_M-2000_CP5_madgraph-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TstarTstarToTgammaTgamma_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgammaTgamma_M-2000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/TstarTstarToTgammaTgamma_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/TstarTstarToTgammaTgamma_M-2000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TstarTstarToTgammaTgamma_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/TstarTstarToTgammaTgamma_M-2000_CP5_madgraph-pythia8_Summer20UL18_v3.xml", XmlSource_UL18="/TstarTstarToTgammaTgamma_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3/MINIAODSIM",
            ),
        },

        "TstarTstarToTgammaTgamma_M-2250" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=216000,
                NEVT_UL16postVFP=184000,
                NEVT_UL17=400000,
                NEVT_UL18=400000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/TstarTstarToTgammaTgamma_M-2250_CP5_madgraph-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TstarTstarToTgammaTgamma_M-2250_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgammaTgamma_M-2250_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgammaTgamma_M-2250_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/TstarTstarToTgammaTgamma_M-2250_CP5_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TstarTstarToTgammaTgamma_M-2250_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/TstarTstarToTgammaTgamma_M-2250_CP5_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TstarTstarToTgammaTgamma_M-2250_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TstarTstarToTgammaTgamma_M-2500" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=212000,
                NEVT_UL16postVFP=184000,
                NEVT_UL17=373000,
                NEVT_UL18=364000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/TstarTstarToTgammaTgamma_M-2500_CP5_madgraph-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TstarTstarToTgammaTgamma_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgammaTgamma_M-2500_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgammaTgamma_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/TstarTstarToTgammaTgamma_M-2500_CP5_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TstarTstarToTgammaTgamma_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/TstarTstarToTgammaTgamma_M-2500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TstarTstarToTgammaTgamma_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TstarTstarToTgammaTgamma_M-2750" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=214000,
                NEVT_UL16postVFP=184000,
                NEVT_UL17=391000,
                NEVT_UL18=379000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/TstarTstarToTgammaTgamma_M-2750_CP5_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/TstarTstarToTgammaTgamma_M-2750_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgammaTgamma_M-2750_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgammaTgamma_M-2750_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/TstarTstarToTgammaTgamma_M-2750_CP5_madgraph-pythia8_Summer20UL17_v3.xml", XmlSource_UL17="/TstarTstarToTgammaTgamma_M-2750_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v3/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/TstarTstarToTgammaTgamma_M-2750_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TstarTstarToTgammaTgamma_M-2750_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TstarTstarToTgammaTgamma_M-3000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=212000,
                NEVT_UL16postVFP=184000,
                NEVT_UL17=364000,
                NEVT_UL18=391000,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/TstarTstarToTgammaTgamma_M-3000_CP5_madgraph-pythia8_Summer20UL16APV_v3.xml", XmlSource_UL16preVFP="/TstarTstarToTgammaTgamma_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/TstarTstarToTgammaTgamma_M-3000_CP5_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TstarTstarToTgammaTgamma_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/TstarTstarToTgammaTgamma_M-3000_CP5_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TstarTstarToTgammaTgamma_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/TstarTstarToTgammaTgamma_M-3000_CP5_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TstarTstarToTgammaTgamma_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
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
