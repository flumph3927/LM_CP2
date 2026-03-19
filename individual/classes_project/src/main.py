#LM 1st geometry calculator
import two_d, individual.classes_project.src.tre_d as tre_d, relations, transform

#create function main
def main():
    shapes={}
    #loop
    while True:
        #display menu to create shape, view shapes, draw shape, transform shape, compare shapes, sort 2d shapes, sort 3d shapes, get formula explanations, or exit
        choic=input('1. Create Shape\n2. View Shapes\n3. Draw Shape\n4. Transform Shape\n5. Compare Shape\n6. Sort 2d Shapes\n7. Sort 3d Shapes\n8. Get Formula Explanations\n9. Exit\n')
        while choic not in ['1','2','3','4','5','6','7','8','9']:
            print('Invalid Input. Try Again.')
            choic=input('1. Create Shape\n2. View Shapes\n3. Transform Shape\n4. Compare Shape\n5. Sort 2d Shapes\n6. Sort 3d Shapes\n7. Get Formula Explanations\n8. Exit\n')
        #if create shape:
        if choic=='1':
            #get name for shape(will replace)
            nme=input('What are you naming this shape(will replace previous shapes of the same name): ')
            #get type of shape
            typ=input('What type of shape are you generating:\n1. Circle\n2. Rectangle\n3. Triangle\n4. Cube\n5. Cylinder\n6. Tetrahedron\n')
            while type not in [str(x+1) for x in range(6)]:
                print('Invalid Input. Try Again.')
                typ=input('What type of shape are you generating:\n1. Circle\n2. Rectangle\n3. Triangle\n4. Cube\n5. Cylinder\n6. Tetrahedron\n')
            #create appropriate object
            if typ==f'1': shapes[nme]=two_d.circ(nme)
            elif typ=='2':shapes[nme]=two_d.rect(nme)
            elif typ=='3': shapes[nme]=two_d.tri(nme)
            elif typ=='4':shapes[nme]=tre_d.cube(nme)
            elif typ=='5': shapes[nme]=tre_d.cyl(nme)
            if typ=='6': shapes[nme]=tre_d.tetra(nme)
        #elif view shapes:
        elif choic=='2':
            #loop through shape dict and display
        #elif transform shape:
            #run function select shape
            #get modification, run appropriate function in transform
        #elif compare shape:
            #run function select shape
            #run function select shape on shapes of the same dimensions as the first shape
            #get comparison type, run choice function in compare
            #display results
        #elif sort 2d shapes:
            #run sort function on all 2d shapes
            #show results
        #elif sort 3d shapes:
            #run sort function on all 3d shapes
            #show results
        #else:
            #break out of loop

