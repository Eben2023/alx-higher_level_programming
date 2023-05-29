#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints information about a Python list
 * @p: Pointer to a PyObject representing a Python list
 */
void print_python_list(PyObject *p)
{
Py_ssize_t size, alloc, i;
PyObject *item;

size = PyList_Size(p);
alloc = ((PyListObject *)p)->allocated;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", alloc);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to a PyObject representing a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *data;

printf("[.] bytes object info\n");

if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
data = PyBytes_AsString(p);

printf("  size: %zd\n", size);
printf("  trying string: %s\n", data);

printf("  first %zd bytes:", (size + 1 < 10 ? size + 1 : 10));
for (i = 0; i < size + 1 && i < 10; i++)
printf(" %02x", (unsigned char)data[i]);
printf("\n");
}

/**
 * print_python_float - Prints information about a Python float object
 * @p: Pointer to a PyObject representing a Python float object
 */
void print_python_float(PyObject *p)
{
double value;

printf("[.] float object info\n");

if (!PyFloat_Check(p))
{
printf("  [ERROR] Invalid Float Object\n");
return;
}

value = PyFloat_AsDouble(p);

printf("  value: %g\n", value);
}
