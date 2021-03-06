#include <Python.h>

/**
 * print_python_list_info - Function that print infromation about python list
 * @p: A object list named PyOject
 */
void print_python_list_info(PyObject *p)
{
	PyObject *pyt;
	int i = 0, size, memory;

	memory = ((PyListObject *)p)->allocated; /* Memory allocated*/
	size = Py_SIZE(p);                       /* Knowing size*/

	printf("[*] Size of the Python List = %d", size);
	printf("\n[*] Allocated = %d\n", memory);

	while (i < size)
	{
		printf("Element %d: ", i);
		pyt = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(pyt)->tp_name);
		i++;
	}
}
