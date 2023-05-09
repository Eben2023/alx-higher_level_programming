#include "lists.h"

/**
 * check_cycle - Function checks for cycle
 * @list: A pointer to the head node
 * Return: 0 for no cycle, else 1
 */

int check_cycle(listint_t *list)
{
listint_t *slow, *fast;

if (list == NULL)
{
return (0);
}

slow = list;
fast = list->next;

while (fast != NULL && fast->next != NULL)
{
if (fast == slow)
{
return (1);
}

slow = slow->next;
fast = fast->next->next;
}

return (0);
}

