fov = 450
specimen = 15
ml = 6.9

ml = ml * 10000
al = fov/specimen
print('AL = FoV/#Specimen')
print("AL = " + str(fov) + "um/" + str(specimen))
print("AL = " + str(al) + "um")
lm = ml/al
print('LM = ML/AL')
print("LM = " + str(ml) + "um/" + str(al) + "um")
print("LM = " + str(lm) + "x")
sb = al/(ml / 10000)
print('SB = AL/ML')
print("SB = " + str(al) + "um/" + str(ml / 10000) + "cm")
print("SB = " + str(sb) + "um/cm")