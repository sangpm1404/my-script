#coding=utf-8
import requests
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import json

#Define var
#stock_list=['AMS','ACB']
stock_list=['A32', 'AAA', 'AAH', 'AAM', 'AAS', 'AAT', 'AAV', 'ABB', 'ABC', 'ABI', 'ABR', 'ABS', 'ABT', 'ABW', 'ACB', 'ACC', 'ACE', 'ACG', 'ACL', 'ACM', 'ACS', 'ACV', 'ADC', 'ADG', 'ADP', 'ADS', 'AFX', 'AG1', 'AGF', 'AGG', 'AGM', 'AGP', 'AGR', 'AGX', 'AIC', 'AIG', 'ALT', 'ALV', 'AMC', 'AMD', 'AME', 'AMP', 'AMS', 'AMV', 'ANT', 'ANV', 'APC', 'APF', 'APG', 'APH', 'API', 'APL', 'APP', 'APS', 'APT', 'ARM', 'ART', 'ASA', 'ASG', 'ASM', 'ASP', 'AST', 'ATB', 'ATG', 'ATS', 'AVC', 'AVF', 'AVG', 'BAB', 'BAF', 'BAL', 'BAX', 'BBC', 'BBH', 'BBM', 'BBS', 'BBT', 'BCA', 'BCB', 'BCC', 'BCE', 'BCF', 'BCG', 'BCM', 'BCP', 'BCR', 'BCV', 'BDB', 'BDG', 'BDT', 'BDW', 'BED', 'BEL', 'BFC', 'BGE', 'BGW', 'BHA', 'BHC', 'BHG', 'BHI', 'BHK', 'BHN', 'BHP', 'BIC', 'BID', 'BIG', 'BII', 'BIO', 'BKC', 'BKG', 'BLF', 'BLI', 'BLN', 'BLT', 'BMC', 'BMD', 'BMF', 'BMG', 'BMI', 'BMJ', 'BMK', 'BMN', 'BMP', 'BMS', 'BMV', 'BNA', 'BNW', 'BOT', 'BPC', 'BQB', 'BRC', 'BRR', 'BRS', 'BSA', 'BSC', 'BSD', 'BSG', 'BSH', 'BSI', 'BSL', 'BSP', 'BSQ', 'BSR', 'BST', 'BT1', 'BT6', 'BTB', 'BTD', 'BTG', 'BTH', 'BTN', 'BTP', 'BTS', 'BTT', 'BTU', 'BTV', 'BTW', 'BVB', 'BVG', 'BVH', 'BVL', 'BVN', 'BVS', 'BWA', 'BWE', 'BWS', 'BXH', 'C12', 'C21', 'C22', 'C32', 'C47', 'C4G', 'C69', 'C92', 'CAG', 'CAN', 'CAP', 'CAR', 'CAT', 'CBI', 'CBS', 'CC1', 'CC4', 'CCA', 'CCC', 'CCI', 'CCL', 'CCM', 'CCP', 'CCR', 'CCT', 'CCV', 'CDC', 'CDG', 'CDH', 'CDN', 'CDO', 'CDP', 'CDR', 'CE1', 'CEG', 'CEN', 'CEO', 'CET', 'CFM', 'CFV', 'CGV', 'CH5', 'CHC', 'CHP', 'CHS', 'CI5', 'CIA', 'CID', 'CIG', 'CII', 'CIP', 'CJC', 'CK8', 'CKA', 'CKD', 'CKG', 'CKV', 'CLC', 'CLG', 'CLH', 'CLL', 'CLM', 'CLW', 'CLX', 'CMC', 'CMD', 'CMF', 'CMG', 'CMI', 'CMK', 'CMM', 'CMN', 'CMP', 'CMS', 'CMT', 'CMV', 'CMW', 'CMX', 'CNA', 'CNC', 'CNG', 'CNN', 'CNT', 'COM', 'CPA', 'CPC', 'CPH', 'CPI', 'CQN', 'CQT', 'CRC', 'CRE', 'CSC', 'CSI', 'CSM', 'CST', 'CSV', 'CT3', 'CT6', 'CTA', 'CTB', 'CTD', 'CTF', 'CTG', 'CTI', 'CTN', 'CTP', 'CTR', 'CTS', 'CTT', 'CTW', 'CTX', 'CVN', 'CVT', 'CX8', 'CYC', 'D11', 'D2D', 'DAC', 'DAD', 'DAE', 'DAG', 'DAH', 'DAN', 'DAS', 'DAT', 'DBC', 'DBD', 'DBM', 'DBT', 'DC1', 'DC2', 'DC4', 'DCF', 'DCG', 'DCH', 'DCL', 'DCM', 'DCR', 'DCS', 'DDB', 'DDG', 'DDH', 'DDM', 'DDN', 'DDV', 'DFC', 'DFF', 'DGC', 'DGT', 'DGW', 'DHA', 'DHB', 'DHC', 'DHD', 'DHG', 'DHM', 'DHN', 'DHP', 'DHT', 'DIC', 'DID', 'DIG', 'DIH', 'DKC', 'DKW', 'DL1', 'DLD', 'DLG', 'DLR', 'DLT', 'DM7', 'DMC', 'DMN', 'DMS', 'DNA', 'DNC', 'DND', 'DNE', 'DNH', 'DNL', 'DNM', 'DNN', 'DNP', 'DNT', 'DNW', 'DOC', 'DOP', 'DP1', 'DP2', 'DP3', 'DPC', 'DPG', 'DPH', 'DPM', 'DPP', 'DPR', 'DPS', 'DQC', 'DRC', 'DRG', 'DRH', 'DRI', 'DRL', 'DS3', 'DSC', 'DSD', 'DSE', 'DSG', 'DSN', 'DSP', 'DST', 'DTA', 'DTB', 'DTC', 'DTD', 'DTE', 'DTG', 'DTI', 'DTK', 'DTL', 'DTP', 'DTT', 'DUS', 'DVC', 'DVG', 'DVM', 'DVN', 'DVP', 'DVW', 'DWC', 'DWS', 'DXG', 'DXL', 'DXP', 'DXS', 'DXV', 'DZM', 'E12', 'E29', 'EBS', 'ECI', 'ECO', 'EFI', 'EIB', 'EIC', 'EID', 'EIN', 'ELC', 'EME', 'EMG', 'EMS', 'EPC', 'EPH', 'EVE', 'EVF', 'EVG', 'EVS', 'FBA', 'FBC', 'FCC', 'FCM', 'FCN', 'FCS', 'FDC', 'FGL', 'FHN', 'FHS', 'FIC', 'FID', 'FIR', 'FIT', 'FLC', 'FMC', 'FOC', 'FOX', 'FPT', 'FRC', 'FRM', 'FRT', 'FSO', 'FT1', 'FTI', 'FTM', 'FTS', 'G36', 'GAB', 'GAS', 'GCB', 'GCF', 'GDA', 'GDT', 'GDW', 'GEE', 'GEG', 'GER', 'GEX', 'GGG', 'GH3', 'GHC', 'GIC', 'GIL', 'GKM', 'GLC', 'GLT', 'GLW', 'GMA', 'GMC', 'GMD', 'GMH', 'GMX', 'GND', 'GPC', 'GSM', 'GSP', 'GTA', 'GTD', 'GTS', 'GTT', 'GVR', 'GVT', 'H11', 'HAC', 'HAD', 'HAF', 'HAG', 'HAH', 'HAI', 'HAM', 'HAN', 'HAP', 'HAR', 'HAS', 'HAT', 'HAV', 'HAX', 'HBC', 'HBD', 'HBH', 'HBS', 'HC1', 'HC3', 'HCB', 'HCC', 'HCD', 'HCI', 'HCM', 'HCT', 'HD2', 'HD6', 'HD8', 'HDA', 'HDB', 'HDC', 'HDG', 'HDM', 'HDO', 'HDP', 'HDS', 'HDW', 'HEC', 'HEJ', 'HEP', 'HES', 'HEV', 'HFB', 'HFC', 'HFX', 'HGM', 'HGT', 'HHC', 'HHG', 'HHN', 'HHP', 'HHS', 'HHV', 'HID', 'HIG', 'HII', 'HIO', 'HJC', 'HJS', 'HKB', 'HKT', 'HLA', 'HLB', 'HLC', 'HLD', 'HLO', 'HLS', 'HLT', 'HLY', 'HMC', 'HMD', 'HMG', 'HMH', 'HMR', 'HMS', 'HNA', 'HNB', 'HND', 'HNF', 'HNG', 'HNI', 'HNM', 'HNP', 'HNR', 'HOM', 'HOT', 'HPB', 'HPD', 'HPG', 'HPH', 'HPI', 'HPM', 'HPP', 'HPT', 'HPW', 'HPX', 'HQC', 'HRB', 'HRC', 'HSA', 'HSG', 'HSI', 'HSL', 'HSM', 'HSP', 'HSV', 'HT1', 'HTC', 'HTE', 'HTG', 'HTI', 'HTL', 'HTM', 'HTN', 'HTP', 'HTT', 'HTV', 'HU1', 'HU3', 'HU4', 'HU6', 'HUB', 'HUG', 'HUT', 'HVA', 'HVG', 'HVH', 'HVN', 'HVT', 'HVX', 'HWS', 'IBC', 'IBD', 'ICC', 'ICF', 'ICG', 'ICI', 'ICN', 'ICT', 'IDC', 'IDI', 'IDJ', 'IDP', 'IDV', 'IFS', 'IHK', 'IJC', 'ILA', 'ILB', 'ILC', 'ILS', 'IME', 'IMP', 'IN4', 'INC', 'ING', 'INN', 'IPA', 'IRC', 'ISG', 'ISH', 'IST', 'ITA', 'ITC', 'ITD', 'ITQ', 'ITS', 'IVS', 'JOS', 'JVC', 'KAC', 'KBC', 'KCB', 'KCE', 'KDC', 'KDH', 'KDM', 'KGM', 'KHD', 'KHG', 'KHL', 'KHP', 'KHS', 'KHW', 'KIP', 'KKC', 'KLB', 'KLF', 'KMR', 'KMT', 'KOS', 'KPF', 'KSB', 'KSD', 'KSF', 'KSH', 'KSQ', 'KST', 'KSV', 'KTC', 'KTL', 'KTS', 'KTT', 'KVC', 'KWA', 'L10', 'L12', 'L14', 'L18', 'L35', 'L40', 'L43', 'L44', 'L45', 'L61', 'L62', 'L63', 'LAF', 'LAI', 'LAS', 'LAW', 'LBE', 'LBM', 'LCC', 'LCD', 'LCG', 'LCM', 'LCS', 'LDG', 'LDP', 'LDW', 'LEC', 'LG9', 'LGC', 'LGL', 'LGM', 'LHC', 'LHG', 'LIC', 'LIG', 'LIX', 'LKW', 'LLM', 'LM3', 'LM7', 'LM8', 'LMC', 'LMH', 'LMI', 'LNC', 'LO5', 'LPB', 'LPT', 'LQN', 'LSG', 'LSS', 'LTC', 'LTG', 'LUT', 'M10', 'MA1', 'MAC', 'MAS', 'MBB', 'MBG', 'MBN', 'MBS', 'MCC', 'MCF', 'MCG', 'MCH', 'MCM', 'MCO', 'MCP', 'MDA', 'MDC', 'MDF', 'MDG', 'MEC', 'MED', 'MEF', 'MEL', 'MES', 'MFS', 'MGC', 'MGG', 'MGR', 'MH3', 'MHC', 'MHL', 'MIC', 'MIE', 'MIG', 'MIM', 'MKP', 'MKV', 'MLC', 'MLS', 'MML', 'MNB', 'MND', 'MPC', 'MPT', 'MPY', 'MQB', 'MQN', 'MRF', 'MSB', 'MSH', 'MSN', 'MSR', 'MST', 'MTA', 'MTB', 'MTC', 'MTG', 'MTH', 'MTL', 'MTP', 'MTS', 'MTV', 'MTX', 'MVB', 'MVC', 'MVN', 'MWG', 'MZG', 'NAB', 'NAC', 'NAF', 'NAG', 'NAP', 'NAS', 'NAU', 'NAV', 'NAW', 'NBB', 'NBC', 'NBE', 'NBP', 'NBT', 'NBW', 'NCG', 'NCS', 'NCT', 'ND2', 'NDC', 'NDF', 'NDN', 'NDP', 'NDT', 'NDW', 'NDX', 'NED', 'NEM', 'NET', 'NFC', 'NGC', 'NHA', 'NHC', 'NHH', 'NHP', 'NHT', 'NHV', 'NJC', 'NKG', 'NLG', 'NLS', 'NNC', 'NNT', 'NO1', 'NOS', 'NQB', 'NQN', 'NQT', 'NRC', 'NS2', 'NSC', 'NSG', 'NSH', 'NSL', 'NSS', 'NST', 'NT2', 'NTB', 'NTC', 'NTF', 'NTH', 'NTL', 'NTP', 'NTT', 'NTW', 'NUE', 'NVB', 'NVL', 'NVP', 'NVT', 'NWT', 'NXT', 'OCB', 'OCH', 'ODE', 'OGC', 'OIL', 'ONE', 'ONW', 'OPC', 'ORS', 'PAC', 'PAI', 'PAN', 'PAP', 'PAS', 'PAT', 'PBC', 'PBP', 'PBT', 'PC1', 'PCC', 'PCE', 'PCF', 'PCG', 'PCH', 'PCM', 'PCT', 'PDB', 'PDC', 'PDN', 'PDR', 'PDV', 'PEC', 'PEG', 'PEN', 'PEQ', 'PET', 'PFL', 'PGB', 'PGC', 'PGD', 'PGI', 'PGN', 'PGS', 'PGT', 'PGV', 'PHC', 'PHH', 'PHN', 'PHP', 'PHR', 'PHS', 'PIA', 'PIC', 'PID', 'PIS', 'PIT', 'PIV', 'PJC', 'PJS', 'PJT', 'PLA', 'PLC', 'PLE', 'PLO', 'PLP', 'PLX', 'PMB', 'PMC', 'PMG', 'PMJ', 'PMP', 'PMS', 'PMT', 'PMW', 'PNC', 'PND', 'PNG', 'PNJ', 'PNP', 'PNT', 'POB', 'POM', 'POS', 'POT', 'POV', 'POW', 'PPC', 'PPE', 'PPH', 'PPI', 'PPP', 'PPS', 'PPT', 'PPY', 'PQN', 'PRC', 'PRE', 'PRO', 'PRT', 'PSB', 'PSC', 'PSD', 'PSE', 'PSG', 'PSH', 'PSI', 'PSL', 'PSN', 'PSP', 'PSW', 'PTB', 'PTC', 'PTD', 'PTE', 'PTG', 'PTH', 'PTI', 'PTL', 'PTO', 'PTP', 'PTS', 'PTT', 'PTV', 'PTX', 'PV2', 'PVA', 'PVB', 'PVC', 'PVD', 'PVE', 'PVG', 'PVH', 'PVI', 'PVL', 'PVM', 'PVO', 'PVP', 'PVR', 'PVS', 'PVT', 'PVV', 'PVX', 'PVY', 'PWA', 'PWS', 'PX1', 'PXA', 'PXC', 'PXI', 'PXL', 'PXS', 'PXT', 'QBS', 'QCC', 'QCG', 'QHD', 'QHW', 'QNC', 'QNP', 'QNS', 'QNT', 'QNU', 'QNW', 'QPH', 'QSP', 'QST', 'QTC', 'QTP', 'RAL', 'RAT', 'RBC', 'RCC', 'RCD', 'RCL', 'RDP', 'REE', 'RIC', 'RTB', 'RYG', 'S12', 'S27', 'S4A', 'S55', 'S72', 'S74', 'S96', 'S99', 'SAB', 'SAC', 'SAF', 'SAL', 'SAM', 'SAP', 'SAS', 'SAV', 'SB1', 'SBA', 'SBB', 'SBD', 'SBG', 'SBH', 'SBL', 'SBM', 'SBR', 'SBS', 'SBT', 'SBV', 'SC5', 'SCC', 'SCD', 'SCG', 'SCI', 'SCJ', 'SCL', 'SCO', 'SCR', 'SCS', 'SCY', 'SD1', 'SD2', 'SD3', 'SD4', 'SD5', 'SD6', 'SD7', 'SD8', 'SD9', 'SDA', 'SDB', 'SDC', 'SDD', 'SDG', 'SDJ', 'SDK', 'SDN', 'SDP', 'SDT', 'SDU', 'SDV', 'SDX', 'SDY', 'SEA', 'SEB', 'SED', 'SEP', 'SFC', 'SFG', 'SFI', 'SFN', 'SGB', 'SGC', 'SGD', 'SGH', 'SGI', 'SGN', 'SGP', 'SGR', 'SGS', 'SGT', 'SHA', 'SHB', 'SHC', 'SHE', 'SHG', 'SHI', 'SHN', 'SHP', 'SHS', 'SID', 'SIG', 'SII', 'SIP', 'SIV', 'SJ1', 'SJC', 'SJD', 'SJE', 'SJF', 'SJG', 'SJM', 'SJS', 'SKG', 'SKH', 'SKN', 'SKV', 'SLS', 'SMA', 'SMB', 'SMC', 'SMN', 'SMT', 'SNC', 'SNZ', 'SP2', 'SPB', 'SPC', 'SPD', 'SPH', 'SPI', 'SPM', 'SPV', 'SQC', 'SRA', 'SRB', 'SRC', 'SRF', 'SSB', 'SSC', 'SSF', 'SSG', 'SSH', 'SSI', 'SSM', 'SSN', 'ST8', 'STB', 'STC', 'STG', 'STH', 'STK', 'STL', 'STP', 'STS', 'STT', 'STW', 'SVC', 'SVD', 'SVG', 'SVH', 'SVI', 'SVN', 'SVT', 'SWC', 'SZB', 'SZC', 'SZE', 'SZG', 'SZL', 'TA6', 'TA9', 'TAB', 'TAL', 'TAN', 'TAR', 'TAW', 'TB8', 'TBC', 'TBD', 'TBH', 'TBR', 'TBT', 'TBW', 'TBX', 'TCB', 'TCD', 'TCH', 'TCI', 'TCJ', 'TCK', 'TCL', 'TCM', 'TCO', 'TCR', 'TCT', 'TCW','TCX' ,'TDB', 'TDC', 'TDF', 'TDG', 'TDH', 'TDM', 'TDP', 'TDS', 'TDT', 'TDW', 'TED', 'TEG', 'TEL', 'TET', 'TFC', 'TGG', 'TGP', 'TH1', 'THB', 'THD', 'THG', 'THM', 'THN', 'THP', 'THS', 'THT', 'THU', 'THW', 'TID', 'TIE', 'TIG', 'TIN', 'TIP', 'TIS', 'TIX', 'TJC', 'TKA', 'TKC', 'TKG', 'TKU', 'TL4', 'TLD', 'TLG', 'TLH', 'TLI', 'TLP', 'TLT', 'TMB', 'TMC', 'TMG', 'TMP', 'TMS', 'TMT', 'TMW', 'TMX', 'TN1', 'TNA', 'TNB', 'TNC', 'TNG', 'TNH', 'TNI', 'TNM', 'TNP', 'TNS', 'TNT', 'TNV', 'TNW', 'TOP', 'TOS', 'TOT', 'TOW', 'TPB', 'TPC', 'TPH', 'TPP', 'TPS', 'TQN', 'TQW', 'TR1', 'TRA', 'TRC', 'TRS', 'TRT', 'TS3', 'TS4', 'TSA', 'TSB', 'TSC', 'TSD', 'TSG', 'TSJ', 'TST', 'TT6', 'TTA', 'TTB', 'TTC', 'TTD', 'TTE', 'TTF', 'TTG', 'TTH', 'TTL', 'TTN', 'TTS', 'TTT', 'TTZ', 'TUG', 'TV1', 'TV2', 'TV3', 'TV4', 'TV6', 'TVA', 'TVB', 'TVC', 'TVD', 'TVG', 'TVH', 'TVM', 'TVN', 'TVS', 'TVT', 'TW3', 'TXM', 'TYA', 'UCT', 'UDC', 'UDJ', 'UDL', 'UEM', 'UIC', 'UMC', 'UNI', 'UPC', 'UPH', 'USC', 'USD', 'UXC', 'V11', 'V12', 'V15', 'V21', 'VAB', 'VAF', 'VAV', 'VBB', 'VBC', 'VBG', 'VBH', 'VC1', 'VC2', 'VC3', 'VC5', 'VC6', 'VC7', 'VC9', 'VCA', 'VCB', 'VCC', 'VCE', 'VCF', 'VCG', 'VCI', 'VCM', 'VCP', 'VCR', 'VCS', 'VCT', 'VCW', 'VCX', 'VDB', 'VDG', 'VDL', 'VDN', 'VDP', 'VDS', 'VDT', 'VE1', 'VE2', 'VE3', 'VE4', 'VE8', 'VE9', 'VEA', 'VEC', 'VEF', 'VES', 'VET', 'VFC', 'VFG', 'VFR', 'VFS', 'VGC', 'VGG', 'VGI', 'VGL', 'VGP', 'VGR', 'VGS', 'VGT', 'VGV', 'VHC', 'VHD', 'VHE', 'VHF', 'VHG', 'VHH', 'VHL', 'VHM', 'VIB', 'VIC', 'VID', 'VIE', 'VIF', 'VIG', 'VIH', 'VIM', 'VIN', 'VIP', 'VIR', 'VIT', 'VIW', 'VIX', 'VJC', 'VKC', 'VKP', 'VLA', 'VLB', 'VLC', 'VLF', 'VLG', 'VLP', 'VLW', 'VMA', 'VMC', 'VMD', 'VMG', 'VMK', 'VMS', 'VMT', 'VNA', 'VNB', 'VNC', 'VND', 'VNE', 'VNF', 'VNG', 'VNH', 'VNI', 'VNL', 'VNM', 'VNP', 'VNR', 'VNS', 'VNT', 'VNX', 'VNY', 'VNZ', 'VOC', 'VOS', 'VPA', 'VPB', 'VPC', 'VPD', 'VPG', 'VPH', 'VPI', 'VPR', 'VPS', 'VPW', 'VQC', 'VRC', 'VRE', 'VRG', 'VSA', 'VSC', 'VSE', 'VSF', 'VSG', 'VSH', 'VSI', 'VSM', 'VSN', 'VST', 'VTA', 'VTB', 'VTC', 'VTD', 'VTE', 'VTG', 'VTH', 'VTI', 'VTJ', 'VTK', 'VTL', 'VTM', 'VTO', 'VTP', 'VTQ', 'VTR', 'VTS', 'VTV', 'VTX', 'VTZ', 'VUA', 'VVN', 'VVS', 'VW3', 'VWS', 'VXB', 'VXP', 'VXT', 'WCS', 'WSB', 'WSS', 'WTC', 'X20', 'X26', 'X77', 'XDH', 'XHC', 'XLV', 'XMC', 'XMD', 'XMP', 'XPH', 'YBC', 'YBM', 'YEG', 'YTC']
time_frame="1D"
verification_token_ta="zHUPPy_pi-bcHkEzamyjKIRtedLIh8EipmA1p52Y-ok7SVmMMeJVKFxvhOaEsxyZ_cdbe-hAWQCfZOiB9Qg340wMa2md_V2GYNaZe10Mm141"
verification_token_fa='liD9Ro6uWtW53XB-4K4tnKUIL6OzZcY-h76J8-jkZSqw1kAPaRQo48ge8IEhZcqSzNjryTRY-BEzRbuJjoaZJHitWmbZPCVco2BQlmH3iws1'
from_date = datetime.now().strftime("%Y-%m-%d")

