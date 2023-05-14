#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow_ptr = *head, *fast_ptr = *head;
    listint_t *prev_slow_ptr = NULL, *mid_ptr = NULL;
    listint_t *second_half = NULL;
    int is_palindrome = 1;

    if (*head != NULL && (*head)->next != NULL)
    {
        while (fast_ptr != NULL && fast_ptr->next != NULL)
        {
            fast_ptr = fast_ptr->next->next;
            prev_slow_ptr = slow_ptr;
            slow_ptr = slow_ptr->next;
        }

        if (fast_ptr != NULL)
        {
            mid_ptr = slow_ptr;
            slow_ptr = slow_ptr->next;
        }

        second_half = slow_ptr;
        prev_slow_ptr->next = NULL;
        reverse_list(&second_half);
        is_palindrome = compare_lists(*head, second_half);
        reverse_list(&second_half);

        if (mid_ptr != NULL)
        {
            prev_slow_ptr->next = mid_ptr;
            mid_ptr->next = second_half;
        }
        else
            prev_slow_ptr->next = second_half;
    }

    return is_palindrome;
}

/**
 * reverse_list - reverses a singly linked list
 * @head: pointer to head of list
 */
void reverse_list(listint_t **head)
{
    listint_t *prev_node = NULL, *current_node = *head, *next_node = NULL;

    while (current_node != NULL)
    {
        next_node = current_node->next;
        current_node->next = prev_node;
        prev_node = current_node;
        current_node = next_node;
    }

    *head = prev_node;
}

/**
 * compare_lists - compares two singly linked lists
 * @head1: pointer to head of first list
 * @head2: pointer to head of second list
 * Return: 0 if the lists are not equal, 1 if they are equal
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
    listint_t *temp1 = head1, *temp2 = head2;

    while (temp1 && temp2)
    {
        if (temp1->n == temp2->n)
        {
            temp1 = temp1->next;
            temp2 = temp2->next;
        }
        else
            return 0;
    }

    if (temp1 == NULL && temp2 == NULL)
        return 1;

    return 0;
}
