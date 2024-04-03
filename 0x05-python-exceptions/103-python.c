#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid PyListObject\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);

    // You may need to use setbuf(stdout, NULL); or fflush(stdout); here
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "Invalid PyBytesObject\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AS_STRING(p));

    printf("  first 10 bytes: ");
    for (Py_ssize_t i = 0; i < size && i < 10; i++) {
        printf("%02hhx ", (unsigned char) PyBytes_AS_STRING(p)[i]);
    }
    printf("\n");

    // You may need to use setbuf(stdout, NULL); or fflush(stdout); here
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "Invalid PyFloatObject\n");
        return;
    }

    printf("[.] float object info\n");
    printf("  value: %f\n", PyFloat_AS_DOUBLE(p));

    // You may need to use setbuf(stdout, NULL); or fflush(stdout); here
}

