#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tushare as ts
import csv
import xlsxwriter
import sys
import pandas as pd

reload(sys)
sys.setdefaultencoding('utf8')

def get_all(listOutput={}, year=2014, quoter=1):
    """
    获取沪深上市公司基本情况。属性包括：
    code,代码
    name,名称
    industry,所属行业
    area,地区
    pe,市盈率
    outstanding,流通股本(亿)
    totals,总股本(亿)
    totalAssets,总资产(万)
    liquidAssets,流动资产
    fixedAssets,固定资产
    reserved,公积金
    reservedPerShare,每股公积金
    esp,每股收益
    bvps,每股净资
    pb,市净率
    timeToMarket,上市日期
    undp,未分利润
    perundp, 每股未分配
    rev,收入同比(%)
    profit,利润同比(%)
    gpr,毛利率(%)
    npr,净利润率(%)
    holders,股东人数
    """
    listOutput["stock"] = ts.get_stock_basics()

    """
    按年度、季度获取业绩报表数据。数据获取需要一定的时间，网速取决于您的网速，请耐心等待。结果返回的数据属性说明如下：
    code,代码
    name,名称
    esp,每股收益
    eps_yoy,每股收益同比(%)
    bvps,每股净资产
    roe,净资产收益率(%)
    epcf,每股现金流量(元)
    net_profits,净利润(万元)
    profits_yoy,净利润同比(%)
    distrib,分配方案
    report_date,发布日期
    """
    #获取2018年第3季度的业绩报表数据
    listOutput["Performance report"] = ts.get_report_data(year,quoter)

    """
    按年度、季度获取盈利能力数据，结果返回的数据属性说明如下：
    code,代码
    name,名称
    roe,净资产收益率(%)
    net_profit_ratio,净利率(%)
    gross_profit_rate,毛利率(%)
    net_profits,净利润(万元)
    esp,每股收益
    business_income,营业收入(百万元)
    bips,每股主营业务收入(元)
    """
    #获取2018年第3季度的盈利能力数据
    ts.get_profit_data(year,quoter)

    """
    营运能力
    按年度、季度获取营运能力数据，结果返回的数据属性说明如下：

    code,代码
    name,名称
    arturnover,应收账款周转率(次)
    arturndays,应收账款周转天数(天)
    inventory_turnover,存货周转率(次)
    inventory_days,存货周转天数(天)
    currentasset_turnover,流动资产周转率(次)
    currentasset_days,流动资产周转天数(天)
    #获取2014年第3季度的营运能力数据
    """
    listOutput["operating capacity"] = ts.get_operation_data(year, quoter)

    """
    成长能力
    按年度、季度获取成长能力数据，结果返回的数据属性说明如下：

    code,代码
    name,名称
    mbrg,主营业务收入增长率(%)
    nprg,净利润增长率(%)
    nav,净资产增长率
    targ,总资产增长率
    epsg,每股收益增长率
    seg,股东权益增长率
    """
    #获取2014年第3季度的成长能力数据
    listOutput["Growth ability"] = ts.get_growth_data(year, quoter)

    """偿债能力
    按年度、季度获取偿债能力数据，结果返回的数据属性说明如下：

    code,代码
    name,名称
    currentratio,流动比率
    quickratio,速动比率
    cashratio,现金比率
    icratio,利息支付倍数
    sheqratio,股东权益比率
    adratio,股东权益增长率
    """
    #获取2014年第3季度的偿债能力数据
    listOutput["debt paying ability"] = ts.get_debtpaying_data(year, quoter)

    """现金流量
    按年度、季度获取现金流量数据，结果返回的数据属性说明如下：

    code,代码
    name,名称
    cf_sales,经营现金净流量对销售收入比率
    rateofreturn,资产的经营现金流量回报率
    cf_nm,经营现金净流量与净利润的比率
    cf_liabilities,经营现金净流量对负债比率
    cashflowratio,现金流量比率
    """
    #获取2014年第3季度的现金流量数据
    listOutput["Cash flow"] = ts.get_cashflow_data(year, quoter)


if __name__ == '__main__':
    path = "/home/yuanmin/Documents/data"+"_"+str(year)+"_"+str(quoter)+ ".xlsx"
    year = 2018
    quoter = 1
    listOutput = {}
    get_all(listOutput, year, quoter)
    #listOutput["stock"] = ts.get_stock_basics()
    #workbook = xlsxwriter.Workbook('/home/yuanmin/Documents/data.xlsx')
    writer = pd.ExcelWriter(path)

    row = 1
    col = 1

    for key in listOutput.keys():
        listOutput[key].to_excel(writer, key+" "+str(year)+"_"+str(quoter))
    #    worksheet = workbook.add_worksheet(key)
    #    str = listOutput[key].tostring()
    #    worksheet.write_string(row, col, str)
        #for item in listOutput[key]:
            #print item
            #worksheet.write_string(row, col, item)

    #workbook.close()
    writer.save()
