a=[4,-3,-2,2,3,1,-2,-3,6,-6,-4,2,1]
c=0
st=0
poi=0
end=0
m=a[0]
for i in range (0,13):
    c=c+a[1]
    if(m<c):
        m=c
        end=1
        st=poi
    if(c<0):
        c=0
        poi=i+1
print(a)

print(c)
print(m)
print(st)
print(poi)
print(end)

