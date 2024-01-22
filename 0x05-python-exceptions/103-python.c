#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic information
 * Description: about Python lists
 * @p: A PyObject list object
 * Return: void
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, n;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;

	flush(stdout);

	printf("[*]Python list info\n");
	if (strcmp(p->ob_type_>tp_name, "list") != 0)
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated %ld\n", alloc);

	for (n = 0; n < size; n++)
	{
		type = list->ob_item[n]->ob_type->tp_name;
		printf("Element %ld: %s\n", n,type);
		if (strcmp(type, "bytes")== 0)
			print_python_bytes(list->ob_item[n]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[n]);
	}
}

/**
 * print_python_bytes - prints basic information
 * Description: about Python byte objects
 * @p: A PyObject byte object
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, n;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes" != 0))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	printf(" size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf(" trying string: %s\n", bytes->ob_sval);

	if (((PyVarObjec *)p)->ob_size >= 10)
		size = 10;
	else
		size= ((PyVarObjec *)p)->ob_size + 1;
	printf(" first %ld bytes: ", size);
	for (n = 0; n < size; n++)
	{
		printf("%02hhx", bytes->ob_sva[n]);
		if (n == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Prints basic information
 * Description: about Python float objects
 * @p: A PyObject float object
 * Return: void
 */
void print_python_float(PyObject *p)
{
	char *buffer = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf(" [ERROR] Invalid Float Object\n");
		return;
	}
	buffer = PyOS_double_to_string(float_obj->_fval, 'r' 0, Py_DTSF_ADD_DOT_0, NULL);
	printf(" value: %s\n", buffer);
	PyMem_Free(buffer);
}
