#include <errno.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <sys/mman.h>

int main(int argc, char** argv) {
    /* Print usage if the wrong number of arguments are provided. */
    if (argc != 3) {
        printf("Writes a value to a particular memory address, and then reads the memory address and prints out its value every second.\n");
        printf("Usage: %s <address> <value>\n", argv[0]);
        return 1;
    }

    /* Parse the provided arguments. */
    errno = 0;
    unsigned long long argaddress = strtoull(argv[1], NULL, 0);
    if (errno != 0) {
        printf("Address is not a valid unsigned integer: got %s\n", argv[1]);
        return 2;
    }

    unsigned long long argvalue = strtoull(argv[2], NULL, 0);
    if (errno != 0) {
        printf("Value is not a valid unsigned integer: got %s\n", argv[2]);
        return 2;
    }

    unsigned char value = (unsigned char) argvalue;
    if (value != argvalue) {
        printf("Value must be an integer from 0 to 255; got %llu\n", argvalue);
        return 2;
    }

    /* Allocate the memory address using mmap. The allocated memory block will
       start on a page boundary (for Linux), so we need to allocate a full page
       worth of memory to guarantee that the provided address is valid. */
    unsigned long long pagesize = (unsigned long long) getpagesize();
    unsigned long long alignedaddr = argaddress & ~(pagesize - 1);
    void* pageptr = mmap((void*) alignedaddr, (size_t) pagesize, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_FIXED, -1, 0);
    if (pageptr == MAP_FAILED) {
        perror("mmap() error");
        pageptr = mmap((void*) alignedaddr, (size_t) pagesize, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
        if (pageptr != MAP_FAILED) {
            printf("A nearby address range that would work is: %p to %p\n", pageptr, ((char*) pageptr) + (pagesize - 1));
        }
        return 3;
    }

    volatile unsigned char* addr = (volatile unsigned char*) argaddress;

    if (addr < (volatile unsigned char*) pageptr || addr >= (addr + pagesize)) {
        printf("mmap() did not allocate the correct page\n");
        return 4;
    }

    /* At this point, addr is a valid pointer. */
    *addr = value;
    printf("Wrote value %u to memory address %p\n", value, addr);
    while (true) {
        sleep(1);
        printf("The value at memory address %p is %u\n", addr, *addr);
    }

    return 0;
}
