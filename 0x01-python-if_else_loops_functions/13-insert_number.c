#include "lists.h"

/**
 * instert_node - inserts a node into a linked list
 * @head: linked list head
 * @number: number value for new node
 * Return: pointer to new node or NULL for fail
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *tmp = *head, *prev;

	if (new == NULL)
		return (NULL);
	while (tmp && tmp->n < number)
	{
			prev = tmp;
			tmp = tmp->next;
	}
	new->n = number;
	if (prev == NULL || tmp == *head)
	{
		prev = *head;
		new->next = prev;
		*head = new;
		return (new);
	}
	if (*head == NULL)
	{
		new->next = tmp;
		*head = new;
		return (new);
	}
	new->next = prev->next;
	prev->next = new;

	return (new);
}
