#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import time
def callCvesApi(pubStartDate=None,pubEndDate=None,resultsPerPage=2000):
    url=u'https://services.nvd.nist.gov/rest/json/cves/2.0/'
    cveID = 'CVE-2024-1312'
    #if pubStartDate==None or pubEndDate==None:
    #    now=datetime.datetime.now()
    #    pubStartDate=datetime.datetime(now.year,now.month,now.day-1,0,0,0)
    #    pubEndDate=datetime.datetime(now.year,now.month,now.day,0,0,0)
    #pubStartDateStr=pubStartDate.strftime('%Y-%m-%d 00:00:00 000 UTC+09:00')
    #pubEndDateStr=pubEndDate.strftime('%Y-%m-%d 00:00:00 000 UTC+09:00')
    #urlstr=u'{0}?modStartDate={1}&modEndDate={2}'.format(url,pubStartDateStr,pubEndDateStr)
    urlstr=u'{0}?cveId={1}'.format(url,cveID)
    start = time.time()
    response=requests.get(urlstr)
    end = time.time()
    print(start - end)
    values=json.loads(response.text)
    return values

if __name__ == '__main__':
    today_CVEs=callCvesApi()
    print(today_CVEs)
