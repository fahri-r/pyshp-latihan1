import shapefile

w=shapefile.Writer('./soal10',shapeType=shapefile.POLYGON)
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu")
w.record("crot","dua")
w.record("alah","tiga")
w.record("aduh","empat")
w.record("duka","lima")



w.poly([[[1,4], [1,0], [4,0]]])
w.poly([[[1,5], [5,5], [5,1]]])
w.poly([[[7,4], [7,0], [9,0]]])
w.poly([[[7,8], [7,6], [9,6]]])
w.poly([[[1,6], [6,6], [6,8]]])
