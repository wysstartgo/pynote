import imp
import importlib
import inspect
import glob
import requests
import os


def import_from_string(content, module_name, file_name=None):
    if not file_name:
        file_name = '{0}.py'.format(module_name)

    value = compile(content, file_name, 'exec')
    module = imp.new_module(module_name)
    exec(value, module.__dict__)
    return module


def import_from_url(url, module_name=None):
    file_name = os.path.basename(url).lower()
    if not module_name:
        module_name = os.path.splitext(file_name)[0]

    r = requests.get(url)
    r.raise_for_status()

    return import_from_string(r.content, module_name, file_name=file_name)


def import_plugins(plugins_package_directory_path, base_class=None, create_instance=True, filter_abstract=True):
    plugins_package_name = os.path.basename(plugins_package_directory_path)

    # -----------------------------
    # Iterate all python files within that directory
    plugin_file_paths = glob.glob(os.path.join(plugins_package_directory_path, "*.py"))
    for plugin_file_path in plugin_file_paths:
        plugin_file_name = os.path.basename(plugin_file_path)

        module_name = os.path.splitext(plugin_file_name)[0]

        if module_name.startswith("__"):
            continue

        # -----------------------------
        # Import python file

        module = importlib.import_module("." + module_name, package=plugins_package_name)

        # -----------------------------
        # Iterate items inside imported python file

        for item in dir(module):
            value = getattr(module, item)
            if not value:
                continue

            if not inspect.isclass(value):
                continue

            if filter_abstract and inspect.isabstract(value):
                continue

            if base_class is not None:
                if type(value) != type(base_class):
                    continue

            # -----------------------------
            # Instantiate / return type (depends on create_instance)

            yield value() if create_instance else value


def import_from_file(file_path):
    module_name, file_extension = os.path.splitext(os.path.basename(file_path).lower())

    if file_extension == '.py':
        return imp.load_source(module_name, file_path)
    elif file_extension == '.pyc':
        return imp.load_compiled(module_name, file_path)

    raise Exception('Unsupported file extension {0}'.format(file_extension))


if __name__ == '__main__':
    fileName = '../tmp/100'
    # B = imp.load_source('B',fileName)
    # import B
    # B.testPrint()
    with open(fileName,mode = 'r',encoding='utf-8') as f:
        content = f.read()

    modules = {}
    modules['B'] = content
    # print(content)
    try:
        B = import_from_string(content,'B')
        # import B
        B.testPrint()
    except Exception as e:
        print(e)

