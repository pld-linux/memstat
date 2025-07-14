Summary:	Identify what's using up virtual memory
Summary(pl.UTF-8):	Identyfikacja procesów korzystających z pamięci wirtualnej
Name:		memstat
Version:	0.9
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://ftp.debian.org/debian/pool/main/m/memstat/%{name}_%{version}.tar.gz
# Source0-md5:	b4ee74125d9da23d64646f5feee4b149
Patch0:		%{name}-make.patch
URL:		http://packages.qa.debian.org/m/memstat.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lists all the processes, executables, and shared libraries that are
using up virtual memory. It's helpful to see how the shared memory is
used and which 'old' libs are loaded.

%description -l pl.UTF-8
Program ten wyświetla listę procesów, plików uruchamialnych oraz
bibliotek współdzielonych korzystających z pamięci wirtualnej.
Narzędzie to jest przydatne, aby dowiedzieć się jak pamięć
współdzielona jest wykorzystywana i jakie starsze wersje bibliotek są
załadowane.

%prep
%setup -q -n %{name}tool
%patch -P0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man1}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc memstat-tutorial.txt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/memstat.1*
