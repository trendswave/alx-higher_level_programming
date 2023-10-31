#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 *struct s_listint - singly linked list
 *@int1: integer
 *@node: points to the next node
 *
 *Description: singly linked list node structure
 *for ALX project
 */
typedef struct s_listint
{
	    int int1;
	        struct s_listint *node;
} s_listint;



#endif /* LISTS_H */
