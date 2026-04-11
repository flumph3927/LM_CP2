#LM 1st geometry calculator
import classes_project.two_d, classes_project.tre_d, classes_project.relations, classes_project.transform as transform

#create function main
def main():
    shapes={}
    #loop
    while True:
        #display menu to create shape, view shapes, draw shape, transform shape, compare shapes, sort 2d shapes, sort 3d shapes, get formula explanations, or exit
        choic=input('1. Create Shape\n2. View Shapes\n3. Draw Shape\n4. Transform Shape\n5. Compare Shape\n6. Sort 2d Shapes\n7. Sort 3d Shapes\n8. Get Formula Explanations\n9. Exit\n')
        while choic not in ['1','2','3','4','5','6','7','8','9']:
            print('Invalid Input. Try Again.')
            choic=input('1. Create Shape\n2. View Shapes\n3. Draw Shape\n4. Transform Shape\n5. Compare Shape\n6. Sort 2d Shapes\n7. Sort 3d Shapes\n8. Get Formula Explanations\n9. Exit\n')
        #if create shape:
        if choic=='1':
            #get name for shape(will replace)
            nme=input('What are you naming this shape(will replace previous shapes of the same name): ')
            #get type of shape
            typ=input('What type of shape are you generating:\n1. Circle\n2. Rectangle\n3. Triangle\n4. Cube\n5. Cylinder\n6. Tetrahedron\n')
            while typ not in [str(x+1) for x in range(6)]:
                print('Invalid Input. Try Again.')
                typ=input('What type of shape are you generating:\n1. Circle\n2. Rectangle\n3. Triangle\n4. Cube\n5. Cylinder\n6. Tetrahedron\n')
            #create appropriate object
            if typ==f'1': shapes[nme]=classes_project.two_d.Circ(nme)
            elif typ=='2':shapes[nme]=classes_project.two_d.Rect(nme)
            elif typ=='3': shapes[nme]=classes_project.two_d.Tri(nme)
            elif typ=='4':shapes[nme]=classes_project.tre_d.Cube(nme)
            elif typ=='5': shapes[nme]=classes_project.tre_d.Cyl(nme)
            if typ=='6': shapes[nme]=classes_project.tre_d.Tetra(nme)
        #elif view shapes:
        elif choic=='2':
            #loop through shape dict and display
            classes_project.relations.view(shapes)
        #elif draw shape:
        elif choic=='3':
            #choose then draw shape
            classes_project.relations.select(shapes).draw()
        #elif transform shape:
        elif choic=='4':
            #run function transforms
            shap=classes_project.relations.select(shapes)
            shape=transform.transforms(shap)
            shapes[shap.name]=shape
        #elif compare shape:
        elif choic=='5':
            #run function select shape
            shap=classes_project.relations.select(shapes)
            #run function select shape on shapes of the same dimensions as the first shape
            same={}
            for i,v in shapes.items():
                if v.typ==shap.typ:
                    same[i]=v
            also=classes_project.relations.select(same)
            #get comparison type, run choice function in compare
            #display results
            print(f'{classes_project.relations.choice([also,shap]).name} has a larger value in the selected field.')
        #elif sort 2d shapes:
        elif choic=='6':
            #run sort function on all 2d shapes
            same={}
            for i,v in shapes.items():
                if v.typ==2:
                    same[i]=v
            #show results
            classes_project.relations.view(classes_project.relations.sort(same))
        #elif sort 3d shapes:
        elif choic=='7':
            #run sort function on all 3d shapes
            same={}
            for i,v in shapes.items():
                if v.typ==3:
                    same[i]=v
            #show results
            classes_project.relations.view(classes_project.relations.sort(same))
        #elif get formula explanations
        elif choic=='8':
            #get type of shape
            while True:
                try:
                    shp_typ=int(input('1. Circle\n2. Rectangle\n3. Triangle\n4. Cube\n5. Cylinder\n6. Tetrahedron\n'))
                    if shp_typ not in [1,2,3,4,5,6]:
                        int('hi')
                    break
                except:
                    print('Invalid input. Try again.')
            #show appropriate formulas
            forms=[classes_project.two_d.Circ,classes_project.two_d.Rect,classes_project.two_d.Tri,classes_project.tre_d.Cube,classes_project.tre_d.Cyl,classes_project.tre_d.Tetra]
            forms[shp_typ-1].info()
        #else:
        else:
            #break out of loop
            break
