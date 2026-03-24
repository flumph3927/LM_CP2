#LM 1st geometry calculator
import two_d, tre_d, relations, transform

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
            if typ==f'1': shapes[nme]=two_d.circ(nme)
            elif typ=='2':shapes[nme]=two_d.rect(nme)
            elif typ=='3': shapes[nme]=two_d.tri(nme)
            elif typ=='4':shapes[nme]=tre_d.cube(nme)
            elif typ=='5': shapes[nme]=tre_d.cyl(nme)
            if typ=='6': shapes[nme]=tre_d.tetra(nme)
        #elif view shapes:
        elif choic=='2':
            #loop through shape dict and display
            relations.view(shapes)
        #elif draw shape:
        elif choic=='3':
            #choose then draw shape
            relations.select(shapes).draw()
        #elif transform shape:
        elif choic=='4':
            #run function transforms
            shap=relations.select(shapes)
            shape=transform.transforms(shap)
            shapes[shap.name]=shape
        #elif compare shape:
        elif choic=='5':
            #run function select shape
            shap=relations.select(shapes)
            #run function select shape on shapes of the same dimensions as the first shape
            same={}
            for i,v in shapes.items():
                if v.typ==shap.typ:
                    same[i]=v
            also=relations.select(same)
            #get comparison type, run choice function in compare
            #display results
            print(f'{relations.choice([same,shap]).name} has a larger value in the selected field.')
        #elif sort 2d shapes:
        elif choic=='6':
            #run sort function on all 2d shapes
            same={}
            for i,v in shapes.items():
                if v.typ==2:
                    same[i]=v
            #show results
            relations.view(relations.sort(same))
        #elif sort 3d shapes:
        elif choic=='7':
            #run sort function on all 3d shapes
            same={}
            for i,v in shapes.items():
                if v.typ==3:
                    same[i]=v
            #show results
            relations.view(relations.sort(same))
        #elif get formula explanations
            #get type of shape
            #show appropriate formulas
        #else:
        else:
            #break out of loop
            break

main()