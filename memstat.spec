Summary:	Identify what's using up virtual memory
Summary(pl.UTF-8):	Identyfikacja procesów korzystających z pamięci wirtualnej
Name:		memstat
Version:	0.5
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://ftp.debian.org/debian/pool/main/m/memstat/%{name}_%{version}.tar.gz
# Source0-md5:	5dd028c194decf7ff83653eea6972cc1
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
%setup -q
%{__sed} -e 's,-o root -g root,,g' -i Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man1}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc memstat-tutorial.txt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/memstat.1*
