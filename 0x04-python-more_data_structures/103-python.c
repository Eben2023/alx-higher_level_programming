#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size, i;
    char *string;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(bytes))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", string);

    printf("  first %zd bytes:", (size < 10 ? size + 1 : 10));

    for (i = 0; i < size && i < 10; i++)
    {
        printf(" %02x", string[i] & 0xff);
    }

    printf("\n");
}

void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size, alloc, i;
    PyObject *item;

    printf("[*] Python list info\n");

    size = PyList_Size(p);
    alloc = list->allocated;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", alloc);

    for (i = 0; i < size; i++)
    {
        item = PyList_GET_ITEM(p, i);
        printf("Element %zd: ", i);
        if (PyBytes_Check(item))
        {
            printf("bytes\n");
            print_python_bytes(item);
        }
        else if (PyList_Check(item))
        {
            printf("list\n");
        }
        else if (PyTuple_Check(item))
        {
            printf("tuple\n");
        }
        else if (PyFloat_Check(item))
        {
            printf("float\n");
        }
        else if (PyLong_Check(item))
        {
            printf("int\n");
        }
        else if (PyUnicode_Check(item))
        {
            printf("str\n");
        }
        else
        {
            printf("other\n");
        }
    }
}

