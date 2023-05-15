#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
if (!head || !(*head))
return (*head);

listint_t *prev = NULL, *current = *head, *next = NULL;
while (current)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}
*head = prev;
return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 * If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
if (!head || !(*head))
return (1);

listint_t *slow = *head, *fast = *head;
while (fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
}

listint_t *prev = NULL, *curr = slow, *next = NULL;
while (curr)
{
next = curr->next;
curr->next = prev;
prev = curr;
curr = next;
}

listint_t *p1 = *head, *p2 = prev;
while (p2)
{
if (p1->n != p2->n)
return (0);
p1 = p1->next;
p2 = p2->next;
}

return (1);
}
