#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 * If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
listint_t *slow_ptr, *fast_ptr, *prev_slow_ptr, *mid_node, *second_half;
listint_t *tmp = *head;
int is_pal = 1;

if (*head != NULL && (*head)->next != NULL)
{
slow_ptr = *head;
fast_ptr = *head;
prev_slow_ptr = *head;

while (fast_ptr != NULL && fast_ptr->next != NULL)
{
fast_ptr = fast_ptr->next->next;
prev_slow_ptr = slow_ptr;
slow_ptr = slow_ptr->next;
}

if (fast_ptr != NULL)
{
mid_node = slow_ptr;
slow_ptr = slow_ptr->next;
}

second_half = slow_ptr;
prev_slow_ptr->next = NULL;
reverse_listint(&second_half);
is_pal = compare_lists(*head, second_half);
reverse_listint(&second_half);

if (mid_node != NULL)
{
prev_slow_ptr->next = mid_node;
mid_node->next = second_half;
}
else
{
prev_slow_ptr->next = second_half;
}
}
return (is_pal);
}

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next = NULL;

while (current != NULL)
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
 * compare_lists - Compares two singly linked lists for equality.
 * @head1: A pointer to the head of the first linked list.
 * @head2: A pointer to the head of the second linked list.
 *
 * Return: If the two lists are equal - 1.
 * Otherwise - 0.
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
while (head1 != NULL && head2 != NULL)
{
if (head1->n != head2->n)
{
return (0);
}
head1 = head1->next;
head2 = head2->next;
}

return (head1 == NULL && head2 == NULL);
}
