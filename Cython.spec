#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Cython
Version  : 0.24
Release  : 26
URL      : http://cython.org/release/Cython-0.24.tar.gz
Source0  : http://cython.org/release/Cython-0.24.tar.gz
Summary  : The Cython compiler for writing C extensions for the Python language.
Group    : Development/Tools
License  : Apache-2.0 Python-2.0
Requires: Cython-bin
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
== Pyximport ==
Download: pyx-import-1.0.tar.gz
<http://www.prescod.net/pyximport/pyximport-1.0.tar.gz>

%package bin
Summary: bin components for the Cython package.
Group: Binaries

%description bin
bin components for the Cython package.


%package python
Summary: python components for the Cython package.
Group: Default
Provides: cython-python

%description python
python components for the Cython package.


%prep
%setup -q -n Cython-0.24

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python runtests.py ||:
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cygdb
/usr/bin/cython
/usr/bin/cythonize

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
