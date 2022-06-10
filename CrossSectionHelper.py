from collections import namedtuple,Mapping
import os

def namedtuple_with_defaults(typename, field_names, default_values=()):
    T = namedtuple(typename, field_names)
    T.__new__.__defaults__ = (None,) * len(T._fields)
    if isinstance(default_values, Mapping):
        prototype = T(**default_values)
    else:
        prototype = T(*default_values)
    T.__new__.__defaults__ = tuple(prototype)
    return T


class MCSampleValuesHelper():
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

    __years = ["UL16preVFP","UL16postVFP","UL17","UL18"]
    __energies = ["13TeV"]
    __xs_field_names = []
    __nevt_field_names = []
    __br_field_names = []
    __kfactor_field_names = []
    __corr_field_names = []
    __xml_field_names = []
    __key_field_map = {
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
    XSValues      = namedtuple_with_defaults("XSValues",      __xs_field_names,       [__key_field_map["CrossSection"][1],""]*len(__years+__energies))
    NEventsValues = namedtuple_with_defaults("NEventsValues", __nevt_field_names,     [__key_field_map["NEvents"][1],""]*len(__years+__energies))
    BRValues      = namedtuple_with_defaults("BRValues",      __br_field_names,       [__key_field_map["BranchingRatio"][1],""]*len(__years+__energies))
    kFactorValues = namedtuple_with_defaults("kFactorValues", __kfactor_field_names,  [__key_field_map["kFactor"][1],""]*len(__years+__energies))
    CorrValues    = namedtuple_with_defaults("CorrValues",    __corr_field_names,     [__key_field_map["Correction"][1],""]*len(__years+__energies))
    XMLValues     = namedtuple_with_defaults("XMLValues",     __xml_field_names,      [__key_field_map["XMLname"][1],""]*len(__years+__energies))

    __values_dict = {

        "SingleMuon_RunA": {
            "NEvents" : NEventsValues(
                NEVT_UL18=241608232,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/SingleMuon_Run2018A-UL2018_MiniAODv2-v3.xml", XmlSource_UL18="/SingleMuon/Run2018A-UL2018_MiniAODv2-v3/MINIAOD",
            ),
        },

        "SingleMuon_RunB": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2789243+158145722,
                NEVT_UL17=136300266,
                NEVT_UL18=119918017,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleMuon_Run2016B-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleMuon/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleMuon_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleMuon/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/SingleMuon_Run2018B-UL2018_MiniAODv2-v2.xml", XmlSource_UL18="/SingleMuon/Run2018B-UL2018_MiniAODv2-v2/MINIAOD",
            ),
        },

        "SingleMuon_RunC": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=67441308,
                NEVT_UL17=165652756,
                NEVT_UL18=109986009,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleMuon_Run2016C-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleMuon/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleMuon_Run2017C-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleMuon/Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/SingleMuon_Run2018C-UL2018_MiniAODv2-v2.xml", XmlSource_UL18="/SingleMuon/Run2018C-UL2018_MiniAODv2-v2/MINIAOD",
            ),
        },

        "SingleMuon_RunD": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=98017996,
                NEVT_UL17=70361660,
                NEVT_UL18=513909894,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleMuon_Run2016D-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleMuon/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleMuon_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleMuon/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/SingleMuon_Run2018D-UL2018_MiniAODv2-v3.xml", XmlSource_UL18="/SingleMuon/Run2018D-UL2018_MiniAODv2-v3/MINIAOD",
            ),
        },

        "SingleMuon_RunE": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=90984718,
                NEVT_UL17=154618774,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleMuon_Run2016E-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleMuon/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleMuon_Run2017E-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleMuon/Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleMuon_RunF": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=57465359,
                NEVT_UL16postVFP=8024195,
                NEVT_UL17=242140980,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleMuon_Run2016F-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleMuon/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SingleMuon_Run2016F-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SingleMuon/Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleMuon_Run2017F-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleMuon/Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleMuon_RunG": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=149916849,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SingleMuon_Run2016G-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SingleMuon/Run2016G-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "SingleMuon_RunH": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=174035164,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SingleMuon_Run2016H-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SingleMuon/Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "SingleElectron_RunB": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1422819+246440440,
                NEVT_UL17=60537490,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleElectron_Run2016B-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleElectron/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleElectron_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleElectron/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleElectron_RunC": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=97259854,
                NEVT_UL17=136637888,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleElectron_Run2016C-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleElectron/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleElectron_Run2017C-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleElectron/Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleElectron_RunD": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=148167727,
                NEVT_UL17=51526521,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleElectron_Run2016D-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleElectron/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleElectron_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleElectron/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleElectron_RunE": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=117269446,
                NEVT_UL17=102122055,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleElectron_Run2016E-HIPM_UL2016_MiniAODv2-v5.xml", XmlSource_UL16preVFP="/SingleElectron/Run2016E-HIPM_UL2016_MiniAODv2-v5/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleElectron_Run2017E-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleElectron/Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleElectron_RunF": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=61735326,
                NEVT_UL16postVFP=8858206,
                NEVT_UL17=128467223,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleElectron_Run2016F-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleElectron/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SingleElectron_Run2016F-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SingleElectron/Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleElectron_Run2017F-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleElectron/Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleElectron_RunG": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=153363109,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SingleElectron_Run2016G-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SingleElectron/Run2016G-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "SingleElectron_RunH": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=129021893,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SingleElectron_Run2016H-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SingleElectron/Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "SinglePhoton_RunB": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=13119462+56878553,
                NEVT_UL17=15950935,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SinglePhoton_Run2016B-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SinglePhoton/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SinglePhoton_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SinglePhoton/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SinglePhoton_RunC": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=23147235,
                NEVT_UL17=42182948,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SinglePhoton_Run2016C-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SinglePhoton/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SinglePhoton_Run2017C-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SinglePhoton/Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SinglePhoton_RunD": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=29801360,
                NEVT_UL17=9753462,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SinglePhoton_Run2016D-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SinglePhoton/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SinglePhoton_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SinglePhoton/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SinglePhoton_RunE": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=22322869,
                NEVT_UL17=19011446,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SinglePhoton_Run2016E-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SinglePhoton/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SinglePhoton_Run2017E-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SinglePhoton/Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SinglePhoton_RunF": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=12806145,
                NEVT_UL16postVFP=1860761,
                NEVT_UL17=29783015,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SinglePhoton_Run2016F-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SinglePhoton/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SinglePhoton_Run2016F-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SinglePhoton/Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SinglePhoton_Run2017F-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SinglePhoton/Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SinglePhoton_RunG": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=33288854,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SinglePhoton_Run2016G-UL2016_MiniAODv2-v3.xml", XmlSource_UL16postVFP="/SinglePhoton/Run2016G-UL2016_MiniAODv2-v3/MINIAOD",
            ),
        },

        "SinglePhoton_RunH": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=35035661,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SinglePhoton_Run2016H-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SinglePhoton/Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "EGamma_RunA": {
            "NEvents" : NEventsValues(
                NEVT_UL18=339013231,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/EGamma_Run2018A-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/EGamma/Run2018A-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "EGamma_RunB": {
            "NEvents" : NEventsValues(
                NEVT_UL18=153792795,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/EGamma_Run2018B-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/EGamma/Run2018B-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "EGamma_RunC": {
            "NEvents" : NEventsValues(
                NEVT_UL18=147827904,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/EGamma_Run2018C-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/EGamma/Run2018C-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "EGamma_RunD": {
            "NEvents" : NEventsValues(
                NEVT_UL18=752522245,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/EGamma_Run2018D-UL2018_MiniAODv2-v2.xml", XmlSource_UL18="/EGamma/Run2018D-UL2018_MiniAODv2-v2/MINIAOD",
            ),
        },

        "DoubleMuon_RunA": {
            "NEvents" : NEventsValues(
                NEVT_UL18=75491789,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/DoubleMuon_Run2018A-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/DoubleMuon/Run2018A-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "DoubleMuon_RunB": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=4199947+82535526,
                NEVT_UL17=14501767,
                NEVT_UL18=35057758,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/DoubleMuon_Run2016B-HIPM_UL2016_MiniAODv2-v1.xml", XmlSource_UL16preVFP="/DoubleMuon/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/DoubleMuon_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/DoubleMuon/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/DoubleMuon_Run2018B-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/DoubleMuon/Run2018B-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "DoubleMuon_RunC": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=27934629,
                NEVT_UL17=49636525,
                NEVT_UL18=34565869,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/DoubleMuon_Run2016C-HIPM_UL2016_MiniAODv2-v1.xml", XmlSource_UL16preVFP="/DoubleMuon/Run2016C-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/DoubleMuon_Run2017C-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/DoubleMuon/Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/DoubleMuon_Run2018C-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/DoubleMuon/Run2018C-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "DoubleMuon_RunD": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=33861745,
                NEVT_UL17=23075733,
                NEVT_UL18=168600679,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/DoubleMuon_Run2016D-HIPM_UL2016_MiniAODv2-v1.xml", XmlSource_UL16preVFP="/DoubleMuon/Run2016D-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/DoubleMuon_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/DoubleMuon/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/DoubleMuon_Run2018D-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/DoubleMuon/Run2018D-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "DoubleMuon_RunE": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=28246946,
                NEVT_UL17=51531477,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/DoubleMuon_Run2016E-HIPM_UL2016_MiniAODv2-v1.xml", XmlSource_UL16preVFP="/DoubleMuon/Run2016E-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/DoubleMuon_Run2017E-UL2017_MiniAODv2-v2.xml", XmlSource_UL17="/DoubleMuon/Run2017E-UL2017_MiniAODv2-v2/MINIAOD",
            ),
        },

        "DoubleMuon_RunF": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=17900759,
                NEVT_UL16postVFP=2429162,
                NEVT_UL17=79756560,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/DoubleMuon_Run2016F-HIPM_UL2016_MiniAODv2-v1.xml", XmlSource_UL16preVFP="/DoubleMuon/Run2016F-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/DoubleMuon_Run2016F-UL2016_MiniAODv2-v1.xml", XmlSource_UL16postVFP="/DoubleMuon/Run2016F-UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/DoubleMuon_Run2017F-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/DoubleMuon/Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "DoubleMuon_RunG": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=45235604,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/DoubleMuon_Run2016G-UL2016_MiniAODv2-v1.xml", XmlSource_UL16postVFP="/DoubleMuon/Run2016G-UL2016_MiniAODv2-v1/MINIAOD",
            ),
        },

        "DoubleMuon_RunH": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=48912812,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/DoubleMuon_Run2016H-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/DoubleMuon/Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "DoubleEG_RunB": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=5686987+143073268,
                NEVT_UL17=58088760
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/DoubleEG_Run2016B-HIPM_UL2016_MiniAODv2.xml", XmlSource_UL16preVFP="/DoubleEG/{Run2016B-ver1_HIPM_UL2016_MiniAODv2-v1,Run2016B-ver2_HIPM_UL2016_MiniAODv2-v3}/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/DoubleEG_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/DoubleEG/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "DoubleEG_RunC": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=47677856,
                NEVT_UL17=65181125
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/DoubleEG_Run2016C-HIPM_UL2016_MiniAODv2-v1.xml", XmlSource_UL16preVFP="/DoubleEG/Run2016C-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/DoubleEG_Run2017C-UL2017_MiniAODv2-v2.xml", XmlSource_UL17="/DoubleEG/Run2017C-UL2017_MiniAODv2-v2/MINIAOD",
            ),
        },

        "DoubleEG_RunD": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=53324960,
                NEVT_UL17=25911432
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/DoubleEG_Run2016D-HIPM_UL2016_MiniAODv2-v1.xml", XmlSource_UL16preVFP="/DoubleEG/Run2016D-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/DoubleEG_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/DoubleEG/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "DoubleEG_RunE": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=49877710,
                NEVT_UL17=56241190
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/DoubleEG_Run2016E-HIPM_UL2016_MiniAODv2-v1.xml", XmlSource_UL16preVFP="/DoubleEG/Run2016E-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/DoubleEG_Run2017E-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/DoubleEG/Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "DoubleEG_RunF": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=30216940,
                NEVT_UL16postVFP=4360689,
                NEVT_UL17=74265012
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/DoubleEG_Run2016F-HIPM_UL2016_MiniAODv2-v1.xml", XmlSource_UL16preVFP="/DoubleEG/Run2016F-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/DoubleEG_Run2016F-UL2016_MiniAODv2-v1.xml", XmlSource_UL16postVFP="/DoubleEG/Run2016F-UL2016_MiniAODv2-v1/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/DoubleEG_Run2017F-UL2017_MiniAODv2-v2.xml", XmlSource_UL17="/DoubleEG/Run2017F-UL2017_MiniAODv2-v2/MINIAOD",
            ),
        },

        "DoubleEG_RunG": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=78797031,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/DoubleEG_Run2016G-UL2016_MiniAODv2-v1.xml", XmlSource_UL16postVFP="/DoubleEG/Run2016G-UL2016_MiniAODv2-v1/MINIAOD",
            ),
        },

        "DoubleEG_RunH": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=85388734,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/DoubleEG_Run2016H-UL2016_MiniAODv2-v1.xml", XmlSource_UL16postVFP="/DoubleEG/Run2016H-UL2016_MiniAODv2-v1/MINIAOD",
            ),
        },

        "JetHT_RunA": {
            "NEvents" : NEventsValues(
                NEVT_UL18=171484635,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/JetHT_Run2018A-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/JetHT/JetHT_Run2018A-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "JetHT_RunB": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=9726665+133752091,
                NEVT_UL17=63043590,
                NEVT_UL18=78255208,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016B-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/JetHT_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/JetHT_Run2018B-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/JetHT/JetHT_Run2018B-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "JetHT_RunC": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=46495988,
                NEVT_UL17=96264601,
                NEVT_UL18=70027804,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016C-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/JetHT_Run2017C-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/JetHT_Run2018C-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/JetHT/JetHT_Run2018C-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "JetHT_RunD": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=73330042,
                NEVT_UL17=46145204,
                NEVT_UL18=356976276,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016D-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/JetHT_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/JetHT_Run2018D-UL2018_MiniAODv2-v2.xml", XmlSource_UL18="/JetHT/JetHT_Run2018D-UL2018_MiniAODv2-v2/MINIAOD",
            ),
        },

        "JetHT_RunE": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=69219288,
                NEVT_UL17=89630771,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016E-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/JetHT_Run2017E-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "JetHT_RunF": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=41564915,
                NEVT_UL16postVFP=6613811,
                NEVT_UL17=115429972,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016F-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/JetHT_Run2016F-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/JetHT/JetHT_Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/JetHT_Run2017F-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "JetHT_RunG": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=120745085,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/JetHT_Run2016G-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/JetHT/JetHT_Run2016G-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "JetHT_RunH": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=124054791,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/JetHT_Run2016H-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/JetHT/JetHT_Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "MET_RunA": {
            "NEvents" : NEventsValues(
                NEVT_UL18=52759851,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/MET_Run2018A-UL2018_MiniAODv2-v2.xml", XmlSource_UL18="/MET/Run2018A-UL2018_MiniAODv2-v2/MINIAOD",
            ),
        },

        "MET_RunB": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=583427+35987712,
                NEVT_UL17=51623474,
                NEVT_UL18=29713483,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/MET_Run2016B-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/MET/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/MET_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/MET/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/MET_Run2018B-UL2018_MiniAODv2-v2.xml", XmlSource_UL18="/MET/Run2018B-UL2018_MiniAODv2-v2/MINIAOD",
            ),
        },

        "MET_RunC": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=17381222,
                NEVT_UL17=115906496,
                NEVT_UL18=31237456,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/MET_Run2016C-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/MET/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/MET_Run2017C-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/MET/Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/MET_Run2018C-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/MET/Run2018C-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "MET_RunD": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=20947429,
                NEVT_UL17=20075033,
                NEVT_UL18=160411782,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/MET_Run2016D-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/MET/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/MET_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/MET/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/MET_Run2018D-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/MET/Run2018D-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "MET_RunE": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=22348402,
                NEVT_UL17=71418865,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/MET_Run2016E-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/MET/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/MET_Run2017E-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/MET/Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "MET_RunF": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=11936579,
                NEVT_UL16postVFP=1383250,
                NEVT_UL17=177521562,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/MET_Run2016F-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/MET/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/MET_Run2016F-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/MET/Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/MET_Run2017F-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/MET/Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "MET_RunG": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=26974131,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/MET_Run2016G-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/MET/Run2016G-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "MET_RunH": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=39773485,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/MET_Run2016H-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/MET/Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "TTTo2L2Nu" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2704527656.31,
                NEVT_UL16postVFP=3146182352.62,
                NEVT_UL17=7695841652.46,
                NEVT_UL18=10528968536.7,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=39772305956.8,
                NEVT_UL16postVFP=43624104390.1,
                NEVT_UL17=1.06922359713e+11,
                NEVT_UL18=1.44128770259e+11,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TTToHadronic" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=30637661153.8,
                NEVT_UL16postVFP=34334910058.7,
                NEVT_UL17=73994630561.7,
                NEVT_UL18=1.07748739105e+11,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_hdampDOWN" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1223965702.6,
                NEVT_UL16postVFP=1305254604.97,
                NEVT_UL17=2929943912.75,
                NEVT_UL18=4323628397.15,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_hdampDOWN_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_hdampDOWN_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_hdampDOWN_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_hdampDOWN_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_hdampDOWN" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=14214658267.7,
                NEVT_UL16postVFP=18249770082.9,
                NEVT_UL17=40416900003.0,
                NEVT_UL18=58140739277.2,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_hdampDOWN_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_hdampDOWN_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_hdampDOWN_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_hdampDOWN_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToHadronic_hdampDOWN" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=11601553106.6,
                NEVT_UL16postVFP=13097955883.4,
                NEVT_UL17=29913495414.4,
                NEVT_UL18=43787698273.3,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_hdampDOWN_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_hdampDOWN_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_hdampDOWN_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_hdampDOWN_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_hdampUP" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1071941341.28,
                NEVT_UL16postVFP=1361059107.92,
                NEVT_UL17=2905584113.05,
                NEVT_UL18=3930878067.9,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_hdampUP_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_hdampUP_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_hdampUP_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_hdampUP_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_hdampUP" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=17142541164.3,
                NEVT_UL16postVFP=18309172997.5,
                NEVT_UL17=40017266549.6,
                NEVT_UL18=60002115817.1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_hdampUP_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_hdampUP_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_hdampUP_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_hdampUP_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToHadronic_hdampUP" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=9575911366.78,
                NEVT_UL16postVFP=13200254086.6,
                NEVT_UL17=31228727737.2,
                NEVT_UL18=43349104310.5,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_hdampUP_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_hdampUP_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_hdampUP_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_hdampUP_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_CR1" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1119057340.27,
                NEVT_UL16postVFP=1312806896.64,
                NEVT_UL17=3087505516.57,
                NEVT_UL18=4299241561.71,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_CP5CR1_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_CP5CR1_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_CP5CR1_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TTTo2L2Nu_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_CP5CR1_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TTTo2L2Nu_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_CR1" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=16921209832.3,
                NEVT_UL16postVFP=18364178884.6,
                NEVT_UL17=40926808850.1,
                NEVT_UL18=59945066416.3,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_CP5CR1_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_CP5CR1_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_CP5CR1_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TTToSemiLeptonic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_CP5CR1_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TTToSemiLeptonic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TTToHadronic_CR1" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=12368881966.2,
                NEVT_UL16postVFP=13839889370.4,
                NEVT_UL17=30702921824.0,
                NEVT_UL18=43873260589.6,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_CP5CR1_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_CP5CR1_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_CP5CR1_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TTToHadronic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_CP5CR1_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TTToHadronic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_CR2" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1209778279.97,
                NEVT_UL16postVFP=1299119114.88,
                NEVT_UL17=3072219680.55,
                NEVT_UL18=4131775059.13,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_CP5CR2_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_CP5CR2_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_CP5CR2_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TTTo2L2Nu_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_CP5CR2_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_CR2" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=12530751795.3,
                NEVT_UL16postVFP=13150665656.7,
                NEVT_UL17=31341511293.6,
                NEVT_UL18=40134252735.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_CP5CR2_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_CP5CR2_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_CP5CR2_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TTToSemiLeptonic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_CP5CR2_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TTToSemiLeptonic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TTToHadronic_CR2" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=16948358553.1,
                NEVT_UL16postVFP=18864528471.5,
                NEVT_UL17=42705231787.4,
                NEVT_UL18=58707487112.6,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_CP5CR2_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_CP5CR2_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_CP5CR2_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TTToHadronic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_CP5CR2_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TTToHadronic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_erdON" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1168614174.19,
                NEVT_UL16postVFP=1262397311.77,
                NEVT_UL17=3082948641.33,
                NEVT_UL18=4324824676.27,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_CP5_erdON_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_CP5_erdON_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_CP5_erdON_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_CP5_erdON_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_erdON" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=16726593539.7,
                NEVT_UL16postVFP=16421547047.6,
                NEVT_UL17=38348035890.5,
                NEVT_UL18=59635849358.2,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_CP5_erdON_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_CP5_erdON_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_CP5_erdON_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_CP5_erdON_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToHadronic_erdON" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=11878757774.9,
                NEVT_UL16postVFP=11754179667.0,
                NEVT_UL17=28336527346.1,
                NEVT_UL18=43789654069.6,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_CP5_erdON_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_CP5_erdON_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_CP5_erdON_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_CP5_erdON_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_TuneCP5down" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1224164110.83,
                NEVT_UL16postVFP=1324614555.14,
                NEVT_UL17=2835763505.61,
                NEVT_UL18=4320812892.96,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_CP5down_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_CP5down_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_CP5down_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_CP5down_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_TuneCP5down" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=16776724056.4,
                NEVT_UL16postVFP=5845786351.82,
                NEVT_UL17=40047980719.4,
                NEVT_UL18=57198370847.7,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_CP5down_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_CP5down_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_CP5down_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_CP5down_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToHadronic_TuneCP5down" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=11934112109.7,
                NEVT_UL16postVFP=12201812600.9,
                NEVT_UL17=30498725616.3,
                NEVT_UL18=43890851036.3,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_CP5down_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_CP5down_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_CP5down_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_CP5down_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_TuneCP5up" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=748555526.718,
                NEVT_UL16postVFP=1302743997.7,
                NEVT_UL17=3089320938.48,
                NEVT_UL18=4166003310.52,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_CP5up_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_CP5up_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_CP5up_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_CP5up_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_TuneCP5up" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=14002115305.3,
                NEVT_UL16postVFP=17450463976.7,
                NEVT_UL17=41805223200.5,
                NEVT_UL18=60018531229.9,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_CP5up_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_CP5up_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_CP5up_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_CP5up_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToHadronic_TuneCP5up" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=9061754000.63,
                NEVT_UL16postVFP=13137584217.8,
                NEVT_UL17=30221996666.9,
                NEVT_UL18=43103983319.8,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_CP5up_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_CP5up_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_CP5up_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_CP5up_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_mtop171p5" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1247209911.7,
                NEVT_UL16postVFP=1275439759.52,
                NEVT_UL17=3068554700.44,
                NEVT_UL18=4430081553.62,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_mtop171p5_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_mtop171p5_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_mtop171p5_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_mtop171p5_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_mtop171p5" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=16496523942.8,
                NEVT_UL16postVFP=19430417371.5,
                NEVT_UL17=41027336990.9,
                NEVT_UL18=60382346845.6,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_mtop171p5_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_mtop171p5_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_mtop171p5_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToSemiLeptonic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_mtop171p5_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToSemiLeptonic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToHadronic_mtop171p5" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=10400225567.8,
                NEVT_UL16postVFP=13887377089.6,
                NEVT_UL17=31554168422.7,
                NEVT_UL18=43655351059.1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_mtop171p5_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_mtop171p5_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_mtop171p5_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToHadronic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_mtop171p5_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToHadronic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_mtop173p5" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1182257745.72,
                NEVT_UL16postVFP=1310088463.23,
                NEVT_UL17=2999283697.73,
                NEVT_UL18=4209786948.32,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_mtop173p5_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_mtop173p5_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_mtop173p5_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTTo2L2Nu_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_mtop173p5_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_mtop173p5" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=15939101868.2,
                NEVT_UL16postVFP=18394065573.8,
                NEVT_UL17=40668584045.2,
                NEVT_UL18=57813777930.1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_mtop173p5_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_mtop173p5_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_mtop173p5_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToSemiLeptonic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_mtop173p5_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToSemiLeptonic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToHadronic_mtop173p5" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=11960383001.0,
                NEVT_UL16postVFP=12063746928.3,
                NEVT_UL17=27837363220.7,
                NEVT_UL18=42651494870.7,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_mtop173p5_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_mtop173p5_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_mtop173p5_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToHadronic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_mtop173p5_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToHadronic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TT_Mtt-700to1000" : {
            "CrossSection" : XSValues(XSec_13TeV=6.472e+01, XSecSource_13TeV="GenXSecAnalyzer (NLO) run on UL17 (other years and also XSDB give similar results); accuracy: NLO"),
            "Correction" : CorrValues(Corr_13TeV=1.20965315498, CorrSource_13TeV="Scales to NNLO+NNLL x-section of TTTo2L2Nu/TTToSemiLeptonic/TTToHadronic. This correction factor should always be used"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=15678094533.0,
                NEVT_UL16postVFP=22646592839.0,
                NEVT_UL17=24182708233.9,
                NEVT_UL18=20714868719.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TT_Mtt-700to1000_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TT_Mtt-700to1000_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TT_Mtt-700to1000_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TT_Mtt-700to1000_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TT_Mtt-1000toInf" : {
            "CrossSection" : XSValues(XSec_13TeV=1.644e+01, XSecSource_13TeV="GenXSecAnalyzer (NLO) run on UL17 (other years and also XSDB give similar results); accuracy: NLO"),
            "Correction" : CorrValues(Corr_13TeV=1.21062828535, CorrSource_13TeV="Scales to NNLO+NNLL x-section of TTTo2L2Nu/TTToSemiLeptonic/TTToHadronic. This correction factor should always be used"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=15221498037.0,
                NEVT_UL16postVFP=15749293533.9,
                NEVT_UL17=14803424869.0,
                NEVT_UL18=15475388953.2,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TT_Mtt-1000toInf_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TT_Mtt-1000toInf_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TT_Mtt-1000toInf_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TT_Mtt-1000toInf_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTZToLLNuNu_M-10_TuneCP5" : {
            "CrossSection" : XSValues(XSec_13TeV=0.86, XSecSource_13TeV="Phys. Rev. Lett. 113 (2014) 212001 [doi:10.1103/PhysRevLett.113.212001]"),
            "BranchingRatio" : BRValues(BRat_13TeV=3*(0.0337+0.0667), BRatSource_13TeV="P.A. Zyla et al. (Particle Data Group), Prog. Theor. Exp. Phys. 2020, 083C01 (2020) and 2021 update"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1415599.92644,
                NEVT_UL16postVFP=1477923.21991,
                NEVT_UL17=3464156.46185,
                NEVT_UL18=4782962.66323,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTZToLLNuNu_M-10_CP5_amcatnlo-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTZToLLNuNu_M-10_CP5_amcatnlo-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTZToLLNuNu_M-10_CP5_amcatnlo-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTZToLLNuNu_M-10_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TTZToQQ_TuneCP5" : {
            "CrossSection" : XSValues(XSec_13TeV=0.86, XSecSource_13TeV="Phys. Rev. Lett. 113 (2014) 212001 [doi:10.1103/PhysRevLett.113.212001]"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.69911, BRatSource_13TeV="P.A. Zyla et al. (Particle Data Group), Prog. Theor. Exp. Phys. 2020, 083C01 (2020) and 2021 update"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=3206904.47682,
                NEVT_UL16postVFP=2758738.86304,
                NEVT_UL17=7143394.7065,
                NEVT_UL18=10134247.2843,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTZToQQ_CP5_amcatnlo-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTZToQQ_CP5_amcatnlo-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTZToQQ_CP5_amcatnlo-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTZToQQ_CP5_amcatnlo-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTWJetsToLNu_TuneCP5" : {
            "CrossSection" : XSValues(XSec_13TeV=0.55, XSecSource_13TeV="Phys. Rev. Lett. 113 (2014) 212001 [doi:10.1103/PhysRevLett.113.212001]"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.3259, BRatSource_13TeV="P.A. Zyla et al. (Particle Data Group), Prog. Theor. Exp. Phys. 2020, 083C01 (2020) and 2021 update"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=953960.422456,
                NEVT_UL16postVFP=1113150.39282,
                NEVT_UL17=2500272.10687,
                NEVT_UL18=3525043.5175,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTWJetsToLNu_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTWJetsToLNu_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTWJetsToLNu_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTWJetsToLNu_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTWJetsToQQ_TuneCP5" : {
            "CrossSection" : XSValues(XSec_13TeV=0.55, XSecSource_13TeV="Phys. Rev. Lett. 113 (2014) 212001 [doi:10.1103/PhysRevLett.113.212001]"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.6741, BRatSource_13TeV="P.A. Zyla et al. (Particle Data Group), Prog. Theor. Exp. Phys. 2020, 083C01 (2020) and 2021 update"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=184218.52966,
                NEVT_UL16postVFP=209107.004822,
                NEVT_UL17=444333.97475,
                NEVT_UL18=656374.27724,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTWJetsToQQ_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTWJetsToQQ_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTWJetsToQQ_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTWJetsToQQ_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ST_tW_top_5f_inclusiveDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=74624668.1199,
                NEVT_UL16postVFP=80821434.5381,
                NEVT_UL17=183284892.424,
                NEVT_UL18=258137404.807,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_top_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_top_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_top_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_top_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_antitop_5f_inclusiveDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=74766341.164,
                NEVT_UL16postVFP=83024147.0626,
                NEVT_UL17=184446306.91,
                NEVT_UL18=251902154.492,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_antitop_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_antitop_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_antitop_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_antitop_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_top_5f_NoFullyHadronicDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=106897142.991,
                NEVT_UL16postVFP=109290196.259,
                NEVT_UL17=276021555.615,
                NEVT_UL18=365675749.158,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_top_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_top_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_top_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_top_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ST_tW_antitop_5f_NoFullyHadronicDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=103260113.113,
                NEVT_UL16postVFP=118799348.667,
                NEVT_UL17=274168362.629,
                NEVT_UL18=358102373.387,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_antitop_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_antitop_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_antitop_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_antitop_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ST_tW_top_5f_NoFullyHadronicDecays_PDFWeights" : {
            "CrossSection" : XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=117273917.767,
                NEVT_UL16postVFP=112600644.777,
                NEVT_UL17=270017136.126,
                NEVT_UL18=401653774.864,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_top_5f_NoFullyHadronicDecays_CP5_PDFWeights-powheg-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV_PDFWeights-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_top_5f_NoFullyHadronicDecays_CP5_PDFWeights-powheg-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV_PDFWeights-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_top_5f_NoFullyHadronicDecays_CP5_PDFWeights-powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV_PDFWeights-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_top_5f_NoFullyHadronicDecays_CP5_PDFWeights-powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV_PDFWeights-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_antitop_5f_NoFullyHadronicDecays_PDFWeights" : {
            "CrossSection" : XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=116845339.127,
                NEVT_UL16postVFP=130104849.514,
                NEVT_UL17=270692843.383,
                NEVT_UL18=382916540.679,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_antitop_5f_NoFullyHadronicDecays_CP5_PDFWeights-powheg-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV_PDFWeights-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_antitop_5f_NoFullyHadronicDecays_CP5_PDFWeights-powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV_PDFWeights-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_antitop_5f_NoFullyHadronicDecays_CP5_PDFWeights-powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV_PDFWeights-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_antitop_5f_NoFullyHadronicDecays_CP5_PDFWeights-powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV_PDFWeights-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_top_5f_DS_NoFullyHadronicDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=43834506.9753,
                NEVT_UL16postVFP=47205739.4822,
                NEVT_UL17=102955021.229,
                NEVT_UL18=151137516.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_top_5f_DS_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ST_tW_top_5f_DS_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_top_5f_DS_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ST_tW_top_5f_DS_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_top_5f_DS_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ST_tW_top_5f_DS_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_top_5f_DS_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_top_5f_DS_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_antitop_5f_DS_NoFullyHadronicDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=47163863.9087,
                NEVT_UL16postVFP=49448706.2988,
                NEVT_UL17=112417073.827,
                NEVT_UL18=156305198.741,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_antitop_5f_DS_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ST_tW_antitop_5f_DS_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_antitop_5f_DS_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ST_tW_antitop_5f_DS_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_antitop_5f_DS_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_tW_antitop_5f_DS_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_antitop_5f_DS_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_antitop_5f_DS_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_top_5f_hdampdown_NoFullyHadronicDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=45069892.8416,
                NEVT_UL16postVFP=46832452.8296,
                NEVT_UL17=112933709.709,
                NEVT_UL18=152124659.855,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_top_5f_hdampdown_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ST_tW_top_5f_hdampdown_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_top_5f_hdampdown_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ST_tW_top_5f_hdampdown_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_top_5f_hdampdown_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ST_tW_top_5f_hdampdown_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_top_5f_hdampdown_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_top_5f_hdampdown_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_antitop_5f_hdampdown_NoFullyHadronicDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=44858915.6433,
                NEVT_UL16postVFP=50345517.9472,
                NEVT_UL17=108841119.452,
                NEVT_UL18=152035456.84,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_antitop_5f_hdampdown_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ST_tW_antitop_5f_hdampdown_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_antitop_5f_hdampdown_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ST_tW_antitop_5f_hdampdown_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_antitop_5f_hdampdown_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ST_tW_antitop_5f_hdampdown_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_antitop_5f_hdampdown_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_antitop_5f_hdampdown_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_top_5f_hdampup_NoFullyHadronicDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=44499753.1117,
                NEVT_UL16postVFP=48701601.1062,
                NEVT_UL17=111075592.757,
                NEVT_UL18=148292224.868,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_top_5f_hdampup_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ST_tW_top_5f_hdampup_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_top_5f_hdampup_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ST_tW_top_5f_hdampup_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_top_5f_hdampup_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ST_tW_top_5f_hdampup_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_top_5f_hdampup_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_top_5f_hdampup_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_antitop_5f_hdampup_NoFullyHadronicDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=44764839.0862,
                NEVT_UL16postVFP=48895564.3112,
                NEVT_UL17=106200092.194,
                NEVT_UL18=150756696.573,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_antitop_5f_hdampup_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ST_tW_antitop_5f_hdampup_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_antitop_5f_hdampup_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ST_tW_antitop_5f_hdampup_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_antitop_5f_hdampup_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ST_tW_antitop_5f_hdampup_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_antitop_5f_hdampup_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_antitop_5f_hdampup_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_t-channel_top_4f_InclusiveDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=136.02, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=5948135154.41,
                NEVT_UL16postVFP=6703801970.36,
                NEVT_UL17=13808000646.6,
                NEVT_UL18=19000619397.2,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_t-channel_top_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL16APV_v3.xml", XmlSource_UL16preVFP="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_t-channel_top_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL16_v3.xml", XmlSource_UL16postVFP="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v3/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_t-channel_top_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_t-channel_top_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ST_t-channel_antitop_4f_InclusiveDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=80.95, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1983864432.65,
                NEVT_UL16postVFP=1957283183.22,
                NEVT_UL17=4471058679.95,
                NEVT_UL18=6128118195.12,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_t-channel_antitop_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL16APV_v3.xml", XmlSource_UL16preVFP="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_t-channel_antitop_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL16_v3.xml", XmlSource_UL16postVFP="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v3/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_t-channel_antitop_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_t-channel_antitop_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ST_s-channel_4f_leptonDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=10.32, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.326, BRatSource_13TeV="https://pdg.lbl.gov/2021/listings/rpp2021-list-w-boson.pdf (page 5, W->lnu times 3, rounded)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=19592486.3309,
                NEVT_UL16postVFP=19433132.1012,
                NEVT_UL17=49292566.8068,
                NEVT_UL18=68767081.0067,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_s-channel_4f_leptonDecays_CP5_amcatnlo-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_s-channel_4f_leptonDecays_CP5_amcatnlo-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_s-channel_4f_leptonDecays_CP5_amcatnlo-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_s-channel_4f_leptonDecays_CP5_amcatnlo-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WW" : {
            "CrossSection" : XSValues(
                XSec_13TeV=75.91, XSecSource_13TeV="GenXSecAnalyzer (LO) for UL 16",
                XSec_UL16preVFP=75.96,
                XSec_UL16postVFP=75.91,
                XSec_UL17=75.92,
                XSec_UL18=75.91,
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=15859130.7832,
                NEVT_UL16postVFP=15821137.255,
                NEVT_UL17=15634116.2001,
                NEVT_UL18=15679122.7141,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WW_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WW_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WW_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WW_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WZ" : {
            "CrossSection" : XSValues(
                XSec_13TeV=27.56, XSecSource_13TeV="GenXSecAnalyzer (LO) for UL 16",
                XSec_UL16preVFP=27.55,
                XSec_UL16postVFP=27.56,
                XSec_UL17=27.54,
                XSec_UL18=27.58,
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=7934000.0,
                NEVT_UL16postVFP=7584000.0,
                NEVT_UL17=7889000.0,
                NEVT_UL18=7940000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WZ_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WZ_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WZ_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WZ_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZZ" : {
            "CrossSection" : XSValues(
                XSec_13TeV=12.13, XSecSource_13TeV="GenXSecAnalyzer (LO) for UL 16",
                XSec_UL16preVFP=12.12,
                XSec_UL16postVFP=12.13,
                XSec_UL17=12.14,
                XSec_UL18=12.13,
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1282000.0,
                NEVT_UL16postVFP=1151000.0,
                NEVT_UL17=2706000.0,
                NEVT_UL18=3526000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZZ_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZZ_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZZ_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZZ_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-70to100" : {
            "CrossSection" : XSValues(XSec_13TeV=140.1, XSecSource_13TeV="GenXSecAnalyzer"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=6724232,
                NEVT_UL16postVFP=5893910,
                NEVT_UL17=12205958,
                NEVT_UL18=17004433,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-70to100_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-70to100_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-70to100_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-70to100_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-100to200" : {
            "CrossSection" : XSValues(XSec_13TeV=140.2, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.2245, kFacSource_UL16preVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL16postVFP=1.2245, kFacSource_UL16postVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL17=1.1374, kFacSource_UL17="XSDB NNLO/LO=6077.22/5343",
                kFac_UL18=1.1421, kFacSource_UL18="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                CorrSource_UL17="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                CorrSource_UL18="Same as 2017",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=9570042,
                NEVT_UL16postVFP=8316351,
                NEVT_UL17=18955253,
                NEVT_UL18=26202328,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-100to200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-100to200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-100to200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-100to200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-200to400" : {
            "CrossSection" : XSValues(XSec_13TeV=38.399, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.2245, kFacSource_UL16preVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL16postVFP=1.2245, kFacSource_UL16postVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL17=1.1374, kFacSource_UL17="XSDB NNLO/LO=6077.22/5343",
                kFac_UL18=1.1421, kFacSource_UL18="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_UL17=0.999, CorrSource_UL17="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_UL18=0.999, CorrSource_UL18="Same as 2017",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=5862631,
                NEVT_UL16postVFP=5653782,
                NEVT_UL17=12513057,
                NEVT_UL18=18455718,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-200to400_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-200to400_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-200to400_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-200to400_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-400to600" : {
            "CrossSection" : XSValues(XSec_13TeV=5.21278, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.2245, kFacSource_UL16preVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL16postVFP=1.2245, kFacSource_UL16postVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL17=1.1374, kFacSource_UL17="XSDB NNLO/LO=6077.22/5343",
                kFac_UL18=1.1421, kFacSource_UL18="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_UL17=0.990, CorrSource_UL17="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_UL18=0.990, CorrSource_UL18="Same as 2017",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2716892,
                NEVT_UL16postVFP=2491416,
                NEVT_UL17=5543804,
                NEVT_UL18=8908406,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-400to600_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-400to600_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-400to600_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-400to600_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-600to800" : {
            "CrossSection" : XSValues(XSec_13TeV=1.26567, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.2245, kFacSource_UL16preVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL16postVFP=1.2245, kFacSource_UL16postVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL17=1.1374, kFacSource_UL17="XSDB NNLO/LO=6077.22/5343",
                kFac_UL18=1.1421, kFacSource_UL18="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_UL17=0.975, CorrSource_UL17="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_UL18=0.975, CorrSource_UL18="Same as 2017",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2681650,
                NEVT_UL16postVFP=2299853,
                NEVT_UL17=5278417,
                NEVT_UL18=7035971,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-600to800_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-600to800_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-600to800_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-600to800_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-800to1200" : {
            "CrossSection" : XSValues(XSec_13TeV=0.5684304, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.2245, kFacSource_UL16preVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL16postVFP=1.2245, kFacSource_UL16postVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL17=1.1374, kFacSource_UL17="XSDB NNLO/LO=6077.22/5343",
                kFac_UL18=1.1421, kFacSource_UL18="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_UL17=0.907, CorrSource_UL17="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_UL18=0.907, CorrSource_UL18="Same as 2017",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2411091,
                NEVT_UL16postVFP=2393976,
                NEVT_UL17=4506887,
                NEVT_UL18=6678036,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-800to1200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-800to1200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-800to1200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-800to1200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-1200to2500" : {
            "CrossSection" : XSValues(XSec_13TeV=0.1331514, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.2245, kFacSource_UL16preVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL16postVFP=1.2245, kFacSource_UL16postVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL17=1.1374, kFacSource_UL17="XSDB NNLO/LO=6077.22/5343",
                kFac_UL18=1.1421, kFacSource_UL18="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_UL17=0.833, CorrSource_UL17="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_UL18=0.833, CorrSource_UL18="Same as 2017",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2189664,
                NEVT_UL16postVFP=1970857,
                NEVT_UL17=4802716,
                NEVT_UL18=6166852,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-1200to2500_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-1200to2500_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-1200to2500_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-1200to2500_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-2500toInf" : {
            "CrossSection" : XSValues(XSec_13TeV=0.00297803565, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.2245, kFacSource_UL16preVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL16postVFP=1.2245, kFacSource_UL16postVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL17=1.1374, kFacSource_UL17="XSDB NNLO/LO=6077.22/5343",
                kFac_UL18=1.1421, kFacSource_UL18="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_UL17=1.015, CorrSource_UL17="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_UL18=1.015, CorrSource_UL18="Same as 2017",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=721404,
                NEVT_UL16postVFP=696811,
                NEVT_UL17=1480047,
                NEVT_UL18=1978203,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-2500toInf_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-2500toInf_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-2500toInf_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-2500toInf_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-70to100" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1271, XSecSource_13TeV="GenXSecAnalyzer on UL16postVFP",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=16931765.0,
                NEVT_UL16postVFP=19439931.0,
                NEVT_UL17=44736228.0,
                NEVT_UL18=66569448.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-70To100_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-70To100_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-70To100_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-70To100_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-100to200" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1253, XSecSource_13TeV="GenXSecAnalyzer on UL16preVFP",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=21734530.0,
                NEVT_UL16postVFP=19753958.0,
                NEVT_UL17=47424468.0,
                NEVT_UL18=51541593.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-200to400" : {
            "CrossSection" : XSValues(
                XSec_13TeV=335.9, XSecSource_13TeV="GenXSecAnalyzer on UL16preVFP",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=17870845.0,
                NEVT_UL16postVFP=15067621.0,
                NEVT_UL17=42602407.0,
                NEVT_UL18=58331446.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-400to600" : {
            "CrossSection" : XSValues(
                XSec_13TeV=45.21, XSecSource_13TeV="GenXSecAnalyzer on UL16preVFP",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2467498.0,
                NEVT_UL16postVFP=2115509.0,
                NEVT_UL17=5468473.0,
                NEVT_UL18=7444030.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-600to800" : {
            "CrossSection" : XSValues(
                XSec_13TeV=10.99, XSecSource_13TeV="GenXSecAnalyzer on UL16preVFP",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2344130.0,
                NEVT_UL16postVFP=2251807.0,
                NEVT_UL17=5545298.0,
                NEVT_UL18=7718765.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-800to1200" : {
            "CrossSection" : XSValues(
                XSec_13TeV=4.936, XSecSource_13TeV="GenXSecAnalyzer on UL16preVFP",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2510487.0,
                NEVT_UL16postVFP=2132228.0,
                NEVT_UL17=5088483.0,
                NEVT_UL18=7306187.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-1200to2500" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1.156, XSecSource_13TeV="GenXSecAnalyzer on UL16preVFP",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2119975.0,
                NEVT_UL16postVFP=2090561.0,
                NEVT_UL17=4955636.0,
                NEVT_UL18=6481518.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-2500toInf" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.02623, XSecSource_13TeV="GenXSecAnalyzer on UL16preVFP",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=808649.0,
                NEVT_UL16postVFP=709514.0,
                NEVT_UL17=1185699.0,
                NEVT_UL18=2097648.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZJetsToNuNu_HT-100to200" : {
            "CrossSection" : XSValues(XSec_13TeV=266.6, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.23, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.23, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.23, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.23, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=7784090,
                NEVT_UL16postVFP=7083216,
                NEVT_UL17=18983897,
                NEVT_UL18=28876062,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToNuNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToNuNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToNuNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZJetsToNuNu_HT-200to400" : {
            "CrossSection" : XSValues(XSec_13TeV=73.08, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.23, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.23, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.23, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.23, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=7531529,
                NEVT_UL16postVFP=6814106,
                NEVT_UL17=17349597,
                NEVT_UL18=22749608,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToNuNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToNuNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToNuNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZJetsToNuNu_HT-400to600" : {
            "CrossSection" : XSValues(XSec_13TeV=9.932, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.23, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.23, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.23, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.23, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=6632524,
                NEVT_UL16postVFP=6114046,
                NEVT_UL17=13963690,
                NEVT_UL18=19810491,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToNuNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToNuNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToNuNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZJetsToNuNu_HT-600to800" : {
            "CrossSection" : XSValues(XSec_13TeV=2.407, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.23, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.23, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.23, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.23, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2030858,
                NEVT_UL16postVFP=1881671,
                NEVT_UL17=4418971,
                NEVT_UL18=5968910,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToNuNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToNuNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToNuNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZJetsToNuNu_HT-800to1200" : {
            "CrossSection" : XSValues(XSec_13TeV=1.078, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.23, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.23, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.23, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.23, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=703970,
                NEVT_UL16postVFP=633500,
                NEVT_UL17=1513585,
                NEVT_UL18=2129122,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToNuNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToNuNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToNuNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZJetsToNuNu_HT-1200to2500" : {
            "CrossSection" : XSValues(XSec_13TeV=0.2514, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.23, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.23, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.23, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.23, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=136393,
                NEVT_UL16postVFP=115609,
                NEVT_UL17=267125,
                NEVT_UL18=381695,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToNuNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToNuNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToNuNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZJetsToNuNu_HT-2500toInf" : {
            "CrossSection" : XSValues(XSec_13TeV=0.005569, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.23, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.23, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.23, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.23, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=111838,
                NEVT_UL16postVFP=110461,
                NEVT_UL17=176201,
                NEVT_UL18=268224,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToNuNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToNuNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToNuNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WJetsToQQ_HT200to400" : {
            "CrossSection" : XSValues(
                XSec_13TeV=2565.301991, XSecSource_13TeV="GenXSecAnalyzer run on UL17"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=8000572.0,
                NEVT_UL16postVFP=7065076.0,
                NEVT_UL17=15968057.0,
                NEVT_UL18=14310025.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "WJetsToQQ_HT400to600" : {
            "CrossSection" : XSValues(
                XSec_13TeV=276.629780, XSecSource_13TeV="GenXSecAnalyzer run on UL17"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=5144427.0,
                NEVT_UL16postVFP=4455853.0,
                NEVT_UL17=9927793.0,
                NEVT_UL18=9335298.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "WJetsToQQ_HT600to800" : {
            "CrossSection" : XSValues(
                XSec_13TeV=59.078057, XSecSource_13TeV="GenXSecAnalyzer run on UL17"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=7644050.0,
                NEVT_UL16postVFP=6793578.0,
                NEVT_UL17=14667933.0,
                NEVT_UL18=13633226.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "WJetsToQQ_HT800toInf" : {
            "CrossSection" : XSValues(
                XSec_13TeV=28.761363, XSecSource_13TeV="GenXSecAnalyzer run on UL17"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=7606882.0,
                NEVT_UL16postVFP=6769101.0,
                NEVT_UL17=14722417.0,
                NEVT_UL18=13557328.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZJetsToQQ_HT200to400" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1010.200257, XSecSource_13TeV="GenXSecAnalyzer run on UL18"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=8753905.0,
                NEVT_UL16postVFP=7285673.0,
                NEVT_UL17=-1,
                NEVT_UL18=14738284.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZJetsToQQ_HT400to600" : {
            "CrossSection" : XSValues(
                XSec_13TeV=114.207953, XSecSource_13TeV="GenXSecAnalyzer run on UL17"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=7709128.0,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=14884962.0,
                NEVT_UL18=13930474.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZJetsToQQ_HT600to800" : {
            "CrossSection" : XSValues(
                XSec_13TeV=25.348623, XSecSource_13TeV="GenXSecAnalyzer run on UL17"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=6116617.0,
                NEVT_UL16postVFP=5500386.0,
                NEVT_UL17=11702567.0,
                NEVT_UL18=12029507.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZJetsToQQ_HT800toInf" : {
            "CrossSection" : XSValues(
                XSec_13TeV=12.914550, XSecSource_13TeV="GenXSecAnalyzer run on UL17"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=3726992.0,
                NEVT_UL16postVFP=4388402.0,
                NEVT_UL17=9384525.0,
                NEVT_UL18=9681521.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-15To20_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=2.804e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=4750325.22185,
                NEVT_UL16postVFP=4530702.5042,
                NEVT_UL17=9021334.99026,
                NEVT_UL18=9354640.99415,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-15To20_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-15To20_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-15To20_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-15To20_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-20To30_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=2.525e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=31927152.3197,
                NEVT_UL16postVFP=30854055.9904,
                NEVT_UL17=64635562.4735,
                NEVT_UL18=60641468.4388,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-20To30_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-20To30_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-20To30_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-20To30_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-30To50_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=1.366e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=28664840.0,
                NEVT_UL16postVFP=35474172.0,
                NEVT_UL17=58749714.0,
                NEVT_UL18=58627984.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-30To50_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-30To50_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-30To50_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-30To50_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-50To80_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=3.777e+05, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=19724658.0,
                NEVT_UL16postVFP=21491325.0,
                NEVT_UL17=40377957.0,
                NEVT_UL18=40022458.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-50To80_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-50To80_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-50To80_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-50To80_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-80To120_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=8.862e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=21981180.5514,
                NEVT_UL16postVFP=22008310.1674,
                NEVT_UL17=45986550.6848,
                NEVT_UL18=45571985.8354,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-80To120_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-80To120_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-80To120_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-80To120_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-120To170_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=2.118e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=19137392.9596,
                NEVT_UL16postVFP=19773251.4183,
                NEVT_UL17=39395152.0766,
                NEVT_UL18=39115540.5162,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-120To170_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-120To170_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-120To170_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-120To170_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-170To300_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=7.015e+03, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=37080544.0,
                NEVT_UL16postVFP=34290911.0,
                NEVT_UL17=73071987.0,
                NEVT_UL18=71926577.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-170To300_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-170To300_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-170To300_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-170To300_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-300To470_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=6.201e+02, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=28238400.9104,
                NEVT_UL16postVFP=29908658.4042,
                NEVT_UL17=58692920.2804,
                NEVT_UL18=58949766.2915,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-300To470_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-300To470_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-300To470_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-300To470_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-470To600_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=5.908e+01, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=19695374.4020,
                NEVT_UL16postVFP=19771535.0062,
                NEVT_UL17=39491905.0538,
                NEVT_UL18=38453444.9014,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-470To600_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-470To600_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-470To600_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-470To600_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-600To800_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=1.825e+01, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=19598815.552,
                NEVT_UL16postVFP=18763139.5706,
                NEVT_UL17=39321941.1416,
                NEVT_UL18=38412789.1215,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-600To800_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-600To800_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-600To800_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-600To800_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-800To1000_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=3.276e+00, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=39092964.0,
                NEVT_UL16postVFP=38921526.0,
                NEVT_UL17=78215559.0,
                NEVT_UL18=78942993.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-800To1000_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-800To1000_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-800To1000_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-800To1000_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-1000_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=1.077e+00, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=13660999.0,
                NEVT_UL16postVFP=14243204.0,
                NEVT_UL17=27478273.0,
                NEVT_UL18=27427130.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-1000_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-1000_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-1000_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-1000_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-15to20_EMEnriched" : {
            "CrossSection" : XSValues(XSec_13TeV=1.322e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=4026788.18611,
                NEVT_UL17=7967858.63254,
                NEVT_UL18=7900796.928,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-15to20_EMEnriched_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-15to20_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-15to20_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-20to30_EMEnriched" : {
            "CrossSection" : XSValues(XSec_13TeV=4.915e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=7134791.3549,
                NEVT_UL17=14166154.329,
                NEVT_UL18=14328852.5239,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-20to30_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-20to30_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-20to30_EMEnriched_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_Pt-30to50_EMEnriched" : {
            "CrossSection" : XSValues(XSec_13TeV=6.418e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=4361931.0,
                NEVT_UL16postVFP=4351014.0,
                NEVT_UL17=8784542.0,
                NEVT_UL18=8574589.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-30to50_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-30to50_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-30to50_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-30to50_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-50to80_EMEnriched" : {
            "CrossSection" : XSValues(XSec_13TeV=1.987e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=5440758.0,
                NEVT_UL16postVFP=5443934.0,
                NEVT_UL17=10210400.0,
                NEVT_UL18=10524400.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-50to80_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-50to80_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-50to80_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-50to80_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-80to120_EMEnriched" : {
            "CrossSection" : XSValues(XSec_13TeV=3.671e+05, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=4848176.90015,
                NEVT_UL16postVFP=4805600.8317,
                NEVT_UL17=9617412.94144,
                NEVT_UL18=9469962.10221,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-80to120_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-80to120_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-80to120_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-80to120_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-120to170_EMEnriched" : {
            "CrossSection" : XSValues(XSec_13TeV=6.661e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=4852628.34648,
                NEVT_UL16postVFP=5007404.35617,
                NEVT_UL17=9904361.63759,
                NEVT_UL18=9678015.18575,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-120to170_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-120to170_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-120to170_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-120to170_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-170to300_EMEnriched" : {
            "CrossSection" : XSValues(XSec_13TeV=1.654e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1855461.0,
                NEVT_UL16postVFP=1861129.0,
                NEVT_UL17=3678200.0,
                NEVT_UL18=3714642.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-170to300_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-170to300_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-170to300_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-170to300_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-300toInf_EMEnriched" : {
            "CrossSection" : XSValues(XSec_13TeV=1.100e+03, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1142775.0,
                NEVT_UL16postVFP=1138742.0,
                NEVT_UL17=2214934.0,
                NEVT_UL18=2215994.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-300toInf_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-300toInf_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-300toInf_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-300toInf_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt_15to20_bcToE" : {
            "CrossSection" : XSValues(XSec_13TeV=1.869e+05, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=8337713.15922,
                NEVT_UL17=-1,
                NEVT_UL18=16551388.1334,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_15to20_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_15to20_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_15to20_bcToE_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt_15to20_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt_20to30_bcToE" : {
            "CrossSection" : XSValues(XSec_13TeV=3.055e+05, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=7913585.84161,
                NEVT_UL16postVFP=7308537.32977,
                NEVT_UL17=14171713.7236,
                NEVT_UL18=14061668.0471,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt_20to30_bcToE_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_20to30_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt_20to30_bcToE_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_20to30_bcToE_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt_30to80_bcToE" : {
            "CrossSection" : XSValues(XSec_13TeV=3.612e+05, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=7971435.43066,
                NEVT_UL16postVFP=7718567.59966,
                NEVT_UL17=15246295.0499,
                NEVT_UL18=15366710.0093,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt_30to80_bcToE_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_30to80_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt_30to80_bcToE_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_30to80_bcToE_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt_80to170_bcToE" : {
            "CrossSection" : XSValues(XSec_13TeV=3.376e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=7690702.0,
                NEVT_UL16postVFP=7882938.0,
                NEVT_UL17=15571255.0,
                NEVT_UL18=15186397.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt_80to170_bcToE_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_80to170_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt_80to170_bcToE_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_80to170_bcToE_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt_170to250_bcToE" : {
            "CrossSection" : XSValues(XSec_13TeV=2.127e+03, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=7343309.67453,
                NEVT_UL16postVFP=7864034.40369,
                NEVT_UL17=15503825.881,
                NEVT_UL18=15736781.2064,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt_170to250_bcToE_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_170to250_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt_170to250_bcToE_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_170to250_bcToE_CP5_pythia8_Summer20UL18_v3.xml", XmlSource_UL18="/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3/MINIAODSIM",
            ),
        },

        "QCD_Pt_250toInf_bcToE" : {
            "CrossSection" : XSValues(XSec_13TeV=5.634e+02, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=6856820.0,
                NEVT_UL16postVFP=8152626.0,
                NEVT_UL17=15557421.0,
                NEVT_UL18=15767690.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt_250toInf_bcToE_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_250toInf_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt_250toInf_bcToE_CP5_pythia8_Summer20UL17_v3.xml", XmlSource_UL17="/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v3/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_250toInf_bcToE_CP5_pythia8_Summer20UL18_v3.xml", XmlSource_UL18="/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3/MINIAODSIM",
            ),
        },

        "QCD_HT50to100" : {
            "CrossSection" : XSValues(
                XSec_13TeV=185900000, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=36599034.0,
                NEVT_UL16postVFP=11197186.0,
                NEVT_UL17=26243010.0,
                NEVT_UL18=38599389.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT50to100_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT50to100_CP5_PSWeights_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT50to100_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT50to100_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT100to200" : {
            "CrossSection" : XSValues(
                XSec_13TeV=23610000, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=67431856.0,
                NEVT_UL16postVFP=73506112.0,
                NEVT_UL17=54760426.0,
                NEVT_UL18=84461486.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT100to200_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT100to200_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT100to200_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT100to200_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT200to300" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1551000, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=18273591.0,
                NEVT_UL16postVFP=43280518.0,
                NEVT_UL17=42714435.0,
                NEVT_UL18=57336623.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT200to300_CP5_PSWeights_madgraph-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT200to300_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT200to300_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT200to300_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT300to500" : {
            "CrossSection" : XSValues(
                XSec_13TeV=324300, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=15341307.0,
                NEVT_UL16postVFP=46863466.0,
                NEVT_UL17=43589739.0,
                NEVT_UL18=61705174.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT300to500_CP5_PSWeights_madgraph-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT300to500_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT300to500_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT300to500_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT500to700" : {
            "CrossSection" : XSValues(
                XSec_13TeV=30340, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=56868784.0,
                NEVT_UL16postVFP=15222746.0,
                NEVT_UL17=36194860.0,
                NEVT_UL18=49184771.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT500to700_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT500to700_CP5_PSWeights_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT500to700_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT500to700_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT700to1000" : {
            "CrossSection" : XSValues(
                XSec_13TeV=6440, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=15808790.0,
                NEVT_UL16postVFP=13905714.0,
                NEVT_UL17=34051754.0,
                NEVT_UL18=48506751.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT700to1000_CP5_PSWeights_madgraph-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT700to1000_CP5_PSWeights_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT700to1000_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT700to1000_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_HT1000to1500" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1118, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=13823774.0,
                NEVT_UL16postVFP=12675816.0,
                NEVT_UL17=10256089.0,
                NEVT_UL18=14527915.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT1000to1500_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT1000to1500_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT1000to1500_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT1000to1500_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT1500to2000" : {
            "CrossSection" : XSValues(
                XSec_13TeV=108, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=10031077.0,
                NEVT_UL16postVFP=9376965.0,
                NEVT_UL17=7701876.0,
                NEVT_UL18=10871473.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT1500to2000_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT1500to2000_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT1500to2000_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT1500to2000_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT2000toInf" : {
            "CrossSection" : XSValues(
                XSec_13TeV=22, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=4996082.0,
                NEVT_UL16postVFP=4867995.0,
                NEVT_UL17=4112573.0,
                NEVT_UL18=5374711.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT2000toInf_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT2000toInf_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT2000toInf_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT2000toInf_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZlepHinc-600": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=100000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-600_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="ZprimeToZHToZlepHinc_narrow_M-600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-600_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-600_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-800": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=100000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-800_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-800_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-800_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-1000": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=44000,
                    NEVT_UL17=100000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-1000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-1000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-1000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-1200": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=45000,
                    NEVT_UL17=100000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-1200_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-1200_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-1200_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-1400": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=45000,
                    NEVT_UL17=100000,
                    NEVT_UL18=97000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-1400_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-1400_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-1400_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-1600": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=93000,
                    NEVT_UL18=98000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-1600_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-1600_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-1600_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-1800": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=97000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-1800_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-1800_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-1800_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-2000": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=100000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-2000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-2000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-2000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-2500": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=100000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-2500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-2500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-2500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-3000": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=99000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-3000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-3000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-3000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-3500": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=97000,
                    NEVT_UL18=97000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-3500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-3500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-3500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-3500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-3500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-3500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-4000": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=45000,
                    NEVT_UL17=97000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-4000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-4000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-4000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-4000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-4000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-4000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-4500": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=100000,
                    NEVT_UL18=97000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-4500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-4500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-4500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-4500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-4500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-4500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-5000": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=44000,
                    NEVT_UL17=100000,
                    NEVT_UL18=97000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-5000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-5000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-5000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-5000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-5000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-5000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-5500": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=44000,
                    NEVT_UL17=97000,
                    NEVT_UL18=94000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-5500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-5500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-5500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-5500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-5500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-5500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-6000": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=45000,
                    NEVT_UL17=100000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-6000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-6000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-6000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-6000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-6000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-6000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-7000": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=100000,
                    NEVT_UL18=97000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-7000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-7000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-7000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-7000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-7000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-7000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-8000": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=97000,
                    NEVT_UL18=97000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-8000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-8000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-8000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-8000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-8000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-8000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

    "ZprimeToZHToZinvHinc-600": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : XMLValues(
            Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-600_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP=    "ZprimeToZHToZinvHinc_narrow_M-600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-600_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-600_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-800": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=91000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-800_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-800_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-800_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-1000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=98000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-1000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-1000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-1000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-1200": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-1200_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-1200_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-1200_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-1400": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=97000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-1400_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-1400_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-1400_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-1600": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-1600_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-1600_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-1600_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-1800": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=96000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-1800_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-1800_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-1800_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-2000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-2000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-2000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-2000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-2500": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=97000,
                NEVT_UL17=100000,
                NEVT_UL18=97000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-2500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-2500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-2500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-3000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=97000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-3000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-3000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-3000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-3500": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=44000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-3500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-3500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-3500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-3500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-3500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-3500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-4000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-4000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-4000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-4000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-4000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-4000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-4000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-4500": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=97000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-4500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-4500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-4500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-4500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-4500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-4500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-5000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-5000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-5000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-5000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-5000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-5000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-5000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-5500": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=97000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-5500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-5500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-5500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-5500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-5500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-5500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-6000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=97000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-6000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-6000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-6000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-6000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-6000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-6000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-7000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=97000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-7000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-7000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-7000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-7000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-7000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-7000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-8000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-8000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-8000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-8000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-8000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-8000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-8000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ALP_ttbar_signal": {
            "CrossSection" : XSValues( XSec_13TeV=7.048, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=5380000,
                NEVT_UL16postVFP=4600000,
                NEVT_UL17=9970000,
                NEVT_UL18=9733000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ALP_ttbar_signal_CP5_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ALP_ttbar_signal_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ALP_ttbar_signal_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ALP_ttbar_signal_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ALP_ttbar_signal_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ALP_ttbar_signal_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ALP_ttbar_signal_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ALP_ttbar_signal_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ALP_ttbar_interference": {
            "CrossSection" : XSValues( XSec_13TeV=-28.248020, XSecSource_13TeV="GenXSecAnalyzer run on UL18"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=5399000,
                NEVT_UL16postVFP=4572000,
                NEVT_UL17=10000000,
                NEVT_UL18=9960000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ALP_ttbar_interference_CP5_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ALP_ttbar_interference_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ALP_ttbar_interference_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ALP_ttbar_interference_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ALP_ttbar_interference_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ALP_ttbar_interference_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ALP_ttbar_interference_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ALP_ttbar_interference_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AZHToLLTT_mA900_mH350": {
            "CrossSection": XSValues( XSec_13TeV=1, XSecSource_13TeV="arbitrary normalization"),
            "NEvents": NEventsValues(
              NEVT_UL17=25000
              ),
            "XMLname": XMLValues(
              Xml_UL17="RunII_106X_v2/BSM/UL17/AZH_UL2017_mA900_mH350_Summer20UL17.xml", XmlSource_UL17="/AZH_UL2017_mA900_mH350_LHEGEN/mihawksw-AZH_UL2017_mA900_mH350_MiniAODv2-3f0b140a720de1c801ff414923884f7b/USER",
              )
            },

        "AZHToLLTT_mA900_mH600": {
            "CrossSection": XSValues( XSec_13TeV=1, XSecSource_13TeV="arbitrary normalization"),
            "NEvents": NEventsValues(
              NEVT_UL17=25000
              ),
            "XMLname": XMLValues(
              Xml_UL17="RunII_106X_v2/BSM/UL17/AZH_UL2017_mA900_mH600_Summer20UL17.xml", XmlSource_UL17="/AZH_UL2017_2HDMtII_NLO_mA900_mH600/mihawksw-AZH_UL2017_2HDMtII_NLO_mA900_mH600_MiniAODv2-3f0b140a720de1c801ff414923884f7b/USER",
              )
            },

        "AZHToLLTT_mA2100_mH1600": {
            "CrossSection": XSValues( XSec_13TeV=1, XSecSource_13TeV="arbitrary normalization"),
            "NEvents": NEventsValues(
              NEVT_UL17=25000
              ),
            "XMLname": XMLValues(
              Xml_UL17="RunII_106X_v2/BSM/UL17/AZH_UL2017_mA2100_mH1600_Summer20UL17.xml", XmlSource_UL17="/AZH_UL2017_mA2100_mH1600_LHEGEN/mihawksw-AZH_UL2017_mA2100_mH1600_MiniAODv2-3f0b140a720de1c801ff414923884f7b/USER",
              )
            },

        "ZprimeToTT_M400_W4" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=569211.0,
                NEVT_UL16postVFP=570127.0,
                NEVT_UL17=201853.0,
                NEVT_UL18=200177.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M400_W4_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M400_W4_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M400_W4_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M400_W4_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M400_W4_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M400_W4_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M400_W4_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M400_W4_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M500_W5" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=537434.0,
                NEVT_UL16postVFP=526301.0,
                NEVT_UL17=188083.0,
                NEVT_UL18=191959.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M500_W5_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M500_W5_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M500_W5_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M500_W5_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M500_W5_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M500_W5_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M500_W5_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M500_W5_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M600_W6" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=509112.0,
                NEVT_UL16postVFP=510991.0,
                NEVT_UL17=198225.0,
                NEVT_UL18=190965.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M600_W6_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M600_W6_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M600_W6_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M600_W6_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M600_W6_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M600_W6_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M600_W6_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M600_W6_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M700_W7" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=468063.0,
                NEVT_UL16postVFP=491452.0,
                NEVT_UL17=200215.0,
                NEVT_UL18=199814.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M700_W7_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M700_W7_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M700_W7_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M700_W7_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M700_W7_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M700_W7_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M700_W7_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M700_W7_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M800_W8" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=425095.0,
                NEVT_UL16postVFP=474239.0,
                NEVT_UL17=193169.0,
                NEVT_UL18=191956.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M800_W8_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M800_W8_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M800_W8_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M800_W8_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M800_W8_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M800_W8_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M800_W8_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M800_W8_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M900_W9" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=463051.0,
                NEVT_UL16postVFP=461916.0,
                NEVT_UL17=199844.0,
                NEVT_UL18=197077.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M900_W9_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M900_W9_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M900_W9_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M900_W9_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M900_W9_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M900_W9_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M900_W9_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M900_W9_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M1000_W10" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=452264.0,
                NEVT_UL16postVFP=449628.0,
                NEVT_UL17=194229.0,
                NEVT_UL18=201398.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M1000_W10_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M1000_W10_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M1000_W10_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M1000_W10_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M1000_W10_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M1000_W10_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M1000_W10_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M1000_W10_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M1200_W12" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=464061.0,
                NEVT_UL16postVFP=497321.0,
                NEVT_UL17=195613.0,
                NEVT_UL18=198217.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M1200_W12_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M1200_W12_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M1200_W12_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M1200_W12_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTT_M1200_W12_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZprimeToTT_M1200_W12_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTT_M1200_W12_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZprimeToTT_M1200_W12_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M1400_W14" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=505378.0,
                NEVT_UL16postVFP=548913.0,
                NEVT_UL17=208708.0,
                NEVT_UL18=217763.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M1400_W14_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M1400_W14_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M1400_W14_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M1400_W14_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTT_M1400_W14_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZprimeToTT_M1400_W14_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTT_M1400_W14_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZprimeToTT_M1400_W14_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M1600_W16" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=538175.0,
                NEVT_UL16postVFP=548012.0,
                NEVT_UL17=219802.0,
                NEVT_UL18=207930.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M1600_W16_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M1600_W16_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M1600_W16_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M1600_W16_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTT_M1600_W16_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZprimeToTT_M1600_W16_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTT_M1600_W16_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZprimeToTT_M1600_W16_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M1800_W18" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=518707.0,
                NEVT_UL16postVFP=533048.0,
                NEVT_UL17=208252.0,
                NEVT_UL18=203473.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M1800_W18_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M1800_W18_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M1800_W18_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M1800_W18_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTT_M1800_W18_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZprimeToTT_M1800_W18_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTT_M1800_W18_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZprimeToTT_M1800_W18_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M2000_W20" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=457884.0,
                NEVT_UL16postVFP=527279.0,
                NEVT_UL17=211425.0,
                NEVT_UL18=196868.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M2000_W20_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M2000_W20_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M2000_W20_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M2000_W20_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTT_M2000_W20_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZprimeToTT_M2000_W20_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTT_M2000_W20_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZprimeToTT_M2000_W20_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M2500_W25" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=456081.0,
                NEVT_UL16postVFP=508484.0,
                NEVT_UL17=203518.0,
                NEVT_UL18=201970.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M2500_W25_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M2500_W25_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M2500_W25_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M2500_W25_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTT_M2500_W25_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZprimeToTT_M2500_W25_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTT_M2500_W25_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZprimeToTT_M2500_W25_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M3000_W30" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=482947.0,
                NEVT_UL16postVFP=490008.0,
                NEVT_UL17=192535.0,
                NEVT_UL18=194745.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M3000_W30_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M3000_W30_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M3000_W30_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M3000_W30_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTT_M3000_W30_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZprimeToTT_M3000_W30_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTT_M3000_W30_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZprimeToTT_M3000_W30_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M3500_W35" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=466444.0,
                NEVT_UL16postVFP=426819.0,
                NEVT_UL17=189565.0,
                NEVT_UL18=187591.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M3500_W35_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M3500_W35_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M3500_W35_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M3500_W35_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTT_M3500_W35_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZprimeToTT_M3500_W35_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTT_M3500_W35_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZprimeToTT_M3500_W35_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M4000_W40" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=422942.0,
                NEVT_UL16postVFP=452977.0,
                NEVT_UL17=184083.0,
                NEVT_UL18=184021.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M4000_W40_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M4000_W40_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M4000_W40_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M4000_W40_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTT_M4000_W40_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZprimeToTT_M4000_W40_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTT_M4000_W40_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZprimeToTT_M4000_W40_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),

        },
        "ZprimeToTT_M4500_W45" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=413509.0,
                NEVT_UL16postVFP=417527.0,
                NEVT_UL17=174039.0,
                NEVT_UL18=179341.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTT_M4500_W45_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZprimeToTT_M4500_W45_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTT_M4500_W45_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZprimeToTT_M4500_W45_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTT_M4500_W45_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZprimeToTT_M4500_W45_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTT_M4500_W45_CP2_PSweights_madgraph-pythiaMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZprimeToTT_M4500_W45_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M5000_W50" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=109600.0,
                NEVT_UL16postVFP=90300.0,
                NEVT_UL17=194238.0,
                NEVT_UL18=193733.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTTJets_M5000_W50_CP2_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZprimeToTTJets_M5000_W50_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTTJets_M5000_W50_CP2_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToTTJets_M5000_W50_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M5000_W50_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M5000_W50_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M5000_W50_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M5000_W50_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M6000_W60" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=107673.0,
                NEVT_UL16postVFP=91498.0,
                NEVT_UL17=202610.0,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTTJets_M6000_W60_CP2_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZprimeToTTJets_M6000_W60_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTTJets_M6000_W60_CP2_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToTTJets_M6000_W60_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M6000_W60_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M6000_W60_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ZprimeToTT_M7000_W70" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=107295.0,
                NEVT_UL16postVFP=89723.0,
                NEVT_UL17=192854.0,
                NEVT_UL18=197279.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTTJets_M7000_W70_CP2_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZprimeToTTJets_M7000_W70_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTTJets_M7000_W70_CP2_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToTTJets_M7000_W70_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M7000_W70_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M7000_W70_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M7000_W70_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M7000_W70_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M8000_W80" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=105321.0,
                NEVT_UL16postVFP=91227.0,
                NEVT_UL17=191551.0,
                NEVT_UL18=194397.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTTJets_M8000_W80_CP2_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZprimeToTTJets_M8000_W80_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTTJets_M8000_W80_CP2_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToTTJets_M8000_W80_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M8000_W80_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M8000_W80_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToTTJets_M8000_W80_CP2_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToTTJets_M8000_W80_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToTT_M9000_W90" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=106005.0,
                NEVT_UL16postVFP=91144.0,
                NEVT_UL17=182122.0,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZprimeToTTJets_M9000_W90_CP2_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZprimeToTTJets_M9000_W90_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToTTJets_M9000_W90_CP2_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToTTJets_M9000_W90_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToTTJets_M9000_W90_CP2_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToTTJets_M9000_W90_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ZPrimeToTT_M400_W40" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=261000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=497000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M400_W40_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M400_W40_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M400_W40_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M400_W40_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M400_W40_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M400_W40_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M400_W40_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M400_W40_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M500_W50" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=229000.0,
                NEVT_UL17=491000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M500_W50_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M500_W50_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M500_W50_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M500_W50_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M500_W50_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M500_W50_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M500_W50_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M500_W50_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M600_W60" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=268000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=494000.0,
                NEVT_UL18=491000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M600_W60_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M600_W60_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M600_W60_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M600_W60_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M600_W60_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M600_W60_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M600_W60_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M600_W60_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M700_W70" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=464000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M700_W70_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M700_W70_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M700_W70_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M700_W70_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M700_W70_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M700_W70_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M700_W70_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M700_W70_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M800_W80" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=266000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=494000.0,
                NEVT_UL18=482000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M800_W80_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M800_W80_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M800_W80_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M800_W80_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M800_W80_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M800_W80_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M800_W80_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M800_W80_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M900_W90" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M900_W90_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M900_W90_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M900_W90_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M900_W90_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M900_W90_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M900_W90_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M900_W90_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M900_W90_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M1000_W100" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M1000_W100_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M1000_W100_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M1000_W100_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M1000_W100_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M1000_W100_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M1000_W100_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M1000_W100_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M1000_W100_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M1200_W120" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=497000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M1200_W120_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M1200_W120_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M1200_W120_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M1200_W120_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M1200_W120_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M1200_W120_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M1200_W120_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M1200_W120_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M1400_W140" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=262000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=482000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M1400_W140_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M1400_W140_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M1400_W140_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M1400_W140_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M1400_W140_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M1400_W140_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M1400_W140_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M1400_W140_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M1600_W160" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=494000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M1600_W160_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M1600_W160_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M1600_W160_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M1600_W160_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M1600_W160_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M1600_W160_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M1600_W160_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M1600_W160_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M1800_W180" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=264000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=491000.0,
                NEVT_UL18=482000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M1800_W180_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M1800_W180_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M1800_W180_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M1800_W180_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M1800_W180_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M1800_W180_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M1800_W180_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M1800_W180_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M2000_W200" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M2000_W200_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M2000_W200_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M2000_W200_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M2000_W200_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M2000_W200_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M2000_W200_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M2000_W200_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M2000_W200_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M2500_W250" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=267000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=489000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M2500_W250_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M2500_W250_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M2500_W250_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M2500_W250_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M2500_W250_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M2500_W250_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M2500_W250_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M2500_W250_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M3000_W300" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=491000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M3000_W300_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M3000_W300_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M3000_W300_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M3000_W300_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M3000_W300_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M3000_W300_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M3000_W300_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M3000_W300_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M3500_W350" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M3500_W350_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M3500_W350_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M3500_W350_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M3500_W350_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M3500_W350_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M3500_W350_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M3500_W350_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M3500_W350_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M4000_W400" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=267000.0,
                NEVT_UL16postVFP=210000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M4000_W400_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M4000_W400_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M4000_W400_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M4000_W400_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M4000_W400_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M4000_W400_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M4000_W400_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M4000_W400_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M4500_W450" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=497000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M4500_W450_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M4500_W450_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM ",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M4500_W450_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M4500_W450_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M4500_W450_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M4500_W450_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M4500_W450_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M4500_W450_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M5000_W500" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=194000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M5000_W500_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M5000_W500_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M5000_W500_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M5000_W500_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M5000_W500_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M5000_W500_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M5000_W500_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M5000_W500_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M6000_W600" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=200000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M6000_W600_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M6000_W600_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M6000_W600_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M6000_W600_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M6000_W600_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M6000_W600_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M6000_W600_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M6000_W600_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M7000_W700" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=200000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M7000_W700_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M7000_W700_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M7000_W700_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M7000_W700_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M7000_W700_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M7000_W700_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M7000_W700_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M7000_W700_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M8000_W800" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=190000.0,
                NEVT_UL18=200000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M8000_W800_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M8000_W800_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M8000_W800_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M8000_W800_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M8000_W800_CP2_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZPrimeToTT_M8000_W800_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M8000_W800_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M8000_W800_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M9000_W900" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=194000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M9000_W900_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M9000_W900_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M9000_W900_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M9000_W900_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M9000_W900_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M9000_W900_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M9000_W900_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M9000_W900_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M400_W120" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M400_W120_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M400_W120_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M400_W120_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M400_W120_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M400_W120_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M400_W120_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M400_W120_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M400_W120_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M500_W150" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=494000.0,
                NEVT_UL18=485000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M500_W150_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M500_W150_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM ",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M500_W150_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M500_W150_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M500_W150_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M500_W150_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M500_W150_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M500_W150_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M600_W180" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=491000.0,
                NEVT_UL18=497000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M600_W180_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M600_W180_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M600_W180_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M600_W180_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M600_W180_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M600_W180_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M600_W180_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M600_W180_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M700_W210" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M700_W210_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M700_W210_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M700_W210_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M700_W210_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M700_W210_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M700_W210_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M700_W70_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M700_W210_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M800_W240" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M800_W240_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M800_W240_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M800_W240_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M800_W240_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M800_W240_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M800_W240_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M800_W240_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M800_W240_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M900_W270" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=227000.0,
                NEVT_UL17=461000.0,
                NEVT_UL18=497000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M900_W270_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M900_W270_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M900_W270_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M900_W270_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M900_W270_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M900_W270_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M900_W270_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M900_W270_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M1000_W300" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M1000_W300_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M1000_W300_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M1000_W300_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M1000_W300_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M1000_W300_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M1000_W300_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M1000_W300_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M1000_W300_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M1200_W360" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=494000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M1200_W360_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M1200_W360_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M1200_W360_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M1200_W360_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M1200_W360_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M1200_W360_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M1200_W360_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M1200_W360_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M1400_W420" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=488000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M1400_W420_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M1400_W420_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M1400_W420_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M1400_W420_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M1400_W420_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M1400_W420_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M1400_W420_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M1400_W420_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M1600_W480" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=497000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M1600_W480_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M1600_W480_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M1600_W480_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M1600_W480_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M1600_W480_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M1600_W480_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M1600_W480_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M1600_W480_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M1800_W540" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=228000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M1800_W540_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M1800_W540_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M1800_W540_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M1800_W540_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M1800_W540_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M1800_W540_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M1800_W540_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M1800_W540_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M2000_W600" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M2000_W600_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M2000_W600_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M2000_W600_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M2000_W600_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M2000_W600_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M2000_W600_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M2000_W600_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M2000_W600_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M2500_W750" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=489000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M2500_W750_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M2500_W750_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M2500_W750_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M2500_W750_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M2500_W750_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M2500_W750_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M2500_W750_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M2500_W750_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M3000_W900" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=488000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M3000_W900_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M3000_W900_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M3000_W900_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M3000_W900_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M3000_W900_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M3000_W900_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M3000_W900_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M3000_W900_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M3500_W1050" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M3500_W1050_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M3500_W1050_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M3500_W1050_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M3500_W1050_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M3500_W1050_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M3500_W1050_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M3500_W1050_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M3500_W1050_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M4000_W1200" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=228000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M4000_W1200_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M4000_W1200_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M4000_W1200_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M4000_W1200_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M4000_W1200_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M4000_W1200_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M4000_W1200_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M4000_W1200_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M4500_W1350" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=270000.0,
                NEVT_UL16postVFP=230000.0,
                NEVT_UL17=500000.0,
                NEVT_UL18=500000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M4500_W1350_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M4500_W1350_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M4500_W1350_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M4500_W1350_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM ",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M4500_W1350_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M4500_W1350_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M4500_W1350_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M4500_W1350_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M5000_W1500" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=200000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M5000_W1500_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M5000_W1500_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M5000_W1500_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M5000_W1500_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M5000_W1500_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M5000_W1500_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M5000_W1500_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M5000_W1500_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M6000_W1800" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=200000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M6000_W1800_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M6000_W1800_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M6000_W1800_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M6000_W1800_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M6000_W1800_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M6000_W1800_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M6000_W1800_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M6000_W1800_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M7000_W2100" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=200000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M7000_W2100_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M7000_W2100_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M7000_W2100_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M7000_W2100_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M7000_W2100_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M7000_W2100_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M7000_W2100_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M7000_W2100_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M8000_W2400" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=197000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M8000_W2400_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M8000_W2400_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M8000_W2400_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M8000_W2400_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M8000_W2400_CP2_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZPrimeToTT_M8000_W2400_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M8000_W2400_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M8000_W2400_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZPrimeToTT_M9000_W2700" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=108000.0,
                NEVT_UL16postVFP=92000.0,
                NEVT_UL17=200000.0,
                NEVT_UL18=194000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ZPrimeToTT_M9000_W2700_CP2_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZPrimeToTT_M9000_W2700_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZPrimeToTT_M9000_W2700_CP2_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZPrimeToTT_M9000_W2700_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZPrimeToTT_M9000_W2700_CP2_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZPrimeToTT_M9000_W2700_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZPrimeToTT_M9000_W2700_CP2_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZPrimeToTT_M9000_W2700_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-500" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=235000,
                NEVT_UL16postVFP=250000,
                NEVT_UL17=500000,
                NEVT_UL18=500000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-500_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-500_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-500_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-500_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-500_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-500_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-1000" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=244000,
                NEVT_UL16postVFP=250000,
                NEVT_UL17=485000,
                NEVT_UL18=479000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-1000_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-1000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-1000_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-1000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-1000_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-1000_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-1000_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-1000_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-1500" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=240000,
                NEVT_UL16postVFP=228000,
                NEVT_UL17=500000,
                NEVT_UL18=500000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-1500_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-1500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-1500_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-1500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-1500_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-1500_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-1500_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-1500_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-2000" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=250000,
                NEVT_UL16postVFP=208000,
                NEVT_UL17=494000,
                NEVT_UL18=494000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-2000_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-2000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-2000_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-2000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-2000_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-2000_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-2000_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-2000_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-2500" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=250000,
                NEVT_UL16postVFP=196000,
                NEVT_UL17=497000,
                NEVT_UL18=488000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-2500_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-2500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-2500_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-2500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-2500_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-2500_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-2500_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-2500_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-3000" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=241000,
                NEVT_UL16postVFP=248000,
                NEVT_UL17=500000,
                NEVT_UL18=500000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-3000_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-3000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-3000_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-3000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-3000_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-3000_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-3000_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-3000_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-3500" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=250000,
                NEVT_UL16postVFP=250000,
                NEVT_UL17=497000,
                NEVT_UL18=500000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-3500_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-3500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-3500_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-3500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-3500_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-3500_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-3500_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-3500_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-4000" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=250000,
                NEVT_UL16postVFP=239000,
                NEVT_UL17=497000,
                NEVT_UL18=484000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-4000_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-4000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-4000_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-4000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-4000_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-4000_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-4000_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-4000_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-4500" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=250000,
                NEVT_UL16postVFP=249000,
                NEVT_UL17=464000,
                NEVT_UL18=482000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-4500_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-4500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-4500_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-4500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-4500_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-4500_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-4500_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-4500_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-5000" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=250000,
                NEVT_UL16postVFP=234000,
                NEVT_UL17=500000,
                NEVT_UL18=500000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-5000_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-5000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-5000_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-5000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-5000_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-5000_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-5000_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-5000_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-5500" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=238000,
                NEVT_UL16postVFP=248000,
                NEVT_UL17=494000,
                NEVT_UL18=479000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-5500_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-5500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-5500_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-5500_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-5500_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-5500_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-5500_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-5500_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "RSGluonToTT_M-6000" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=250000,
                NEVT_UL16postVFP=248000,
                NEVT_UL17=476000,
                NEVT_UL18=455000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/RSGluonToTT_M-6000_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/RSGluonToTT_M-6000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/RSGluonToTT_M-6000_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/RSGluonToTT_M-6000_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/RSGluonToTT_M-6000_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/RSGluonToTT_M-6000_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/RSGluonToTT_M-6000_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/RSGluonToTT_M-6000_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m365_w91p25_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.384058, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.37211, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=81204.09208,
                NEVT_UL16postVFP=82251.48621,
                NEVT_UL17=171213.0027,
                NEVT_UL18=172236.535667,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m365_w91p25_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m365_w91p25_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m365_w91p25_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m365_w91p25_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m365_w91p25_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m365_w91p25_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m365_w91p25_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m365_w91p25_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM ",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m400_w100p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.392964, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.25867, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=88520.838147,
                NEVT_UL16postVFP=88492.02305,
                NEVT_UL17=177113.8621,
                NEVT_UL18=176982.22823,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m400_w100p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m400_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m400_w100p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m400_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m400_w100p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m400_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m400_w100p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m400_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m500_w125p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.222718, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.13856, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=50395.421986,
                NEVT_UL16postVFP=50202.848086,
                NEVT_UL17=100770.483906,
                NEVT_UL18=98974.44703,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m500_w125p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m500_w125p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m500_w125p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m500_w125p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m500_w125p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m500_w125p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m500_w125p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m500_w125p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m600_w150p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.108418, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.0793, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=24356.66183,
                NEVT_UL16postVFP=23560.2129205,
                NEVT_UL17=48805.85248,
                NEVT_UL18=48779.242473,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m600_w150p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m600_w150p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m600_w150p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m600_w150p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m600_w150p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m600_w150p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m600_w150p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m600_w150p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m800_w200p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.02871, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.01433, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=6505.440998,
                NEVT_UL16postVFP=6501.2446068,
                NEVT_UL17=13009.3894694,
                NEVT_UL18=13010.468379,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m800_w200p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m800_w200p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m800_w200p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m800_w200p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m800_w200p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m800_w200p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m800_w200p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m800_w200p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m1000_w250p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.00935898, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.97913, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2119.7220377,
                NEVT_UL16postVFP=2069.06411289,
                NEVT_UL17=4224.5618954,
                NEVT_UL18=4242.4866877,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m1000_w250p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m1000_w250p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m1000_w250p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m1000_w250p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m1000_w250p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m1000_w250p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m1000_w250p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m1000_w250p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m365_w91p25_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-3.51387, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.88314, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-794059.0838,
                NEVT_UL16postVFP=-795879.67662,
                NEVT_UL17=-1586370.3368,
                NEVT_UL18=-1586907.61682,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m365_w91p25_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m365_w91p25_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m365_w91p25_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m365_w91p25_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m365_w91p25_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m365_w91p25_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m365_w91p25_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m365_w91p25_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m400_w100p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-2.80865, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.83756, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-639506.25796,
                NEVT_UL16postVFP=-643622.5466,
                NEVT_UL17=-1248131.677,
                NEVT_UL18=-1278265.00519,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m400_w100p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m400_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m400_w100p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m400_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m400_w100p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m400_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m400_w100p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m400_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m500_w125p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-1.06139, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.78803, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-243627.29086,
                NEVT_UL16postVFP=-246766.59487,
                NEVT_UL17=-486918.76265,
                NEVT_UL18=-488398.0432,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m500_w125p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m500_w125p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m500_w125p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m500_w125p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m500_w125p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m500_w125p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m500_w125p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m500_w125p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m600_w150p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-0.354892, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.76308, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-83281.641741,
                NEVT_UL16postVFP=-84832.311593,
                NEVT_UL17=-165008.109821,
                NEVT_UL18=-165895.03658,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m600_w150p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m600_w150p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m600_w150p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m600_w150p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m600_w150p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m600_w150p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m600_w150p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m600_w150p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m800_w200p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.0131675, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.73532, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2275.8078853,
                NEVT_UL16postVFP=1220.2306676,
                NEVT_UL17=3818.12660971,
                NEVT_UL18=3542.98394915,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m800_w200p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m800_w200p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m800_w200p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m800_w200p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m800_w200p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m800_w200p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m800_w200p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m800_w200p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m1000_w250p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.0630704, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.72009, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=13939.756035,
                NEVT_UL16postVFP=13721.556921,
                NEVT_UL17=28024.216226,
                NEVT_UL18=27824.657441,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m1000_w250p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m1000_w250p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m1000_w250p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m1000_w250p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m1000_w250p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m1000_w250p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m1000_w250p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m1000_w250p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m365_36p5_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1.18764, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.88312, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=256294.89633,
                NEVT_UL16postVFP=145074.15602,
                NEVT_UL17=523391.4965,
                NEVT_UL18=529368.49437,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m365_w36p5_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m365_w36p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m365_w36p5_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m365_w36p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m365_w36p5_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m365_w36p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m365_w36p5_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m365_w36p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m400_w40p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1.28105, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.83757, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=288659.16832,
                NEVT_UL16postVFP=286415.1199,
                NEVT_UL17=574027.6727,
                NEVT_UL18=573900.86455,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m400_w40p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m400_w40p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m400_w40p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m400_w40p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m400_w40p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m400_w40p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m400_w40p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m400_w40p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m500_w50p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.660745, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.78803, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=149616.08465,
                NEVT_UL16postVFP=149629.914053,
                NEVT_UL17=299162.2687,
                NEVT_UL18=296686.89491,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m500_w50p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m500_w50p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m500_w50p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m500_w50p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m500_w50p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m500_w50p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m500_w50p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m500_w50p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m600_w60p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.29944, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.76302, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=66829.024208,
                NEVT_UL16postVFP=67582.717264,
                NEVT_UL17=135699.902294,
                NEVT_UL18=134971.091663,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m600_w60p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m600_w60p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m600_w60p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m600_w60p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m600_w60p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m600_w60p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m600_w60p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m600_w60p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m800_w80p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.0709866, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.73535, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=16087.587782,
                NEVT_UL16postVFP=16093.945433,
                NEVT_UL17=32174.2228,
                NEVT_UL18=31987.80998,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m800_w80p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m800_w80p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m800_w80p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m800_w80p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m800_w80p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m800_w80p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m800_w80p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m800_w80p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m1000_w100p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.0209362, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.72011, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=4745.017413,
                NEVT_UL16postVFP=4747.91728,
                NEVT_UL17=9494.3699807,
                NEVT_UL18=9263.5783702,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m1000_w100p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m1000_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m1000_w100p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m1000_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m1000_w100p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m1000_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m1000_w100p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m1000_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m365_36p5_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-4.92926, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.88312, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1112972.69016,
                NEVT_UL16postVFP=-1117513.98756,
                NEVT_UL17=-2210403.7067,
                NEVT_UL18=-2171094.16728,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m365_w36p5_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m365_w36p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m365_w36p5_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m365_w36p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m365_w36p5_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m365_w36p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m365_w36p5_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m365_w36p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m400_w40p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-3.44265, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.83757, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-786867.006,
                NEVT_UL16postVFP=-789101.34692,
                NEVT_UL17=-1579406.2598,
                NEVT_UL18=-1579689.1022,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m400_w40p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m400_w40p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m400_w40p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m400_w40p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m400_w40p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m400_w40p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m400_w40p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m400_w40p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m500_w50p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-0.937263, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.78803, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-219110.9435,
                NEVT_UL16postVFP=-227201.4818,
                NEVT_UL17=-421949.39712,
                NEVT_UL18=-436120.3311,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m500_w50p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m500_w50p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m500_w50p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m500_w50p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m500_w50p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m500_w50p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m500_w50p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m500_w50p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m600_w60p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-0.166936, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.76302, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-37340.34489,
                NEVT_UL16postVFP=-44194.05708,
                NEVT_UL17=-83092.998201,
                NEVT_UL18=-81900.821139,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m600_w60p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m600_w60p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m600_w60p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m600_w60p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m600_w60p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m600_w60p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m600_w60p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m600_w60p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m800_w80p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.135484, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.73535, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=29430.640305,
                NEVT_UL16postVFP=28099.969551,
                NEVT_UL17=58927.923394,
                NEVT_UL18=60225.44581,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m800_w80p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m800_w80p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m800_w80p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m800_w80p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m800_w80p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m800_w80p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m800_w80p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m800_w80p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m1000_w100p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.136502, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.72011, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=30483.761009,
                NEVT_UL16postVFP=30111.835363,
                NEVT_UL17=60820.291822,
                NEVT_UL18=60547.235299,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m1000_w100p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m1000_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m1000_w100p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m1000_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m1000_w100p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m1000_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m1000_w100p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m1000_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m365_w9p125_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=5.86888, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.37207, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1303218.1199,
                NEVT_UL16postVFP=1303405.7415,
                NEVT_UL17=2607335.746,
                NEVT_UL18=2607045.7854,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m365_w9p125_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m365_w9p125_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m365_w9p125_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m365_w9p125_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m365_w9p125_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m365_w9p125_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m365_w9p125_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m365_w9p125_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m400_w10p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=6.03581, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.2587, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1361550.8595,
                NEVT_UL16postVFP=1345760.2621,
                NEVT_UL17=2657277.9441,
                NEVT_UL18=2543868.1279,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m400_w10p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m400_w10p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m400_w10p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m400_w10p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m400_w10p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m400_w10p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m400_w10p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m400_w10p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m500_w12p5_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=2.8598, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.13858, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=647810.9576,
                NEVT_UL16postVFP=648333.9809,
                NEVT_UL17=1295076.4766,
                NEVT_UL18=1295687.9387,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m500_w12p5_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m500_w12p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m500_w12p5_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m500_w12p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m500_w12p5_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m500_w12p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m500_w12p5_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m500_w12p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m600_w15p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1.23894, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.07926, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=280849.12182,
                NEVT_UL16postVFP=280878.1883,
                NEVT_UL17=561601.46323,
                NEVT_UL18=561805.4832,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m600_w15p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m600_w15p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m600_w15p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m600_w15p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m600_w15p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m600_w15p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m600_w15p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m600_w15p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m800_w20p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.273973, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.0144, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=62120.010172,
                NEVT_UL16postVFP=29574.237047,
                NEVT_UL17=124281.764049,
                NEVT_UL18=124293.07307,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m800_w20p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m800_w20p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m800_w20p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m800_w20p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m800_w20p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m800_w20p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m800_w20p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m800_w20p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m1000_w25p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.0754245, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.97911, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=17104.940015,
                NEVT_UL16postVFP=16626.1296345,
                NEVT_UL17=34005.567704,
                NEVT_UL18=31349.5508702,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m1000_w25p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m1000_w25p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m1000_w25p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m1000_w25p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m1000_w25p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m1000_w25p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m1000_w25p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m1000_w25p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m365_w9p125_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-6.08885, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.88312, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1382651.7808,
                NEVT_UL16postVFP=-1390762.68325,
                NEVT_UL17=-1779358.20887,
                NEVT_UL18=-2770824.941,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m365_w9p125_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m365_w9p125_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m365_w9p125_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m365_w9p125_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m365_w9p125_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m365_w9p125_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m365_w9p125_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m365_w9p125_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m400_w10p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-3.71856, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.83757, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-861366.33313,
                NEVT_UL16postVFP=-839948.9534,
                NEVT_UL17=-1565961.86264,
                NEVT_UL18=-1658473.7532,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m400_w10p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m400_w10p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m400_w10p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m400_w10p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m400_w10p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m400_w10p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m400_w10p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m400_w10p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m500_w12p5_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-0.787467, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.78804, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-183156.43415,
                NEVT_UL16postVFP=-195530.84382,
                NEVT_UL17=-374395.86068,
                NEVT_UL18=-358621.8006,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m500_w12p5_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m500_w12p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m500_w12p5_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m500_w12p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m500_w12p5_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m500_w12p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m500_w12p5_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m500_w12p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m600_w15p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-0.0280567, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.76307, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-5320.2340722,
                NEVT_UL16postVFP=-10244.00829,
                NEVT_UL17=-13291.4155487,
                NEVT_UL18=-23223.570779,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m600_w15p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m600_w15p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m600_w15p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m600_w15p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m600_w15p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m600_w15p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m600_w15p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m600_w15p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m800_w20p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.208417, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.73535, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=47685.61398,
                NEVT_UL16postVFP=46310.2176,
                NEVT_UL17=84343.846579,
                NEVT_UL18=91382.61924,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m800_w20p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m800_w20p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m800_w20p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m800_w20p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m800_w20p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m800_w20p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m800_w20p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m800_w20p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HpseudoToTTTo1L1Nu2J_m1000_w25p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.17625, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.72008, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=39879.742145,
                NEVT_UL16postVFP=39097.948724,
                NEVT_UL17=78350.880834,
                NEVT_UL18=78197.12187,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HpseudoToTTTo1L1Nu2J_m1000_w25p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HpseudoToTTTo1L1Nu2J_m1000_w25p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HpseudoToTTTo1L1Nu2J_m1000_w25p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HpseudoToTTTo1L1Nu2J_m1000_w25p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HpseudoToTTTo1L1Nu2J_m1000_w25p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HpseudoToTTTo1L1Nu2J_m1000_w25p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HpseudoToTTTo1L1Nu2J_m1000_w25p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HpseudoToTTTo1L1Nu2J_m1000_w25p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m365_w91p25_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.0399425, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.36163, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=8579.9033952,
                NEVT_UL16postVFP=9012.0945942,
                NEVT_UL17=17879.6904069,
                NEVT_UL18=18024.894798,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m365_w91p25_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m365_w91p25_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m365_w91p25_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m365_w91p25_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m365_w91p25_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m365_w91p25_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m365_w91p25_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m365_w91p25_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m400_w100p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.0530526, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.28739, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=11974.2015662,
                NEVT_UL16postVFP=4893.3040849,
                NEVT_UL17=23944.04088,
                NEVT_UL18=23973.1011264,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m400_w100p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m400_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m400_w100p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m400_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m400_w100p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m400_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m400_w100p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m400_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m500_w125p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.057073, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.17333, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=12707.539589,
                NEVT_UL16postVFP=12912.4057126,
                NEVT_UL17=25794.11704,
                NEVT_UL18=25806.64633,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m500_w125p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m500_w125p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m500_w125p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m500_w125p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m500_w125p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m500_w125p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m500_w125p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m500_w125p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m600_w150p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.0388742, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.11279, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=8806.4777909,
                NEVT_UL16postVFP=8800.454386,
                NEVT_UL17=17599.58449,
                NEVT_UL18=17594.696292,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m600_w150p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m600_w150p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m600_w150p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m600_w150p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m600_w150p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m600_w150p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m600_w150p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m600_w150p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m800_w200p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.0138542, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.04658, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=3139.3466361,
                NEVT_UL16postVFP=3127.4778621,
                NEVT_UL17=5951.5560198,
                NEVT_UL18=6278.8737025,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m800_w200p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m800_w200p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m800_w200p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m800_w200p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m800_w200p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m800_w200p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m800_w200p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m800_w200p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m1000_w250p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.00503847, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.01067, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1141.80461993,
                NEVT_UL16postVFP=1114.5434492,
                NEVT_UL17=2283.7764545,
                NEVT_UL18=2283.69269757,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m1000_w250p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m1000_w250p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m1000_w250p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m1000_w250p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m1000_w250p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m1000_w250p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m1000_w250p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m1000_w250p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m365_w91p25_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-0.761555, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.87897, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-170318.50717,
                NEVT_UL16postVFP=-171810.31304,
                NEVT_UL17=-344502.76034,
                NEVT_UL18=-487802.62975,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m365_w91p25_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m365_w91p25_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m365_w91p25_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m365_w91p25_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m365_w91p25_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m365_w91p25_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m365_w9p125_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m365_w91p25_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m400_w100p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-0.742658, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.8492, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-158971.77207,
                NEVT_UL16postVFP=-168691.582527,
                NEVT_UL17=-337111.85529,
                NEVT_UL18=-335632.73832,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m400_w100p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m400_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m400_w100p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m400_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m400_w100p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m400_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m400_w100p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m400_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m500_w125p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-0.427226, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.80251, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-97678.856612,
                NEVT_UL16postVFP=-97902.080091,
                NEVT_UL17=-188882.123508,
                NEVT_UL18=-193539.89372,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m500_w125p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m500_w125p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m500_w125p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m500_w125p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m500_w125p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m500_w125p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m500_w125p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m500_w125p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m600_w150p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-0.187834, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.77723, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-43744.150087,
                NEVT_UL16postVFP=-44496.672295,
                NEVT_UL17=-86039.06483,
                NEVT_UL18=-86085.894465,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m600_w150p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m600_w150p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m600_w150p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m600_w150p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m600_w150p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m600_w150p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m600_w150p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m600_w150p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m800_w200p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-0.0147037, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.74916, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-3449.2540368,
                NEVT_UL16postVFP=-4074.59180793,
                NEVT_UL17=-7569.7416882,
                NEVT_UL18=-7089.446475,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m800_w200p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m800_w200p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m800_w200p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m800_w200p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m800_w200p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m800_w200p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m800_w200p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m800_w200p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m1000_w250p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.0194944, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.73374, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=4328.6188608,
                NEVT_UL16postVFP=3866.5128433,
                NEVT_UL17=8502.5593978,
                NEVT_UL18=8534.8189202,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m1000_w250p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m1000_w250p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m1000_w250p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m1000_w250p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m1000_w250p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m1000_w250p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m1000_w250p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m1000_w250p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m365_36p5_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.0733756, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.36165, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=16550.0099108,
                NEVT_UL17=32682.539549,
                NEVT_UL18=33072.517701,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m365_w36p5_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m365_w36p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m365_w36p5_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m365_w36p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m365_w36p5_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m365_w36p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m400_w40p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.134601, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.28741, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=30318.763244,
                NEVT_UL16postVFP=30308.935418,
                NEVT_UL17=60666.94613,
                NEVT_UL18=60389.66898,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m400_w40p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m400_w40p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m400_w40p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m400_w40p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m400_w40p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m400_w40p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m400_w40p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m400_w40p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m500_w50p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.172511, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.17323, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=39022.080062,
                NEVT_UL16postVFP=38888.924959,
                NEVT_UL17=77994.05398,
                NEVT_UL18=78030.369961,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m500_w50p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m500_w50p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m500_w50p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m500_w50p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m500_w50p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m500_w50p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m500_w50p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m500_w50p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m600_w60p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.115724, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.11283, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=26205.193565,
                NEVT_UL16postVFP=26193.54991,
                NEVT_UL17=52100.11534,
                NEVT_UL18=51118.092581,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m600_w60p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m600_w60p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m600_w60p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m600_w60p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m600_w60p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m600_w60p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m600_w60p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m600_w60p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m800_w80p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.0381515, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.04663, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=8641.8341922,
                NEVT_UL16postVFP=8643.5531192,
                NEVT_UL17=17186.548258,
                NEVT_UL18=17291.628299,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m800_w80p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m800_w80p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m800_w80p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m800_w80p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m800_w80p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m800_w80p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m800_w80p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m800_w80p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m1000_w100p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.0127637, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.01064, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2893.9334362,
                NEVT_UL16postVFP=2893.8290827,
                NEVT_UL17=5786.270134,
                NEVT_UL18=5751.8822019,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m1000_w100p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m1000_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m1000_w100p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m1000_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m1000_w100p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m1000_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m1000_w100p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m1000_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m365_36p5_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-0.941809, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.87898, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-210896.53462,
                NEVT_UL16postVFP=-210239.509572,
                NEVT_UL17=-421755.8942,
                NEVT_UL18=-422050.40195,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m365_w36p5_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m365_w36p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m365_w36p5_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m365_w36p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m365_w36p5_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m365_w36p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m365_w36p5_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m365_w36p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m400_w40p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-0.936429, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.84921, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-211991.76306,
                NEVT_UL16postVFP=-212560.040131,
                NEVT_UL17=-424753.80961,
                NEVT_UL18=-416737.97976,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m400_w40p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m400_w40p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m400_w40p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m400_w40p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m400_w40p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m400_w40p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m400_w40p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m400_w40p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m500_w50p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-0.466654, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.80247, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-107012.401862,
                NEVT_UL16postVFP=-109145.38449,
                NEVT_UL17=-212458.66898,
                NEVT_UL18=-215769.226969,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m500_w50p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m500_w50p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m500_w50p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m500_w50p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m500_w50p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m500_w50p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m500_w50p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m500_w50p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m600_w60p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-0.160288, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.77724, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-37050.257408,
                NEVT_UL16postVFP=-38852.607288,
                NEVT_UL17=-75166.427755,
                NEVT_UL18=-74999.493927,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m600_w60p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m600_w60p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m600_w60p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m600_w60p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m600_w60p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m600_w60p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m600_w60p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m600_w60p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m800_w80p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.0234526, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.74918, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=4588.718688,
                NEVT_UL16postVFP=3859.553408,
                NEVT_UL17=9505.6351939,
                NEVT_UL18=9729.5129279,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m800_w80p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m800_w80p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m800_w80p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m800_w80p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m800_w80p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m800_w80p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m800_w80p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m800_w80p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m1000_w100p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.0452619, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.73373, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=9766.364654,
                NEVT_UL16postVFP=9822.1785528,
                NEVT_UL17=19995.912164,
                NEVT_UL18=20101.750115,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m1000_w100p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m1000_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m1000_w100p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m1000_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m1000_w100p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m1000_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m1000_w100p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m1000_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m365_w9p125_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.202185, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.36181, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=45455.192162,
                NEVT_UL16postVFP=45490.800092,
                NEVT_UL17=90946.860925,
                NEVT_UL18=88844.529901,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m365_w9p125_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m365_w9p125_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m365_w9p125_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m365_w9p125_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m365_w9p125_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m365_w9p125_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m365_w9p125_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m365_w9p125_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m400_w10p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.54795, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.28735, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=122270.328234,
                NEVT_UL16postVFP=119834.460985,
                NEVT_UL17=241956.114212,
                NEVT_UL18=245091.00191,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m400_w10p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m400_w10p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m400_w10p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m400_w10p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m400_w10p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m400_w10p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m400_w10p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m400_w10p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m500_w12p5_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.770716, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.1733, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=174249.05999,
                NEVT_UL16postVFP=174336.8065,
                NEVT_UL17=348465.2412,
                NEVT_UL18=348466.27838,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m500_w12p5_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m500_w12p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m500_w12p5_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m500_w12p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m500_w12p5_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m500_w12p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m500_w12p5_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m500_w12p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m600_w15p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.506278, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.11286, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=112831.104056,
                NEVT_UL16postVFP=114779.796842,
                NEVT_UL17=229209.57815,
                NEVT_UL18=228276.924753,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m600_w15p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m600_w15p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m600_w15p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m600_w15p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m600_w15p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m600_w15p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m600_w15p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m600_w15p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m800_w20p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.158117, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.04658, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=34699.165952,
                NEVT_UL16postVFP=35824.651047,
                NEVT_UL17=71710.15077,
                NEVT_UL18=71697.69614,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m800_w20p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m800_w20p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m800_w20p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m800_w20p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m800_w20p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m800_w20p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m800_w20p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m800_w20p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m1000_w25p0_res" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.0500883, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.01071, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=11354.2339702,
                NEVT_UL16postVFP=11358.4466789,
                NEVT_UL17=22709.4169,
                NEVT_UL18=22709.2436044,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m1000_w25p0_res_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m1000_w25p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m1000_w25p0_res_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m1000_w25p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m1000_w25p0_res_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m1000_w25p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m1000_w25p0_res_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m1000_w25p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m365_w9p125_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-1.08972, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.87905, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-243891.57659,
                NEVT_UL16postVFP=-244752.00579,
                NEVT_UL17=-484864.87445,
                NEVT_UL18=-487802.62975,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m365_w9p125_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m365_w9p125_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m365_w9p125_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m365_w9p125_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m365_w9p125_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m365_w9p125_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m365_w9p125_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m365_w9p125_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m400_w10p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-1.07602, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.84919, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-240712.32609,
                NEVT_UL16postVFP=-244155.378094,
                NEVT_UL17=-486247.94155,
                NEVT_UL18=-463615.99297,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m400_w10p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m400_w10p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m400_w10p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m400_w10p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m400_w10p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m400_w10p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m400_w10p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m400_w10p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m500_w12p5_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-0.473926, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.8025, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-108303.190639,
                NEVT_UL16postVFP=-110955.45375,
                NEVT_UL17=-219185.5194,
                NEVT_UL18=-221095.84215,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m500_w12p5_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m500_w12p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m500_w12p5_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m500_w12p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m500_w12p5_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m500_w12p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m500_w12p5_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m500_w12p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m600_w15p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=-0.133391, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.77726, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-28958.368656,
                NEVT_UL16postVFP=-33767.930485,
                NEVT_UL17=-61134.476633,
                NEVT_UL18=-64189.754372,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m600_w15p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m600_w15p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m600_w15p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m600_w15p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m600_w15p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m600_w15p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m600_w15p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m600_w15p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m800_w20p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.0478693, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.74916, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=10641.0264321,
                NEVT_UL16postVFP=10966.333264,
                NEVT_UL17=20316.226675,
                NEVT_UL18=19546.6785,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m800_w20p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m800_w20p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m800_w20p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m800_w20p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m800_w20p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m800_w20p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m800_w20p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m800_w20p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "HscalarToTTTo1L1Nu2J_m1000_w25p0_int" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.0599909, XSecSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.73376, kFacSource_13TeV="Provided by DESY group (Alexander Grohsjean)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=13776.0977588,
                NEVT_UL16postVFP=13125.219647,
                NEVT_UL17=25812.899749,
                NEVT_UL18=26211.349801,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/HscalarToTTTo1L1Nu2J_m1000_w25p0_int_CP5_madgraph_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/HscalarToTTTo1L1Nu2J_m1000_w25p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/HscalarToTTTo1L1Nu2J_m1000_w25p0_int_CP5_madgraph_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/HscalarToTTTo1L1Nu2J_m1000_w25p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/HscalarToTTTo1L1Nu2J_m1000_w25p0_int_CP5_madgraph_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/HscalarToTTTo1L1Nu2J_m1000_w25p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/HscalarToTTTo1L1Nu2J_m1000_w25p0_int_CP5_madgraph_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/HscalarToTTTo1L1Nu2J_m1000_w25p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },
    }

    def __init__(self, extra_dicts=None):

        if extra_dicts is not None:
            if type(extra_dicts) == dict:
                self.__values_dict.update(extra_dicts)
            elif type(extra_dicts) == list:
                for ed in extra_dicts:
                    self.__values_dict.update(ed)

    def get_value(self, name, energy, year, key, strict=False, info = ""):
        """Return the value for a given MC sample, energy or year, and information type

        If information is stored for both an energy and a year, the value for the given energy will be preferentially returned.
        If strict checking is turned on the function will raise an error if a given dictionary or piece of information isn't found.
          Otherwise the default value will be returned with no error (i.e. will return 1.0 for kFactors)

        Args:
            name (`str`): The process name for a given MC sample
            energy (`str`): The simulated energy used during production of the MC sample
            year (`str`): The production year of the MC sample
            key (`str`): The type of information being requested. The Options can be found in the __key_field_map.
            strict (`bool`): Whether or not to perform strict checking of the dictionary

        """
        fields = [self.__key_field_map[key][0]+info+"_"+energy,self.__key_field_map[key][0]+info+"_"+year]
        if not name in self.__values_dict:
            raise KeyError("ERROR MCSampleValuesHelper::Unknown process \"" + str(name) + "\"")
        if not key in self.__values_dict[name]:
            if strict:
                print(self.__values_dict[name])
                raise KeyError("ERROR MCSampleValuesHelper::The process \"" + str(name) + "\" does not contain a " + str(key) + " tuple")
            else:
                return self.__key_field_map[key][1]
        if not any(f in self.__values_dict[name][key]._fields for f in fields):
            if strict:
                print(self.__values_dict[name][key])
                raise KeyError("ERROR MCSampleValuesHelper::The " + str(key) + " tuple for process \"" + str(name) + "\" does contain the key(s) \"" + str(fields) + "\"")
            else:
                self.__key_field_map[key][1]

        if self.__values_dict[name][key].__getattribute__(fields[0]) != self.__key_field_map[key][1]:
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
    energies = MCSampleValuesHelper.__dict__["_MCSampleValuesHelper__energies"]
    years = MCSampleValuesHelper.__dict__["_MCSampleValuesHelper__years"]
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
