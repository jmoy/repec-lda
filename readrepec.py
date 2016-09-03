#!/usr/bin/python3

import sqlite3
import tarfile
import lxml.etree
import sys

NS = {"amf":"http://amf.openlib.org"}

def extract_one(element,path):
    res = element.xpath(path,namespaces=NS)
    if len(res)==0:
        return None
    else:
        return res[0].text

def get_series(s):
   return ":".join(s.split(":")[1:3])
    
if __name__=="__main__":
    dbcon = sqlite3.connect(sys.argv[2])
    dbcon.execute("""DROP TABLE IF EXISTS article""")
    dbcon.execute("""CREATE TABLE article 
                        (id TEXT PRIMARY KEY, title TEXT,abstract TEXT, 
                        series TEXT,issue TEXT,volume TEXT,date TEXT,url TEXT,
                        authors TEXT)""")
    dbcon.execute("""CREATE INDEX IF NOT EXISTS dateix ON article (date)""")
    with tarfile.open(sys.argv[1],"r:xz") as tar:
        err_count = 0
        for item in tar:
            try:
                if not item.isfile():
                    continue
                path = item.name
                if not path.endswith(".xml"):
                  continue
                tree = lxml.etree.parse(tar.extractfile(item))
                text = tree.xpath("amf:text",namespaces=NS)[0]
                ident = text.get("id")
                title = extract_one(tree,"amf:text/amf:title")
                abstract = extract_one(tree,"amf:text/amf:abstract")
                series = get_series(ident)
                issue = extract_one(tree,"amf:text/amf:serial/amf:issue")
                volume = extract_one(tree,"amf:text/amf:serial/amf:volume")
                date = extract_one(tree,"amf:text/amf:serial/amf:issuedate")
                url = extract_one(tree,"amf:text/amf:file/amf:url")
                authors = ", ".join(e.text for e in tree.xpath("amf:text/amf:hasauthor/amf:person/amf:name",namespaces=NS))
                dbcon.execute("INSERT INTO article VALUES (?,?,?,?,?,?,?,?,?)",
                          (ident,title,abstract,series,issue,volume,date,url,authors))
                print(ident)
            except (IndexError
                    ,lxml.etree.Error
                    ,sqlite3.Error) as e:
                print("Failed "+path, file=sys.stderr)
                print(e, file=sys.stderr)
                err_count += 1
    if err_count:
      print("Total errors = {}".format(err_count)
            ,file=sys.stderr)
    dbcon.commit()        
    dbcon.close()
                                
