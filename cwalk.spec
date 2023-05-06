%global upstream likle
%global gitbase  https://github.com

%define libname %mklibname %{name}
%define devname %mklibname %{name} -d

Summary: Path library for C/C++, cross-platform
Name:    cwalk
Version: 1.2.7
Release: 1
License: MIT
Url:     https://%{upstream}.github.io/%{name}
Source0: %{gitbase}/%{upstream}/%{name}/archive/refs/tags/v%{version}.tar.gz
Patch0:  CMake-Rely-on-GNUInstallDirs-for-installation-direct.patch

BuildRequires: cmake
BuildRequires: ninja

%description
Path library for C/C++, cross-platform.
Supports UNIX and Windows path styles on those platforms.

%package -n %{libname}
Summary:  %{summary}
Group:    System/Libraries
Provides: %{name} = %{version}-%{release}

%description -n %{libname}
This package contains the %{name} runtime library.

%package -n %{devname}
Summary:  %{summary}
Group:    Development/C
Requires: %{libname} = %{version}-%{release}

%description -n %{devname}
This package contains the %{name} development headers and library.

%prep
%autosetup -p 1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/lib%{name}*.so

%files -n %{devname}
%doc README.md
%license LICENSE.md
%{_includedir}/%{name}.h
%{_libdir}/cmake/%{name}
