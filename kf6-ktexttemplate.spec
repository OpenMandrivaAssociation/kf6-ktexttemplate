%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6TextTemplate
%define devname %mklibname KF6TextTemplate -d
#define git 20240217

Name: kf6-ktexttemplate
Version: 6.3.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/ktexttemplate/-/archive/master/ktexttemplate-master.tar.bz2#/ktexttemplate-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/frameworks/%{major}/ktexttemplate-%{version}.tar.xz
%endif
Summary: Library to allow application developers to separate the structure of documents from the data they contain
URL: https://invent.kde.org/frameworks/ktexttemplate
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: gettext
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: gperf
Requires: %{libname} = %{EVRD}

%description
Library to allow application developers to separate the structure
of documents from the data they contain

%package -n %{libname}
Summary: Library to allow application developers to separate the structure of documents from the data they contain
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Library to allow application developers to separate the structure of documents
from the data they contain

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%{name} is a library to allow application developers to separate the structure of
documents from the data they contain

%prep
%autosetup -p1 -n ktexttemplate-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories6/ktexttemplate.*

%files -n %{devname}
%{_includedir}/KF6/KTextTemplate
%{_libdir}/cmake/KF6TextTemplate
%{_qtdir}/doc/KF6TextTemplate.*

%files -n %{libname}
%{_libdir}/libKF6TextTemplate.so*
%{_qtdir}/plugins/kf6/ktexttemplate
