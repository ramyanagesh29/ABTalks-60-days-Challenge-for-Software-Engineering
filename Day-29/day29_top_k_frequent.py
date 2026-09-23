import heapq

def frequency_count(hashtags):
    frequency = {}
    for hashtag in hashtags:
        frequency[hashtag] = frequency.get(hashtag, 0) + 1
    return frequency

def top_k_sorting(hashtags, k):
    frequency = frequency_count(hashtags)
    ranked = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    return [hashtag for hashtag, count in ranked[:k]]

def top_k_heap(hashtags, k):
    frequency = frequency_count(hashtags)
    heap = []
    for hashtag, count in frequency.items():
        heapq.heappush(heap, (count, hashtag))
        if len(heap) > k:
            heapq.heappop(heap)
    result = []
    while heap:
        count, hashtag = heapq.heappop(heap)
        result.append((hashtag, count))
    result.reverse()
    return [hashtag for hashtag, count in result]

hashtags = ["#python", "#ai", "#coding", "#python", "#ai", "#python", "#coding", "#tech", "#ai", "#python", "#tech", "#coding", "#ai", "#python", "#cloud"]
k = 3
frequency = frequency_count(hashtags)
sorting_result = top_k_sorting(hashtags, k)
heap_result = top_k_heap(hashtags, k)

print("----- Viral Hashtag Tracker -----")
print("Hashtags:", hashtags)
print("K:", k)
print("\nFrequency Analysis:")
for hashtag, count in frequency.items():
    print(hashtag, "->", count)
print("\nTop K Using Sorting:")
for hashtag in sorting_result:
    print(hashtag, "->", frequency[hashtag])
print("\nTop K Using Heap:")
for hashtag in heap_result:
    print(hashtag, "->", frequency[hashtag])
print("\nComplexity Comparison:")
print("Sorting: O(N + U log U) time, O(U) space")
print("Heap: O(N + U log K) time, O(U + K) space")
