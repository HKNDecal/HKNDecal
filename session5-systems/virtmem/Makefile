all: vmem

vmem: vmem.o
	gcc -ggdb3 vmem.o -o vmem

vmem.o: vmem.c
	gcc -ggdb3 -c vmem.c -o vmem.o

clean:
	rm -f vmem.o vmem
