#include "lists.h"

/**
 *check_cycle - checks if a linked list contains a cycle
 *@list: linked list to check
 *
 *Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
		listint_t *too_slow = list;
			listint_t *too_fast = list;

				if (!list)
							return (0);

					while (too_slow && too_fast && too_fast->next)
							{
										too_slow = too_slow->next;
												too_fast = too_fast->next->next;
														if (too_slow == too_fast)
																		return (1);
															}

						return (0);
}
