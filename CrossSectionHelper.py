from collections import namedtuple,Mapping

def namedtuple_with_defaults(typename, field_names, default_values=()):
    T = namedtuple(typename, field_names, verbose=False)
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
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "SingleMuon_RunB": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "SingleMuon_RunC": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "SingleMuon_RunD": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "SingleMuon_RunE": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL17=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL17="", XmlSource_UL17="",
            ),
        },

        "SingleMuon_RunF": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
            ),
        },

        "SingleMuon_RunG": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
            ),
        },

        "SingleMuon_RunH": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
            ),
        },

        "SingleElectron_RunB": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL17=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL17="", XmlSource_UL17="",
            ),
        },

        "SingleElectron_RunC": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL17=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL17="", XmlSource_UL17="",
            ),
        },

        "SingleElectron_RunD": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL17=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL17="", XmlSource_UL17="",
            ),
        },

        "SingleElectron_RunE": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL17=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL17="", XmlSource_UL17="",
            ),
        },

        "SingleElectron_RunF": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
            ),
        },

        "SingleElectron_RunG": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
            ),
        },

        "SingleElectron_RunH": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
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
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "EGamma_RunB": {
            "NEvents" : NEventsValues(
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "EGamma_RunC": {
            "NEvents" : NEventsValues(
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "EGamma_RunD": {
            "NEvents" : NEventsValues(
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "JetHT_RunA": {
            "NEvents" : NEventsValues(
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "JetHT_RunB": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=9726665+133752091,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016B-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "JetHT_RunC": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=46495988,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016C-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "JetHT_RunD": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=73330042,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016D-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "JetHT_RunE": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=69219288,
                NEVT_UL17=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016E-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="", XmlSource_UL17="",
            ),
        },

        "JetHT_RunF": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=41564915,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016F-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
            ),
        },

        "JetHT_RunG": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
            ),
        },

        "JetHT_RunH": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
            ),
        },

        "MET_RunA": {
            "NEvents" : NEventsValues(
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "MET_RunB": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "MET_RunC": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "MET_RunD": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "MET_RunE": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL17=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL17="", XmlSource_UL17="",
            ),
        },

        "MET_RunF": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
            ),
        },

        "MET_RunG": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
            ),
        },

        "MET_RunH": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
            ),
        },

        "TTbarTo2L2Nu" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18=""
            ),
        },

        "TTbarToSemiLeptonic" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "TTbarToHadronic" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "TT_Mtt-700to1000" : {
            "CrossSection" : XSValues(XSec_13TeV=6.472e+01, XSecSource_13TeV="GenXSecAnalyzer run on UL17 (other years and also XSDB give similar results); accuracy: NLO"),
            "Correction" : CorrValues(CorrSource_13TeV="FIXME; This sample uses Gen NLO Xsec but the normal TTbar samples are scaled to NNLO theory Xsec. Will need to derive a correction factor later on and put it here"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=22646592839.0,
                NEVT_UL17=24182708233.9,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TT_Mtt-700to1000_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TT_Mtt-700to1000_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="", XmlSource_UL18="/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TT_Mtt-1000toInf" : {
            "CrossSection" : XSValues(XSec_13TeV=1.644e+01, XSecSource_13TeV="GenXSecAnalyzer run on UL17 (other years and also XSDB give similar results); accuracy: NLO"),
            "Correction" : CorrValues(CorrSource_13TeV="FIXME; This sample uses Gen NLO Xsec but the normal TTbar samples are scaled to NNLO theory Xsec. Will need to derive a correction factor later on and put it here"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=15749293533.9,
                NEVT_UL17=14803424869.0,
                NEVT_UL18=15475388953.2,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TT_Mtt-1000toInf_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TT_Mtt-1000toInf_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TT_Mtt-1000toInf_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
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
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=109290196.259,
                NEVT_UL17=276021555.615,
                NEVT_UL18=365675749.158,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
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

        "ST_t-channel_top_4f_InclusiveDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=136.02, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=5948135154.41,
                NEVT_UL16postVFP=6703801970.36,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_t-channel_top_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL16APV_v3.xml", XmlSource_UL16preVFP="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_t-channel_top_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL16_v3.xml", XmlSource_UL16postVFP="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v3/MINIAODSIM",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ST_t-channel_antitop_4f_InclusiveDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=80.95, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1983864432.65,
                NEVT_UL16postVFP=1957283183.22,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_t-channel_antitop_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL16APV_v3.xml", XmlSource_UL16preVFP="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_t-channel_antitop_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL16_v3.xml", XmlSource_UL16postVFP="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v3/MINIAODSIM",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ST_s-channel_4f_leptonDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=10.32, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.326, BRatSource_13TeV="https://pdg.lbl.gov/2021/listings/rpp2021-list-w-boson.pdf (page 5, W->lnu times 3, rounded)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=19592486.3309,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=49292566.8068,
                NEVT_UL18=68767081.0067,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_s-channel_4f_leptonDecays_CP5_amcatnlo-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_s-channel_4f_leptonDecays_CP5_amcatnlo-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_s-channel_4f_leptonDecays_CP5_amcatnlo-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WW" : {
            "CrossSection" : XSValues(
                XSec_13TeV=64.3, XSecSource_13TeV="GenXSecAnalyzer (LO)",
                XSec_UL16preVFP=64.3,
                XSec_UL16postVFP=64.3,
                XSec_UL17=64.3,
                XSec_UL18=64.3,
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "WZ" : {
            "CrossSection" : XSValues(
                XSec_13TeV=23.43, XSecSource_13TeV="XSDB (NNLO)",
                XSec_UL16preVFP=23.43,
                XSec_UL16postVFP=23.43,
                XSec_UL17=23.43,
                XSec_UL18=23.43,
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=2.01, kFacSource_13TeV="NNLO https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns",
                kFac_UL16preVFP=2.01,
                kFac_UL16postVFP=2.01,
                kFac_UL17=2.01,
                kFac_UL18=2.01,
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ZZ" : {
            "CrossSection" : XSValues(
                XSec_13TeV=10.16, XSecSource_13TeV="XSDB (NNLO)",
                XSec_UL16preVFP=10.16,
                XSec_UL16postVFP=10.16,
                XSec_UL17=10.16,
                XSec_UL18=10.16,
            ),
            "kFactor" : kFactorValues(
                kFac_13TeV=1.62, kFacSource_13TeV="NNLO https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns",
                kFac_UL16preVFP=1.62,
                kFac_UL16postVFP=1.62,
                kFac_UL17=1.62,
                kFac_UL18=1.62,
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
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
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=5543804,
                NEVT_UL18=8908406,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
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
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=4802716,
                NEVT_UL18=6166852,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
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
                XSec_13TeV=-1, XSecSource_13TeV="",
                XSec_UL16preVFP=-1, XSecSource_UL16preVFP="",
                XSec_UL16postVFP=-1, XSecSource_UL16postVFP="",
                XSec_UL17=-1, XSecSource_UL17="",
                XSec_UL18=-1, XSecSource_UL18="",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "WJetsToLNu_HT-100to200" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1395, XSecSource_13TeV="XSDB (LO)",
                XSec_UL16preVFP=1345, XSecSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                XSec_UL16postVFP=1345, XSecSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                XSec_UL17=1395, XSecSource_UL17="XSDB (LO)",
                XSec_UL18=1395, XSecSource_UL18="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "WJetsToLNu_HT-200to400" : {
            "CrossSection" : XSValues(
                XSec_13TeV=407.9, XSecSource_13TeV="XSDB (LO)",
                XSec_UL16preVFP=359.7, XSecSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                XSec_UL16postVFP=359.7, XSecSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                XSec_UL17=407.9, XSecSource_UL17="XSDB (LO)",
                XSec_UL18=407.9, XSecSource_UL18="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "WJetsToLNu_HT-400to600" : {
            "CrossSection" : XSValues(
                XSec_13TeV=57.48, XSecSource_13TeV="XSDB (LO)",
                XSec_UL16preVFP=48.9, XSecSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                XSec_UL16postVFP=48.9, XSecSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                XSec_UL17=57.48, XSecSource_UL17="XSDB (LO)",
                XSec_UL18=57.48, XSecSource_UL18="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "WJetsToLNu_HT-600to800" : {
            "CrossSection" : XSValues(
                XSec_13TeV=12.87, XSecSource_13TeV="XSDB (LO)",
                XSec_UL16preVFP=12.05, XSecSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                XSec_UL16postVFP=12.05, XSecSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                XSec_UL17=12.87, XSecSource_UL17="XSDB (LO)",
                XSec_UL18=12.87, XSecSource_UL18="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "WJetsToLNu_HT-800to1200" : {
            "CrossSection" : XSValues(
                XSec_13TeV=5.366, XSecSource_13TeV="XSDB (LO)",
                XSec_UL16preVFP=5.501, XSecSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                XSec_UL16postVFP=5.501, XSecSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                XSec_UL17=5.366, XSecSource_UL17="XSDB (LO)",
                XSec_UL18=5.366, XSecSource_UL18="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "WJetsToLNu_HT-1200to2500" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1.329, XSecSource_13TeV="XSDB (LO)",
                XSec_UL16preVFP=1.329, XSecSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                XSec_UL16postVFP=1.329, XSecSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                XSec_UL17=1.329, XSecSource_UL17="XSDB (LO)",
                XSec_UL18=1.329, XSecSource_UL18="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "WJetsToLNu_HT-2500toInf" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.03216, XSecSource_13TeV="XSDB (LO)",
                XSec_UL16preVFP=0.03216, XSecSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                XSec_UL16postVFP=0.03216, XSecSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                XSec_UL17=0.03216, XSecSource_UL17="XSDB (LO)",
                XSec_UL18=0.03216, XSecSource_UL18="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
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
                NEVT_UL16postVFP=-1,
                NEVT_UL17=13963690,
                NEVT_UL18=19810491,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
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
                NEVT_UL16postVFP=-1,
                NEVT_UL17=4418971,
                NEVT_UL18=5968910,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
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
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=1513585,
                NEVT_UL18=2129122,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
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
                NEVT_UL16postVFP=-1,
                NEVT_UL17=267125,
                NEVT_UL18=381695,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
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

        "QCD_Pt-30to50_EMEnriched" : {
            "CrossSection" : XSValues(XSec_13TeV=6.418e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=4351014.0,
                NEVT_UL17=8784542.0,
                NEVT_UL18=8574589.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-30to50_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-30to50_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-30to50_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-50to80_EMEnriched" : {
            "CrossSection" : XSValues(XSec_13TeV=1.987e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=5443934.0,
                NEVT_UL17=10210400.0,
                NEVT_UL18=10524400.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-50to80_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-50to80_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-50to80_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-80to120_EMEnriched" : {
            "CrossSection" : XSValues(XSec_13TeV=3.671e+05, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=4805600.8317,
                NEVT_UL17=9617412.94144,
                NEVT_UL18=9469962.10221,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-80to120_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-80to120_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-80to120_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-120to170_EMEnriched" : {
            "CrossSection" : XSValues(XSec_13TeV=6.661e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=5007404.35617,
                NEVT_UL17=9904361.63759,
                NEVT_UL18=9678015.18575,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-120to170_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-120to170_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-120to170_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-170to300_EMEnriched" : {
            "CrossSection" : XSValues(XSec_13TeV=1.654e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=1861129.0,
                NEVT_UL17=3678200.0,
                NEVT_UL18=3714642.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-170to300_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-170to300_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-170to300_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-300toInf_EMEnriched" : {
            "CrossSection" : XSValues(XSec_13TeV=1.100e+03, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=1138742.0,
                NEVT_UL17=2214934.0,
                NEVT_UL18=2215994.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-300toInf_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-300toInf_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-300toInf_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_HT50to100" : {
            "CrossSection" : XSValues(
                XSec_UL16preVFP=27990000, XSecSource_UL16preVFP="XSDB (LO)",
                XSec_UL16postVFP=27990000, XSecSource_UL16postVFP="XSDB (LO)",
                XSec_UL17=23610000, XSecSource_UL17="XSDB (LO)",
                XSec_UL18=25600000, XSecSource_UL18="XSDB (LO)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "QCD_HT100to200" : {
            "CrossSection" : XSValues(
                XSec_UL16preVFP=27990000, XSecSource_UL16preVFP="XSDB (LO)",
                XSec_UL16postVFP=27990000, XSecSource_UL16postVFP="XSDB (LO)",
                XSec_UL17=23610000, XSecSource_UL17="XSDB (LO)",
                XSec_UL18=25600000, XSecSource_UL18="XSDB (LO)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "QCD_HT200to300" : {
            "CrossSection" : XSValues(
                XSec_UL16preVFP=1710000, XSecSource_UL16preVFP="XSDB (LO)",
                XSec_UL16postVFP=1710000, XSecSource_UL16postVFP="XSDB (LO)",
                XSec_UL17=1547000, XSecSource_UL17="XSDB (LO)",
                XSec_UL18=1557000, XSecSource_UL18="XSDB (LO)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "QCD_HT300to500" : {
            "CrossSection" : XSValues(
                XSec_UL16preVFP=347500, XSecSource_UL16preVFP="XSDB (LO)",
                XSec_UL16postVFP=347500, XSecSource_UL16postVFP="XSDB (LO)",
                XSec_UL17=322600, XSecSource_UL17="XSDB (LO)",
                XSec_UL18=323400, XSecSource_UL18="XSDB (LO)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "QCD_HT500to700" : {
            "CrossSection" : XSValues(
                XSec_UL16preVFP=32060, XSecSource_UL16preVFP="XSDB (LO)",
                XSec_UL16postVFP=32060, XSecSource_UL16postVFP="XSDB (LO)",
                XSec_UL17=29980, XSecSource_UL17="XSDB (LO)",
                XSec_UL18=30140, XSecSource_UL18="XSDB (LO)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "QCD_HT700to1000" : {
            "CrossSection" : XSValues(
                XSec_UL16preVFP=6829, XSecSource_UL16preVFP="XSDB (LO)",
                XSec_UL16postVFP=6829, XSecSource_UL16postVFP="XSDB (LO)",
                XSec_UL17=6334, XSecSource_UL17="XSDB (LO)",
                XSec_UL18=6310, XSecSource_UL18="XSDB (LO)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "QCD_HT1000to1500" : {
            "CrossSection" : XSValues(
                XSec_UL16preVFP=1207, XSecSource_UL16preVFP="XSDB (LO)",
                XSec_UL16postVFP=1207, XSecSource_UL16postVFP="XSDB (LO)",
                XSec_UL17=1088, XSecSource_UL17="XSDB (LO)",
                XSec_UL18=1094, XSecSource_UL18="XSDB (LO)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "QCD_HT1500to2000" : {
            "CrossSection" : XSValues(
                XSec_UL16preVFP=120, XSecSource_UL16preVFP="XSDB (LO)",
                XSec_UL16postVFP=120, XSecSource_UL16postVFP="XSDB (LO)",
                XSec_UL17=99.11, XSecSource_UL17="XSDB (LO)",
                XSec_UL18=99.38, XSecSource_UL18="XSDB (LO)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "QCD_HT2000toInf" : {
            "CrossSection" : XSValues(
                XSec_UL16preVFP=25.25, XSecSource_UL16preVFP="XSDB (LO)",
                XSec_UL16postVFP=25.25, XSecSource_UL16postVFP="XSDB (LO)",
                XSec_UL17=20.23, XSecSource_UL17="XSDB (LO)",
                XSec_UL18=20.20, XSecSource_UL18="XSDB (LO)",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ZprimeToZHToZlepHinc-600": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ZprimeToZHToZlepHinc-800": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ZprimeToZHToZlepHinc-1000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ZprimeToZHToZlepHinc-1200": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ZprimeToZHToZlepHinc-1400": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ZprimeToZHToZlepHinc-1600": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ZprimeToZHToZlepHinc-1800": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ZprimeToZHToZlepHinc-2000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ZprimeToZHToZlepHinc-2500": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ZprimeToZHToZlepHinc-3000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ZprimeToZHToZlepHinc-3500": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ZprimeToZHToZlepHinc-4000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ZprimeToZHToZlepHinc-4500": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ZprimeToZHToZlepHinc-5000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ZprimeToZHToZlepHinc-5500": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ZprimeToZHToZlepHinc-6000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ZprimeToZHToZlepHinc-7000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "ZprimeToZHToZlepHinc-8000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="", XmlSource_UL18="",
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

    def get_value(self, name, energy, year, key, strict=False):
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
        fields = [self.__key_field_map[key][0]+"_"+energy,self.__key_field_map[key][0]+"_"+year]
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

    def get_xs(self, name, energy, year):
        return self.get_value(name, energy, year, "CrossSection", True)

    def get_nevt(self, name, energy, year):
        return self.get_value(name, energy, year, "NEvents", True)

    def get_br(self, name, energy, year):
        return self.get_value(name, energy, year, "BranchingRatio", False)

    def get_kfactor(self, name, energy, year):
        return self.get_value(name, energy, year, "kFactor", False)

    def get_corr(self, name, energy, year):
        return self.get_value(name, energy, year, "Correction", False)

    def get_xml(self, name, energy, year):
        return self.get_value(name, energy, year, "XMLname", False)

    def get_lumi(self, name, energy, year, kFactor=False, Corrections=False):
        xsec = self.get_xs(name, energy, year)
        xsec *= self.get_br(name, energy, year)
        if kFactor: xsec *= self.get_kfactor(name, energy, year)
        if Corrections: xsec *= self.get_corr(name, energy, year)
        return self.get_nevt(name, energy, year)/xsec
