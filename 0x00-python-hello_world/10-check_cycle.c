#include "lists.h"

/**
 * check_cycle - Function used to check if it is a cycle
 * @list: Structure of type listint_t which content the node to check
 * Return:
 *        1 if has cycle
 *        0 if has not cycle
 **/
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *quick = list;

	while (quick != NULL && slow != NULL && quick->next != NULL)
	{
		/* Making validations inside loop*/
		slow = slow->next;
		quick = quick->next->next;
		if (quick == slow)
			return (1);
	}
	return (0);
}
