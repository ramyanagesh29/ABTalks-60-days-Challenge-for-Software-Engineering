text="hello"
character=list(text)
left=0
right=len(character)-1
while(left<right):
  character[left],character[right]=character[right],character[left]
  left=left+1
  right=right-1
print("Reverse String:","".join(character))


//Output

Reverse String: olleh
