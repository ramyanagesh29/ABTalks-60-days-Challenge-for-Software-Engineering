def maximum_happy_children(children,cookies):
    children.sort(); cookies.sort(); child=0; cookie=0; happy=0
    while child<len(children) and cookie<len(cookies):
        if cookies[cookie]>=children[child]:
            happy+=1; child+=1; cookie+=1
        else:
            cookie+=1
    return happy

children=[1,2,3]; cookies=[1,1]
print('----- Cookie Distribution Crisis -----')
print('Children happiness requirements:',children); print('Cookie sizes:',cookies)
print('Maximum happy children:',maximum_happy_children(children,cookies))
print('\nComplexity:'); print('Sorting: O(N log N + M log M)'); print('Greedy traversal: O(N + M)')
