#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Function that inserts a number into a singly linked list
 * @head: Pointer to head pointer that points to head node
 * @number: The number to be inserted into the list
 *
 * Return: Returns a pointer to new node, returns NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node = NULL, *current = NULL;

new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
return (NULL);
new_node->n = number;
new_node->next = NULL;

if (*head == NULL || number < (*head)->n)
{
new_node->next = *head;
*head = new_node;
return (new_node);
}

current = *head;
while (current->next != NULL && current->next->n <= number)
current = current->next;

new_node->next = current->next;
current->next = new_node;

return (new_node);
}
