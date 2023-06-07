#include "Python.h"
#include <stdio.h>

/**
 * print_python_string - Prints information about Python strings
 * @p: PyObject pointer representing the Python string
 *
 * Description:
 *   This function prints the type, length, and value of the
 * given Python string.
 *   If the PyObject is not a valid string, it prints an error message.
 */

void print_python_string(PyObject *p)
{
PyUnicodeObject *str = (PyUnicodeObject *)p;

printf("[.] string object info\n");
if (!PyUnicode_Check(str))
{
printf("  [ERROR] Invalid String Object\n");
return;
}
if (PyUnicode_IS_COMPACT_ASCII(str))
printf("  type: compact ascii\n");
else
printf("  type: compact unicode object\n");
printf("  length: %ld\n", PyUnicode_GET_LENGTH(str));
printf("  value: %ls\n", PyUnicode_AS_UNICODE(str));
}
