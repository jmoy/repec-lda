#!/usr/bin/python3
import sqlite3
import sys

archives = [
    ("oup:qjecon", "Quarterly Journal of Economics",2),
    ("aea:aecrev", "American Economic Review",1),
    ("aea:aejmac", "American Economic Journal: Macroeconomics",3),
    ("bla:ijethy", "International Journal of Economic Theory",4),
    ("bla:jeurec", "Journal of European Economic Association",4),
    ("bla:restud", "Review of Economic Studies",1),
    ("ecm:emetrp", "Econometrica",1),
    ("eee:dyncon", "Journal of Economic Dynamics and Control",3),
    ("eee:gamebe", "Games and Economic Behaviour",3),
    ("eee:jbfina", "Journal of Banking and Finance",3),
    ("eee:jetheo", "Journal of Economic Theory",2),
    ("eee:moneco", "Journal of Monetary Economics",3),
    ("mcb:jmoncb", "Journal of Money, Credit and Banking",3),
    ("oup:restud", "Review of Economic Studies",3),
    ("red:issued", "Review of Economic Dynamics",3),
    ("spr:joecth", "Economic Theory",4),
    ("spr:jogath", "International Journal of Game Theory",4),
    ("the:publsh", "Theoretical Economics",2),
    ("tpr:jeurec", "Journal of European Economic Association",4),
    ("tpr:qjecon", "Quarterly Journal of Economics",2),
    ("tpr:restat", "Review of Economics and Statistics",2),
    ("ucp:macann", "NBER Macroeconomics Annual",3),
    ("wly:emetrp", "Econometrica",1),
    ("wly:jmoncb", "Journal of Money, Credit and Banking",3),
    ("eee:matsoc", "Mathematical Social Sciences",4)
]


if __name__=="__main__":
  dbcon = sqlite3.connect(sys.argv[1])
  dbcon.execute("DROP TABLE IF EXISTS series")
  dbcon.execute("""CREATE TABLE series
                        (seriesid TEXT PRIMARY KEY, name TEXT,rank SMALLINT)""")
  dbcon.executemany("INSERT INTO series VALUES (?,?,?)",archives)
  dbcon.commit()
  dbcon.close()
