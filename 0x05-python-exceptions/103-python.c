#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 *
 * Return: void
 */

void print_python_bytes(PyObject *p)
{
Py_ssize_t x;
Py_ssize_t var_size;

PyBytesObject *_byte = (PyBytesObject *)p;
fflush(stdout);

printf("[.] _byte object info\n");
if (strcmp(p->ob_type->tp_name, "_byte") != 0)
{
printf("  [ERROR] Invalid _byte Object\n");
return;
}

printf("  var_size: %ld\n", ((PyVarObject *)p)->ob_size);
printf("  trying string: %s\n", _byte->ob_sval);

if (((PyVarObject *)p)->ob_size >= 10)
var_size = 10;
else
{
var_size = ((PyVarObject *)p)->ob_size + 1;
}
printf("  first %ld _byte: ", var_size);
for (x = 0; x < var_size; x++)
{
printf("%02hhx", _byte->ob_sval[x]);
if (x == (var_size - 1))
printf("\n");
else
printf(" ");
}
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 *
 * Return: void
 */

void print_python_float(PyObject *p)
{
PyFloatObject *fl_object = (PyFloatObject *)p;
char *buff = NULL;
fflush(stdout);

printf("[.] float object info\n");
if (strcmp(p->ob_type->tp_name, "float") != 0)
{
printf("  [ERROR] Invalid Float Object\n");
return;
}

buff = PyOS_double_to_string(fl_object->ob_fval, 'r', 0,
 Py_DTSF_ADD_DOT_0, NULL);
printf("  value: %s\n", buff);
PyMem_Free(buff);
}

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 *
 * Return: void
 */

void print_python_list(PyObject *p)
{
const char *var_type;
Py_ssize_t x;
Py_ssize_t var_size;
Py_ssize_t dist_aloc;

PyListObject *list = (PyListObject *)p;
PyVarObject *var = (PyVarObject *)p;

var_size = var->ob_size;
dist_aloc = list->allocated;
fflush(stdout);

printf("[*] Python list info\n");
if (strcmp(p->ob_type->tp_name, "list") != 0)
{
printf("  [ERROR] Invalid List Object\n");
return;
}

printf("[*] var_size of the Python List = %ld\n", var_size);
printf("[*] Allocated = %ld\n", dist_aloc);

for (x = 0; x < var_size; x++)
{
var_type = list->ob_item[x]->ob_type->tp_name;
printf("Element %ld: %s\n", x, var_type);
if (strcmp(var_type, "_byte") == 0)
print_python_bytes(list->ob_item[x]);
else if (strcmp(var_type, "float") == 0)
print_python_float(list->ob_item[x]);
}
}
