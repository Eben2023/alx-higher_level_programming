#include <Python.h>

/**
 * print_python_list_info - Prints basic info about a Python list object.
 * @p: A pointer to a PyObject list object.
 *
 * Description: This function prints the size of the list, and the data
 * type of each element in the list.
 *
 * Return: Nothing.
 */

void print_python_list_info(PyObject *p)
{
int size = (int)PyList_Size(p);
printf("[*] Size of the Python List = %d\n", size);

int alloc = (int)(((PyListObject *)p)->allocated);
printf("[*] Allocated = %d\n", alloc);

int i;
PyObject *item;
PyListObject *plist = (PyListObject *)p;
for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
}
}
