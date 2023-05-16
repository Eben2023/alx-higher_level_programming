#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
PyListObject *list = (PyListObject *)p;
Py_ssize_t size = PyList_Size(p);
Py_ssize_t i;
PyObject *obj;

printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", list->allocated);

for (i = 0; i < size; i++)
{
obj = PyList_GetItem(p, i);
printf("Element %zd: ", i);
if (PyFloat_Check(obj))
printf("float\n");
else if (PyLong_Check(obj))
printf("int\n");
else if (PyUnicode_Check(obj))
printf("str\n");
else if (PyList_Check(obj))
printf("list\n");
else if (PyTuple_Check(obj))
printf("tuple\n");
else if (PyDict_Check(obj))
printf("dict\n");
else if (PyBool_Check(obj))
printf("bool\n");
else if (PyBytes_Check(obj))
printf("bytes\n");
else if (PyByteArray_Check(obj))
printf("bytearray\n");
else if (PySet_Check(obj))
printf("set\n");
else if (PyAnySet_Check(obj))
printf("set\n");
else if (PyFrozenSet_Check(obj))
printf("frozenset\n");
else if (PyAnySet_CheckExact(obj))
printf("set\n");
else
printf("%s\n", obj->ob_type->tp_name);
}
}
