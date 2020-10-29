from distutils.core import setup, Extension

module = Extension('macos_notifications',
                    sources = ['notify.c'],
                    extra_compile_args = ["-ObjC"],
                    extra_link_args = ["-framework", "Foundation"])

setup(name='macos-notifications',
      version = '1.0',
      description = 'macOS package for sending notifications',
      python_requires = '>=3',
      platforms = ['MacOS X'],
      ext_modules = [module])