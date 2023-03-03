import sys

sys.path.append("..")
from CrossSectionHelper import MCSampleValuesHelperPrototype as P


class MCSignalValuesHelper(P):

    signal_values_dict = {
        "AZHToLLTT_mA900_mH350": {
            "CrossSection": P.XSValues( XSec_13TeV=1, XSecSource_13TeV="arbitrary normalization"),
            "NEvents": P.NEventsValues(
              NEVT_UL17=25000
              ),
            "XMLname": P.XMLValues(
              Xml_UL17="RunII_106X_v2/BSM/UL17/AZH_UL2017_mA900_mH350_Summer20UL17.xml", XmlSource_UL17="/AZH_UL2017_mA900_mH350_LHEGEN/mihawksw-AZH_UL2017_mA900_mH350_MiniAODv2-3f0b140a720de1c801ff414923884f7b/USER",
              )
            },

        "AZHToLLTT_mA900_mH600": {
            "CrossSection": P.XSValues( XSec_13TeV=1, XSecSource_13TeV="arbitrary normalization"),
            "NEvents": P.NEventsValues(
              NEVT_UL17=25000
              ),
            "XMLname": P.XMLValues(
              Xml_UL17="RunII_106X_v2/BSM/UL17/AZH_UL2017_mA900_mH600_Summer20UL17.xml", XmlSource_UL17="/AZH_UL2017_2HDMtII_NLO_mA900_mH600/mihawksw-AZH_UL2017_2HDMtII_NLO_mA900_mH600_MiniAODv2-3f0b140a720de1c801ff414923884f7b/USER",
              )
            },

        "AZHToLLTT_mA1200_mH400": {
            "CrossSection": P.XSValues( XSec_13TeV=1, XSecSource_13TeV="arbitrary normalization"),
            "NEvents": P.NEventsValues(
              NEVT_UL17=24000
              ),
            "XMLname": P.XMLValues(
              Xml_UL17="RunII_106X_v2/BSM/UL17/AZH_UL2017_mA1200_mH400_Summer20UL17.xml", XmlSource_UL17="/AZH_UL2017_mA1200_mH400_SIM/srudrabh-AZH_UL2017_mA1200_mH400_MiniAODv2-3f0b140a720de1c801ff414923884f7b/USER",
              )
            },

        "AZHToLLTT_mA2100_mH1600": {
            "CrossSection": P.XSValues( XSec_13TeV=1, XSecSource_13TeV="arbitrary normalization"),
            "NEvents": P.NEventsValues(
              NEVT_UL17=25000
              ),
            "XMLname": P.XMLValues(
              Xml_UL17="RunII_106X_v2/BSM/UL17/AZH_UL2017_mA2100_mH1600_Summer20UL17.xml", XmlSource_UL17="/AZH_UL2017_mA2100_mH1600_LHEGEN/mihawksw-AZH_UL2017_mA2100_mH1600_MiniAODv2-3f0b140a720de1c801ff414923884f7b/USER",
              )
            },

        "AToZHToLLTTbar_MA-1000_MH-600" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-1000_MH-600_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-1000_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-1000_MH-600_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-1000_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-1000_MH-600_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-1000_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-1000_MH-600_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-1000_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-1000_MH-700" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-1000_MH-700_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-1000_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-1000_MH-700_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-1000_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-1000_MH-700_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-1000_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-1000_MH-700_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-1000_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-1000_MH-800" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=49000,
                NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-1000_MH-800_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-1000_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-1000_MH-800_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-1000_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-1000_MH-800_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-1000_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-1000_MH-800_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-1000_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-1200_MH-1000" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=22068,
                NEVT_UL17=50000,
                NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-1200_MH-1000_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-1200_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-1200_MH-1000_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-1200_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-1200_MH-1000_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-1200_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-1200_MH-1000_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-1200_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-1200_MH-400" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-1200_MH-400_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-1200_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-1200_MH-400_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-1200_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-1200_MH-400_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-1200_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-1200_MH-400_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-1200_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-1200_MH-850" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-1200_MH-850_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-1200_MH-850_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-1200_MH-850_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-1200_MH-850_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-1200_MH-850_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-1200_MH-850_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-1200_MH-850_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-1200_MH-850_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-1500_MH-1000" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-1500_MH-1000_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-1500_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-1500_MH-1000_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-1500_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-1500_MH-1000_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-1500_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-1500_MH-1000_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-1500_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-1500_MH-1400" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-1500_MH-1400_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-1500_MH-1400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-1500_MH-1400_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-1500_MH-1400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-1500_MH-1400_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-1500_MH-1400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-1500_MH-1400_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-1500_MH-1400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-1500_MH-400" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-1500_MH-400_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-1500_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-1500_MH-400_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-1500_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-1500_MH-400_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-1500_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-1500_MH-400_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-1500_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-1800_MH-1600" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-1800_MH-1600_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-1800_MH-1600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-1800_MH-1600_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-1800_MH-1600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-1800_MH-1600_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-1800_MH-1600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-1800_MH-1600_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-1800_MH-1600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-1800_MH-400" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-1800_MH-400_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-1800_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-1800_MH-400_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-1800_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-1800_MH-400_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-1800_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-1800_MH-400_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-1800_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-2100_MH-1000" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-2100_MH-1000_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-2100_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-2100_MH-1000_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-2100_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-2100_MH-1000_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-2100_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-2100_MH-1000_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-2100_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-2100_MH-1600" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=49000,
                # NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-2100_MH-1600_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-2100_MH-1600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-2100_MH-1600_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-2100_MH-1600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-2100_MH-1600_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-2100_MH-1600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                # Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-2100_MH-1600_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-2100_MH-1600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-2100_MH-2000" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=49000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-2100_MH-2000_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-2100_MH-2000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-2100_MH-2000_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-2100_MH-2000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-2100_MH-2000_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-2100_MH-2000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-2100_MH-2000_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-2100_MH-2000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-2100_MH-400" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-2100_MH-400_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-2100_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-2100_MH-400_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-2100_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-2100_MH-400_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-2100_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-2100_MH-400_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-2100_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-500_MH-350" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=49000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-500_MH-350_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-500_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-500_MH-350_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-500_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-500_MH-350_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-500_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-500_MH-350_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-500_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-500_MH-370" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=49000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-500_MH-370_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-500_MH-370_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-500_MH-370_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-500_MH-370_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-500_MH-370_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-500_MH-370_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-500_MH-370_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-500_MH-370_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-500_MH-400" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-500_MH-400_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-500_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-500_MH-400_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-500_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-500_MH-400_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-500_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-500_MH-400_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-500_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-700_MH-350" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-700_MH-350_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-700_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-700_MH-350_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-700_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-700_MH-350_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-700_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-700_MH-350_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-700_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-700_MH-370" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-700_MH-370_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-700_MH-370_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-700_MH-370_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-700_MH-370_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-700_MH-370_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-700_MH-370_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-700_MH-370_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-700_MH-370_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-700_MH-400" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-700_MH-400_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-700_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-700_MH-400_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-700_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-700_MH-400_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-700_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-700_MH-400_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-700_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-800_MH-600" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=49000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-800_MH-600_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-800_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-800_MH-600_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-800_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-800_MH-600_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-800_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-800_MH-600_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-800_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-800_MH-650" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-800_MH-650_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-800_MH-650_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-800_MH-650_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-800_MH-650_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-800_MH-650_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-800_MH-650_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-800_MH-650_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-800_MH-650_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-900_MH-350" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-900_MH-350_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-900_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-900_MH-350_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-900_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-900_MH-350_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-900_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-900_MH-350_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-900_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-900_MH-370" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-900_MH-370_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-900_MH-370_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-900_MH-370_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-900_MH-370_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-900_MH-370_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-900_MH-370_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-900_MH-370_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-900_MH-370_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "AToZHToLLTTbar_MA-900_MH-400" : {
            "CrossSection" : P.XSValues(
                XSec_13TeV=1, XSecSource_13TeV="Fixed to 1 pb",
            ),
            "NEvents" : P.NEventsValues(
                NEVT_UL16preVFP=27000,
                NEVT_UL16postVFP=23000,
                NEVT_UL17=50000,
                NEVT_UL18=50000,
            ),
            "XMLname" : P.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/AToZHToLLTTbar_MA-900_MH-400_CP5_amcatnlo-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/AToZHToLLTTbar_MA-900_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/AToZHToLLTTbar_MA-900_MH-400_CP5_amcatnlo-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/AToZHToLLTTbar_MA-900_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/AToZHToLLTTbar_MA-900_MH-400_CP5_amcatnlo-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/AToZHToLLTTbar_MA-900_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/AToZHToLLTTbar_MA-900_MH-400_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/AToZHToLLTTbar_MA-900_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },
    }
