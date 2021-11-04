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

    __years = ["2016","2017","2018"]
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
        "TTbar" : {
            "CrossSection" :   XSValues(XSec_13TeV=831.8, XSec_2016=831.8, XSecSource_13TeV="PDG XS - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"),
            "BranchingRatio" : BRValues(BRat_13TeV=1., BRatSource_13TeV="PDG BR (t=tbar) - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"),
            "NEvents" :   NEventsValues(NEVT_2016=-1),
            "XMLname" :   XMLValues(Xml_2016="UHH2-datasets/RunII_106X_v2/SM/UL17/name.xml", XmlSource_2016="/TTbar*to*/RunIISummer20MiniAODv2*/MINIAODSIM"),
        },
        "TTbarTo2L2Nu" : {
            "CrossSection" :   XSValues(XSec_13TeV=831.8, XSec_2017=831.8, XSec_2018=831.8, XSecSource_13TeV="PDG XS - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.105, BRat_2017=0.105, BRat_2018=0.105, BRatSource_13TeV="PDG BR (t=tbar) - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"),
            "NEvents" :   NEventsValues(NEVT_2017=-1, NEVT_2018=-1),
        },

        "TTbarToSemiLeptonic" : {
            "CrossSection" :   XSValues(XSec_13TeV=831.8, XSec_2017=831.8, XSec_2018=831.8, XSecSource_13TeV="PDG XS - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.438, BRat_2017=0.438, BRat_2018=0.438, BRatSource_13TeV="PDG BR (t=tbar) - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"),
            "NEvents" :   NEventsValues(NEVT_2017=-1, NEVT_2018=-1),
        },

        "TTbarToHadronic" : {
            "CrossSection" :   XSValues(XSec_13TeV=831.8, XSec_2017=831.8, XSec_2018=831.8, XSecSource_13TeV="PDG XS - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.457, BRat_2017=0.457, BRat_2018=0.457, BRatSource_13TeV="PDG BR (t=tbar) - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"),
            "NEvents" :   NEventsValues(NEVT_2017=-1, NEVT_2018=-1),
        },
        "WW" : {
            "CrossSection" :   XSValues(XSec_13TeV=64.3, XSec_2016=64.3, XSec_2017=64.3, XSec_2018=64.3, XSecSource_13TeV="GenXSecAnalyzer (LO)",),
            "kFactor" :   kFactorValues(kFac_13TeV=1.79, kFac_2016=1.79, kFac_2017=1.1374,kFac_2018=1.1421, kFacSource_13TeV="NNLO https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns",),
            "NEvents" :   NEventsValues(NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "WZ" : {
            "CrossSection" :   XSValues(XSec_13TeV=23.43, XSec_2016=23.43, XSec_2017=23.43, XSec_2018=23.43, XSecSource_13TeV="XSDB (NNLO)",),
            "kFactor" :   kFactorValues(kFac_13TeV=2.01,  kFac_2016=2.01, kFac_2017=2.01,kFac_2018=2.01, kFacSource_13TeV="NNLO https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns",),
            "NEvents" :   NEventsValues(NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZZ" : {
            "CrossSection" :   XSValues(XSec_13TeV=10.16, XSec_2016=10.16, XSec_2017=10.16, XSec_2018=10.16, XSecSource_13TeV="XSDB (NNLO)",),
            "kFactor" :   kFactorValues(kFac_13TeV=1.62,  kFac_2016=1.62, kFac_2017=1.62,kFac_2018=1.62, kFacSource_13TeV="NNLO https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns",),
            "NEvents" :   NEventsValues(NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },

        "DYJetsToLL_M-50_HT-100to200" : {
            "CrossSection" : XSValues( XSec_13TeV=150,XSec_2016=147.4, XSec_2017=161.1, XSec_2018=160.8, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="XSDB (LO)",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.2245,kFac_2017=1.1374,kFac_2018=1.1421,kFacSource_2016="XSDB NNLO/LO=6077.22/4963", kFacSource_2017="XSDB NNLO/LO=6077.22/5343", kFacSource_2018="XSDB NNLO/LO=6077.22/5321",),
            "Correction" : CorrValues( CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M", CorrSource_2018="Same as 2017",),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "DYJetsToLL_M-50_HT-200to400" : {
            "CrossSection" : XSValues( XSec_13TeV=40.99,XSec_2016=41.04, XSec_2017=48.66, XSec_2018=48.61, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="GenXSecAnalyzer",),
            "kFactor" : kFactorValues( kFac_2016=1.2245,kFac_2017=1.1374,kFac_2018=1.1421, kFacSource_2016="XSDB NNLO/LO=6077.22/4963", kFacSource_2017="XSDB NNLO/LO=6077.22/5343", kFacSource_2018="XSDB NNLO/LO=6077.22/5321",),
            "Correction" : CorrValues( Corr_2017=0.999, Corr_2018=0.999, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M", CorrSource_2018="Same as 2017"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "DYJetsToLL_M-50_HT-400to600" : {
            "CrossSection" : XSValues( XSec_13TeV=5.678,XSec_2016=5.674, XSec_2017=6.968, XSec_2018=6.978, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.2245,kFac_2017=1.1374,kFac_2018=1.1421, kFacSource_2016="XSDB NNLO/LO=6077.22/4963", kFacSource_2017="XSDB NNLO/LO=6077.22/5343", kFacSource_2018="XSDB NNLO/LO=6077.22/5321",),
            "Correction" : CorrValues( Corr_2017=0.990, Corr_2018=0.990,CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M", CorrSource_2018="Same as 2017"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "DYJetsToLL_M-50_HT-600to800" : {
            "CrossSection" : XSValues( XSec_13TeV=1.367,XSec_2016=1.358, XSec_2017=1.743, XSec_2018=1.757,XSecSource_13TeV="XSDB (LO)", XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="GenXSecAnalyzer",),
            "kFactor" : kFactorValues( kFac_2016=1.2245,kFac_2017=1.1374,kFac_2018=1.1421, kFacSource_2016="XSDB NNLO/LO=6077.22/4963", kFacSource_2017="XSDB NNLO/LO=6077.22/5343", kFacSource_2018="XSDB NNLO/LO=6077.22/5321",),
            "Correction" : CorrValues( Corr_2017=0.975, Corr_2018=0.975,CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M", CorrSource_2018="Same as 2017"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "DYJetsToLL_M-50_HT-800to1200" : {
            "CrossSection" : XSValues( XSec_13TeV=0.6304,XSec_2016=0.6229, XSec_2017=0.8052, XSec_2018=0.8094,XSecSource_13TeV="XSDB (LO)", XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="GenXSecAnalyzer",),
            "kFactor" : kFactorValues( kFac_2016=1.2245,kFac_2017=1.1374,kFac_2018=1.1421, kFacSource_2016="XSDB NNLO/LO=6077.22/4963", kFacSource_2017="XSDB NNLO/LO=6077.22/5343", kFacSource_2018="XSDB NNLO/LO=6077.22/5321",),
            "Correction" : CorrValues( Corr_2017=0.907, Corr_2018=0.907,CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M", CorrSource_2018="Same as 2017"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "DYJetsToLL_M-50_HT-1200to2500" : {
            "CrossSection" : XSValues( XSec_13TeV=0.1514,XSec_2016=0.1512, XSec_2017=0.1933, XSec_2018=0.1931,XSecSource_13TeV="XSDB (LO)", XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="GenXSecAnalyzer",),
            "kFactor" : kFactorValues( kFac_2016=1.2245,kFac_2017=1.1374,kFac_2018=1.1421, kFacSource_2016="XSDB NNLO/LO=6077.22/4963", kFacSource_2017="XSDB NNLO/LO=6077.22/5343", kFacSource_2018="XSDB NNLO/LO=6077.22/5321",),
            "Correction" : CorrValues( Corr_2017=0.833, Corr_2018=0.833,CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M", CorrSource_2018="Same as 2017"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "DYJetsToLL_M-50_HT-2500toInf" : {
            "CrossSection" : XSValues( XSec_13TeV=0.003565,XSec_2016=0.003659, XSec_2017=0.003468, XSec_2018=0.003514,XSecSource_13TeV="XSDB (LO)", XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="GenXSecAnalyzer",),
            "kFactor" : kFactorValues( kFac_2016=1.2245,kFac_2017=1.1374,kFac_2018=1.1421, kFacSource_2016="XSDB NNLO/LO=6077.22/4963", kFacSource_2017="XSDB NNLO/LO=6077.22/5343", kFacSource_2018="XSDB NNLO/LO=6077.22/5321",),
            "Correction" : CorrValues( Corr_2017=1.015, Corr_2018=1.015,CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M", CorrSource_2018="Same as 2017"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "WJetsToLNu_HT-100to200" : {
            "CrossSection" : XSValues( XSec_13TeV=1395,XSec_2016=1345, XSec_2017=1395, XSec_2018=1395, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.21,kFac_2017=1.21,kFac_2018=1.21,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "WJetsToLNu_HT-200to400" : {
            "CrossSection" : XSValues( XSec_13TeV=407.9,XSec_2016=359.7, XSec_2017=407.9, XSec_2018=407.9, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.21,kFac_2017=1.21,kFac_2018=1.21,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "WJetsToLNu_HT-400to600" : {
            "CrossSection" : XSValues( XSec_13TeV=57.48,XSec_2016=48.9, XSec_2017=57.48, XSec_2018=57.48, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.21,kFac_2017=1.21,kFac_2018=1.21,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "WJetsToLNu_HT-600to800" : {
            "CrossSection" : XSValues( XSec_13TeV=12.87,XSec_2016=12.05, XSec_2017=12.87, XSec_2018=12.87, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.21,kFac_2017=1.21,kFac_2018=1.21,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "WJetsToLNu_HT-800to1200" : {
            "CrossSection" : XSValues( XSec_13TeV=5.366,XSec_2016=5.501, XSec_2017=5.366, XSec_2018=5.366, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.21,kFac_2017=1.21,kFac_2018=1.21,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "WJetsToLNu_HT-1200to2500" : {
            "CrossSection" : XSValues( XSec_13TeV=1.329,XSec_2016=1.329, XSec_2017=1.329, XSec_2018=1.329, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.21,kFac_2017=1.21,kFac_2018=1.21,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "WJetsToLNu_HT-2500toInf" : {
            "CrossSection" : XSValues( XSec_13TeV=0.03216,XSec_2016=0.03216, XSec_2017=0.03216, XSec_2018=0.03216, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.21,kFac_2017=1.21,kFac_2018=1.21,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZJetsToNuNu_HT-100to200" : {
            "CrossSection" : XSValues( XSec_13TeV=302.8,XSec_2016=280.35, XSec_2017=302.8, XSec_2018=302.8, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.23,kFac_2017=1.23,kFac_2018=1.23,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZJetsToNuNu_HT-200to400" : {
            "CrossSection" : XSValues( XSec_13TeV=92.59,XSec_2016=77.67, XSec_2017=92.59, XSec_2018=92.59, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.23,kFac_2017=1.23,kFac_2018=1.23,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZJetsToNuNu_HT-400to600" : {
            "CrossSection" : XSValues( XSec_13TeV=13.18,XSec_2016=10.73, XSec_2017=13.18, XSec_2018=13.18, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.23,kFac_2017=1.23,kFac_2018=1.23,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZJetsToNuNu_HT-600to800" : {
            "CrossSection" : XSValues( XSec_13TeV=3.257,XSec_2016=2.559, XSec_2017=3.257, XSec_2018=3.257, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.23,kFac_2017=1.23,kFac_2018=1.23,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZJetsToNuNu_HT-800to1200" : {
            "CrossSection" : XSValues( XSec_13TeV=1.49,XSec_2016=1.1796, XSec_2017=1.49, XSec_2018=1.49, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.23,kFac_2017=1.23,kFac_2018=1.23,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZJetsToNuNu_HT-1200to2500" : {
            "CrossSection" : XSValues( XSec_13TeV=0.3419,XSec_2016=0.28833, XSec_2017=0.3419, XSec_2018=0.3419, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.23,kFac_2017=1.23,kFac_2018=1.23,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZJetsToNuNu_HT-2500toInf" : {
            "CrossSection" : XSValues( XSec_13TeV=0.006945,XSec_2016=0.006945, XSec_2017=0.006945, XSec_2018=0.006945, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.23,kFac_2017=1.23,kFac_2018=1.23,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZprimeToZHToZlepHinc-600": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZprimeToZHToZlepHinc-800": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZprimeToZHToZlepHinc-1000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZprimeToZHToZlepHinc-1200": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZprimeToZHToZlepHinc-1400": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZprimeToZHToZlepHinc-1600": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZprimeToZHToZlepHinc-1800": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZprimeToZHToZlepHinc-2000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZprimeToZHToZlepHinc-2500": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZprimeToZHToZlepHinc-3000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZprimeToZHToZlepHinc-3500": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZprimeToZHToZlepHinc-4000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZprimeToZHToZlepHinc-4500": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZprimeToZHToZlepHinc-5000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZprimeToZHToZlepHinc-5500": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZprimeToZHToZlepHinc-6000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZprimeToZHToZlepHinc-7000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "ZprimeToZHToZlepHinc-8000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },

        "SingleMuon_RunA": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SingleMuon_RunB": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SingleMuon_RunC": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SingleMuon_RunD": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SingleMuon_RunE": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SingleMuon_RunF": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SingleMuon_RunG": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SingleMuon_RunH": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },

        "SingleElectron_RunA": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SingleElectron_RunB": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SingleElectron_RunC": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SingleElectron_RunD": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SingleElectron_RunE": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SingleElectron_RunF": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SingleElectron_RunG": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SingleElectron_RunH": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },

        "SinglePhoton_RunA": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SinglePhoton_RunB": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SinglePhoton_RunC": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SinglePhoton_RunD": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SinglePhoton_RunE": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SinglePhoton_RunF": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SinglePhoton_RunG": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SinglePhoton_RunH": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },

        "MET_RunA": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "MET_RunB": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "MET_RunC": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "MET_RunD": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "MET_RunE": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "MET_RunF": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "MET_RunG": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "MET_RunH": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },

        "QCD_HT100to200" : {
            "CrossSection" : XSValues( XSec_2016=27990000, XSec_2017=23610000, XSec_2018=25600000, XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "QCD_HT200to300" : {
            "CrossSection" : XSValues( XSec_2016=1710000, XSec_2017=1547000, XSec_2018=1557000, XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "QCD_HT300to500" : {
            "CrossSection" : XSValues( XSec_2016=347500, XSec_2017=322600, XSec_2018=323400, XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "QCD_HT500to700" : {
            "CrossSection" : XSValues( XSec_2016=32060, XSec_2017=29980, XSec_2018=30140, XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "QCD_HT700to1000" : {
            "CrossSection" : XSValues( XSec_2016=6829, XSec_2017=6334, XSec_2018=6310, XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "QCD_HT1000to1500" : {
            "CrossSection" : XSValues( XSec_2016=1207, XSec_2017=1088, XSec_2018=1094, XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "QCD_HT1500to2000" : {
            "CrossSection" : XSValues( XSec_2016=120, XSec_2017=99.11, XSec_2018=99.38, XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "QCD_HT2000toInf" : {
            "CrossSection" : XSValues( XSec_2016=25.25, XSec_2017=20.23, XSec_2018=20.20, XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=-1991645, NEVT_2017=-1, NEVT_2018=-1),
        },

        # #not yet verified
        # "WJetsToLNu" : {
        #     "CrossSection" : XSValues(
        #         XSec_13TeV=61526.7, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#W_jets NNLO (60430.0 @ NLO)",
        #         XSec_2016=50260, XSecSource_2016="XSDB (LO)",
        #         XSec_2017=52940, XSecSource_2017="XSDB (LO)",
        #         XSec_2018=52850, XSecSource_2018="XSDB (LO)",
        #     ),
        # },
        # "WJetsToQQ_HT400to600_qc19_3j" : {
        #     "CrossSection" : XSValues(
        #         XSec_2017=315.2, XSecSource_2017="GenXSecAnalyzer",
        #         XSec_2018=314.6, XSecSource_2018="GenXSecAnalyzer",
        #     ),
        # },
        # "WJetsToQQ_HT600to800_qc19_3j" : {
        #     "CrossSection" : XSValues(
        #         XSec_2017=68.61, XSecSource_2017="GenXSecAnalyzer",
        #         XSec_2018=68.58, XSecSource_2018="GenXSecAnalyzer",
        #     ),
        # },
        # "WJetsToQQ_HT-800toInf_qc19_3j" : {
        #     "CrossSection" : XSValues(
        #         XSec_2017=34.71, XSecSource_2017="GenXSecAnalyzer",
        #         XSec_2018=34.74, XSecSource_2018="GenXSecAnalyzer",
        #     ),
        # },
        # "WJetsToQQ_HT-600toInf" : {
        #     "CrossSection" : XSValues(
        #         XSec_2016=99.65, XSecSource_2016="XSDB (LO)"
        #     ),
        # },
        #
        # "DYJetsToLL_M-50" : {
        #     "CrossSection" : XSValues( XSec_13TeV=6077.22, XSecSource_13TeV="XSDB (NNLO)",),
        # },
        # "WWTo2L2Nu" : {
        #     "CrossSection" : XSValues(
        #         XSec_13TeV=12.178, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson, WW>2l2v NNLO",
        #     ),
        # },
        #
        # "WWTo1L1Nu2Q" : {
        #     "CrossSection" : XSValues(
        #         XSec_2016=45.68, XSecSource_2016="XSDB (LO)",
        #         XSec_2017=80.74, XSecSource_2017="XSDB (LO)",
        #         XSec_2018=81.46, XSecSource_2018="GenXSecAnalyzer",
        #     ),
        # },
        # "WZTo1L1Nu2Q" : {
        #     "CrossSection" : XSValues(
        #         XSec_2016=10.73, XSecSource_2016="XSDB (LO)",
        #         XSec_2017=11.66, XSecSource_2017="XSDB (LO)",
        #         XSec_2018=11.76, XSecSource_2018="GenXSecAnalyzer",
        #     ),
        # },
        # "WZTo1L3Nu" : {
        #     "CrossSection" : XSValues(
        #         XSec_2016=3.054, XSecSource_2016="XSDB (LO)",
        #         XSec_2017=3.294, XSecSource_2017="GenXSecAnalyzer",
        #         XSec_2018=3.322, XSecSource_2018="GenXSecAnalyzer",
        #     ),
        # },
        # "ZZTo2L2Nu" : {
        #     "CrossSection" : XSValues(
        #         XSec_2016=0.5644, XSecSource_2016="GenXSecAnalyzer",
        #         XSec_2017=0.6008, XSecSource_2017="GenXSecAnalyzer",
        #         XSec_2018=0.6008, XSecSource_2018="GenXSecAnalyzer",
        #     ),
        # },
        # "ZZTo2L2Q" : {
        #     "CrossSection" : XSValues(
        #         XSec_2016=3.222, XSecSource_2016="XSDB (unknown)",
        #         XSec_2017=3.688, XSecSource_2017="XSDB (unknown)",
        #         XSec_2018=3.709, XSecSource_2018="GenXSecAnalyzer",
        #     ),
        # },
        # "ZZTo2Q2Nu" : {
        #     "CrossSection" : XSValues(
        #         XSec_2016=4.033, XSecSource_2016="XSDB (unknown)",
        #     ),
        # },

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
