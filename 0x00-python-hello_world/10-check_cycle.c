#include"lists.h"
/**
 * check_cycle - checks if the list is cycle
 * Desription: if the list is cycle list
 * @list: pointer to the list
 * Return: 1 if there is a cycle and 0 if none
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (!list || !list->next)
		return (0);
	fast = list;
	slow = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
