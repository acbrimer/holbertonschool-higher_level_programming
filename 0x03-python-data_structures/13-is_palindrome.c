#include "lists.h"

/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: linked list head
 *
 * Return: 1 for palindrome, else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *tail = *head, *rev = *head, *next, *prev = NULL;
	unsigned int list_len, h_len, i;
	int p = 1;

	if (head == NULL || *head == NULL)
		return (1);
	/* get total length of linked list */
	for (list_len = 0; tail; list_len++)
		tail = tail->next;
	h_len = list_len / 2;
	/* set rev to halfway point in linked list */
	for (i = 0; i < h_len; i++)
		rev = rev->next;
	/* skip middle item for odd number linked lists */
	if (list_len % 2 != 0)
		rev = rev->next;
	/* reverse from half point node rev */
	while (rev)
	{
		next = rev->next;
		rev->next = prev;
		prev = rev;
		rev = next;
	}
	rev = prev;
	/* compare reversed second half of list to first half */
	for (i = 0; i < h_len &&  p == 1; i++, *head = (*head)->next, rev = rev->next)
		if (rev->n != (*head)->n)
			p = 0;

	return (p);
}
