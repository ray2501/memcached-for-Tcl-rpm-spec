%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          memcached-for-Tcl
Summary:       Memcached client library for Tcl based applications
Version:       1.2.1
Release:       2
License:       BSD-3-Clause
Group:         Development/Libraries/Tcl
Source:        https://github.com/bovine/memcached-for-Tcl/memcached-for-Tcl-1.2.1.tar.gz
URL:           https://github.com/bovine/memcached-for-Tcl
BuildRequires: autoconf
BuildRequires: make
BuildRequires: tcl-devel >= 8.5
BuildRequires: libmemcached-devel
BuildRequires: libsasl2-3
Requires:      libmemcached
Requires:      tcl >= 8.5
BuildRoot:     %{buildroot}

%description
Memcached client library for Tcl based applications.

%prep
%setup -q -n %{name}-%{version}

%build
autoconf
./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{directory}/%{_lib}/tcl \
        --with-sasl
make 

%install
make DESTDIR=%{buildroot} pkglibdir=%{tcl_archdir}/%{name}%{version} install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{tcl_archdir}
