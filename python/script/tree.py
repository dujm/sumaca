from contextfree import *

@check_limits
def branch():
    line(0,0.99)
    with transform(y=1, alpha=-0.05): # remove scale=0.7 + rnd(0.15), 
        with transform(angle=15+prnd(20)):
            branch()
        with transform(angle=-15-prnd(20)):
            branch()


init(canvas_size=(600, 600), face_color="#DEF2F1",background_color="#3AAFA9",max_depth=9) 
with transform():
    branch()
    write_to_png("../pics/tree.png")