## call TA data
def call_TA(stock_code, time_frame, verification_token):
    url = "https://finance.vietstock.vn/TechnicalRating/GetFinalRanking"
    
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://finance.vietstock.vn/VCG/phan-tich-ky-thuat.htm",
        "Origin": "https://finance.vietstock.vn",
        "Cookie": "language=vi-VN; Theme=Light; AnonymousNotification=; ASP.NET_SessionId=usff2fjt1wh1c0eknpk2onn0; __RequestVerificationToken=rWh4MEFmhQtsZvrVO6LK784J6XN-scm9HLvQW1kctT5lmtQOQIaHaT4kvsPDnsKJ2Z1NDuu0ChdFOcGesPdl8mIWZtOqJJoR9xGLEkCVJ081;language=en-US",
    }

    data = {
        "stockCode": stock_code,
        "timeFrame": time_frame,
        "__RequestVerificationToken": verification_token
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        try:
            clean_text = response.text.lstrip("\ufeff")  # Delete BOM
            return json.loads(clean_text)  # Convert Json
        except json.JSONDecodeError:
            return {"error": "Invalid JSON response"}
    else:
        return {"error": f"Request failed with status code {response.status_code}"}

# call FA data
def call_FA(code, from_date, verification_token):
    url = "https://finance.vietstock.vn/data/gettradingresult"
    
    headers = {
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://finance.vietstock.vn/VIC/thong-ke-giao-dich.htm",
        "Origin": "https://finance.vietstock.vn",
        "Cookie": "language=vi-VN; Theme=Light; ASP.NET_SessionId=juuvlr3fvwd3n3ewlnz2nsps; __RequestVerificationToken=WvwqC0vxaLMZKcGFAqIj7EwF8fukDCPgOqfEZwsw9RSyytYNFProvyge8L8szfe8kJ1xviaR3cxXeatsfMwMVxBIHZuZVkkPbSNwH2TZq041;language=en-US",
    }

    data = {
        "Code": code,
        "OrderBy": "",
        "OrderDirection": "desc",
        "FromDate": from_date,
        "__RequestVerificationToken": verification_token
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        try:
            clean_text = response.text.lstrip("\ufeff")  # Delete BOM
            return json.loads(clean_text)  # Convert Json
        except json.JSONDecodeError:
            return {"error": "Invalid JSON response"}
    else:
        return {"error": f"Request failed with status code {response.status_code}"}




# Send message to telegram
BOT_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX' #Tele Bot Token
CHAT_ID = 'XXXXXXXXXXX' #Channel ID
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML" 
    }

    response = requests.post(url, data=data)
    return response.json()

# check to send telegram
def is_ngon(rsi,ma20,ma50,price, vol,pe):
    if ma50 == None: return False 
    price_above_ma20 = price > ma20 and (price - ma20) / ma20 <= 0.03
    ma20_above_ma50 = ma20 > ma50 and (ma20 - ma50) / ma50 <= 0.02
    vol_ok = vol > 200000
    pe_ok = pe > 0 and pe < 20
    rsi_ok = rsi < 80
    if rsi <= 30 and vol_ok  and pe_ok:
        return True
    elif price_above_ma20 and ma20_above_ma50 and vol_ok and pe_ok and rsi_ok:
        return True
    else:
        return False

##Main
#Init data frame
df = pd.DataFrame({"STO": [], "Price": [],"+-%": [], "PE": [], "PB": [], "MA20": [], "RSI": [],"ADX": []})
for stock in stock_list:
    ## process data
    try:
        TA_result = call_TA(stock, time_frame, verification_token_ta)
        if "data" in TA_result and isinstance(TA_result["data"], list) and len(TA_result["data"]) > 0:
            TA_data = TA_result["data"][0]
            print("✅ Lấy dữ liệu thành công TA")
            try:
                FA_result = call_FA(stock, from_date, verification_token_fa)
                if "Data" in FA_result and isinstance(FA_result["Data"], list) and len(FA_result["Data"]) > 0:
                    FA_data = FA_result["Data"][0]
                    print("✅ Lấy dữ liệu thành công FA")
                    print(stock + " RSI: " + str(TA_data.get("RSI","N/A")) + " - MA20: " + str(TA_data.get("SMA20","N/A"))+ " MA50: "+ str(TA_data.get("SMA50","N/A"))+ " P: "+str(FA_data.get("ClosePrice","N/A")))
                    #Check data 
                    if is_ngon(TA_data.get("RSI","N/A"),TA_data.get("SMA20","N/A"),TA_data.get("SMA50","N/A"),FA_data.get("ClosePrice","N/A"),FA_data.get("TotalVol","N/A"),FA_data.get("PE","N/A")) :
                        print(stock + "- ngon")
                        df.loc[len(df)] = [stock, FA_data.get("ClosePrice","N/A"),FA_data.get("PerChange","N/A"),FA_data.get("PE","N/A"),FA_data.get("PB","N/A"),TA_data.get("SMA20","N/A"),TA_data.get("RSI","N/A"),TA_data.get("ADX","N/A") ]
                else:
                    raise ValueError("⚠ Không có dữ liệu FA hợp lệ trong 'Data'!")
                    continue
            except (IndexError, KeyError, ValueError, Exception) as e:
                    print(f"❌ Lỗi khi lấy dữ liệu cho {stock}: {e}")
        else:
            raise ValueError("⚠ Không có dữ liệu TA hợp lệ trong 'data'!")
            continue
    except (IndexError, KeyError, ValueError, Exception) as e:
        print(f"❌ Lỗi khi lấy dữ liệu cho {stock}: {e}")

note = send_telegram_message("🚀📊📈 Daily Report - "+from_date +"🚀📊📈")
stock_table = "<pre>" + df.to_string(index=False) + "</pre>"
send_telegram_message(stock_table)
with open('C:\\Users\\sangpm4\\Desktop\\code\\temp\\list_review_stock.txt', 'w') as f:
    f.write(stock_table)


