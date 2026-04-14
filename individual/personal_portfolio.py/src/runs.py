#file to run other files
#import all files for projects
import fractal_generator.main as frac, classes_project.main as clas, class_relationships.src.main as crel, movie_reccomender_project.movie_recommender as mrec

#create function run, get number
def run(num):
    #run file corresponding to that number.
    if num==1:
        frac.main()
    elif num==2:
        clas.main()
    elif num==3:
        crel.main()
    else:
        mrec.main()