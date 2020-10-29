
#include <Python.h>
#include <Foundation/Foundation.h>
#include <objc/objc-runtime.h>
#include <string.h>

static char bundle_identifier[128] = "org.python.PythonLauncher";

static PyObject *set_bundle_identifier(PyObject *self, PyObject *args) {
    const char *temp;
    if (!PyArg_ParseTuple(args, "s", &temp)) {
        return NULL;
    }
    strncpy(bundle_identifier, temp, sizeof(bundle_identifier));
    Py_RETURN_NONE;
}

static PyObject *send_notification(PyObject *self, PyObject *args, PyObject *kwargs) {
    const char *title;
    const char *subtitle = "";
    const char *text = "";
    static char *keywords[] = {"", "subtitle", "text", NULL};
    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "s|$ss", keywords, &title, &subtitle, &text)) {
        return NULL;
    }
    NSUserNotification *notification = [[NSUserNotification alloc] init];
    notification.title = [NSString stringWithUTF8String: title];
    notification.subtitle = [NSString stringWithUTF8String: subtitle];
    notification.informativeText = [NSString stringWithUTF8String: text];
    [[NSUserNotificationCenter defaultUserNotificationCenter] deliverNotification: notification];
    [notification release];
    Py_RETURN_NONE;
}

static PyMethodDef macos_notifications_methods[] = {
    {"set_bundle_identifier", set_bundle_identifier, METH_VARARGS, "Set bundleIdentifier."},
    {"send_notification", (PyCFunction)send_notification, METH_VARARGS | METH_KEYWORDS, "Send notification."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef macos_notifications_defination = {
    PyModuleDef_HEAD_INIT, "macos_notifications", "A Python module that send notifications on macOS.", -1, macos_notifications_methods
};

PyMODINIT_FUNC PyInit_macos_notifications(void) {
    Py_Initialize();
    return PyModule_Create(&macos_notifications_defination);
}

__attribute__((unused)) static void register_hook(Class class, SEL cmd, IMP new, IMP *old) {
    unsigned int count, i;
    Class searchedClass = class;
    Method *methods;
    while (searchedClass) {
        methods = class_copyMethodList(searchedClass, &count);
        for (i = 0; i < count; ++i) {
            if (method_getName(methods[i]) == cmd) {
                if (class == searchedClass) {
                    *old = method_getImplementation(methods[i]);
                    *old = method_setImplementation(methods[i], new);
                } else {
                    class_addMethod(class, cmd, new, method_getTypeEncoding(methods[i]));
                }
                free(methods);
                return;
            }
        }
        free(methods);
        searchedClass = class_getSuperclass(searchedClass);
    }
}

@class NSBundle;
static NSString *(*origin_method)(__unsafe_unretained NSBundle* const, SEL);

static NSString *new_method(__unsafe_unretained NSBundle* const __unused self, SEL __unused _cmd) {
    return [NSString stringWithUTF8String: bundle_identifier];
}

static __attribute__((constructor)) void lib_loaded() {
    Class class = objc_getClass("NSBundle");
    register_hook(class, @selector(bundleIdentifier), (IMP)&new_method, (IMP *)&origin_method);
}