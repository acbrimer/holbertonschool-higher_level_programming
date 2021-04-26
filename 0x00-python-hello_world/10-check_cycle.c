#include "lists.h"

/**
 * check_cycle - checks if linked list has a cycle
 * @list: starting node for linked list
 *
 * Return: 1 for cycle, else 0
*/
int check_cycle(listint_t *list)
{
	listint_t *tmp = list;
	listint_t *head = list;

	if (list == NULL)
		return (0);
	while (tmp)
	{
		if (tmp->next == head)
			return (1);
		tmp = tmp->next;
	}

	return (0);
}
