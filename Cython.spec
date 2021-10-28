#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Cython
Version  : 0.29.24
Release  : 115
URL      : https://files.pythonhosted.org/packages/59/e3/78c921adf4423fff68da327cc91b73a16c63f29752efe7beb6b88b6dd79d/Cython-0.29.24.tar.gz
Source0  : https://files.pythonhosted.org/packages/59/e3/78c921adf4423fff68da327cc91b73a16c63f29752efe7beb6b88b6dd79d/Cython-0.29.24.tar.gz
Summary  : The Cython compiler for writing C extensions for the Python language.
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
BuildRequires : python3-dev

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
        covered by one of the wheel packages provided on PyPI *and* the pure Python wheel
        that we provide is not used, it is substantially faster than a full source build

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
Provides: pypi(cython)

%description python3
python3 components for the Cython package.


%prep
%setup -q -n Cython-0.29.24
cd %{_builddir}/Cython-0.29.24

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1626274197
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python runtests.py %{?_smp_mflags} --no-doctest --no-examples --no-code-style -vv -3 || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Cython
cp %{_builddir}/Cython-0.29.24/COPYING.txt %{buildroot}/usr/share/package-licenses/Cython/38099d4531dd3d32b72df546041f15201123547f
cp %{_builddir}/Cython-0.29.24/LICENSE.txt %{buildroot}/usr/share/package-licenses/Cython/a6a5418b4d67d9f3a33cbf184b25ac7f9fa87d33
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
/usr/share/package-licenses/Cython/38099d4531dd3d32b72df546041f15201123547f
/usr/share/package-licenses/Cython/a6a5418b4d67d9f3a33cbf184b25ac7f9fa87d33

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
