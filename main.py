import pandas
import openpyxl
from openpyxl.styles import colors
from openpyxl.styles import Font, Color
from openpyxl.styles.borders import Border, Side
from openpyxl import load_workbook
from openpyxl.chart import BarChart3D, Reference, AreaChart, AreaChart3D, Series, LineChart, LineChart3D
import os
import pdb
from openpyxl.styles import NamedStyle, Font, Border, Side
# import excel2img
import time
import datetime
import xlsxwriter
import math
import numpy
from time import gmtime, strftime


def OD_IBS_SLA_STATUS(input_1, input_2, Output_path):
    # if datetime.datetime.now() < datetime.datetime(2022, 1, 1):
    print('Processing Start Please Wait!')
    start = time.time()
    print('Processing!')



    input_2_df = pandas.read_csv(input_2, skiprows=[0, 1, 2, 3, 4, 5], low_memory=False)
    # input_2_df = pandas.read_excel(input_2)
    input_2_df = input_2_df[:-1]
    # pdb.set_trace()

    input_2_df['NR Total Traffic Volume(GB)'] = input_2_df['Total Traffic Volume (GB)']
    del input_2_df['Total Traffic Volume (GB)']
    input_2_df['NR DL Traffic Volume(GB)'] = input_2_df['Downlink Traffic Volume (GB)']
    del input_2_df['Downlink Traffic Volume (GB)']

    input_2_df['NR UL Traffic Volume(GB)'] = input_2_df['Uplink Traffic Volume (GB)']
    del input_2_df['Uplink Traffic Volume (GB)']

    input_2_df['PDCP DL Traffic Volume(GB)'] = input_2_df['5G PDCP DL Traffic (GB)']
    del input_2_df['5G PDCP DL Traffic (GB)']

    input_2_df['PDCP UL Traffic Volume(GB)'] = input_2_df['5G PDCP UL Traffic (GB)']
    del input_2_df['5G PDCP UL Traffic (GB)']

    input_2_df['NR Cell Downlink Average Throughput(Mbps)'] = input_2_df['NR Cell Downlink Average Throughput(Gbit/s)']
    del input_2_df['NR Cell Downlink Average Throughput(Gbit/s)']

    input_2_df['NR Cell Uplink Average Throughput(Mbps)'] = input_2_df['NR Cell Uplink Average Throughput(Gbit/s)']
    del input_2_df['NR Cell Uplink Average Throughput(Gbit/s)']

    input_2_df['NR User Downlink Average Throughput(Mbps)'] = input_2_df['User Downlink Throughput (Mbps)']
    del input_2_df['User Downlink Throughput (Mbps)']

    input_2_df['NR User Uplink Average Throughput(Mbps)'] = input_2_df['User Uplink Throughput (Mbps)']
    del input_2_df['User Uplink Throughput (Mbps)']

    input_2_df['NR DC SgNB Addition SR_SLA(%)'] = input_2_df['SgNB Addition Success Rate']
    del input_2_df['SgNB Addition Success Rate']

    input_2_df['SgNB Modification Success Rate_SLA(%)'] = input_2_df['SgNB Modification Reqd SR (%)']
    del input_2_df['SgNB Modification Reqd SR (%)']

    input_2_df['SgNB Change Success Rate_SLA(%)'] = input_2_df['SgNB  Change Success Rate(%)']
    del input_2_df['SgNB  Change Success Rate(%)']

    input_2_df['NR DC PScell SgNB Change SR(%)'] = input_2_df['Inter-SgNB PSCell Change Success Rate(%)']
    del input_2_df['Inter-SgNB PSCell Change Success Rate(%)']

    input_2_df['Intra-Freq SgNB Change SR_SLA(%)'] = input_2_df['Intra-SgNB PSCell Change Success Rate(%)']
    del input_2_df['Intra-SgNB PSCell Change Success Rate(%)']

    input_2_df['NR SgNB Call Drop Rate_SLA(%)'] = input_2_df['SgNB Abnormal Release Rate(%)']
    del input_2_df['SgNB Abnormal Release Rate(%)']



    input_2_df['NR Downlink PRB Utilizing Rate(%)'] = input_2_df['DL PRB Utilization_Avg (%)']
    del input_2_df['DL PRB Utilization_Avg (%)']

    input_2_df['NR Uplink PRB Utilizing Rate(%)'] = input_2_df['UL PRB Utilization_Avg (%)']
    del input_2_df['UL PRB Utilization_Avg (%)']

    input_2_df['NR DL SCH IBLER(%)'] = input_2_df['iBLER_DL (%)']
    del input_2_df['iBLER_DL (%)']

    input_2_df['NR UL SCH IBLER(%)'] = input_2_df['iBLER_UL (%)']
    del input_2_df['iBLER_UL (%)']

    input_2_df['NR Radio Network Availability Rate(%)'] = input_2_df['Radio Network Unavailability Rate(%)']
    del input_2_df['Radio Network Unavailability Rate(%)']

    input_2_df['NR RACH Setup Success Rate(%)'] = input_2_df['Contention-based RACH success rate(%)']
    del input_2_df['Contention-based RACH success rate(%)']

    input_2_df['InterSgNB Pscell Change Success Rate -irf'] = input_2_df['Inter-SgNB PSCell Change Success Rate']
    del input_2_df['Inter-SgNB PSCell Change Success Rate']

    input_2_df['IntraSgNB Pscell Change Success Rate irf'] = input_2_df['Intra-SgNB PSCell Change Success Rate']
    del input_2_df['Intra-SgNB PSCell Change Success Rate']

    input_2_df['NR Pscell change Success Rate -irf'] = input_2_df['SgNB Change Failures']
    del input_2_df['SgNB Change Failures']

    input_2_df['NsaDc SgNB Add Fail'] = input_2_df['SgNB Addition Failures(number)']
    del input_2_df['SgNB Addition Failures(number)']

    # column = ['Date',
    # 'gNodeB Name',
    # 'Cell Name',
    # 'NR Cell ID',
    # 'gNodeB Function Name',
    # 'Downlink NARFCN',
    # 'Frequency Band',
    # 'Integrity',
    # 'NR Total Traffic Volume(GB)',
    # 'NR DL Traffic Volume(GB)',
    # 'NR UL Traffic Volume(GB)',
    # 'MAX User Number',
    # 'NR Average User Number',
    # 'PDCP DL Traffic Volume(GB)',
    # 'PDCP UL Traffic Volume(GB)',
    # 'NR Cell Downlink Average Throughput(Mbps)',
    # 'NR Cell Uplink Average Throughput(Mbps)',
    # 'NR User Downlink Average Throughput(Mbps)',
    # 'NR User Uplink Average Throughput(Mbps)',
    # 'NR DC SgNB Addition SR_SLA(%)',
    # 'SgNB Modification Success Rate_SLA(%)',
    # 'SgNB Change Success Rate_SLA(%)',
    # 'NR DC PScell SgNB Change SR(%)',
    # 'Intra-Freq SgNB Change SR_SLA(%)',
    # 'NR SgNB Call Drop Rate_SLA(%)',
    # 'NR Downlink PRB Utilizing Rate(%)',
    # 'NR Uplink PRB Utilizing Rate(%)',
    # 'NR PDSCH Average MCS',
    # 'NR PUSCH Average MCS',
    # 'NR Average CQI',
    # 'N.UL.NI.Max(dBm)',
    # 'N.UL.NI.Avg(dBm)',
    # 'NR DL SCH IBLER(%)',
    # 'NR UL SCH IBLER(%)',
    # 'NR Radio Network Availability Rate(%)',
    # 'NR RACH Setup Success Rate(%)',
    # 'InterSgNB Pscell Change Success Rate -irf',
    # 'IntraSgNB Pscell Change Success Rate irf',
    # 'NR Pscell change Success Rate -irf',
    # 'NsaDc SgNB Add Fail',
    # 'N.NsaDc.SgNB.Add.Ack',
    # 'N.NsaDc.SgNB.Add.Att',
    # 'N.NsaDc.SgNB.Add.Fail.Radio',
    # 'N.NsaDc.SgNB.Add.Fail.Radio.License',
    # 'N.NsaDc.SgNB.Add.Fail.Radio.NoRes',
    # 'N.NsaDc.SgNB.Add.Fail.Radio.UeCapability',
    # 'N.NsaDc.SgNB.Add.Fail.TNL',
    # 'N.NsaDc.SgNB.Add.Succ',
    # 'Intra and InterSgNB PSCell Change Fail',
    # 'N.NsaDc.SgNB.Mod.Req.Att',
    # 'N.NsaDc.SgNB.Mod.Req.Fail.Radio',
    # 'N.NsaDc.SgNB.Mod.Req.Fail.TNL',
    # 'N.NsaDc.SgNB.Mod.Req.Succ',
    # 'N.NsaDc.SgNB.Mod.Required.Att',
    # 'N.NsaDc.SgNB.Mod.Required.Fail.Conflict',
    # 'N.NsaDc.SgNB.Mod.Required.Succ',
    # 'N.NsaDc.IntraSgNB.IntraFreq.PSCell.Change.Att',
    # 'N.NsaDc.IntraSgNB.IntraFreq.PSCell.Change.Succ',
    # 'N.NsaDc.IntraSgNB.PSCell.Change.Att',
    # 'N.NsaDc.IntraSgNB.PSCell.Change.Fail.Conflict',
    # 'N.NsaDc.IntraSgNB.PSCell.Change.Succ',
    # 'N.NsaDc.InterSgNB.PSCell.Change.Att',
    # 'N.NsaDc.InterSgNB.PSCell.Change.Fail.Conflict',
    # 'N.NsaDc.InterSgNB.PSCell.Change.Fail.Trans',
    # 'N.NsaDc.InterSgNB.PSCell.Change.Succ',
    # 'N.NsaDc.InterSgNB.PSCell.Change.UeContextRel',
    # 'N.NsaDc.InterSgNB.SgNB.Add.Ack',
    # 'N.NsaDc.InterSgNB.SgNB.Add.Att',
    # 'N.NsaDc.InterSgNB.SgNB.Add.Succ',
    # 'N.NsaDc.SgNB.AbnormRel',
    # 'N.NsaDc.SgNB.AbnormRel.NoReply',
    # 'N.NsaDc.SgNB.AbnormRel.Radio',
    # 'N.NsaDc.SgNB.AbnormRel.Radio.SUL',
    # 'N.NsaDc.SgNB.AbnormRel.Radio.UeLost',
    # 'N.NsaDc.SgNB.AbnormRel.Radio.ULSyncFail',
    # 'N.NsaDc.SgNB.AbnormRel.Trans',
    # 'N.NsaDc.SgNB.Rel',
    # 'N.NsaDc.SgNB.Rel.Coverage',
    # 'N.DRB.Active.DL.Avg',
    # 'N.DRB.Active.DL.Max',
    # 'N.User.CA.SCell.UL.Act.Avg',
    # 'N.User.RRCConn.Active.Avg',
    # 'N.User.RRCConn.Active.DL.Avg',
    # 'N.User.RRCConn.Active.DL.Max',
    # 'N.User.RRCConn.Active.Max',
    # 'N.User.RRCConn.Active.UL.Avg',
    # 'N.User.RRCConn.Active.UL.Max',
    # 'N.NsaDc.DRB.AbnormRel',
    # 'N.NsaDc.DRB.Rel',
    # 'N.NsaDc.SgNB.Rel.MeNBTrigger.NormalRel',
    # 'N.NsaDc.SgNB.Rel.SgNBTrigger',
    # 'N.NsaDc.InterSgNB.IntraFreq.PSCell.Change.Att',
    # 'N.NsaDc.InterSgNB.IntraFreq.PSCell.Change.Succ',
    # 'N.Cell.Unavail.Dur.System(s)',
    # 'N.Cell.Unavail.Dur.Manual(s)',
    # 'Avg Num of DL MU-MIMO Layers on Each PRB in Cell',
    # 'Avg Num of UL MU-MIMO Layers on Each PRB in Cell',
    # 'N.ChMeas.MIMO.DL.Pair.Layer',
    # 'N.ChMeas.MIMO.DL.Pair.PRB',
    # 'N.ChMeas.MIMO.DL.Transmission.Layer',
    # 'N.ChMeas.MIMO.DL.Transmission.Layer.Max',
    # 'N.ChMeas.MIMO.UL.Pair.Layer',
    # 'N.ChMeas.MIMO.UL.Pair.PRB',
    # 'N.ChMeas.MIMO.UL.Trans.Layer',
    # 'N.ChMeas.MIMO.UL.Trans.Layer.Max',
    # 'N.ThpVol.DL(kbit)',
    # 'N.ThpVol.UL(kbit)',
    # 'N.User.RRCConn.Avg',
    # 'N.User.RRCConn.Max',
    # 'N.PRB.DL.Used.Avg',
    # 'N.PRB.UL.Used.Avg',
    # 'N.PRB.DL.Avail.Avg',
    # 'N.PRB.UL.Avail.Avg',
    # 'N.ThpVol.DL.Cell(kbit)',
    # 'N.ThpVol.DL.LastSlot(kbit)',
    # 'N.ThpVol.UL.Cell(kbit)',
    # 'N.ThpVol.UE.UL.SmallPkt(kbit)',
    # 'N.ThpTime.DL.Cell(microsecond)',
    # 'N.ThpTime.DL.RmvLastSlot(microsecond)',
    # 'N.ThpTime.UL.Cell(microsecond)',
    # 'N.ThpTime.UE.UL.RmvSmallPkt(microsecond)',
    # 'SUM.N.PRB.DL.Used.Avg',
    # 'SUM.N.PRB.UL.Used.Avg',
    # 'SUM.N.PRB.DL.Avai',
    # 'SUM.N.PRB.UL.Avai',
    # 'SUM.N.CCE.Used.Avg',
    # 'SUM.N.CCE.Avail.Avg']
    # pdb.set_trace()
    # input_2_df.columns = column

    try:
        input_1_df = pandas.read_csv(input_1, low_memory=False)
        input_1_df = input_1_df.append(input_2_df)
    except:
        input_1_df = input_2_df

    # time_ = str(datetime.datetime.now()).split(' ')[0]
    time_ = str(strftime("%Y-%m-%d (%Hh %Mm %Ss)", gmtime()))


    print('Output Path: ', Output_path)

    input_1_df['Date'] = pandas.to_datetime(input_1_df['Date']).dt.strftime('%m/%d/%Y')
    input_1_df = input_1_df.replace(to_replace=["NIL", "/0"], value=0)
    input_1_df.to_csv(Output_path + '\\' + '5G Cell Level Output Combined File ' + time_  + '.csv', index=False)

    end = time.time()
    Execute_Time = "{:.3f}".format((end - start) / 60)
    print('The Execution Time of this Tool is %s minutes.' % Execute_Time)
    time.sleep(1)
    print('Execution Completed Succcessfully!')
    time.sleep(1)
    print('')
    print('')
    print('---------------Huawei RF Middle East----------------')
    print('---------For Support: Danish Ali(dwx854280)---------')
    print('---------------Contact: 00971508552942--------------')
    time.sleep(3)


