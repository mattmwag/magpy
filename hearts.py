import squares as s, triangles as t, harshad as h, digit as d

ac1 = d.has_3(list(set(s.up_to(999) + t.up_to(999))))
ac1 = filter(lambda n: n < 500, ac1)

dn4 = range(100, 180)

# print([(ac,dn) for ac in ac1 for dn in dn4 if d.third(ac+dn*2) == d.first(ac+dn*3)
#        and d.second(ac+dn*4) == d.third(dn) and d.third(ac+dn*5) == d.first(ac)
#        and ac+dn*5 < 1000])
# [(136,155), (121, 152)]

print(d.has_3(h.up_to(1000)))

