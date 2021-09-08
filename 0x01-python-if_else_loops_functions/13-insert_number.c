#include "lists.h"

/**
 * *insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to a pointer of the beggining of the list
 * @number: number to add
 * Return: A new node added
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *first;

	first = *head;
/* creating an filling node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (first->n >= new_node->n || !*head)
	{ /* Case new is less than head*/
		new_node->next = first;
		*head = new_node;
		return (new_node);
	}
	while (first != NULL && first->next != NULL && first->next->n < new_node->n)
		first = first->next;
	new_node->next = first->next;
	first->next = new_node;
	return (new_node);
}
