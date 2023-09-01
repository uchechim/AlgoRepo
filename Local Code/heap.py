import heapq

arr = [100,9,20,30,40,10,1]
print("\nOriginal Array :", arr)

#create a heap from an existing array (O(N)) ? - default is a minheap
heapq.heapify(arr)
print("Newly created heap :", arr)

#adding element to heap 
heapq.heappush(arr, 25)

print("\nAdding element '25' to heap :", arr)


#popping root element from heap
val = heapq.heappop(arr)

print("\nValue popped:", val)
print("Heap structure after pop:", arr)


maxHeap = []
heapq.heapify(maxHeap)

#clearly O(N*Log(N)) time.
for num in arr:
    heapq.heappush(maxHeap, num*-1)

print("\nMax heap creation: ", maxHeap)