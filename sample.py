import ex3 as e
a=e.Movement.movement_by_product(e.p1)
# b=e.Movement.movement_by_product(e.p2)
# c=e.Movement.movement_by_product(e.p3)
# d=e.Movement.movement_by_product(e.p4)
# e=e.Movement.movement_by_product(e.p5)
str(a)
# output = [a,b,c,d,e]
file = open("output.txt","w")
# for o in output:
file.write(a)

