

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
import requests
from datetime import datetime,timedelta

from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
from bson.objectid import ObjectId
import dateutil.parser
import re



def Servermonitor(request):
    r = requests.get('http://52.9.185.212:4567/results/')
    ptolist =[]

    for i in r.json():
        ptolist.append(i['client'])
    prolist = list(set(ptolist))

    return render(request,'monitorgraph/servermonitorlist.html',{'prolist':prolist})


def Monitorlist(request):
    proname = request.GET.get('proname')
    print proname
    client = MongoClient()
    db = client.mcollection
    mcursor = db.mcollection.find({'project':proname})
    mchecks = []
    for document in mcursor:
        mchecks.append(document['mtype'])
    mcheck = list(set(mchecks))
    presentdate = datetime.isoformat(datetime.now())
    lasthourdate = datetime.isoformat(datetime.now()-timedelta(hours =1))
    mdategraph ={'lasthourdate':lasthourdate,"presentdate":presentdate}
    return render(request,'monitorgraph/monitorlistparm.html',{'mcheck':mcheck,'proname':proname,"mdategraph":mdategraph})

#for converting date to google charts date

def mdate(val):
    a = "Date("+str(val.year)+','+str(val.month-1)+','+str(val.day)+","+str(val.hour)+","+str(val.minute)+")"
    return a

#mongodb database collection

def MongodbCollection():
    client = MongoClient()
    dbCollection = client.mcollection
    return dbCollection

#for monitoring memory free
@csrf_exempt
def MonitorCheckMemory(request):
    project = request.GET.get('proname')
    mtype = request.GET.get('mtype')
    pdate = request.GET.get('pdate')
    ldate = request.GET.get('ldate')
    if pdate ==None:
        pdate = datetime.isoformat(datetime.now())
    if ldate ==None:
        ldate = datetime.isoformat(datetime.now()-timedelta(hours =1))

    mcursor = MongodbCollection().mcollection.find({"project":project,"mtype":mtype,"mdatetime":{'$gte':ldate,'$lt':pdate}})

    regex = r'([0-9.]+)?%'

    result = [[mdate(dateutil.parser.parse(item['mdatetime'])),int(re.findall(regex,item['matrix'].strip())[0])] for item in mcursor]
    print result

    return render(request,'monitorgraph/mgraph.html',{'result':result} )


def MonitorCheckCpu(request):
    if request.GET:
        project = request.GET.get('proname')
        mtype = request.GET.get('mtype')
        pdate = request.GET.get('pdate')
        ldate = request.GET.get('ldate')

        if pdate ==None:
            pdate = datetime.isoformat(datetime.now())
        if ldate ==None:
            ldate = datetime.isoformat(datetime.now()-timedelta(hours =1))

        mcursor = MongodbCollection().mcollection.find({"project":project,"mtype":mtype,"mdatetime":{'$gte':ldate,'$lt':pdate}})



        result = []
        for item in mcursor:
            print item
            #result = [[item['matrix'][18:],mdate(dateutil.parser.parse(item['mdatetime']))]for item in mcursor]
            tmp_rs = [float(value) for value in map(lambda x:x.split('=')[1], item['matrix'].strip().split(' ')[3:])]
            tmp_rs.append(mdate(dateutil.parser.parse(item['mdatetime'])))
            result.append(tmp_rs)

        print result

        return render(request,'monitorgraph/monitorcheckcpu.html',{"result":result})