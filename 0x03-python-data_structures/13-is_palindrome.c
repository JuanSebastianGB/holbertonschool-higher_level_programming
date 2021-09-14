#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: Pointer pass by reference pointing to the first node
 * Return: 1 if is palyndrom -0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *traveler = NULL, *reverse = NULL, *aux = NULL;
	size_t size = 0, i = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	traveler = *head;
	size = listint_len(traveler);

	while (i < (size / 2) - 1)
	{
		traveler = traveler->next;
		i++;
	}
	if (!((size % 2) != 0 || traveler->n == traveler->next->n))
		return (0);
	traveler = traveler->next->next;
	reverse = reverse_listint(&traveler); /*Changed traveler because ref.*/
	aux = reverse;
	traveler = *head; /*Recovering traveler*/
	while (reverse != NULL)
	{
		if (traveler->n != reverse->n) /* Not matching is not palyndrome*/
			return (0);
		traveler = traveler->next;
		reverse = reverse->next;
	}
	reverse_listint(&aux);
	return (1);
}

/**
 * *reverse_listint -  reverses a listint_t linked list.
 * @head: head node
 * Return: head node
 *
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev, *next;

	if (!head || !*head)
		return (NULL);

	prev = NULL;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;
	return (*head);
}

/**
 * listint_len - returns the number of elements in a linked listint_t list.
 * @h: pointer to the head
 * Return: length of the list
 *
 */
size_t listint_len(const listint_t *h)
{
	int i = 0;

	while (h != NULL)
	{
		h = (*h).next;
		i++;
	}

	return (i);
}
