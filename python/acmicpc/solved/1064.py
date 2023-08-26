xa,ya,xb,yb,xc,yc = map(float, input().split())

if (ya-yb)*(xc-xb)==(yc-yb)*(xa-xb):
    print(-1.0)

else:
    len1 = 2*(((xb-xa)**2+(yb-ya)**2)**0.5+((xc-xa)**2+(yc-ya)**2)**0.5)
    len2 = 2*(((xa-xb)**2+(ya-yb)**2)**0.5+((xc-xb)**2+(yc-yb)**2)**0.5)
    len3 = 2*(((xa-xc)**2+(ya-yc)**2)**0.5+((xb-xc)**2+(yb-yc)**2)**0.5)

    len=[len1,len2,len3]
    print(max(len)-min(len))