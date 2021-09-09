#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : grpcio-channelz
Version  : 1.40.0
Release  : 5
URL      : https://files.pythonhosted.org/packages/ff/61/a2769df92020c779036269c74a5b83f980e6640825e8faedb6bf006cbe05/grpcio-channelz-1.40.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ff/61/a2769df92020c779036269c74a5b83f980e6640825e8faedb6bf006cbe05/grpcio-channelz-1.40.0.tar.gz
Summary  : Channel Level Live Debug Information Service for gRPC
Group    : Development/Tools
License  : Apache-2.0
Requires: grpcio-channelz-license = %{version}-%{release}
Requires: grpcio-channelz-python = %{version}-%{release}
Requires: grpcio-channelz-python3 = %{version}-%{release}
Requires: grpcio
Requires: protobuf
BuildRequires : buildreq-distutils3
BuildRequires : grpcio
BuildRequires : protobuf

%description
==============================
        
        Channelz is a live debug tool in gRPC Python.
        
        Supported Python Versions
        -------------------------
        Python >= 3.5
        
        Deprecated Python Versions
        --------------------------
        Python == 2.7. Python 2.7 support will be removed on January 1, 2020.
        
        Dependencies
        ------------
        
        Depends on the `grpcio` package, available from PyPI via `pip install grpcio`.

%package license
Summary: license components for the grpcio-channelz package.
Group: Default

%description license
license components for the grpcio-channelz package.


%package python
Summary: python components for the grpcio-channelz package.
Group: Default
Requires: grpcio-channelz-python3 = %{version}-%{release}

%description python
python components for the grpcio-channelz package.


%package python3
Summary: python3 components for the grpcio-channelz package.
Group: Default
Requires: python3-core
Provides: pypi(grpcio_channelz)
Requires: pypi(grpcio)
Requires: pypi(protobuf)

%description python3
python3 components for the grpcio-channelz package.


%prep
%setup -q -n grpcio-channelz-1.40.0
cd %{_builddir}/grpcio-channelz-1.40.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631203573
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/grpcio-channelz
cp %{_builddir}/grpcio-channelz-1.40.0/LICENSE %{buildroot}/usr/share/package-licenses/grpcio-channelz/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/grpcio-channelz/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
