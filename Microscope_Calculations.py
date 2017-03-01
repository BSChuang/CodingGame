fov = 450
specimen = 15
ml = 4.92

ml = ml * 10000
al = fov/specimen
print("al = " + str(fov) + "um/" + str(specimen))
print("al = " + str(al) + "um")
lm = ml/al
print("lm = " + str(ml) + " um/" + str(al) + "um")
print("lm = " + str(lm) + "x")
sb = al/(ml / 10000)
print("sb = " + str(al) + " um/" + str(ml / 10000) + "cm")
print("sb = " + str(sb) + " um/cm")