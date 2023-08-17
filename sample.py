import ex3 as e
file = open("output.txt","w")
file.write(str(e.Movement.movement_by_product(e.p1)))
file.write("\n")
file.write(str(e.Movement.movement_by_product(e.p2)))
file.write("\n")
file.write(str(e.Movement.movement_by_product(e.p3)))
file.write("\n")
file.write(str(e.Movement.movement_by_product(e.p4)))
file.write("\n")
file.write(str(e.Movement.movement_by_product(e.p5)))

