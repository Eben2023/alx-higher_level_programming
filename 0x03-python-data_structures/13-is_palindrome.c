#include "lists.h"

/**
 * is_palindrome - Determines whether a singly linked
 * list is a palindrome.
 *
 * @head: A pointer to the head node of the linked list.
 *
 * Return: 0 if the linked list is not a palindrome, 1
 * if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head, *prev = NULL, *next;

if (*head == NULL || (*head)->next == NULL)
return (1);

while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
next = slow->next;
slow->next = prev;
prev = slow;
slow = next;
}

if (fast != NULL)
slow = slow->next;

while (prev != NULL && slow != NULL)
{
if (prev->n != slow->n)
return (0);
prev = prev->next;
slow = slow->next;
}
return (1);
}
