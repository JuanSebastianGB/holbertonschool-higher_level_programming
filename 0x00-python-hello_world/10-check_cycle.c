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
	listint_t *slow, *quick;

	if (list == NULL || list->next == NULL)
		return (0);
	slow = list->next;
	quick = slow->next;

	while (quick != NULL && slow != NULL && list != NULL)
	{
		if (quick == slow)
			return (1);
		slow = slow->next;
		quick = quick->next->next;
	}
	return (0);
}
