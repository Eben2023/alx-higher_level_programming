#include <Python.h>

void print_python_list(PyObject *list_object);
void print_python_bytes(PyObject *bytes_object);
void print_python_float(PyObject *float_object);

/**
 * print_python_list - Prints basic information about Python lists.
 * @list_object: A PyObject representing a list.
 *
 * Return: void
 */
void print_python_list(PyObject *list_object)
{
Py_ssize_t size, alloc, i;
const char *type;
PyListObject *list;
PyVarObject *var;

setbuf(stdout, NULL);

list = (PyListObject *)list_object;
var = (PyVarObject *)list_object;

size = var->ob_size;
alloc = list->allocated;

printf("[*] Python list info\n");
if (strcmp(list_object->ob_type->tp_name, "list") != 0)
{
printf("  [ERROR] Invalid List Object\n");
return;
}

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", alloc);

for (i = 0; i < size; i++)
{
type = list->ob_item[i]->ob_type->tp_name;
printf("Element %ld: %s\n", i, type);
if (strcmp(type, "bytes") == 0)
print_python_bytes(list->ob_item[i]);
else if (strcmp(type, "float") == 0)
print_python_float(list->ob_item[i]);
}
}

/**
 * print_python_bytes - Prints basic information about Python byte objects.
 * @bytes_object: A PyObject representing a byte object.
 *
 * Return: void
 */
void print_python_bytes(PyObject *bytes_object)
{
Py_ssize_t size, i;
PyBytesObject *bytes;

setbuf(stdout, NULL);

bytes = (PyBytesObject *)bytes_object;

printf("[.] bytes object info\n");
if (strcmp(bytes_object->ob_type->tp_name, "bytes") != 0)
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = ((PyVarObject *)bytes_object)->ob_size;
printf("  size: %ld\n", size);
printf("  trying string: %s\n", bytes->ob_sval);

if (size >= 10)
size = 10;

printf("  first %ld bytes: ", size);
for (i = 0; i < size; i++)
{
printf("%02hhx", bytes->ob_sval[i]);
if (i == size - 1)
printf("\n");
else
printf(" ");
}
}

/**
 * print_python_float - Prints basic information about Python float objects.
 * @float_object: A PyObject representing a float object.
 *
 * Return: void
 */
void print_python_float(PyObject *float_object)
{
char *buffer = NULL;
PyFloatObject *float_obj;

setbuf(stdout, NULL);

float_obj = (PyFloatObject *)float_object;

printf("[.] float object info\n");
if (strcmp(float_object->ob_type->tp_name, "float") != 0)
{
printf("  [ERROR] Invalid Float Object\n");
return;
}

buffer = PyOS_double_to_string(float_obj->ob_fval,
'r', 0,Py_DTSF_ADD_DOT_0, NULL);
                               
printf("  value: %s\n", buffer);
PyMem_Free(buffer);
}
