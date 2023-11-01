#include "lists.h"
#include <stdlib.h>

/**
* add_nodeint - Adds a new node at the beginning of a listint_t list
* @head: Head of the list
* @n: Value of the new element
*
*Return: The address of the new node
*/
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}
/**
* insert_nodeint_at_index - Inserts a new node at a given position
* @head: Head of the list
* @idx: Index
* @n: Value of the new element
*
* Return: Address of the new element
*/
listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n)
{
	int i;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new ==  NULL)
		return (NULL);
	new->n = n;
	if (idx == 0)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	for (i = 0; *head != NULL; i++)
	{
		if (i + 1 == (int) idx)
		{
			new->next = (*head)->next;
			(*head)->next = new;
			return (new);
		}
		head = &(*head)->next;
	}
	return (NULL);
}
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	int index;

	if (head == NULL)
		return (NULL);
	if (*head == NULL)
		return (add_nodeint(head, number));
	current = *head;
	if (current->n >= number)
		return (add_nodeint(head, number));
	for (index = 0; current != NULL && current->next != NULL; current = current->next, index++)
		return (insert_nodeint_at_index(head, index, number));
}
