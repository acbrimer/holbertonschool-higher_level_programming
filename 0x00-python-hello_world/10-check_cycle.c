#include "lists.h"

/**
 * check_cycle - checks if linked list has a cycle
 * @list: starting node for linked list
 *
 * Return: 1 for cycle, else 0
*/
int check_cycle(listint_t *list)
{
	listint_t *tmp, *lead_tmp;

	if (list == NULL)
		return (0);
	tmp = list;
	lead_tmp = tmp->next;
	while (tmp && tmp->next && lead_tmp && lead_tmp->next)
	{
		if (tmp == lead_tmp)
			return (1);
		tmp = tmp->next;
		lead_tmp = lead_tmp->next;
		lead_tmp = lead_tmp->next;
	}
	return (0);
}
