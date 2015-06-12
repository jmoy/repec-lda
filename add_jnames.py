#!/usr/bin/python3
import sqlite3
import sys

archives = [
    ("oup:qjecon", "Quarterly Journal of Economics"),
    ("aea:aecrev", "American Economic Review"),
    ("aea:aejmac", "American Economic Journal: Macroeconomics"),
    ("bla:ijethy", "International Journal of Economic Theory"),
    ("bla:jeurec", "Journal of European Economic Association"),
    ("bla:restud", "Review of Economic Studies"),
    ("ecm:emetrp", "Econometrica"),
    ("eee:dyncon", "Journal of Economic Dynamics and Control"),
    ("eee:gamebe", "Games and Economic Behaviour"),
    ("eee:jbfina", "Journal of Banking and Finance"),
    ("eee:jetheo", "Journal of Economic Theory"),
    ("eee:moneco", "Journal of Monetary Economics"),
    ("mcb:jmoncb", "Journal of Money, Credit and Banking"),
    ("oup:restud", "Review of Economic Studies"),
    ("red:issued", "Review of Economic Dynamics"),
    ("spr:joecth", "Economic Theory"),
    ("spr:jogath", "International Journal of Game Theory"),
    ("the:publsh", "Theoretical Economics"),
    ("tpr:jeurec", "Journal of European Economic Association"),
    ("tpr:qjecon", "Quarterly Journal of Economics"),
    ("tpr:restat", "Review of Economics and Statistics"),
    ("ucp:macann", "NBER Macroeconomics Annual"),
    ("wly:emetrp", "Econometrica"),
    ("wly:jmoncb", "Journal of Money, Credit and Banking"),
    ("eee:matsoc", "Mathematical Social Sciences")
]


if __name__=="__main__":
  dbcon = sqlite3.connect(sys.argv[1])
  dbcon.execute("DROP TABLE IF EXISTS series")
  dbcon.execute("""CREATE TABLE series
                        (seriesid TEXT PRIMARY KEY, name TEXT)""")
  dbcon.executemany("INSERT INTO series VALUES (?,?)",archives)
  dbcon.commit()
  dbcon.close()
