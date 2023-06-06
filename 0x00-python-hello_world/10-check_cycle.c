#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @listt: linked list to check
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *listt)
{
	listint_t *slow = listt;
	listint_t *fast = listt;

	if (!listt)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
