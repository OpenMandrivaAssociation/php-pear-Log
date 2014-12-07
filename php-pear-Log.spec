%define _class		    Log
%define modname	%{_class}

Summary:	Logging Framework
Name:		php-pear-%{modname}
Version:	1.12.8
Release:	2
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/%{modname}
Source0:	http://download.pear.php.net/package/Log-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear
# because it was broken out and the one doing it was pretty careless...
Conflicts:	php-pear < 1:1.9

%description
The Log package provides an abstracted logging framework. It includes output
handlers for log files, databases, syslog, email, Firebug, and the console. It
also provides composite and subject-observer logging mechanisms.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/docs/* %{modname}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/data/%{modname}
%{_datadir}/pear/packages/%{modname}.xml
