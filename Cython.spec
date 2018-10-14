#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Cython
Version  : 0.29
Release  : 61
URL      : https://files.pythonhosted.org/packages/f0/66/6309291b19b498b672817bd237caec787d1b18013ee659f17b1ec5844887/Cython-0.29.tar.gz
Source0  : https://files.pythonhosted.org/packages/f0/66/6309291b19b498b672817bd237caec787d1b18013ee659f17b1ec5844887/Cython-0.29.tar.gz
Summary  : The Cython compiler for writing C extensions for the Python language.
Group    : Development/Tools
License  : Apache-2.0 Python-2.0
Requires: Cython-bin = %{version}-%{release}
Requires: Cython-license = %{version}-%{release}
Requires: Cython-python = %{version}-%{release}
Requires: Cython-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils23
BuildRequires : buildreq-distutils3
BuildRequires : coverage
BuildRequires : gdb
BuildRequires : ipython
BuildRequires : numpy
BuildRequires : python-core
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools-legacypython

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
Requires: Cython-license = %{version}-%{release}

%description bin
bin components for the Cython package.


%package legacypython
Summary: legacypython components for the Cython package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the Cython package.


%package license
Summary: license components for the Cython package.
Group: Default

%description license
license components for the Cython package.


%package python
Summary: python components for the Cython package.
Group: Default
Requires: Cython-python3 = %{version}-%{release}
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
%setup -q -n Cython-0.29

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539539881
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1539539881
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Cython
cp COPYING.txt %{buildroot}/usr/share/package-licenses/Cython/COPYING.txt
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/Cython/LICENSE.txt
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Cython/COPYING.txt
/usr/share/package-licenses/Cython/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
