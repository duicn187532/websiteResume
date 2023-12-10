import urllib.request as req
import moudule.Getrid as Getrid

def Get(url):
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        })

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    import json
    Idata=json.loads(data)
    Sdata=json.dumps(Idata,ensure_ascii=False)
    return Sdata


def run(batch,sect):
    offset=batch*30
    url1="https://tw.stock.yahoo.com/class-quote?sectorId=41&exchange=TAI"
    rid_value =Getrid.getrid(url1)
    nurl = ("https://tw.stock.yahoo.com/_td-stock/api/resource/StockServices.getClassQuotes;exchange=TAI;"
    "offset="+str(offset)+";sectorId="+str(sect)+"?bkt=&device=desktop&ecma=modern&"
    "feature=useNewQuoteTabColor&intl=tw&lang=zh-Hant-TW&partner=none&prid="+str(rid_value)+
    "&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.1979&returnMeta=true")
    return str(Get(nurl))

if __name__=="__main__":
    run()

# for TAIIds in TAIId:
#     for offset in range(0,120, 30):
#         url1="https://tw.stock.yahoo.com/class-quote?sectorId="+str(TAIIds)+"&exchange=TAI"
#         rid_value =Getrid.getrid(url1)
#         nurl = ("https://tw.stock.yahoo.com/_td-stock/api/resource/StockServices.getClassQuotes;exchange=TAI;"
#                 "offset="+str(offset)+";sectorId="+str(TAIIds)+"?bkt=&device=desktop&ecma=modern&"
#                 "feature=useNewQuoteTabColor&intl=tw&lang=zh-Hant-TW&partner=none&prid="+str(rid_value)+
#                 "&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.1979&returnMeta=true")            
# for TWOIds in TWOId:
#     for offset in range(0,120,30):
#         url2="https://tw.stock.yahoo.com/class-quote?sectorId="+str(TWOIds)+"&exchange=TWO"
#         rid_value =Getrid.getrid(url2)
#         nnurl=("https://tw.stock.yahoo.com/_td-stock/api/resource/StockServices.getClassQuotes;exchange=TWO;"
#                 "offset="+str(offset)+";sectorId="+str(TWOIds)+"?bkt=&device=desktop&ecma=modern&"
#                 "feature=useNewQuoteTabColor&intl=tw&lang=zh-Hant-TW&partner=none&prid="+str(rid_value)+
#                 "&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.1979&returnMeta=true")