#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Cython
Version  : 0.29.7
Release  : 76
URL      : https://files.pythonhosted.org/packages/f8/da/c979464858b257b21a6472a85285548c91f5b4dc773cb049cfdfb3ceeb02/Cython-0.29.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/f8/da/c979464858b257b21a6472a85285548c91f5b4dc773cb049cfdfb3ceeb02/Cython-0.29.7.tar.gz
Summary  : C-Extensions for Python
Group    : Development/Tools
License  : Apache-2.0 Python-2.0
Requires: Cython-bin = %{version}-%{release}
Requires: Cython-license = %{version}-%{release}
Requires: Cython-python = %{version}-%{release}
Requires: Cython-python3 = %{version}-%{release}
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
Welcome to Cython's documentation.
To build the documentation on Linux, you need Make and Sphinx installed on your system. Then execute::

%package bin
Summary: bin components for the Cython package.
Group: Binaries
Requires: Cython-license = %{version}-%{release}

%description bin
bin components for the Cython package.


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
%setup -q -n Cython-0.29.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555254096
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Cython
cp COPYING.txt %{buildroot}/usr/share/package-licenses/Cython/COPYING.txt
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/Cython/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Cython/COPYING.txt
/usr/share/package-licenses/Cython/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
