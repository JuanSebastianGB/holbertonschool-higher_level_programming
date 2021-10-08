#include "Python.h"


/**
 * print_python_string - prints Python strings.
 * @p: PyObject expected string
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t length;

	(void)p;
	(void)length;
	fflush(stdout);

	printf("[.] string object info \n");
/* Checking invalid string*/
	if (strcmp("str", p->ob_type->tp_name))
	{
		printf(" [ERROR] Invalid String Object\n");
		return;
	}
	length = ((PyASCIIObject *)(p))->length;
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf(" type: compact ascii\n");
	else
	{
		printf(" type: compact unicode object\n");
	}
	printf(" length: %li\n", length);
	printf(" value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
