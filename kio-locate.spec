Summary:	locate support for KDE
Summary(pl.UTF-8):	Obsługa protokołu locate dla KDE
Name:		kio-locate
Version:	0.4.5
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://arminstraub.com/downloads/kio-locate/%{name}_%{version}.tar.gz
# Source0-md5:	992f8e7eed048bf008de582b596ec84e
URL:		http://arminstraub.com/browse.php?page=programs_kiolocate
Requires:	/usr/bin/locate
BuildRequires:	scons >= 0.96.1
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Locate support for KDE.

%description -l pl.UTF-8
Obsługa protokołu locate dla KDE.

%prep
%setup -q

%build
%scons configure \
	datadir=%{_datadir} \
	prefix=%{_prefix} \
	qtincludes=%{_includedir}/qt
%scons

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/kde3/

export DESTDIR=$RPM_BUILD_ROOT
%scons install \
	datadir=%{_datadir} \
	prefix=%{_prefix} \
	qtincludes=%{_includedir}/qt

mv $RPM_BUILD_ROOT{%{_libdir}lib/kde3/*,%{_libdir}/kde3}
rm -f $RPM_BUILD_ROOT%{_libdir}/kde3/kio_locate.la

%find_lang kio-locate --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kio-locate.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/kio_locate.so
%{_datadir}/services/locate.protocol
%{_datadir}/services/locater.protocol
%{_datadir}/services/rlocate.protocol
%{_datadir}/services/searchproviders/locate.desktop
