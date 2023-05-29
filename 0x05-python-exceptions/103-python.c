#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);


/**
 * print_python_list - Prints basic information about Python lists.
 * @p: A PyObject representing a Python list.
 */
void print_python_list(PyObject *p)
{
Py_ssize_t size, i;
PyObject *item;

if (!PyList_Check(p))
{
printf("[ERROR] Invalid List Object\n");
fflush(stdout);
return;
}

size = PyList_Size(p);

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);

if (PyBytes_Check(item))
print_python_bytes(item);
else if (PyFloat_Check(item))
print_python_float(item);
}
}

/**
 * print_python_bytes - Prints basic information about Python bytes objects.
 * @p: A PyObject representing a Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
const char *data;

if (!PyBytes_Check(p))
{
printf("[ERROR] Invalid Bytes Object\n");
fflush(stdout);
return;
}

size = PyBytes_Size(p);
data = PyBytes_AsString(p);

printf("[.] bytes object info\n");
printf("  size: %ld\n", size);
printf("  trying string: %s\n", data);

printf("  first %ld bytes:", (size < 10 ? size : 10));
for (i = 0; i < size && i < 10; i++)
printf(" %02x", (unsigned char)data[i]);
printf("\n");
}

/**
 * print_python_float - Prints basic information about Python float objects.
 * @p: A PyObject representing a Python float object.
 */
void print_python_float(PyObject *p)
{
double value;

if (!PyFloat_Check(p))
{
printf("[ERROR] Invalid Float Object\n");
fflush(stdout);
return;
}

value = PyFloat_AsDouble(p);

printf("[.] float object info\n");
printf("  value: %g\n", value);
fflush(stdout);
}
