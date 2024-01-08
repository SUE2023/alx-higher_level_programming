#include"lists.h"
#include<stdio.h>
#include<stddef.h>

void reverse(listint_t **head);
int compare_lists(listint_t *head, listint_t *middle, int len);
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * Description: checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the head node
 * Return: integer
 */
int is_palindrome(listint_t **head)
{
	int len, n;
	listint_t *temp;
	listint_t *middle;

	if (head == NULL || *head == NULL)
		return (1);
	temp = *head;
	middle = *head;

	for (len = 0; temp != NULL; len++)
		temp = temp->next;

	len = len / 2;

	for (n = 1; n < len; n++)
		middle = middle->next;
	if (len % 2 != 0 && len != 1)
	{
		middle = middle->next;
		len = len - 1;
	}
	reverse(&middle);
	n = compare_lists(*head, middle, len);

	return (n);
}
/**
 * compare_lists - compare two lists
 * Description: compare two lists
 * @head: pointer to the head node
 * @middle: pointer to the middle node
 * @len: length of the linked list
 * Return: integer
 */
int compare_lists(listint_t *head, listint_t *middle, int len)
{
	int n;

	if (head == NULL || middle == NULL)
		return (1);
	for (n = 0; n < len; n++)
	{
		if (head->next != middle->next)
			return (0);
		head = head->next;
		middle = middle->next;
	}
	return (1);
}
/**
 * reverse - reverses a list
 * Description: reverse a list
 * @head: pointer to pointer head
 * Return: void
 */
void reverse(listint_t **head)
{
	listint_t *current, *next, *previous;

	if (head == NULL || *head == NULL)
		return;
	previous = NULL;
	current = *head;
	while (current != NULL)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	*head = previous;
}
