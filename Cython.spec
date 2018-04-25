#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x44A7D230CCC5497B (consulting@behnel.de)
#
Name     : Cython
Version  : 0.28.2
Release  : 45
URL      : http://pypi.debian.net/Cython/Cython-0.28.2.tar.gz
Source0  : http://pypi.debian.net/Cython/Cython-0.28.2.tar.gz
Source99 : http://pypi.debian.net/Cython/Cython-0.28.2.tar.gz.asc
Summary  : The Cython compiler for writing C extensions for the Python language.
Group    : Development/Tools
License  : Apache-2.0 Python-2.0
Requires: Cython-bin
Requires: Cython-legacypython
Requires: Cython-python3
Requires: Cython-python
BuildRequires : coverage
BuildRequires : gdb
BuildRequires : numpy
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
easy as Python itself.  Cython is a source code translator based on Pyrex_,
        but supports more cutting edge functionality and optimizations.
        
        The Cython language is a superset of the Python language (almost all Python
        code is also valid Cython code), but Cython additionally supports optional
        static typing to natively call C functions, operate with C++ classes and
        declare fast C types on variables and class attributes.  This allows the
        compiler to generate very efficient C code from Cython code.
        
        This makes Cython the ideal language for writing glue code for external
        C/C++ libraries, and for fast C modules that speed up the execution of
        Python code.
        
        Note that for one-time builds, e.g. for CI/testing, on platforms that are not
        covered by one of the wheel packages provided on PyPI, it is substantially faster

%package bin
Summary: bin components for the Cython package.
Group: Binaries

%description bin
bin components for the Cython package.


%package legacypython
Summary: legacypython components for the Cython package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the Cython package.


%package python
Summary: python components for the Cython package.
Group: Default
Requires: Cython-python3
Provides: cython-python

%description python
python components for the Cython package.


%package python3
Summary: python3 components for the Cython package.
Group: Default
Requires: python3-core

%description python3
python3 components for the Cython package.


%prep
%setup -q -n Cython-0.28.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1524730856
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python runtests.py -j4 ||:
%install
export SOURCE_DATE_EPOCH=1524730856
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cygdb
/usr/bin/cython
/usr/bin/cythonize

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
