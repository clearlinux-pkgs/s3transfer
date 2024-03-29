#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : s3transfer
Version  : 0.5.0
Release  : 59
URL      : https://files.pythonhosted.org/packages/88/ef/4d1b3f52ae20a7e72151fde5c9f254cd83f8a49047351f34006e517e1655/s3transfer-0.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/88/ef/4d1b3f52ae20a7e72151fde5c9f254cd83f8a49047351f34006e517e1655/s3transfer-0.5.0.tar.gz
Summary  : An Amazon S3 Transfer Manager
Group    : Development/Tools
License  : Apache-2.0
Requires: s3transfer-license = %{version}-%{release}
Requires: s3transfer-python = %{version}-%{release}
Requires: s3transfer-python3 = %{version}-%{release}
Requires: botocore
BuildRequires : botocore
BuildRequires : buildreq-distutils3

%description
s3transfer - An Amazon S3 Transfer Manager for Python
        =====================================================
        
        S3transfer is a Python library for managing Amazon S3 transfers.

%package license
Summary: license components for the s3transfer package.
Group: Default

%description license
license components for the s3transfer package.


%package python
Summary: python components for the s3transfer package.
Group: Default
Requires: s3transfer-python3 = %{version}-%{release}

%description python
python components for the s3transfer package.


%package python3
Summary: python3 components for the s3transfer package.
Group: Default
Requires: python3-core
Provides: pypi(s3transfer)
Requires: pypi(botocore)

%description python3
python3 components for the s3transfer package.


%prep
%setup -q -n s3transfer-0.5.0
cd %{_builddir}/s3transfer-0.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1626450282
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/s3transfer
cp %{_builddir}/s3transfer-0.5.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/s3transfer/5a7d7df655ba40478fae80a6abafc6afc36f9b6a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/s3transfer/5a7d7df655ba40478fae80a6abafc6afc36f9b6a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
