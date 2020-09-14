#include <stdlib.h>

int main(void) {
	int arr[10];
	size_t i;

	/* Oh no, I forgot there's something called array bounds! */
	for (i = 0; ; i++) {
		arr[i] = 666;
	}
}
