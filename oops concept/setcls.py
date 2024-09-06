# num_set={"ramu",45,25}
# print(len(num_set))
# print(num_set)
#num=set(())
# furite_set=set(("apple","banana"))
# furite_set.add("graps")
# print(furite_set)
#furite_set.remove("graps")  
#furite_set.remove("watermelon")
#furite_set.discard("apple")
#furite_set.discard("watermelon")

#print(furite_set)

frozenset1=frozenset(["apple","banana","grapes"])
frozenset2=frozenset(["mango","apple"])
union1=frozenset1|frozenset2
print(union1)
symm=frozenset1&frozenset2
print(symm)
sym=frozenset1-frozenset2
print(sym)
