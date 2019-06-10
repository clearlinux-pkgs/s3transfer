#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : s3transfer
Version  : 0.2.1
Release  : 28
URL      : https://files.pythonhosted.org/packages/39/12/150cd55c606ebca6725683642a8e7068cd6af10f837ce5419a9f16b7fb55/s3transfer-0.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/39/12/150cd55c606ebca6725683642a8e7068cd6af10f837ce5419a9f16b7fb55/s3transfer-0.2.1.tar.gz
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
=====================================================
s3transfer - An Amazon S3 Transfer Manager for Python
=====================================================

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

%description python3
python3 components for the s3transfer package.


%prep
%setup -q -n s3transfer-0.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1560185233
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/s3transfer
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/s3transfer/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/s3transfer/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
