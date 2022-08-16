def print_designs(incomplete_designs ,completed_designs) :
    while incomplete_designs :
        current_designs =incomplete_designs.pop()
        print("Printing Model :"+ current_designs)


def show_completed_designs(completed_designs) :
    print("The following designs have been printed:")
    for completed_design in completed_designs :
        print(completed_design)


incomplete_designs=['iphone_cover','vivo_cover','mi_cover']
completed_designs=[]
print_designs(incomplete_designs[:],completed_designs)
show_completed_designs(completed_designs)