%define		_class		    Log
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	1.12.7
Release:	5
Summary:	Logging Framework
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/%{upstream_name}
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch
# because it was broken out and the one doing it was pretty careless...
Conflicts:	php-pear < 1:1.9

%description
The Log package provides an abstracted logging framework. It includes output
handlers for log files, databases, syslog, email, Firebug, and the console. It
also provides composite and subject-observer logging mechanisms.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/* %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml



%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.12.7-3mdv2012.0
+ Revision: 741779
- fix major breakage by careless packager

* Wed Dec 14 2011 Oden Eriksson <oeriksson@mandriva.com> 1.12.7-2
+ Revision: 741212
- fix carelessness

* Mon Nov 28 2011 Oden Eriksson <oeriksson@mandriva.com> 1.12.7-1
+ Revision: 735170
- new version

* Thu Jun 16 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.12.6-1
+ Revision: 685574
- update to new version 1.12.6

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.12.5-2
+ Revision: 667546
- mass rebuild

* Fri Dec 31 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.12.5-1mdv2011.0
+ Revision: 626873
- update to new version 1.12.5

* Sun Dec 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.12.4-1mdv2011.0
+ Revision: 622933
- update to new version 1.12.4

* Wed Oct 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.12.3-1mdv2011.0
+ Revision: 583637
- update to new version 1.12.3

* Thu Sep 09 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.12.2-1mdv2011.0
+ Revision: 576923
- update to new version 1.12.2

* Sun Jul 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.12.1-1mdv2011.0
+ Revision: 558761
- update to new version 1.12.1

* Mon Jan 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.12.0-1mdv2010.1
+ Revision: 495839
- update to new version 1.12.0

* Sat Jan 02 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.11.6-1mdv2010.1
+ Revision: 485150
- update to new version 1.11.6

* Fri Dec 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.11.5-2mdv2010.1
+ Revision: 473554
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 29 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.11.5-1mdv2010.0
+ Revision: 451088
- update to new version 1.11.5

* Sun Sep 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.11.4-1mdv2010.0
+ Revision: 450207
- import php-pear-Log


* Fri Sep 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.11.4-1mdv2010.0
- split out from php-pear package
