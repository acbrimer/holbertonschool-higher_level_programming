#include "lists.h"

/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: linked list head
 *
 * Return: 1 for palindrome, else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *tail = *head, *tmp = *head;
	int *list_items = NULL;
	unsigned int list_len, i;
	int palindrome = 1;

	if (head == NULL || *head == NULL)
		return (1);
	/* get total length of linked list */
	for (list_len = 0; tail; list_len++)
		tail = tail->next;
	list_items = malloc(sizeof(int) * ((list_len / 2) + 1));
	if (list_items == NULL)
		return (0);
	/* save first half of list values to array in reverse order */
	for (i = 0; i < (list_len / 2); i++, tmp = tmp->next)
		list_items[(list_len / 2) - i - 1] = tmp->n;
	/* skip middle number for odd lengths */
	if (list_len % 2 != 0)
		tmp = tmp->next;
	/* compare second half of linked list to vals in list_items */
	for (i = 0; tmp && palindrome == 1; i++, tmp = tmp->next)
		if (tmp->n != list_items[i])
			palindrome = 0;
	free(list_items);

	return (palindrome);
}
