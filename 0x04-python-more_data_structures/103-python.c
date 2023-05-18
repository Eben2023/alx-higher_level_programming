#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: A pointer to the PyObject representing the bytes object
 */
void print_python_bytes(PyObject *p)
{
PyBytesObject *bytes = (PyBytesObject *)p;
Py_ssize_t size, i;
unsigned char *string;

printf("[.] bytes object info\n");
if (!PyBytes_Check(bytes))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
string = (unsigned char *)PyBytes_AsString(p);

printf("  size: %ld\n", size);
printf("  trying string: %s\n", PyBytes_AsString(p));
printf("  first %ld bytes:", (size < 10 ? size + 1 : 10));

for (i = 0; i < size && i < 10; i++)
{
printf(" %02x", string[i]);
}
printf("\n");
}

/**
 * print_python_list - Prints information about a Python list object
 * @p: A pointer to the PyObject representing the list object
 */
void print_python_list(PyObject *p)
{
Py_ssize_t size, alloc, i;
PyObject *item;

printf("[*] Python list info\n");
size = PyList_Size(p);
alloc = ((PyListObject *)p)->allocated;
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", alloc);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %ld: ", i);

if (PyBytes_Check(item))
printf("bytes\n");
else if (PyList_Check(item))
printf("list\n");
else if (PyTuple_Check(item))
printf("tuple\n");
else if (PyFloat_Check(item))
printf("float\n");
else if (PyLong_Check(item))
printf("int\n");
else if (PyUnicode_Check(item))
printf("str\n");
else
printf("other\n");
}
}
