import threading

total_sum = 0
lock = threading.Lock()

def partial_sum(start, end):
    global total_sum
    subtotal = 0
    for i in range(start, end + 1):
        subtotal += i
    
    lock.acquire()
    total_sum += subtotal
    lock.release()

start = int(input("Input angka awal: "))
end = int(input("Input angka akhir: "))
num_threads = int(input("Jumlah thread: "))

range_size = (end - start + 1) // num_threads

threads = []
current_start = start

for i in range(num_threads):
    current_end = current_start + range_size - 1
    if i == num_threads - 1:
        current_end = end
    
    t = threading.Thread(target=partial_sum, args=(current_start, current_end))
    threads.append(t)
    t.start()
    
    current_start = current_end + 1

for t in threads:
    t.join()

print("Hasil penjumlahan:", total_sum)