#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : s3transfer
Version  : 0.1.12
Release  : 8
URL      : https://pypi.debian.net/s3transfer/s3transfer-0.1.12.tar.gz
Source0  : https://pypi.debian.net/s3transfer/s3transfer-0.1.12.tar.gz
Summary  : An Amazon S3 Transfer Manager
Group    : Development/Tools
License  : Apache-2.0
Requires: s3transfer-legacypython
Requires: s3transfer-python3
Requires: s3transfer-python
Requires: botocore
Requires: futures
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
s3transfer - An Amazon S3 Transfer Manager for Python
        =====================================================
        
        S3transfer is a Python library for managing Amazon S3 transfers.

%package legacypython
Summary: legacypython components for the s3transfer package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the s3transfer package.


%package python
Summary: python components for the s3transfer package.
Group: Default
Requires: s3transfer-legacypython
Requires: s3transfer-python3

%description python
python components for the s3transfer package.


%package python3
Summary: python3 components for the s3transfer package.
Group: Default
Requires: python3-core

%description python3
python3 components for the s3transfer package.


%prep
%setup -q -n s3transfer-0.1.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1512586241
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1512586241
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
