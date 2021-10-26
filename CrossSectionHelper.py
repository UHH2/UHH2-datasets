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
    """

    __years = ["2016","2017","2018"]
    __energies = ["13TeV"]
    __xs_field_names = []
    __nevt_field_names = []
    __br_field_names = []
    __kfactor_field_names = []
    __corr_field_names = []
    __key_field_map = {
        "CrossSection"   : ("XSec",-1.0),
        "NEvents"        : ("NEVT",-1.0),
        "BranchingRatio" : ("BRat",1.0),
        "kFactor"        : ("kFac",1.0),
        "Correction"     : ("Corr",1.0),
    }
    for __val in __years+__energies:
        for mode in ["", "Source"]:
            __xs_field_names.append("XSec"+mode+"_"+__val)
            __nevt_field_names.append("NEVT"+mode+"_"+__val)
            __br_field_names.append("BRat"+mode+"_"+__val)
            __kfactor_field_names.append("kFac"+mode+"_"+__val)
            __corr_field_names.append("Corr"+mode+"_"+__val)
    XSValues      = namedtuple_with_defaults("XSValues",      __xs_field_names,       [__key_field_map["CrossSection"][1],""]*len(__years+__energies))
    NEventsValues = namedtuple_with_defaults("NEventsValues", __nevt_field_names,     [__key_field_map["NEvents"][1],""]*len(__years+__energies))
    BRValues      = namedtuple_with_defaults("BRValues",      __br_field_names,       [__key_field_map["BranchingRatio"][1],""]*len(__years+__energies))
    kFactorValues = namedtuple_with_defaults("kFactorValues", __kfactor_field_names,  [__key_field_map["kFactor"][1],""]*len(__years+__energies))
    CorrValues    = namedtuple_with_defaults("CorrValues",    __corr_field_names,     [__key_field_map["Correction"][1],""]*len(__years+__energies))

    __values_dict = {
        "TTbar" : {
            "CrossSection" :   XSValues(XSec_13TeV=831.8, XSec_2016=831.8, XSecSource_13TeV="PDG XS - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"),
            "BranchingRatio" : BRValues(BRat_13TeV=1., BRatSource_13TeV="PDG BR (t=tbar) - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"),
            "NEvents" :   NEventsValues(NEVT_2016=76738314),
        },
        "TTbarTo2L2Nu" : {
            "CrossSection" :   XSValues(XSec_13TeV=831.8, XSec_2017=831.8, XSec_2018=831.8, XSecSource_13TeV="PDG XS - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.105, BRat_2017=0.105, BRat_2018=0.105, BRatSource_13TeV="PDG BR (t=tbar) - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"),
            "NEvents" :   NEventsValues(NEVT_2017=648729904, NEVT_2018=4635769526),
        },

        "TTbarToSemiLeptonic" : {
            "CrossSection" :   XSValues(XSec_13TeV=831.8, XSec_2017=831.8, XSec_2018=831.8, XSecSource_13TeV="PDG XS - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.438, BRat_2017=0.438, BRat_2018=0.438, BRatSource_13TeV="PDG BR (t=tbar) - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"),
            "NEvents" :   NEventsValues(NEVT_2017=12852869550, NEVT_2018=30513654675),
        },

        "TTbarToHadronic" : {
            "CrossSection" :   XSValues(XSec_13TeV=831.8, XSec_2017=831.8, XSec_2018=831.8, XSecSource_13TeV="PDG XS - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.457, BRat_2017=0.457, BRat_2018=0.457, BRatSource_13TeV="PDG BR (t=tbar) - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"),
            "NEvents" :   NEventsValues(NEVT_2017=41618896, NEVT_2018=41941925823),
        },
        "WW" : {
            "CrossSection" :   XSValues(XSec_13TeV=64.3, XSec_2016=64.3, XSec_2017=64.3, XSec_2018=64.3, XSecSource_13TeV="GenXSecAnalyzer (LO)",),
            "kFactor" :   kFactorValues(kFac_13TeV=1.79, kFac_2016=1.79, kFac_2017=1.1374,kFac_2018=1.1421, kFacSource_13TeV="NNLO https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns",),
            "NEvents" :   NEventsValues(NEVT_2016=7982310, NEVT_2017=7765891, NEVT_2018=7846136),
        },
        "WZ" : {
            "CrossSection" :   XSValues(XSec_13TeV=23.43, XSec_2016=23.43, XSec_2017=23.43, XSec_2018=23.43, XSecSource_13TeV="XSDB (NNLO)",),
            "kFactor" :   kFactorValues(kFac_13TeV=2.01,  kFac_2016=2.01, kFac_2017=2.01,kFac_2018=2.01, kFacSource_13TeV="NNLO https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns",),
            "NEvents" :   NEventsValues(NEVT_2016=3997571, NEVT_2017=3901180, NEVT_2018=3884167),
        },
        "ZZ" : {
            "CrossSection" :   XSValues(XSec_13TeV=10.16, XSec_2016=10.16, XSec_2017=10.16, XSec_2018=10.16, XSecSource_13TeV="XSDB (NNLO)",),
            "kFactor" :   kFactorValues(kFac_13TeV=1.62,  kFac_2016=1.62, kFac_2017=1.62,kFac_2018=1.62, kFacSource_13TeV="NNLO https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns",),
            "NEvents" :   NEventsValues(NEVT_2016=1988098, NEVT_2017=1928489, NEVT_2018=1978777),
        },

        "DYJetsToLL_M-50_HT-100to200" : {
            "CrossSection" : XSValues( XSec_13TeV=147.4,XSec_2016=147.4, XSec_2017=161.1, XSec_2018=160.8, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="XSDB (LO)",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.2245,kFac_2017=1.1374,kFac_2018=1.1421,kFacSource_2016="XSDB NNLO/LO=6077.22/4963", kFacSource_2017="XSDB NNLO/LO=6077.22/5343", kFacSource_2018="XSDB NNLO/LO=6077.22/5321",),
            "Correction" : CorrValues( Corr_2017=1.000, Corr_2018=1.000, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M", CorrSource_2018="Same as 2017",),
            "NEvents" : NEventsValues( NEVT_2016=10977326, NEVT_2017=11180126, NEVT_2018=11516746),
        },
        "DYJetsToLL_M-50_HT-200to400" : {
            "CrossSection" : XSValues( XSec_13TeV=40.99,XSec_2016=41.04, XSec_2017=48.66, XSec_2018=48.61, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="GenXSecAnalyzer",),
            "kFactor" : kFactorValues( kFac_2016=1.2245,kFac_2017=1.1374,kFac_2018=1.1421, kFacSource_2016="XSDB NNLO/LO=6077.22/4963", kFacSource_2017="XSDB NNLO/LO=6077.22/5343", kFacSource_2018="XSDB NNLO/LO=6077.22/5321",),
            "Correction" : CorrValues( Corr_2017=0.999, Corr_2018=0.999, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M", CorrSource_2018="Same as 2017"),
            "NEvents" : NEventsValues( NEVT_2016=9589193, NEVT_2017=10675441, NEVT_2018=11204573),
        },
        "DYJetsToLL_M-50_HT-400to600" : {
            "CrossSection" : XSValues( XSec_13TeV=5.678,XSec_2016=5.674, XSec_2017=6.968, XSec_2018=6.978, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.2245,kFac_2017=1.1374,kFac_2018=1.1421, kFacSource_2016="XSDB NNLO/LO=6077.22/4963", kFacSource_2017="XSDB NNLO/LO=6077.22/5343", kFacSource_2018="XSDB NNLO/LO=6077.22/5321",),
            "Correction" : CorrValues( Corr_2017=0.990, Corr_2018=0.990,CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M", CorrSource_2018="Same as 2017"),
            "NEvents" : NEventsValues( NEVT_2016=9725661, NEVT_2017=10174800, NEVT_2018=9667789),
        },
        "DYJetsToLL_M-50_HT-600to800" : {
            "CrossSection" : XSValues( XSec_13TeV=1.367,XSec_2016=1.358, XSec_2017=1.743, XSec_2018=1.757,XSecSource_13TeV="XSDB (LO)", XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="GenXSecAnalyzer",),
            "kFactor" : kFactorValues( kFac_2016=1.2245,kFac_2017=1.1374,kFac_2018=1.1421, kFacSource_2016="XSDB NNLO/LO=6077.22/4963", kFacSource_2017="XSDB NNLO/LO=6077.22/5343", kFacSource_2018="XSDB NNLO/LO=6077.22/5321",),
            "Correction" : CorrValues( Corr_2017=0.975, Corr_2018=0.975,CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M", CorrSource_2018="Same as 2017"),
            "NEvents" : NEventsValues( NEVT_2016=8253178, NEVT_2017=8691608, NEVT_2018=8826238),
        },
        "DYJetsToLL_M-50_HT-800to1200" : {
            "CrossSection" : XSValues( XSec_13TeV=0.6304,XSec_2016=0.6229, XSec_2017=0.8052, XSec_2018=0.8094,XSecSource_13TeV="XSDB (LO)", XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="GenXSecAnalyzer",),
            "kFactor" : kFactorValues( kFac_2016=1.2245,kFac_2017=1.1374,kFac_2018=1.1421, kFacSource_2016="XSDB NNLO/LO=6077.22/4963", kFacSource_2017="XSDB NNLO/LO=6077.22/5343", kFacSource_2018="XSDB NNLO/LO=6077.22/5321",),
            "Correction" : CorrValues( Corr_2017=0.907, Corr_2018=0.907,CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M", CorrSource_2018="Same as 2017"),
            "NEvents" : NEventsValues( NEVT_2016=2673066, NEVT_2017=3089712, NEVT_2018=3097089),
        },
        "DYJetsToLL_M-50_HT-1200to2500" : {
            "CrossSection" : XSValues( XSec_13TeV=0.1514,XSec_2016=0.1512, XSec_2017=0.1933, XSec_2018=0.1931,XSecSource_13TeV="XSDB (LO)", XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="GenXSecAnalyzer",),
            "kFactor" : kFactorValues( kFac_2016=1.2245,kFac_2017=1.1374,kFac_2018=1.1421, kFacSource_2016="XSDB NNLO/LO=6077.22/4963", kFacSource_2017="XSDB NNLO/LO=6077.22/5343", kFacSource_2018="XSDB NNLO/LO=6077.22/5321",),
            "Correction" : CorrValues( Corr_2017=0.833, Corr_2018=0.833,CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M", CorrSource_2018="Same as 2017"),
            "NEvents" : NEventsValues( NEVT_2016=596079, NEVT_2017=616923, NEVT_2018=531567),
        },
        "DYJetsToLL_M-50_HT-2500toInf" : {
            "CrossSection" : XSValues( XSec_13TeV=0.003565,XSec_2016=0.003659, XSec_2017=0.003468, XSec_2018=0.003514,XSecSource_13TeV="XSDB (LO)", XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="GenXSecAnalyzer",),
            "kFactor" : kFactorValues( kFac_2016=1.2245,kFac_2017=1.1374,kFac_2018=1.1421, kFacSource_2016="XSDB NNLO/LO=6077.22/4963", kFacSource_2017="XSDB NNLO/LO=6077.22/5343", kFacSource_2018="XSDB NNLO/LO=6077.22/5321",),
            "Correction" : CorrValues( Corr_2017=1.015, Corr_2018=1.015,CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M", CorrSource_2018="Same as 2017"),
            "NEvents" : NEventsValues( NEVT_2016=399492, NEVT_2017=401334, NEVT_2018=415517),
        },
        "WJetsToLNu_HT-100to200" : {
            "CrossSection" : XSValues( XSec_13TeV=1395,XSec_2016=1345, XSec_2017=1395, XSec_2018=1395, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.21,kFac_2017=1.21,kFac_2018=1.21,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=38593839, NEVT_2017=32948954, NEVT_2018=29611903),
        },
        "WJetsToLNu_HT-200to400" : {
            "CrossSection" : XSValues( XSec_13TeV=407.9,XSec_2016=359.7, XSec_2017=407.9, XSec_2018=407.9, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.21,kFac_2017=1.21,kFac_2018=1.21,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=19069732, NEVT_2017=18463508, NEVT_2018=25468933),
        },
        "WJetsToLNu_HT-400to600" : {
            "CrossSection" : XSValues( XSec_13TeV=57.48,XSec_2016=48.9, XSec_2017=57.48, XSec_2018=57.48, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.21,kFac_2017=1.21,kFac_2018=1.21,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=7759701, NEVT_2017=14313274, NEVT_2018=5932701),
        },
        "WJetsToLNu_HT-600to800" : {
            "CrossSection" : XSValues( XSec_13TeV=12.87,XSec_2016=12.05, XSec_2017=12.87, XSec_2018=12.87, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.21,kFac_2017=1.21,kFac_2018=1.21,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=18687480, NEVT_2017=21709087, NEVT_2018=19771294),
        },
        "WJetsToLNu_HT-800to1200" : {
            "CrossSection" : XSValues( XSec_13TeV=5.366,XSec_2016=5.501, XSec_2017=5.366, XSec_2018=5.366, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.21,kFac_2017=1.21,kFac_2018=1.21,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=7830536, NEVT_2017=11261008, NEVT_2018=8192251),
        },
        "WJetsToLNu_HT-1200to2500" : {
            "CrossSection" : XSValues( XSec_13TeV=1.329,XSec_2016=1.329, XSec_2017=1.329, XSec_2018=1.329, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.21,kFac_2017=1.21,kFac_2018=1.21,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=6872441, NEVT_2017=39070488, NEVT_2018=7542264),
        },
        "WJetsToLNu_HT-2500toInf" : {
            "CrossSection" : XSValues( XSec_13TeV=0.03216,XSec_2016=0.03216, XSec_2017=0.03216, XSec_2018=0.03216, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.21,kFac_2017=1.21,kFac_2018=1.21,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=2637821, NEVT_2017=20467960, NEVT_2018=3119311),
        },
        "ZJetsToNuNu_HT-100to200" : {
            "CrossSection" : XSValues( XSec_13TeV=302.8,XSec_2016=280.35, XSec_2017=302.8, XSec_2018=302.8, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.23,kFac_2017=1.23,kFac_2018=1.23,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=19026540, NEVT_2017=22737266, NEVT_2018=23702894),
        },
        "ZJetsToNuNu_HT-200to400" : {
            "CrossSection" : XSValues( XSec_13TeV=92.59,XSec_2016=77.67, XSec_2017=92.59, XSec_2018=92.59, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.23,kFac_2017=1.23,kFac_2018=1.23,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=5136083, NEVT_2017=21675916, NEVT_2018=23276346),
        },
        "ZJetsToNuNu_HT-400to600" : {
            "CrossSection" : XSValues( XSec_13TeV=13.18,XSec_2016=10.73, XSec_2017=13.18, XSec_2018=13.18, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.23,kFac_2017=1.23,kFac_2018=1.23,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=8771480, NEVT_2017=9134120, NEVT_2018=10928927),
        },
        "ZJetsToNuNu_HT-600to800" : {
            "CrossSection" : XSValues( XSec_13TeV=3.257,XSec_2016=2.559, XSec_2017=3.257, XSec_2018=3.257, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.23,kFac_2017=1.23,kFac_2018=1.23,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=5766322, NEVT_2017=5697594, NEVT_2018=5748975),
        },
        "ZJetsToNuNu_HT-800to1200" : {
            "CrossSection" : XSValues( XSec_13TeV=1.49,XSec_2016=1.1796, XSec_2017=1.49, XSec_2018=1.49, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.23,kFac_2017=1.23,kFac_2018=1.23,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=2170137, NEVT_2017=2058077, NEVT_2018=2066798),
        },
        "ZJetsToNuNu_HT-1200to2500" : {
            "CrossSection" : XSValues( XSec_13TeV=0.3419,XSec_2016=0.28833, XSec_2017=0.3419, XSec_2018=0.3419, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.23,kFac_2017=1.23,kFac_2018=1.23,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=143957, NEVT_2017=334332, NEVT_2018=343198),
        },
        "ZJetsToNuNu_HT-2500toInf" : {
            "CrossSection" : XSValues( XSec_13TeV=0.006945,XSec_2016=0.006945, XSec_2017=0.006945, XSec_2018=0.006945, XSecSource_13TeV="XSDB (LO)", XSecSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",XSecSource_2017="XSDB (LO)",XSecSource_2018="GenXSecAnalyzer"),
            "kFactor" : kFactorValues( kFac_2016=1.23,kFac_2017=1.23,kFac_2018=1.23,kFacSource_2016="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2017="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns", kFacSource_2018="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns"),
            "NEvents" : NEventsValues( NEVT_2016=405030, NEVT_2017=6446, NEVT_2018=350181),
        },
        "ZprimeToZHToZlepHinc-600": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=97900, NEVT_2017=100000, NEVT_2018=99975),
        },
        "ZprimeToZHToZlepHinc-800": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=80800, NEVT_2017=100000, NEVT_2018=99968),
        },
        "ZprimeToZHToZlepHinc-1000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=95200, NEVT_2017=100000, NEVT_2018=99962),
        },
        "ZprimeToZHToZlepHinc-1200": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=96800, NEVT_2017=100000, NEVT_2018=99957),
        },
        "ZprimeToZHToZlepHinc-1400": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=99600, NEVT_2017=100000, NEVT_2018=99950),
        },
        "ZprimeToZHToZlepHinc-1600": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=100000, NEVT_2017=100000, NEVT_2018=99945),
        },
        "ZprimeToZHToZlepHinc-1800": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=97200, NEVT_2017=100000, NEVT_2018=99949),
        },
        "ZprimeToZHToZlepHinc-2000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=99800, NEVT_2017=100000, NEVT_2018=99946),
        },
        "ZprimeToZHToZlepHinc-2500": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=95800, NEVT_2017=100000, NEVT_2018=99934),
        },
        "ZprimeToZHToZlepHinc-3000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=99700, NEVT_2017=100000, NEVT_2018=99919),
        },
        "ZprimeToZHToZlepHinc-3500": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=100000, NEVT_2017=100000, NEVT_2018=99885),
        },
        "ZprimeToZHToZlepHinc-4000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=85000, NEVT_2017=100000, NEVT_2018=99830),
        },
        "ZprimeToZHToZlepHinc-4500": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=94000, NEVT_2017=97000, NEVT_2018=99787),
        },
        "ZprimeToZHToZlepHinc-5000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=100000, NEVT_2017=100000, NEVT_2018=99643),
        },
        "ZprimeToZHToZlepHinc-5500": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=92800, NEVT_2017=100000, NEVT_2018=99448),
        },
        "ZprimeToZHToZlepHinc-6000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=92300, NEVT_2017=100000, NEVT_2018=99071),
        },
        "ZprimeToZHToZlepHinc-7000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=98400, NEVT_2017=98000, NEVT_2018=98113),
        },
        "ZprimeToZHToZlepHinc-8000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues( NEVT_2016=100000, NEVT_2017=99000, NEVT_2018=96483),
        },

        "SingleMuon_RunA": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=241488232),
            #TOT in DAS NEVT_2018=241608232
        },
        "SingleMuon_RunB": {
            "NEvents" : NEventsValues( NEVT_2016=160755411, NEVT_2017=136300266, NEVT_2018=119918017),
            #TOT in DAS NEVT_2016=158145722+2789243
        },
        "SingleMuon_RunC": {
            "NEvents" : NEventsValues( NEVT_2016=67441308, NEVT_2017=165563725, NEVT_2018=110032072),
            #TOT in DAS NEVT_2017=165652756
        },
        "SingleMuon_RunD": {
            "NEvents" : NEventsValues( NEVT_2016=98017996, NEVT_2017=70361660, NEVT_2018=514116477),
        },
        "SingleMuon_RunE": {
            "NEvents" : NEventsValues( NEVT_2016=90984718, NEVT_2017=154630534, NEVT_2018=-1),
        },
        "SingleMuon_RunF": {
            "NEvents" : NEventsValues( NEVT_2016=65489554, NEVT_2017=242135500, NEVT_2018=-1),
        },
        "SingleMuon_RunG": {
            "NEvents" : NEventsValues( NEVT_2016=149912248, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SingleMuon_RunH": {
            "NEvents" : NEventsValues( NEVT_2016=174035164, NEVT_2017=-1, NEVT_2018=-1),
        },

        "SingleElectron_RunA": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=327233402),
            #TOT in DAS NEVT_2018=327843843
        },
        "SingleElectron_RunB": {
            "NEvents" : NEventsValues( NEVT_2016=247863259, NEVT_2017=60515844, NEVT_2018=153822427),
            #TOT in DAS NEVT_2016=246440440+1422819, NEVT_2017=60537490
        },
        "SingleElectron_RunC": {
            "NEvents" : NEventsValues( NEVT_2016=97259854, NEVT_2017=136637888, NEVT_2018=147827904),
        },
        "SingleElectron_RunD": {
            "NEvents" : NEventsValues( NEVT_2016=148167727, NEVT_2017=51386033, NEVT_2018=754778781),
            #TOT in DAS NEVT_2017=51526710, NEVT_2018=754798781
        },
        "SingleElectron_RunE": {
            "NEvents" : NEventsValues( NEVT_2016=117321545, NEVT_2017=102121689, NEVT_2018=-1),
        },
        "SingleElectron_RunF": {
            "NEvents" : NEventsValues( NEVT_2016=70593532, NEVT_2017=128388230, NEVT_2018=-1),
            #TOT in DAS NEVT_2017=128467223
        },
        "SingleElectron_RunG": {
            "NEvents" : NEventsValues( NEVT_2016=153363109, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SingleElectron_RunH": {
            "NEvents" : NEventsValues( NEVT_2016=128854598, NEVT_2017=-1, NEVT_2018=-1),
            #TOT in DAS NEVT_2016=129021893
        },

        "SinglePhoton_RunA": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SinglePhoton_RunB": {
            "NEvents" : NEventsValues( NEVT_2016=69998015, NEVT_2017=15950935, NEVT_2018=-1),
            #TOT in DAS NEVT_2016=56878553+13119462
        },
        "SinglePhoton_RunC": {
            "NEvents" : NEventsValues( NEVT_2016=23147235, NEVT_2017=42182948, NEVT_2018=-1),
        },
        "SinglePhoton_RunD": {
            "NEvents" : NEventsValues( NEVT_2016=29801360, NEVT_2017=9753462, NEVT_2018=-1),
        },
        "SinglePhoton_RunE": {
            "NEvents" : NEventsValues( NEVT_2016=22322869, NEVT_2017=19011446, NEVT_2018=-1),
        },
        "SinglePhoton_RunF": {
            "NEvents" : NEventsValues( NEVT_2016=14666906, NEVT_2017=29783015, NEVT_2018=-1),
             #TOT in DAS NEVT_2017=55189+29783015
        },
        "SinglePhoton_RunG": {
            "NEvents" : NEventsValues( NEVT_2016=33288854, NEVT_2017=-1, NEVT_2018=-1),
        },
        "SinglePhoton_RunH": {
            "NEvents" : NEventsValues( NEVT_2016=35035661, NEVT_2017=-1, NEVT_2018=-1),
        },

        "MET_RunA": {
            "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=-1, NEVT_2018=52744621),
        },
        "MET_RunB": {
            "NEvents" : NEventsValues( NEVT_2016=36571139, NEVT_2017=51623474, NEVT_2018=29714277),
            #TOT in DAS NEVT_2016=583427+35987712
        },
        "MET_RunC": {
            "NEvents" : NEventsValues( NEVT_2016=17381222, NEVT_2017=115906496, NEVT_2018=31237456),
        },
        "MET_RunD": {
            "NEvents" : NEventsValues( NEVT_2016=20947429, NEVT_2017=20075033, NEVT_2018=161265239),
            #TOT in DAS NEVT_2018=162272551+26482-160411782
        },
        "MET_RunE": {
            "NEvents" : NEventsValues( NEVT_2016=21702329, NEVT_2017=71417109, NEVT_2018=-1),
        },
        "MET_RunF": {
            "NEvents" : NEventsValues( NEVT_2016=13319829, NEVT_2017=177288136, NEVT_2018=-1),
            #TOT in DAS NEVT_2017=177509826
        },
        "MET_RunG": {
            "NEvents" : NEventsValues( NEVT_2016=26843630, NEVT_2017=-1, NEVT_2018=-1),
            #TOT in DAS NEVT_2016 = 26974131
        },
        "MET_RunH": {
            "NEvents" : NEventsValues( NEVT_2016=39766341, NEVT_2017=-1, NEVT_2018=-1),
        },

        # #xsec verified. number event not
        # "QCD_HT100to200" : {
        #     "CrossSection" : XSValues( XSec_2016=27990000, XSec_2017=23610000, XSec_2018=25600000, XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="XSDB (LO)"),
        #     "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=78574480, NEVT_2018=-1),
        # },
        # "QCD_HT200to300" : {
        #     "CrossSection" : XSValues( XSec_2016=1710000, XSec_2017=1547000, XSec_2018=1557000, XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="XSDB (LO)"),
        #     "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=59032463, NEVT_2018=-1),
        # },
        # "QCD_HT300to500" : {
        #     "CrossSection" : XSValues( XSec_2016=347500, XSec_2017=322600, XSec_2018=323400, XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="XSDB (LO)"),
        #     "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=23246921, NEVT_2018=-1),
        # },
        # "QCD_HT500to700" : {
        #     "CrossSection" : XSValues( XSec_2016=32060, XSec_2017=29980, XSec_2018=30140, XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="XSDB (LO)"),
        #     "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=36745589, NEVT_2018=-1),
        # },
        # "QCD_HT700to1000" : {
        #     "CrossSection" : XSValues( XSec_2016=6829, XSec_2017=6334, XSec_2018=6310, XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="XSDB (LO)"),
        #     "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=46638985, NEVT_2018=-1),
        # },
        # "QCD_HT1000to1500" : {
        #     "CrossSection" : XSValues( XSec_2016=1207, XSec_2017=1088, XSec_2018=1094, XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="XSDB (LO)"),
        #     "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=16770762, NEVT_2018=-1),
        # },
        # "QCD_HT1500to2000" : {
        #     "CrossSection" : XSValues( XSec_2016=120, XSec_2017=99.11, XSec_2018=99.38, XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="XSDB (LO)"),
        #     "NEvents" : NEventsValues( NEVT_2016=-1, NEVT_2017=11508604, NEVT_2018=-1),
        # },
        # "QCD_HT2000toInf" : {
        #     "CrossSection" : XSValues( XSec_2016=25.25, XSec_2017=20.23, XSec_2018=20.20, XSecSource_2016="XSDB (LO)", XSecSource_2017="XSDB (LO)", XSecSource_2018="XSDB (LO)"),
        #     "NEvents" : NEventsValues( NEVT_2016=-1991645, NEVT_2017=5825566, NEVT_2018=-1),
        # },
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

    def get_lumi(self, name, energy, year, kFactor=False, Corrections=False):
        xsec = self.get_xs(name, energy, year)
        xsec *= self.get_br(name, energy, year)
        if kFactor: xsec *= self.get_kfactor(name, energy, year)
        if Corrections: xsec *= self.get_corr(name, energy, year)
        return self.get_nevt(name, energy, year)/xsec

