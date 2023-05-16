#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
if (!*head || !(*head)->next)
return (*head);

listint_t *new_head = reverse_listint(&(*head)->next);

(*head)->next->next = *head;
(*head)->next = NULL;

*head = new_head;

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
if (!*head || !(*head)->next)
return (1);

listint_t *slow = *head, *fast = *head;
listint_t *prev = NULL, *tmp = NULL;

while (fast && fast->next)
{
fast = fast->next->next;

tmp = slow->next;
slow->next = prev;
prev = slow;
slow = tmp;
}

if (fast)
slow = slow->next;

while (prev && slow)
{
if (prev->n != slow->n)
return (0);

prev = prev->next;
slow = slow->next;
}

return (1);
}
