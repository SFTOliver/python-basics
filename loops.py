# loop structure in python

#creating a lit of numbers(iterable items)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];

#we create the loop
for item in a:
    print(item);
count = 0;
while (count < 10):
    print(a[count]);
    count = count + 1;

for index, item in enumerate(a):
    print(index, ". ", item);

b = [x * x for x in a if x != 5]  # list comprehension and for loop.
print(b);
