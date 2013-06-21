%define		php_name	php%{?php_suffix}
%define		modname	lchash
%define		status		stable
Summary:	%{modname} - Libc Hash Interface
Summary(pl.UTF-8):	%{modname} - interfejs tablic haszujących libc
Name:		%{php_name}-pecl-%{modname}
Version:	0.9.1
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	1ad9261f2461db033423e797e67c301c
URL:		http://pecl.php.net/package/lchash/
BuildRequires:	libtool
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The LCHASH extension provides interface to libc implementation of hash
tables described by POSIX 1003.1-2001.

In PECL status of this extension is: %{status}.

%description -l pl.UTF-8
Rozszerzenie LCHASH dostarcza interfejsu do implementacji libc tablic
haszujących określonych przez standard POSIX 1003.1-2001.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}
install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc CREDITS EXPERIMENTAL
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
