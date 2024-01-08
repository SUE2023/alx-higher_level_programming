#include<python.h>
#include<object.h>
#include<listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int n;
	PyListObject *obj = (PyListObject *)p;
	
	printf("[*]Size of the Python List = %li\n, size");
	printf("[*] Allocated = %li\n, obj->allocated");
	for (n = 0; n < size; n++)
		printf("Element %i; %s", n, py_TYPE(obj->ob_item[n])->tp_name);	
}
